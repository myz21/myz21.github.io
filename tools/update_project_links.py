from bs4 import BeautifulSoup
import re

link_map = {
    'GPT': 'https://github.com/myz21/GPT',
    'privacy-policy-analyzer': 'https://github.com/myz21/privacy-policy-analyzer',
    'SkateSync AI': 'https://mutlubilet.com/',
    'AYBUStore': 'https://github.com/myz21/AYBUStore',
    'LetMeFind': 'https://github.com/myz21/LetMeFind',
    'Endpoint Detector': 'https://github.com/myz21/Energy-Based-EndPoint-Detection',
    'DoctorGPT': 'https://github.com/myz21/DoctorGPT',
    'micrograd': 'https://github.com/myz21/micrograd',
    'Spikeflight': 'https://github.com/myz21/Spikeflight',
    'The Traitor': 'https://github.com/myz21/The-Traitor',
}

file_path = '/home/neo/Downloads/yusuf_site/projects.html'

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_='card-info')

for card in cards:
    title_el = card.find('a', class_='project-title-link')
    if not title_el:
        continue
    
    title_text = title_el.get_text(strip=True)
    if title_text in link_map:
        new_url = link_map[title_text]
        # Update title link
        title_el['href'] = new_url
        
        # Also update external link icon if it exists
        ext_link = card.find('a', class_='project-external-link-icon')
        if ext_link:
            ext_link['href'] = new_url
        else:
            # Create external link icon and insert it before the h2
            new_ext_link = soup.new_tag('a', href=new_url, target='_blank', rel='noopener', **{'aria-label': f'Visit {title_text} (opens in new tab)'})
            new_ext_link['class'] = ['project-external-link-icon']
            icon_img = soup.new_tag('img', src='assets/icon_340d47e3.svg')
            new_ext_link.append(icon_img)
            
            h2 = card.find('h2', class_='card-title')
            h2.insert_before(new_ext_link)
            # Add a newline
            h2.insert_before('\n')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Links updated successfully.")
