#!/usr/bin/env python3
"""
Smart link icons on award cards:
- GitHub links  → GitHub logo
- YouTube links → YouTube logo
- Demo/generic  → external link icon (current)
- Global AI Hub → 2 buttons: LinkedIn + YouTube
"""

from bs4 import BeautifulSoup

# ── SVG definitions ──────────────────────────────────────────────────────────
SVG_EXTERNAL = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>'

SVG_GITHUB = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 496 512"><path fill="currentColor" d="M165.9 397.4c0 2-2.3 3.6-5.2 3.6-3.3.3-5.6-1.3-5.6-3.6 0-2 2.3-3.6 5.2-3.6 3-.3 5.6 1.3 5.6 3.6zm-31.1-4.5c-.7 2 1.3 4.3 4.3 4.9 2.6 1 5.6 0 6.2-2s-1.3-4.3-4.3-5.2c-2.6-.7-5.5.3-6.2 2.3zm44.2-1.7c-2.9.7-4.9 2.6-4.6 4.9.3 2 2.9 3.3 5.9 2.6 2.9-.7 4.9-2.6 4.6-4.6-.3-1.9-3-3.2-5.9-2.9zM244.8 8C106.1 8 0 113.3 0 252c0 110.9 69.8 205.8 169.5 239.2 12.8 2.3 17.3-5.6 17.3-12.1 0-6.2-.3-40.4-.3-61.4 0 0-70 15-84.7-29.8 0 0-11.4-29.1-27.8-36.6 0 0-22.9-15.7 1.6-15.4 0 0 24.9 2 38.6 25.8 21.9 38.6 58.6 27.5 72.9 20.9 2.3-16 8.8-27.1 16-33.7-55.9-6.2-112.3-14.3-112.3-110.5 0-27.5 7.6-41.3 23.6-58.9-2.6-6.5-11.1-33.3 2.6-67.9 20.9-6.5 69 27 69 27 20-5.6 41.5-8.5 62.8-8.5s42.8 2.9 62.8 8.5c0 0 48.1-33.6 69-27 13.7 34.7 5.2 61.4 2.6 67.9 16 17.7 25.8 31.5 25.8 58.9 0 96.5-58.9 104.2-114.8 110.5 9.2 7.9 17 22.9 17 46.4 0 33.7-.3 75.4-.3 83.6 0 6.5 4.6 14.4 17.3 12.1C428.2 457.8 496 362.9 496 252 496 113.3 383.5 8 244.8 8z"/></svg>'

SVG_YOUTUBE = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path fill="currentColor" d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z"/></svg>'

# ── Card config: (primary_href, primary_icon, optional extra buttons) ─────────
CARDS = [
    # (title_fragment, primary_href, primary_svg, extra_buttons)
    ("TEKNOFEST",   "https://www.linkedin.com/feed/update/urn:li:activity:7365358690230501376/", SVG_EXTERNAL, []),
    ("Vodafone",    "https://lnkd.in/dZVzU3Wx",                                                SVG_EXTERNAL, []),
    ("ODTU",        "https://github.com/myz21/metu-sports-hackhaton",                           SVG_GITHUB,   []),
    ("Happy",       "https://www.linkedin.com/posts/myzz_dear-connections-i-finished-the-code-jam-activity-7290399937270308865-ghH9/", SVG_EXTERNAL, []),
    ("Hacettepe",   "https://lnkd.in/dAXxunMu",                                                SVG_EXTERNAL, []),
    ("Global",      "https://lnkd.in/dZPajgkh",                                                SVG_EXTERNAL,
     [("https://lnkd.in/dzPcf-uJ", SVG_YOUTUBE, "YouTube Live Stream", "yt")]),
]

with open('awards.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all('div', class_='award-card')
print(f"Processing {len(cards)} cards...")

for i, card in enumerate(cards):
    if i >= len(CARDS):
        break

    title_frag, href, svg_str, extras = CARDS[i]

    # Remove all existing card-ext-link buttons
    for old in card.find_all('a', class_='card-ext-link'):
        old.decompose()

    # Helper to create a link button
    def make_btn(url, svg, aria, extra_class=""):
        btn = soup.new_tag('a',
            href=url, target='_blank', rel='noopener noreferrer',
            attrs={'class': f'card-ext-link {extra_class}'.strip(), 'aria-label': aria}
        )
        btn.append(BeautifulSoup(svg, 'html.parser'))
        return btn

    # Build button group wrapper
    group = soup.new_tag('div', attrs={'class': 'card-link-group'})

    # Primary button
    group.append(make_btn(href, svg_str, f'Open {title_frag} link'))

    # Extra buttons (e.g. YouTube)
    for (ex_href, ex_svg, ex_aria, ex_cls) in extras:
        group.append(make_btn(ex_href, ex_svg, ex_aria, ex_cls))

    card.insert(0, group)
    h3 = card.find('h3')
    print(f"  Card {i+1} ({h3.text[:30] if h3 else '?'}): primary + {len(extras)} extra btn(s)")

# ── Inject / replace CSS for link group & icons ──────────────────────────────
for style in soup.find_all('style'):
    c = style.string or ''
    if 'card-ext-link' in c or 'awards-grid' in c:
        style.decompose()

new_style = soup.new_tag('style')
new_style.string = """
/* ===== AWARDS GRID ===== */
.awards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
    gap: 24px;
    margin-top: 32px;
    align-items: start;
}

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

/* Fixed 16:9 media area */
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

/* Slider nav */
.slider-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background: rgba(0,0,0,0.55);
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
    backdrop-filter: blur(4px);
}
.slider-nav:hover { background: rgba(0,0,0,0.88); }
.slider-nav.prev { left: 8px; }
.slider-nav.next { right: 8px; }

/* Award info */
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
    padding-right: 80px; /* room for buttons */
}
.award-info p {
    margin: 0;
    line-height: 1.55;
    color: var(--color-text-secondary);
    font-size: 0.9em;
}

/* ===== Link button group (top-right) ===== */
.card-link-group {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 20;
    display: flex;
    gap: 6px;
}

.card-ext-link {
    width: 34px;
    height: 34px;
    background: rgba(0,0,0,0.60);
    border: 1px solid rgba(255,255,255,0.18);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    text-decoration: none;
    transition: background 0.2s, transform 0.15s;
    backdrop-filter: blur(6px);
}
.card-ext-link:hover {
    background: rgba(30,30,30,0.92);
    transform: scale(1.12);
}
.card-ext-link svg {
    width: 17px;
    height: 17px;
    fill: currentColor;
    display: block;
}

/* YouTube button — red tint on hover */
.card-ext-link.yt:hover {
    background: rgba(255,0,0,0.75);
    border-color: rgba(255,80,80,0.5);
}
"""
soup.head.append(new_style)

# ── Re-add slider JS ─────────────────────────────────────────────────────────
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
        if (prev) prev.addEventListener('click', function() {
            slider.scrollBy({ left: -slider.clientWidth, behavior: 'smooth' });
        });
        if (next) next.addEventListener('click', function() {
            slider.scrollBy({ left: slider.clientWidth, behavior: 'smooth' });
        });
    });
});
"""
soup.body.append(new_script)

with open('awards.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("\nawards.html updated with smart link icons!")
