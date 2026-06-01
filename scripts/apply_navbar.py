#!/usr/bin/env python3
"""Apply index.html navbar to all pages with correct active link + relative paths."""
import re
from bs4 import BeautifulSoup

PAGES = {
    'index.html':     'index.html',
    'about.html':     'index.html',   # about points to index
    'projects.html':  'projects.html',
    'journey.html':   'journey.html',
    'voluntary.html': 'voluntary.html',
    'awards.html':    'awards.html',
    'art.html':       'art.html',
    'captures.html':  'captures.html',
}

# Build canonical header from index.html
with open('index.html', 'r') as f:
    index_soup = BeautifulSoup(f.read(), 'html.parser')

ref_header = index_soup.find('header', class_='app-header')

def fix_abs_path(href):
    """Convert file:/// absolute paths to relative filenames."""
    if href and href.startswith('file:///'):
        return href.split('/')[-1]
    return href

def build_header(active_file):
    """Clone header and set correct active nav + relative paths."""
    h = BeautifulSoup(str(ref_header), 'html.parser').find('header')

    # Fix name-link href
    name_link = h.find('a', class_='name-link')
    if name_link:
        name_link['href'] = 'index.html'
        name_link['class'] = ['name-link']  # remove active from all first

    # Fix nav links
    nav = h.find('nav')
    if nav:
        for a in nav.find_all('a'):
            href = fix_abs_path(a.get('href', ''))
            a['href'] = href
            # Set active
            if href == active_file:
                a['class'] = ['active']
            else:
                a['class'] = [c for c in a.get('class', []) if c != 'active']

    return h

# Apply to each page
for filename, active in PAGES.items():
    try:
        with open(filename, 'r', encoding='utf-8', errors='replace') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        existing_header = soup.find('header', class_='app-header')
        new_header = build_header(active)

        if existing_header:
            existing_header.replace_with(new_header)
        else:
            # Insert at top of body
            soup.body.insert(0, new_header)

        with open(filename, 'w', encoding='utf-8', errors='replace') as f:
            f.write(str(soup))
        print(f'  ✓ {filename}  (active: {active})')
    except FileNotFoundError:
        print(f'  ⚠ {filename} not found, skipping')

print('\nDone!')
