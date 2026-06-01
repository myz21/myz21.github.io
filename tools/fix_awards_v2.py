#!/usr/bin/env python3
"""
Fix awards.html:
1. Uniform card sizes (consistent grid, fixed aspect ratio on media wrapper)
2. Add external link button to top-right corner of each card
"""

from bs4 import BeautifulSoup

LINKS = [
    "https://www.linkedin.com/feed/update/urn:li:activity:7365358690230501376/",
    "https://lnkd.in/dZVzU3Wx",
    "https://github.com/myz21/metu-sports-hackhaton",
    "https://www.linkedin.com/posts/myzz_dear-connections-i-finished-the-code-jam-activity-7290399937270308865-ghH9/",
    "https://lnkd.in/dAXxunMu",
    "https://lnkd.in/dZPajgkh",
]

with open('awards.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_='award-card')
print(f"Found {len(cards)} cards")

for i, card in enumerate(cards):
    link_url = LINKS[i] if i < len(LINKS) else "#"

    # --- 1. Add link button to top-right of card ---
    # Make card position:relative (via class, CSS handles it)
    # Insert an <a> tag as external link button
    existing_link = card.find('a', class_='card-ext-link')
    if not existing_link:
        link_tag = soup.new_tag('a',
            href=link_url,
            target='_blank',
            rel='noopener noreferrer',
            attrs={'class': 'card-ext-link', 'aria-label': 'Open link'}
        )
        # External link SVG icon
        link_tag.string = ''  # will be replaced by innerHTML trick below
        link_tag['data-href'] = link_url
        card.insert(0, link_tag)

print("Links added to all cards")

# --- 2. Inject/replace CSS for uniform sizing + link button style ---
# Remove old award-related style tags to avoid duplication
for style in soup.find_all('style'):
    content = style.string or ''
    if 'award-card' in content or 'awards-grid' in content:
        style.decompose()

new_style = soup.new_tag('style')
new_style.string = """
/* ===== AWARDS GRID ===== */
.awards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 24px;
    margin-top: 32px;
    align-items: start;
}

/* Uniform card */
.award-card {
    position: relative;
    background: var(--color-bg-secondary);
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-radius: 14px;
    overflow: hidden;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    display: flex;
    flex-direction: column;
}
.award-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
}

/* Fixed 16:9 media area for all cards */
.award-media-wrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    background: #000;
    flex-shrink: 0;
    overflow: hidden;
}

.award-slider {
    display: flex;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    scrollbar-width: none;
    width: 100%;
    height: 100%;
}
.award-slider::-webkit-scrollbar { display: none; }

.award-slide {
    flex: 0 0 100%;
    width: 100%;
    height: 100%;
    scroll-snap-align: center;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}
.award-slide img,
.award-slide video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}

/* Slider nav buttons */
.slider-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0, 0, 0, 0.55);
    color: #fff;
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
    font-size: 14px;
    line-height: 1;
    backdrop-filter: blur(4px);
}
.slider-nav:hover { background: rgba(0, 0, 0, 0.88); }
.slider-nav.prev { left: 8px; }
.slider-nav.next { right: 8px; }

/* Award info text area – fixed min-height so all cards feel equal */
.award-info {
    padding: 18px 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    flex-grow: 1;
    min-height: 110px;
}
.award-info h3 {
    margin: 0;
    font-size: 1.1em;
    font-weight: 700;
    color: var(--color-text-primary);
    line-height: 1.3;
    padding-right: 28px; /* space for link icon */
}
.award-info p {
    margin: 0;
    line-height: 1.55;
    color: var(--color-text-secondary);
    font-size: 0.9em;
}

/* ===== External link button (top-right of card) ===== */
.card-ext-link {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 20;
    width: 34px;
    height: 34px;
    background: rgba(0, 0, 0, 0.60);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-decoration: none;
    transition: background 0.2s, transform 0.2s;
    backdrop-filter: blur(6px);
}
.card-ext-link:hover {
    background: rgba(30, 30, 30, 0.92);
    transform: scale(1.1);
}
.card-ext-link svg {
    width: 16px;
    height: 16px;
    stroke: currentColor;
    fill: none;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
}
"""
soup.head.append(new_style)

# --- 3. Replace link tag text with SVG icon (BS4 workaround) ---
for link_tag in soup.find_all('a', class_='card-ext-link'):
    link_tag.clear()
    # Create SVG inline
    svg_str = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'''
    svg_soup = BeautifulSoup(svg_str, 'html.parser')
    link_tag.append(svg_soup.svg)
    # Restore correct href
    href = link_tag.get('data-href', '#')
    link_tag['href'] = href
    del link_tag['data-href']

# --- 4. Fix slider JS (ensure it's present and correct) ---
# Remove old script tags that handle slider
for script in soup.find_all('script'):
    if 'award-media-wrapper' in (script.string or ''):
        script.decompose()

new_script = soup.new_tag('script')
new_script.string = """
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.award-media-wrapper').forEach(function(wrapper) {
        var slider = wrapper.querySelector('.award-slider');
        var prev = wrapper.querySelector('.prev');
        var next = wrapper.querySelector('.next');
        if (!slider) return;
        if (prev) {
            prev.addEventListener('click', function() {
                slider.scrollBy({ left: -slider.clientWidth, behavior: 'smooth' });
            });
        }
        if (next) {
            next.addEventListener('click', function() {
                slider.scrollBy({ left: slider.clientWidth, behavior: 'smooth' });
            });
        }
    });
});
"""
soup.body.append(new_script)

with open('awards.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("awards.html updated: uniform sizing + link buttons added.")
