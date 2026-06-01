#!/usr/bin/env python3
"""
Patch awards.html:
1. Fix video src: ./awards_files/datathon.mp4 -> ./assets/datathon.mp4
2. Fix broken card structure (ODTU card missing award-media-wrapper closure)
3. Ensure all referenced images exist in assets/
"""

from bs4 import BeautifulSoup
import re

with open('awards.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix video path
html = html.replace('./awards_files/datathon.mp4', './assets/datathon.mp4')

# 2. Parse with BS4 for structural fixes
soup = BeautifulSoup(html, 'html.parser')

# Fix all img src paths: assets/ references that don't have the awards_files prefix are fine
# But we need to check that the structure of each award-card is correct

cards = soup.find_all('div', class_='award-card')
print(f"Found {len(cards)} award cards")

for i, card in enumerate(cards):
    media_wrapper = card.find('div', class_='award-media-wrapper')
    award_info = card.find('div', class_='award-info')
    
    if not media_wrapper:
        print(f"Card {i+1}: Missing award-media-wrapper - attempting fix...")
        # Find the slider inside the card (possibly outside wrapper)
        slider = card.find('div', class_='award-slider')
        if slider:
            # Create wrapper, move slider into it
            wrapper = soup.new_tag('div', attrs={'class': 'award-media-wrapper'})
            slider.extract()
            wrapper.append(slider)
            # Insert at beginning of card
            if award_info:
                card.insert(0, wrapper)
            else:
                card.append(wrapper)
            print(f"  Fixed card {i+1}: created award-media-wrapper")
    else:
        slider = media_wrapper.find('div', class_='award-slider')
        if slider:
            slides = slider.find_all('div', class_='award-slide')
            print(f"Card {i+1}: {len(slides)} slides, title: {award_info.find('h3').text if award_info and award_info.find('h3') else 'N/A'}")

# 3. Re-check all image src paths
for img in soup.find_all('img'):
    src = img.get('src', '')
    if 'assets/' in src and not src.startswith('file://'):
        # relative path, fine
        pass
    elif 'awards_files/' in src:
        # Fix to assets/
        filename = src.split('/')[-1]
        img['src'] = f'./assets/{filename}'
        print(f"Fixed img src: {src} -> ./assets/{filename}")

# 4. Fix any video paths
for video in soup.find_all('video'):
    src = video.get('src', '')
    if 'awards_files/' in src:
        filename = src.split('/')[-1]
        video['src'] = f'./assets/{filename}'
        print(f"Fixed video src: {src} -> ./assets/{filename}")

with open('awards.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("\nDone! awards.html patched successfully.")
