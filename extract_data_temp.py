import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('Lipreader')
if idx != -1:
    print(html[idx-1000:idx+2000])
