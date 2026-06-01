import bs4
import glob

for fpath in glob.glob("*.html"):
    with open(fpath, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    modified = False
    for img in soup.find_all('img'):
        src = img.get('src', '')
        if src.startswith('data:image'):
            img['src'] = 'assets/image_01068eba.webp'
            img['alt'] = '(Örnek Resim)'
            modified = True
            
    if modified:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
