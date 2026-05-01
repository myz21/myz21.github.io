import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's see if those strings exist
for q in ["Lipreader", "GesturePresent", "COMSATS", "Pawsy", "Selecta", "Uniserve"]:
    if q in html:
        print(f"Found {q} in index.html")
    else:
        print(f"NOT found {q} in index.html")
