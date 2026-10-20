from datetime import datetime,timezone
import json
from pathlib import Path
from unittest.mock import MagicMock
import numpy as np
import pytest
import yaml
from src.models import Metric,Stock
from src.config import load_config
from src.fixtures import fixture_bundle
from src.providers import Bundle,collect
from src.providers.http import Client,ProviderError
from src import fundamentals,technicals,scoring,valuation,decisions,news,email_sender
from src.market import market_status
ROOT=Path(__file__).resolve().parents[1]
FIXTURE=ROOT/'tests/fixtures/equities.json'
POLICY=yaml.safe_load((ROOT/'config/scoring.yml').read_text())
def bundle(ticker='AAPL',exchange='NASDAQ'):
    return fixture_bundle(FIXTURE,Stock(ticker=ticker,exchange=exchange))[0]

def test_config():
    config=load_config(str(ROOT/'config/stocks.yml'),'IBM:NYSE,TCS.NS,500325.BO')
    assert [s.exchange for s in config.stocks]==['NYSE','NSE','BSE']
    with pytest.raises(ValueError): Stock(ticker='TCS.NS',exchange='NYSE')
    with pytest.raises(ValueError): load_config(str(ROOT/'config/stocks.yml'),'AAPL AAPL')

@pytest.mark.parametrize('ticker,exchange',[('AAPL','NASDAQ'),('TCS.NS','NSE'),('HDFCBANK.NS','NSE'),('500325.BO','BSE')])
def test_fundamentals(ticker,exchange):
    metrics=fundamentals.analyze(bundle(ticker,exchange))
    assert metrics['roe'].value==pytest.approx(1/6)
    assert metrics['revenue_growth_5y'].value==pytest.approx(.08)
    assert metrics['fcf_conversion'].formula
    assert metrics['fcf'].source=='SYNTHETIC FIXTURE'

def test_technical_split_and_short():
    bars=bundle().bars
    result=technicals.analyze(bars,bars)
    assert result['metrics']['relative_strength_63']['value']==pytest.approx(0)
    assert result['metrics']['sma200']['value']==pytest.approx(bars.Close.iloc[-200:].mean())
    split=bars.copy();split[['Open','High','Low','Close']]=50.
    result=technicals.analyze(split,split)
    assert result['metrics']['rsi14']['value']==50
    assert result['metrics']['atr14']['value']==0
    assert result['metrics']['momentum_63']['value']==0
    assert technicals.analyze(bars.iloc[:10])['metrics']['sma200']['value'] is None
    bad=bars.copy();bad.iloc[-1,bad.columns.get_loc('Close')]=np.nan
    with pytest.raises(ValueError): technicals.analyze(bad)

def test_scoring():
    rules={'a':{'weight':3,'bad':0,'good':1},'b':{'weight':1,'bad':0,'good':1}}
    metrics={'a':Metric(value=.5,source='fixture',freshness='fresh')}
    result=scoring.category_score(metrics,rules,30,.65)
    assert result['score']==15 and result['coverage']==.75
    assert scoring.category_score({},rules,30,.65)['score'] is None
    metrics['a'].freshness='stale'
    assert scoring.category_score(metrics,rules,30,.65)['score'] is None

def test_dcf():
    data=bundle();metrics=fundamentals.analyze(data)
    values=valuation.analyze(data,metrics,POLICY)
    assert values['fair_values']['conservative']['value']<values['fair_values']['base']['value']<values['fair_values']['optimistic']['value']
    bank=bundle('HDFCBANK.NS','NSE')
    assert valuation.analyze(bank,fundamentals.analyze(bank),POLICY)['fair_values'] is None
    data.statements=data.statements[:2]
    assert valuation.analyze(data,metrics,POLICY)['fair_values'] is None

def test_decisions():
    scores={'total':95,'interpretation':'Strong candidate','categories':{'fundamentals':{'score':28},'risk':{'score':14}}}
    val={'verdict':'Overvalued','margin_of_safety':-.4};risks={'critical':[],'concerns':[]}
    assert decisions.decide(scores,val,risks,{},False,True)['verdict']=='WAIT FOR BETTER PRICE'
    assert decisions.decide(scores,val,risks,{},True,True)['verdict']=='INSUFFICIENT DATA'
    risks['critical']=['Default']
    assert decisions.decide(scores,val,risks,{},False,False)['verdict']=='AVOID'

