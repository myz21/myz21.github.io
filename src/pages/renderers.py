from __future__ import annotations

import json
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / 'data'

CAROUSEL_JS = """
function setSlidePosition(wrapper, idx) {
  const slider = wrapper.querySelector('.award-slider');
  if (!slider) return;
  slider.dataset.idx = idx;
  slider.style.transform = `translateX(-${idx * wrapper.clientWidth}px)`;
}
function prevSlide(btn) {
  const wrapper = btn.closest('.award-media-wrapper');
  const slider  = wrapper.querySelector('.award-slider');
  const slides  = slider.querySelectorAll('.award-slide');
  let idx = parseInt(slider.dataset.idx || 0);
  idx = (idx - 1 + slides.length) % slides.length;
  setSlidePosition(wrapper, idx);
}
function nextSlide(btn) {
  const wrapper = btn.closest('.award-media-wrapper');
  const slider  = wrapper.querySelector('.award-slider');
  const slides  = slider.querySelectorAll('.award-slide');
  let idx = parseInt(slider.dataset.idx || 0);
  idx = (idx + 1) % slides.length;
  setSlidePosition(wrapper, idx);
}
function syncAllSliders() {
  document.querySelectorAll('.award-media-wrapper').forEach((wrapper) => {
    const slider = wrapper.querySelector('.award-slider');
    if (!slider) return;
    const idx = parseInt(slider.dataset.idx || 0);
    setSlidePosition(wrapper, idx);
  });
}
window.addEventListener('load', syncAllSliders);
window.addEventListener('resize', syncAllSliders);
"""

PROJECT_STYLE = """
.projects-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:30px;width:100%;max-width:960px;margin:30px 0 0}
.project-card{background:var(--color-bg-primary);border:1px solid var(--color-border-primary);border-radius:12px;box-shadow:0 2px 6px var(--shadow-light);padding:20px 20px 14px;transition:border-color .25s ease,box-shadow .25s ease,transform .25s ease;min-height:100%}
.project-card:hover{border-color:var(--color-secondary);box-shadow:0 8px 22px var(--shadow-light);transform:translateY(-2px)}
.project-card-head{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:8px}
.project-link-icon{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:10px;border:1px solid var(--color-border-primary);background:var(--color-bg-secondary);flex-shrink:0}
.project-link-icon img{width:18px;height:18px;display:block}
.project-title{font-size:1.3rem;font-weight:700;line-height:1.3;margin:0}.project-title-link{color:var(--color-text-primary);text-decoration:underline;text-decoration-color:var(--color-secondary)!important;text-decoration-thickness:3px;text-underline-offset:4px}
.project-tags{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 12px}.project-tag{display:inline-flex;align-items:center;padding:4px 8px;border-radius:16px;font-size:.8rem;font-weight:400;line-height:1.8;background:var(--color-bg-light);color:var(--color-text-tertiary);border:1px solid var(--color-border-primary)}
.project-desc{font-size:1rem;font-weight:600;line-height:1.8;color:var(--color-text-tertiary);margin:0 0 12px}.project-meta{display:flex;justify-content:flex-end;align-items:center;margin-top:auto}.project-date{font-size:.8rem;font-weight:300;line-height:1.8;color:var(--color-text-light)}
[data-theme="dark"] .project-card{background:#1c1c1e;border-color:#333;box-shadow:0 2px 6px rgba(255,255,255,.08)}[data-theme="dark"] .project-link-icon{background:#2c2c2e;border-color:#333}[data-theme="dark"] .project-tag{background:#58585c;border-color:#333;color:#aaa}[data-theme="dark"] .project-desc{color:#aaa}[data-theme="dark"] .project-date{color:#999}
@media (max-width: 900px){.projects-grid{grid-template-columns:1fr;max-width:100%}}@media (max-width: 640px){.project-card{padding:18px}.project-card-head{gap:12px}.project-title{font-size:1.15rem}}
"""


def load_json(name: str):
    return json.loads((DATA_DIR / name).read_text(encoding='utf-8'))


def ensure_shared_stylesheet(soup: BeautifulSoup):
    if not soup.find('link', href='assets/styles/main.css'):
        link = soup.new_tag('link', rel='stylesheet', href='assets/styles/main.css')
        soup.head.append(link)


