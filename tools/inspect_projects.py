import bs4

with open('../yusuf-single/site/projects.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

print("Classes of divs:", set([tuple(d.get('class', [])) for d in soup.find_all('div') if d.get('class')]))
