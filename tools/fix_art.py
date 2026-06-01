from bs4 import BeautifulSoup

with open('art.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

grid = soup.find('div', class_='captures-grid')
if grid:
    grid.clear()
    
    items = [
        ("What U Consume", "./assets/art/what-u-consume.jpeg"),
        ("Sheeps", "./assets/art/sheeps.jpeg"),
        ("Os Femoris", "./assets/art/os-femoris.jpeg"),
        ("Os Calcaneus", "./assets/art/os-calcaneus.jpeg"),
        ("Cyberbullies", "./assets/art/cyberbullies.jpg")
    ]
    
    for title, src in items:
        item = soup.new_tag('div', attrs={'class': 'capture-item'})
        
        img_container = soup.new_tag('div', attrs={'class': 'capture-image-container'})
        img = soup.new_tag('img', src=src, alt=title, attrs={'class': 'capture-thumbnail', 'loading': 'lazy'})
        img_container.append(img)
        item.append(img_container)
        
        info = soup.new_tag('div', attrs={'class': 'capture-card-info'})
        
        title_span = soup.new_tag('h3', attrs={'style': 'margin: 0; font-size: 1.1em; color: var(--color-text-primary);'})
        title_span.string = title
        
        date_container = soup.new_tag('div', attrs={'class': 'capture-date-container'})
        date = soup.new_tag('span', attrs={'class': 'capture-card-date'})
        date.string = "Art Awards"
        date_container.append(date)
        
        info.append(title_span)
        info.append(date_container)
        
        item.append(info)
        grid.append(item)

with open('art.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Fixed art.html grid layout")