def test_news():
    stock=Stock(ticker='AAPL',exchange='NASDAQ')
    item={'headline':'Apple announces earnings outlook','published_at':datetime.now(timezone.utc).isoformat(),'url':'https://example.com/news?utm=x','publisher':'Fixture'}
    result=news.classify([item,{**item,'url':'https://other.com/syndicated'},{**item,'headline':'Pineapple fruit market rallies'}],stock,'Apple Inc.',7)
    assert len(result['items'])==1 and result['items'][0]['sentiment']=='uncertain'
    assert result['items'][0]['url']=='https://example.com/news?utm=x'
    event={**item,'headline':'Apple files for bankruptcy','primary':True,'confirmed':True,'event_code':'bankruptcy_filed','evidence_quote':'Apple filed for bankruptcy'}
    assert news.classify([event],stock,'Apple Inc.',7)['critical']
    assert not news.classify([{**event,'confirmed':False}],stock,'Apple Inc.',7)['critical']

def test_provider_failures_conflicts():
    first=MagicMock();first.name='first'
    first.fetch.return_value=Bundle('Example','USD','Technology','Software',{'pe':Metric(value=10,source='first')})
    failed=MagicMock();failed.name='failed';failed.fetch.side_effect=ProviderError('failure')
    second=MagicMock();second.name='second'
    second.fetch.return_value=Bundle('Example','USD','Technology','Software',{'pe':Metric(value=20,source='second')})
    result=collect(Stock(ticker='AAPL',exchange='NASDAQ'),[failed,first,second])
    assert result.metrics['pe'].value==10 and result.candidates['pe'][0]['value']==20
    assert any('conflict' in w for w in result.warnings)

@pytest.mark.parametrize('exchange,date,last',[('NYSE','2025-12-25T12:00:00+00:00','2025-12-24'),('BSE','2025-01-26T12:00:00+00:00','2025-01-24')])
def test_holidays(exchange,date,last):
    result=market_status(exchange,last,datetime.fromisoformat(date))
    assert result['condition']=='holiday/weekend' and not result['stale']

def test_http_cache_retry(tmp_path,monkeypatch):
    client=Client(tmp_path);response=MagicMock(status_code=200);response.json.return_value={'value':1}
    rate=MagicMock(status_code=429,headers={'Retry-After':'0'})
    client.session.get=MagicMock(side_effect=[rate,response])
    monkeypatch.setattr('src.providers.http.time.sleep',lambda _:None)
    assert client.get('https://example.com')[0]=={'value':1}
    assert client.get('https://example.com')[0]=={'value':1}
    assert client.session.get.call_count==2

def test_email_ambiguous_failure(tmp_path,monkeypatch):
    for k,v in {'GMAIL_ADDRESS':'test@gmail.com','GMAIL_APP_PASSWORD':'test password','REPORT_TO_EMAIL':'reader@example.com'}.items(): monkeypatch.setenv(k,v)
    report=tmp_path/'reports';report.mkdir()
    for suffix in ('json','md','html','csv'): (report/f'latest.{suffix}').write_text('{}' if suffix=='json' else 'fixture')
    state=tmp_path/'delivery.json'
    assert email_sender.reserve(state,report,'day')
    assert not email_sender.reserve(state,report,'day')
    smtp=MagicMock();smtp.__enter__.return_value=smtp
    smtp.send_message.side_effect=ConnectionResetError('secret must not escape')
    mock=MagicMock(return_value=smtp);monkeypatch.setattr(email_sender.smtplib,'SMTP_SSL',mock)
    with pytest.raises(RuntimeError,match='sanitized ledger'): email_sender.send(state,report,'day')
    assert json.loads(state.read_text())['day']['status']=='uncertain'
    assert mock.call_args.kwargs['context'].check_hostname
    assert not email_sender.reserve(state,report,'day')

def test_end_to_end(tmp_path):
    from src.main import run
    result=run(str(ROOT/'config/stocks.yml'),tmp_path,fixture=FIXTURE)
    assert len(result['stocks'])==4
    assert all('error' not in s for s in result['stocks'])
    assert result['stocks'][-1]['verdict']=='INSUFFICIENT DATA'
    assert (tmp_path/'reports/latest.html').exists()
    assert 'SYNTHETIC' in (tmp_path/'reports/latest.html').read_text()

def test_cached_bundle_retains_retrieval(tmp_path):
    from src.providers.cache import CachedProvider
    provider=MagicMock();provider.name='fixture';provider.fetch.return_value=bundle()
    cached=CachedProvider(provider,tmp_path)
    stock=Stock(ticker='AAPL',exchange='NASDAQ')
    first=cached.fetch(stock);second=cached.fetch(stock)
    assert provider.fetch.call_count==1
    assert first.metrics['price'].retrieved_at==second.metrics['price'].retrieved_at
    assert np.allclose(first.bars.Close,second.bars.Close)

