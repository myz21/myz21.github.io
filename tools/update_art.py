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
        
        img = soup.new_tag('img', src=src, alt=title, attrs={'class': 'capture-img'})
        item.append(img)
        
        overlay = soup.new_tag('div', attrs={'class': 'capture-overlay'})
        loc = soup.new_tag('span', attrs={'class': 'capture-location'})
        loc.string = title
        date = soup.new_tag('span', attrs={'class': 'capture-date'})
        date.string = "Art Awards"
        
        overlay.append(loc)
        overlay.append(date)
        item.append(overlay)
        
        grid.append(item)

with open('art.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Updated art.html")
