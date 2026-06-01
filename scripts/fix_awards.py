from bs4 import BeautifulSoup

with open('awards.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

about = soup.find('div', class_='about-section')
if not about:
    print("Could not find about-section")
    exit(1)

# Extract sections
# A section starts with <h3>, followed by <p> (description), then some <p><img></p> or text
sections = []
current_section = None

# Skip the initial h1 and intro text
for el in about.children:
    if el.name == 'h3':
        if current_section:
            sections.append(current_section)
        current_section = {'title': el.get_text().strip(), 'desc': '', 'media': []}
    elif el.name == 'p' and current_section is not None:
        if el.find('img'):
            current_section['media'].append({'type': 'img', 'src': el.find('img')['src']})
        elif 'PROMPT:' in el.get_text():
            if 'datathon.mp4' in el.get_text().lower() or 'awards_files' in el.get_text().lower():
                current_section['media'].append({'type': 'video', 'src': './awards_files/datathon.mp4'})
        else:
            current_section['desc'] += el.get_text().strip() + " "

if current_section:
    sections.append(current_section)

# Rebuild the HTML
about.clear()

h1 = soup.new_tag('h1')
hashtag = soup.new_tag('span', attrs={'class': 'title-hashtag'})
hashtag.string = '#'
h1.append(hashtag)
h1.append(" Awards")
about.append(h1)

intro = soup.new_tag('p')
intro.string = "Welcome to my achievements. I have proven my engineering skills by solving complex algorithmic problems under tight deadlines in various competitions."
about.append(intro)

grid = soup.new_tag('div', attrs={'class': 'awards-grid'})

for sec in sections:
    card = soup.new_tag('div', attrs={'class': 'award-card'})
    
    media_wrapper = soup.new_tag('div', attrs={'class': 'award-media-wrapper'})
    
    slider = soup.new_tag('div', attrs={'class': 'award-slider'})
    
    for m in sec['media']:
        slide = soup.new_tag('div', attrs={'class': 'award-slide'})
        if m['type'] == 'img':
            media_el = soup.new_tag('img', src=m['src'], attrs={'loading': 'lazy'})
            slide.append(media_el)
        elif m['type'] == 'video':
            media_el = soup.new_tag('video', src=m['src'], controls="", preload="metadata")
            slide.append(media_el)
        slider.append(slide)
    
    media_wrapper.append(slider)
    
    if len(sec['media']) > 1:
        prev_btn = soup.new_tag('button', attrs={'class': 'slider-nav prev', 'aria-label': 'Previous'})
        prev_btn.string = '<'
        next_btn = soup.new_tag('button', attrs={'class': 'slider-nav next', 'aria-label': 'Next'})
        next_btn.string = '>'
        media_wrapper.append(prev_btn)
        media_wrapper.append(next_btn)
        
    card.append(media_wrapper)
    
    info = soup.new_tag('div', attrs={'class': 'award-info'})
    title_el = soup.new_tag('h3')
    title_el.string = sec['title']
    desc_el = soup.new_tag('p')
    desc_el.string = sec['desc'].strip()
    info.append(title_el)
    info.append(desc_el)
    card.append(info)
    
    grid.append(card)

about.append(grid)

# Add CSS and JS
style_tag = soup.new_tag('style')
style_tag.string = """
.awards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 24px;
    margin-top: 32px;
}
.award-card {
    background: var(--color-bg-secondary);
    border: 1px solid rgba(255, 255, 255, 0.05);
    border-radius: 12px;
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
}
.award-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
.award-media-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #000;
}
.award-slider {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scrollbar-width: none; /* Firefox */
    width: 100%;
    height: 100%;
}
.award-slider::-webkit-scrollbar {
    display: none; /* Chrome, Safari */
}
.award-slide {
    flex: 0 0 100%;
    width: 100%;
    height: 100%;
    scroll-snap-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
}
.award-slide img, .award-slide video {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.slider-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.6);
    color: white;
    border: none;
    border-radius: 50%;
    width: 32px;
    height: 32px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 10;
    transition: background 0.2s;
    font-weight: bold;
}
.slider-nav:hover {
    background: rgba(0, 0, 0, 0.9);
}
.slider-nav.prev {
    left: 8px;
}
.slider-nav.next {
    right: 8px;
}
.award-info {
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
    flex-grow: 1;
}
.award-info h3 {
    margin: 0;
    font-size: 1.25em;
    font-weight: 600;
    color: var(--color-text-primary);
}
.award-info p {
    margin: 0;
    line-height: 1.5;
    color: var(--color-text-secondary);
    font-size: 0.95em;
}
"""
soup.head.append(style_tag)

script_tag = soup.new_tag('script')
script_tag.string = """
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.award-media-wrapper').forEach(wrapper => {
        const slider = wrapper.querySelector('.award-slider');
        const prev = wrapper.querySelector('.prev');
        const next = wrapper.querySelector('.next');
        if (!slider || !prev || !next) return;
        
        prev.addEventListener('click', () => {
            slider.scrollBy({ left: -slider.clientWidth, behavior: 'smooth' });
        });
        next.addEventListener('click', () => {
            slider.scrollBy({ left: slider.clientWidth, behavior: 'smooth' });
        });
    });
});
"""
soup.body.append(script_tag)

with open('awards.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully generated awards.html layout.")
