from bs4 import BeautifulSoup

# read about.html to get the style block
with open('/home/neo/Downloads/yusuf_site/about.html', 'r', encoding='utf-8') as f:
    about_soup = BeautifulSoup(f.read(), 'html.parser')
    main_style = about_soup.find('style')

with open('/home/neo/Downloads/yusuf_site/projects.html', 'r', encoding='utf-8') as f:
    proj_soup = BeautifulSoup(f.read(), 'html.parser')

# Check if the main_style is already there. The main style starts with :root {
# If not, insert it.
existing_styles = proj_soup.find_all('style')
proj_style = existing_styles[0] if existing_styles else None

if main_style and proj_style:
    # insert before proj_style
    proj_style.insert_before(main_style)
    with open('/home/neo/Downloads/yusuf_site/projects.html', 'w', encoding='utf-8') as f:
        f.write(str(proj_soup))
    print("Injected CSS into projects.html")
else:
    print("Could not find style tags")