def ensure_local_connect_csp(soup: BeautifulSoup):
    meta = soup.find('meta', attrs={'http-equiv': lambda value: value and value.lower() == 'content-security-policy'})
    if not meta:
        return
    content = meta.get('content', '')
    if 'connect-src' in content:
        return
    rule = " connect-src 'self' http://localhost:8081 ws://localhost:8081;"
    if ' script-src ' in content:
        content = content.replace(' script-src ', f'{rule} script-src ', 1)
    elif ' object-src ' in content:
        content = content.replace(' object-src ', f'{rule} object-src ', 1)
    else:
        content = content.rstrip(';') + ';' + rule
    meta['content'] = content


def clean_legacy_scripts(soup: BeautifulSoup):
    for tag in list(soup.find_all('script')):
        text = tag.get_text()
        if (
            'function prevSlide' in text
            or 'function nextSlide' in text
            or "document.querySelectorAll('.carousel')" in text
            or 'setSlidePosition' in text
            or "document.querySelectorAll('.award-media-wrapper')" in text
            or 'syncAllSliders' in text
        ):
            tag.decompose()


def clean_legacy_styles(soup: BeautifulSoup, markers: list[str]):
    for tag in list(soup.find_all('style')):
        text = tag.get_text()
        if any(marker in text for marker in markers):
            tag.decompose()


def build_blur_media(media: list[str]) -> str:
    wrapper = ['<div class="award-media-wrapper">']
    if len(media) > 1:
        wrapper.append('<button class="carousel-btn prev" onclick="prevSlide(this)"><</button>')
    wrapper.append('<div class="award-slider" data-idx="0">')
    for item in media:
        if item.endswith('.mp4'):
            wrapper.append(f'<div class="award-slide"><div class="blur-media-frame"><video src="{item}" autoplay muted loop playsinline></video></div></div>')
        else:
            wrapper.append(f'<div class="award-slide"><div class="blur-media-frame"><img class="blur-media-bg-img" src="{item}" alt="" aria-hidden="true"/><img src="{item}" loading="lazy"/></div></div>')
    wrapper.append('</div>')
    if len(media) > 1:
        wrapper.append('<button class="carousel-btn next" onclick="nextSlide(this)">></button>')
    wrapper.append('</div>')
    return ''.join(wrapper)


def render_projects_page():
    site = load_json('site.json')['projects']
    projects = load_json('projects.json')
    path = ROOT / 'projects.html'
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    ensure_shared_stylesheet(soup)
    ensure_local_connect_csp(soup)
    clean_legacy_styles(soup, ['.projects-grid', '.project-card{'])
    section = soup.select_one('.about-section')
    section.clear()
    section.append(BeautifulSoup(f'<h1><span class="title-hashtag">#</span> {site["title"]}</h1><p>{site["intro"]}</p><div class="projects-grid"></div>', 'html.parser'))
    grid = section.select_one('.projects-grid')
    for project in projects:
        tags = ''.join(f'<span class="project-tag">{tag}</span>' for tag in project['tech'])
        html = f'''<article class="project-card"><div class="project-card-head"><div><h2 class="project-title"><span class="title-hashtag">##</span><a class="project-title-link" href="{project['href']}" target="_blank" rel="noopener">{project['title']}</a></h2></div><a class="project-link-icon" href="{project['href']}" target="_blank" rel="noopener" aria-label="Visit {project['title']}"><img src="assets/icon_340d47e3.svg" alt="external link icon" /></a></div><div class="project-tags">{tags}</div><p class="project-desc">{project['desc']}</p><div class="project-meta"><span class="project-date">{project['date']}</span></div></article>'''
        grid.append(BeautifulSoup(html, 'html.parser'))
    style = soup.new_tag('style')
    style.string = PROJECT_STYLE
    soup.head.append(style)
    path.write_text(str(soup), encoding='utf-8')