def test_llm_rejects_ungrounded_quotes(tmp_path,monkeypatch):
    from src.llm import summarize
    monkeypatch.setenv('LLM_API_KEY','fixture-key');monkeypatch.setenv('LLM_MODEL','fixture-model')
    response=MagicMock(status_code=200)
    response.json.return_value={'output':[{'content':[{'type':'output_text','text':json.dumps({'summaries':[{'article_id':'1','evidence_quote':'invented content','sentiment':'positive','impact':'unsupported'}]})}]}]}
    monkeypatch.setattr('src.llm.requests.post',MagicMock(return_value=response))
    item={'id':'1','headline':'Apple earnings release','summary':'No guidance provided','url':'https://example.com','access':'snippet'}
    assert summarize([item],tmp_path)['items']==[]

def test_missing_bank_metrics_and_critical_override():
    data=bundle('HDFCBANK.NS','NSE')
    metrics=fundamentals.analyze(data)
    score=scoring.score(metrics,'financial',POLICY)
    assert score['total'] is None
    from src.risk import analyze
    metrics['equity']=Metric(value=-1,source='fixture',freshness='fresh')
    assert analyze(metrics,{},True)['critical']

def test_storage_changes_and_previous_day(tmp_path):
    from src.storage import previous,changes,write_json
    write_json(tmp_path/'2025-01-01.json',{'old':True})
    write_json(tmp_path/'2025-01-02.json',{'same_day':True})
    assert previous(tmp_path,'2025-01-02')=={'old':True}
    diff=changes({'price':110,'score':70,'news_ids':['new']},{'price':100,'score':60,'news_ids':[]})
    assert diff['price']['delta']==10 and diff['new_news']==['new']

def test_durable_state_roundtrip(tmp_path,monkeypatch):
    import os,subprocess,sys
    script=ROOT/'scripts/state.py'
    def git(*args,cwd):
        return subprocess.run(['git',*args],cwd=cwd,check=True,capture_output=True,text=True).stdout
    remote=tmp_path/'remote.git';remote.mkdir();git('init','--bare',cwd=remote)
    seed=tmp_path/'seed';seed.mkdir();git('init',cwd=seed)
    git('config','user.name','test',cwd=seed);git('config','user.email','test@example.com',cwd=seed)
    (seed/'README.md').write_text('seed');git('add','.',cwd=seed);git('commit','-m','seed',cwd=seed)
    git('remote','add','origin',str(remote),cwd=seed);git('push','origin','HEAD:main',cwd=seed)
    monkeypatch.delenv('GITHUB_ACTIONS',raising=False)
    def state(action,cwd):
        subprocess.run([sys.executable,str(script),action],cwd=cwd,env=os.environ.copy(),check=True,capture_output=True)
    state('load',seed)
    (seed/'state/delivery.json').write_text('{"day":{"status":"sending"}}')
    state('persist',seed)
    assert 'sending' in git('show','research-state:delivery.json',cwd=remote)
    other=tmp_path/'other';git('clone',str(remote),str(other),cwd=tmp_path)
    state('load',other)
    assert json.loads((other/'state/delivery.json').read_text())['day']['status']=='sending'

def test_fmp_documented_adjusted_schema(tmp_path,monkeypatch):
    from src.providers.fmp import FMP
    monkeypatch.setenv('FMP_API_KEY','test-key')
    client=MagicMock()
    client.get.return_value=([{'symbol':'AAPL','date':'2025-01-02','adjOpen':100,'adjHigh':102,'adjLow':99,'adjClose':101,'volume':1000}], '2025-01-03T00:00:00+00:00')
    bars=FMP(client).history('AAPL')
    assert bars.Close.iloc[0]==101 and bars.attrs['retrieved_at']=='2025-01-03T00:00:00+00:00'
    assert 'dividend-adjusted' in client.get.call_args.args[0]

def test_email_accepted_is_durable(tmp_path,monkeypatch):
    for k,v in {'GMAIL_ADDRESS':'test@gmail.com','GMAIL_APP_PASSWORD':'test password','REPORT_TO_EMAIL':'reader@example.com'}.items(): monkeypatch.setenv(k,v)
    reports=tmp_path/'reports';reports.mkdir()
    for suffix in ('json','md','html','csv'): (reports/f'latest.{suffix}').write_text('{}' if suffix=='json' else 'fixture')
    state=tmp_path/'ledger.json';email_sender.reserve(state,reports,'day')
    smtp=MagicMock();smtp.__enter__.return_value=smtp;smtp.send_message.return_value={}
    monkeypatch.setattr(email_sender.smtplib,'SMTP_SSL',MagicMock(return_value=smtp))
    email_sender.send(state,reports,'day')
    assert json.loads(state.read_text())['day']['status']=='delivered'
    message=smtp.send_message.call_args.args[0]
    assert message.is_multipart() and list(message.iter_attachments())[0].get_filename()=='stock-research.csv'
