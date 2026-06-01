#!/usr/bin/env python3
"""
1. Kart sliderlarına yeni görseller ekle
2. Tüm görsellerde object-fit:cover + object-position:center uygula
"""

from bs4 import BeautifulSoup
import os

CARD_UPDATES = {
    # title_fragment : [ yeni görsel yolları ]
    "TEKNOFEST":   ["awards_files/zenith.jpg", "awards_files/1758305830876.jpeg"],
    "Vodafone":    ["awards_files/IMG-20251215-WA0039.jpg"],
    "ODTU":        ["awards_files/20260520_023904.jpg"],
    "Happy":       ["awards_files/hhs2.jpeg"],
}

with open('awards.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_='award-card')
print(f"Found {len(cards)} cards")

for card in cards:
    h3 = card.find('h3')
    title = h3.text.strip() if h3 else ""

    matched_key = None
    for key in CARD_UPDATES:
        if key in title:
            matched_key = key
            break

    if not matched_key:
        continue

    slider = card.find('div', class_='award-slider')
    if not slider:
        print(f"  ⚠ No slider found in: {title}")
        continue

    for img_path in CARD_UPDATES[matched_key]:
        abs_path = os.path.abspath(img_path)
        if not os.path.exists(abs_path):
            print(f"  ⚠ File not found: {abs_path}")
            continue

        slide_div = soup.new_tag('div', attrs={'class': 'award-slide'})
        img_tag = soup.new_tag('img',
            src=img_path,
            alt=matched_key,
            loading='lazy'
        )
        slide_div.append(img_tag)
        slider.append(slide_div)
        print(f"  ✓ Added slide to '{title[:30]}': {img_path}")

# CSS güncellemesi: object-position center ekle + slide sayısına göre nav göster
for style in soup.find_all('style'):
    c = style.string or ''
    if 'award-slide img' in c:
        updated = c.replace(
            'object-fit: cover;',
            'object-fit: cover;\n    object-position: center center;'
        )
        style.string = updated
        print("  ✓ Added object-position: center to images")
        break

with open('awards.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("\nDone! awards.html updated.")
