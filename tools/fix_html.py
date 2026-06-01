import bs4
import glob

# 1. Update links across all files:
for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        html = f.read()
    
    html = html.replace('href="captures.html"', 'href="art.html"')
    html = html.replace('>captures</a>', '>art</a>')
    html = html.replace('>Captures</a>', '>Art</a>')
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(html)

# 2. Modify art.html
with open('art.html', 'r', encoding="utf-8") as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

# Change title
if soup.title:
    soup.title.string = "Art - Yusuf Danis"

for h1 in soup.find_all('h1'):
    if 'Captures' in h1.text:
        h1.string = h1.text.replace('Captures', 'Art')

# Remove texts from about-section in art
about_section = soup.find('div', class_='about-section')
if about_section:
    for p in about_section.find_all('p', recursive=False):
        p.string = "(Buraya kendi sanat eserlerinizin açıklamasını yazabilirsiniz.)"

# Find gallery items and keep only 1
gallery = soup.find('div', class_='gallery')
if gallery:
    items = gallery.find_all('div', class_='gallery-item')
    if items:
        # Keep the first one
        first_item = items[0]
        # Remove others
        for item in items[1:]:
            item.decompose()

# Save art.html
with open('art.html', 'w', encoding="utf-8") as f:
    f.write(str(soup))
