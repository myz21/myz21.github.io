import re
import os
import bs4

files = ['index.html', 'about.html', 'journey.html', 'voluntary.html', 'awards.html', 'art.html', 'captures.html', 'projects.html']

print(f"{'File':<18} | {'Size (MB)':<10} | {'Base64 Fonts':<12} | {'Base64 Images':<13}")
print("-" * 65)

for fpath in files:
    if not os.path.exists(fpath):
        continue
    size_mb = os.path.getsize(fpath) / (1024 * 1024)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple regex count for data:font and data:image
    fonts_count = len(re.findall(r'data:font/[^;]+;base64,', content))
    images_count = len(re.findall(r'data:image/[^;]+;base64,', content))
    
    print(f"{fpath:<18} | {size_mb:<10.2f} | {fonts_count:<12} | {images_count:<13}")
