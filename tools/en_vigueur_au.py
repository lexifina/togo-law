"""Prints the law of Togo as it stood on a given day, read from this repository's history.

    python tools/en_vigueur_au.py 2022-01-01 code-du-travail 190        # art. 190 before Loi n° 2022-019
    python tools/en_vigueur_au.py 2023-01-01 code-du-travail art-190    # the same article, as replaced
    python tools/en_vigueur_au.py 2020-01-01 donnees-personnelles       # the whole Loi n° 2019-014 on 1 January 2020
    python tools/en_vigueur_au.py --law 2023-01-01 code-du-travail 190  # also name the law behind that wording

A thin wrapper around tools/on.py: the version is chosen by each commit's `In-force:` trailer, never by its commit
date, and branches named wip* are ignored. A bare article number (`55`) means the file `art-055`. Standard library
only.
"""
import re
import runpy
import subprocess
import sys
from pathlib import Path


def article(act: str, unit: str) -> str:
    m = re.fullmatch(r'(\d+)(-?[a-z-]*)', unit)
    if not m:
        return unit
    files = set()
    for ref in ('main', 'futur'):
        out = subprocess.run(['git', 'ls-tree', '-r', '--name-only', ref, f'{act}/'], capture_output=True,
                             text=True, encoding='utf-8')
        files.update(out.stdout.split())
    suffix = '-' + m.group(2).lstrip('-') if m.group(2) else ''
    for width in (3, 4):
        key = f'art-{int(m.group(1)):0{width}d}{suffix}'
        if f'{act}/{key}.md' in files:
            return key
    return unit


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    args = [a for a in sys.argv[1:] if a != '--law']
    if len(args) == 3:
        i = len(sys.argv) - 1 - sys.argv[::-1].index(args[2])
        sys.argv[i] = article(args[1], args[2])
    sys.argv[0] = str(Path(__file__).with_name('on.py'))
    runpy.run_path(sys.argv[0], run_name='__main__')