def render_timeline_page(page_name: str, data_name: str):
    site = load_json('site.json')[page_name]
    items = load_json(data_name)
    path = ROOT / f'{page_name}.html'
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    ensure_shared_stylesheet(soup)
    ensure_local_connect_csp(soup)
    clean_legacy_styles(soup, ['/* ── Timeline Layout ── */', '.timeline-container'])
    clean_legacy_scripts(soup)
    script = soup.new_tag('script')
    script.string = CAROUSEL_JS
    soup.body.append(script)
    section = soup.select_one('.about-section')
    section.clear()
    section.append(BeautifulSoup(f'<h1><span class="title-hashtag">#</span> {site["title"]}</h1><p>{site["intro"]}</p><div class="timeline-container"></div>', 'html.parser'))
    container = section.select_one('.timeline-container')
    current_year = None
    for item in items:
        if item.get('year') and item['year'] != current_year:
            current_year = item['year']
            container.append(BeautifulSoup(f'<div class="tl-year-marker"><span>{current_year}</span></div>', 'html.parser'))
        body = [f'<p>{item["body"]}</p>']
        if item.get('media'):
            body.append(build_blur_media(item['media']))
        link_html = ''
        if item.get('link'):
            link_html = f'<a class="ext-link" href="{item["link"]}" target="_blank">↗ {item.get("link_label", item["link"])}</a>'
        html = f'''<div class="tl-item {item['side']}"><div class="tl-card"><div class="tl-card-header"><div><h3>{item['title']}</h3></div></div>{''.join(body)}<div class="tl-card-footer">{link_html}<span class="date-badge">{item['date']}</span></div></div><div class="tl-dot"><img src="{item['logo']}" alt="logo"/></div></div>'''
        container.append(BeautifulSoup(html, 'html.parser'))
    path.write_text(str(soup), encoding='utf-8')


def render_media_cards_page(page_name: str, data_name: str, mode: str):
    site = load_json('site.json')[page_name]
    items = load_json(data_name)
    path = ROOT / f'{page_name}.html'
    soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
    ensure_shared_stylesheet(soup)
    ensure_local_connect_csp(soup)
    if mode == 'awards':
        clean_legacy_scripts(soup)
        script = soup.new_tag('script')
        script.string = CAROUSEL_JS
        soup.body.append(script)
    section = soup.select_one('.about-section')
    section.clear()
    if page_name == 'art':
        intro_html = ''.join(f'<p>{p}</p>' for p in site['intro_paragraphs'])
        if site.get('instagram_url'):
            intro_html += f'<p><a href="{site["instagram_url"]}" target="_blank" rel="noopener">instagram.com/delusional.myz</a></p>'
    else:
        intro_html = f'<p>{site["intro"]}</p>'
    grid_class = 'awards-grid' if mode == 'awards' else 'captures-grid'
    section.append(BeautifulSoup(f'<h1><span class="title-hashtag">#</span> {site["title"]}</h1>{intro_html}<div class="{grid_class}"></div>', 'html.parser'))
    grid = section.select_one(f'.{grid_class}')
    for item in items:
        if mode == 'awards':
            actions = []
            for link in item['links']:
                classes = 'card-ext-link' + (' yt' if link.get('type') == 'youtube' else '')
                icon = '<svg viewBox="0 0 576 512" xmlns="http://www.w3.org/2000/svg"><path d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z" fill="currentColor"></path></svg>' if link.get('type') == 'youtube' else '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" x2="21" y1="14" y2="3"></line></svg>'
                actions.append(f'<a class="{classes}" href="{link["href"]}" target="_blank" rel="noopener noreferrer">{icon}</a>')
            html = f'''<article class="award-card media-card award-project-card"><div class="media-card-head"><div><h3 class="media-card-title"><span class="title-hashtag">##</span>{item['title']}</h3></div><div class="media-card-actions">{''.join(actions)}</div></div><p class="media-card-desc">{item['desc']}</p>{build_blur_media(item['media'])}</article>'''
        else:
            title = item['title']
            image = item['image']
            meta = f'<div class="media-card-meta"><span class="media-card-date">{item["date"]}</span></div>' if mode == 'captures' else ''
            html = f'''<article class="capture-item media-card {'art-card' if mode == 'art' else ''}"><div class="media-card-head"><div><h3 class="media-card-title"><span class="title-hashtag">##</span>{title}</h3></div></div><div class="capture-image-container"><div class="blur-media-frame"><img class="blur-media-bg-img" src="{image}" alt="" aria-hidden="true"/><img alt="{title}" class="capture-thumbnail" loading="lazy" src="{image}"/></div></div>{meta}</article>'''
        grid.append(BeautifulSoup(html, 'html.parser'))
    path.write_text(str(soup), encoding='utf-8')


def render_all():
    render_projects_page()
    render_timeline_page('journey', 'journey.json')
    render_timeline_page('voluntary', 'voluntary.json')
    render_media_cards_page('awards', 'awards.json', 'awards')
    render_media_cards_page('art', 'art.json', 'art')
    render_media_cards_page('captures', 'captures.json', 'captures')
    for path in ROOT.glob('*.html'):
        soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')
        ensure_local_connect_csp(soup)
        path.write_text(str(soup), encoding='utf-8')
