#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.pages.renderers import render_timeline_page

if __name__ == '__main__':
    render_timeline_page('journey', 'journey.json')
    render_timeline_page('voluntary', 'voluntary.json')
    print('rendered: journey, voluntary')
