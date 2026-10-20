from __future__ import annotations
import argparse
import hashlib
import json
import logging
import os
from pathlib import Path
import re
import smtplib
import ssl
from email.message import EmailMessage
from .storage import write_json


def credentials() -> tuple[str,str,list[str]]:
    sender=os.getenv('GMAIL_ADDRESS','')
    password=''.join(os.getenv('GMAIL_APP_PASSWORD','').split())
    recipients=[x.strip() for x in os.getenv('REPORT_TO_EMAIL','').split(',') if x.strip()]
    if not password or not recipients or not all(re.fullmatch(r'[A-Za-z0-9.!#$%&\x27*+/=?^_`{|}~-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',a) for a in [sender,*recipients]):
        raise ValueError('Missing or invalid SMTP settings')
    return sender,password,recipients


def reserve(state: Path, report: Path, ledger_key: str) -> bool:
    credentials()  # Validate before durable reservation.
    ledger=json.loads(state.read_text()) if state.exists() else {}
    if ledger.get(ledger_key,{}).get('status') in {'sending','delivered','uncertain'}:
        return False
    digest=hashlib.sha256((report/'latest.json').read_bytes()).hexdigest()
    ledger[ledger_key]={'status':'sending','report_sha256':digest}
    write_json(state,ledger)
    return True


def send(state: Path, report: Path, ledger_key: str) -> None:
    ledger=json.loads(state.read_text())
    record=ledger[ledger_key]
    if record['status']!='sending':
        raise ValueError('A persisted sending reservation is required')
    stage='prepare'
    try:
        if hashlib.sha256((report/'latest.json').read_bytes()).hexdigest()!=record['report_sha256']:
            raise ValueError('Report changed after reservation')
        sender,password,recipients=credentials()
        message=EmailMessage()
        message['Subject']='Daily equity research — '+ledger_key
        message['From']=sender
        message['To']=', '.join(recipients)
        message['Message-ID']='<'+hashlib.sha256(ledger_key.encode()).hexdigest()+'@stock-research.local>'
        message.set_content((report/'latest.md').read_text())
        message.add_alternative((report/'latest.html').read_text(),subtype='html')
        message.add_attachment((report/'latest.csv').read_bytes(),maintype='text',subtype='csv',filename='stock-research.csv')
        stage='connect'
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=ssl.create_default_context(),timeout=45) as smtp:
            stage='authenticate'
            smtp.login(sender,password)
            stage='send'
            refused=smtp.send_message(message)
            if refused:
                raise RuntimeError('Partial recipient rejection')
            record['status']='delivered'
            stage='accepted'
    except Exception as error:
        record['status']='uncertain' if stage in {'send','accepted'} else 'failed'
        record['error_type']=type(error).__name__
        logging.error('email_failed stage=%s error_type=%s',stage,type(error).__name__)
        raise RuntimeError('Email delivery failed; inspect sanitized ledger') from None
    finally:
        record['stage']=stage
        write_json(state,ledger)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('action',choices=['reserve','send'])
    parser.add_argument('--state',default='state/delivery.json')
    parser.add_argument('--report',default='reports')
    parser.add_argument('--key',required=True)
    args=parser.parse_args()
    if args.action=='reserve':
        allowed=reserve(Path(args.state),Path(args.report),args.key)
        if os.getenv('GITHUB_OUTPUT'):
            with open(os.environ['GITHUB_OUTPUT'],'a') as output:
                output.write('send='+str(allowed).lower()+'\n')
    else:
        send(Path(args.state),Path(args.report),args.key)


if __name__=='__main__':
    main()
