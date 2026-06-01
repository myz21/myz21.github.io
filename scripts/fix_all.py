import bs4
import glob

for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')

    # Update name links
    for link in soup.find_all('a', class_='name-link'):
        link.string = "Adınız Soyadınız"

    # Update title based on page
    title = soup.title
    if title:
        if fpath == "about.html":
            title.string = "Hakkımda - Portfolio"
        elif fpath == "projects.html":
            title.string = "Projeler - Portfolio"
        elif fpath == "journey.html":
            title.string = "Geçmiş - Portfolio"
        elif fpath == "art.html":
            title.string = "Sanat - Portfolio"

    # Remove meta description and og tags containing my name or replace with template
    for meta in soup.find_all('meta'):
        if meta.get('name') in ['description', 'author']:
            meta['content'] = "(Buraya açıklamanızı/adınızı ekleyin)"
        elif meta.get('property', '').startswith('og:'):
            if meta.get('property') == 'og:title':
                meta['content'] = "Portfolio Template"
            elif meta.get('property') == 'og:description':
                meta['content'] = "(Buraya kısa bir açıklama ekleyin)"
            elif meta.get('property') == 'og:url':
                meta['content'] = "https://siteniz.com"

    # Add comments at the top
    comment = bs4.Comment(" Bu bir portfolio template dosyasıdır. Kendi içeriğinize göre düzenleyebilirsiniz. ")
    soup.insert(0, comment)
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(str(soup))

