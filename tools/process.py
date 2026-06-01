import bs4
import re

files_to_process = {
    '../yusuf-single/site/about.html': 'about.html',
    '../yusuf-single/site/projects.html': 'projects.html',
    '../yusuf-single/site/journey.html': 'journey.html',
    '../yusuf-single/site/captures.html': 'art.html'
}

for src, dst in files_to_process.items():
    with open(src, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
    
    # Remove Monica/MaxAI elements
    for el in soup.find_all(class_=re.compile("use-chat-gpt-ai|max-ai|maxai")):
        el.decompose()

    # Remove all inline scripts and styles from the original heavy files
    # because we want to use the extracted css/js!
    for script in soup.find_all('script'):
        script.decompose()
    for style in soup.find_all('style'):
        style.decompose()

    # Link the stylesheet
    css_name = dst.replace('.html', '.css')
    link = soup.new_tag('link', rel='stylesheet', href=f'css/{css_name}')
    if soup.head:
        soup.head.append(link)
    
    # Generic meta updates
    if soup.title:
        soup.title.string = "Portfolio Template"
    for a in soup.find_all('a', class_='name-link'):
        a.string = "(Adınız Soyadınız)"
    
    # Fix navigation links
    for a in soup.find_all('a'):
        if a.get('href') and 'yusuf.md' in a['href']:
            href = a['href']
            if '/journey' in href: a['href'] = 'journey.html'
            elif '/projects' in href: a['href'] = 'projects.html'
            elif '/art' in href or '/captures' in href: a['href'] = 'art.html'
            elif href.endswith('yusuf.md') or href.endswith('yusuf.md/'): a['href'] = 'about.html'

    # Content replacements based on file type
    if dst == 'about.html':
        about_sec = soup.find('div', class_='about-section')
        if about_sec:
            for child in about_sec.find_all(recursive=False):
                if child.name == 'p':
                    child.string = "(Buraya kendiniz hakkında kısa bir açıklama yazabilirsiniz. Örneğin: Ben bir yazılım geliştiriciyim...)"
                elif child.name == 'h1':
                    child.string = "(İsminiz)"
    elif dst == 'projects.html':
        cards_container = soup.find('div', class_='cards')
        if cards_container:
            cards = cards_container.find_all('div', class_='card', recursive=False)
            if cards:
                # Keep first card, remove others
                for c in cards[1:]:
                    c.decompose()
                
                # Edit the first card to be a template
                c = cards[0]
                title = c.find('h2')
                if title: title.string = "(Proje Adı)"
                desc = c.find('p', class_='card-description')
                if desc: desc.string = "(Buraya proje açıklamanızı yazın)"
                date = c.find('div', class_='project-date-container')
                if date: date.string = "(Tarih / Yıl)"
    elif dst == 'journey.html':
        # the journey items
        items = soup.find_all('div', class_='journey-item')
        if items:
            for item in items[1:]:
                item.decompose()
            item = items[0]
            title = item.find('h3')
            if title: title.string = "(Deneyim / Okul / Etkinlik Adı)"
            desc = item.find('p')
            if desc: desc.string = "(Buraya detayları yazabilirsiniz)"
            date = item.find('span', class_='date')
            if date: date.string = "(Başlangıç - Bitiş)"
    elif dst == 'art.html':
        if soup.title: soup.title.string = "Art - Portfolio Template"
        for h1 in soup.find_all('h1'):
            if 'Captures' in h1.text:
                h1.string = 'Art'
        # art items
        gallery = soup.find('div', class_='gallery')
        if gallery:
            items = gallery.find_all('div', class_='gallery-item')
            if items:
                for item in items[1:]:
                    item.decompose()

    with open(dst, 'w', encoding='utf-8') as f:
        f.write(str(soup))
