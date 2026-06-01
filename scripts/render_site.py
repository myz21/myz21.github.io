#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pages.renderers import render_all

if __name__ == '__main__':
    render_all()
    print('rendered: projects, journey, voluntary, awards, art, captures')
