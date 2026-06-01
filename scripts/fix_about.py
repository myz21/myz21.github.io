import bs4

with open('about.html', 'r', encoding="utf-8") as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

# Find the main tag
main = soup.find('main', class_='main-content')
if main:
    about_sec = main.find('div', class_='about-section')
    if about_sec:
        # Clear out all the existing content in about-section
        for child in about_sec.find_all(recursive=False):
            if child.name not in ['h1', 'img']:
                child.decompose()
        
        # Add new placeholder content
        h1 = about_sec.find('h1')
        if h1:
            h1.string = "(İsminiz)"
            
        p = soup.new_tag('p')
        p.string = "(Buraya kendiniz hakkında kısa bir açıklama yazabilirsiniz. Örneğin: Ben bir yazılım geliştiriciyim...)"
        about_sec.append(p)

# Also update the site title
title = soup.title
if title:
    title.string = "Portfolio Template"

# Update header names
name_links = soup.find_all('a', class_='name-link')
for link in name_links:
    link.string = "Adınız Soyadınız"

# Save about.html
with open('about.html', 'w', encoding="utf-8") as f:
    f.write(str(soup))

