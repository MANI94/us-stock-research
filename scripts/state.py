"""Durable state branch helper. Never force pushes or executes state-branch code."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess


def git(*args: str, cwd: str | None=None) -> str:
    result=subprocess.run(['git',*args],cwd=cwd,check=True,text=True,capture_output=True)
    return result.stdout.strip()


def load() -> None:
    # Distinguish an absent branch from a transport/authentication failure.
    remote=git('ls-remote','--heads','origin','refs/heads/research-state')
    if remote:
        git('fetch','--depth=1','origin','research-state')
        git('worktree','add','--detach','state','FETCH_HEAD')
    else:
        Path('state').mkdir()
        git('init',cwd='state')
        git('checkout','--orphan','research-state',cwd='state')
        git('remote','add','origin',git('remote','get-url','origin'),cwd='state')
        # Reuse checkout's HTTP authorization without copying credentials into files.
        entries=git('config','--get-regexp',r'^http\..*\.extraheader$') if os.getenv('GITHUB_ACTIONS') else ''
        for entry in entries.splitlines():
            key,value=entry.split(' ',1)
            git('config',key,value,cwd='state')
    git('config','user.name','github-actions[bot]',cwd='state')
    git('config','user.email','41898282+github-actions[bot]@users.noreply.github.com',cwd='state')


def persist() -> None:
    git('add','--all',cwd='state')
    if git('status','--porcelain',cwd='state'):
        git('commit','-m','Persist research snapshot and delivery status [skip ci]',cwd='state')
        git('push','origin','HEAD:refs/heads/research-state',cwd='state')


def snapshot() -> None:
    src=Path('run-output')
    report=json.loads((src/'reports/latest.json').read_text())
    prefix=Path('state/manual')/os.environ['GITHUB_RUN_ID'] if os.getenv('TICKER_OVERRIDE','').strip() else Path('state')
    for name in ('reports','history'):
        shutil.copytree(src/name,prefix/name,dirs_exist_ok=True)
    key=report['report_date']+('-manual-'+os.environ['GITHUB_RUN_ID'] if os.getenv('TICKER_OVERRIDE','').strip() else '')
    with open(os.environ['GITHUB_OUTPUT'],'a') as output:
        output.write('key='+key+'\n')
        output.write('email_enabled='+str(report['settings']['enable_email']).lower()+'\n')


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('action',choices=['load','persist','snapshot'])
    action=parser.parse_args().action
    try:
        {'load':load,'persist':persist,'snapshot':snapshot}[action]()
    except subprocess.CalledProcessError:
        raise SystemExit('State Git operation failed; refusing to continue') from None
