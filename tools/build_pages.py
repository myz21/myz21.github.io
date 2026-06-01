#!/usr/bin/env python3
"""
Rebuild journey.html with vertical timeline + logos + carousels.
Also create voluntary.html with same structure.
"""

from bs4 import BeautifulSoup
import copy, re

# ── helpers ──────────────────────────────────────────────────────────────────

CAROUSEL_JS = """
function prevSlide(btn) {
  const wrapper = btn.closest('.award-media-wrapper');
  const slider  = wrapper.querySelector('.award-slider');
  const slides  = slider.querySelectorAll('.award-slide');
  let idx = parseInt(slider.dataset.idx || 0);
  idx = (idx - 1 + slides.length) % slides.length;
  slider.dataset.idx = idx;
  slider.style.transform = `translateX(-${idx * 100}%)`;
}
function nextSlide(btn) {
  const wrapper = btn.closest('.award-media-wrapper');
  const slider  = wrapper.querySelector('.award-slider');
  const slides  = slider.querySelectorAll('.award-slide');
  let idx = parseInt(slider.dataset.idx || 0);
  idx = (idx + 1) % slides.length;
  slider.dataset.idx = idx;
  slider.style.transform = `translateX(-${idx * 100}%)`;
}
"""

TIMELINE_CSS = """
/* ── Timeline Layout ── */
.timeline-container {
  position: relative;
  max-width: 820px;
  margin: 0 auto;
  padding: 20px 0 40px;
}
.timeline-container::before {
  content: '';
  position: absolute;
  left: 50%;
  top: 0; bottom: 0;
  width: 2px;
  background: linear-gradient(to bottom, transparent, var(--accent, #5eead4) 10%, var(--accent, #5eead4) 90%, transparent);
  transform: translateX(-50%);
}
.tl-year-marker {
  position: relative;
  text-align: center;
  margin: 32px 0 8px;
  z-index: 2;
}
.tl-year-marker span {
  background: var(--bg, #111);
  border: 1.5px solid var(--accent, #5eead4);
  color: var(--accent, #5eead4);
  font-size: .75rem;
  font-weight: 700;
  padding: 3px 14px;
  border-radius: 20px;
  letter-spacing: .08em;
}
.tl-item {
  display: flex;
  align-items: flex-start;
  gap: 0;
  margin: 18px 0;
  position: relative;
}
.tl-item.left  { flex-direction: row-reverse; }
.tl-item.right { flex-direction: row; }

/* center dot */
.tl-dot {
  flex: 0 0 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 2;
  padding-top: 12px;
}
.tl-dot img {
  width: 36px; height: 36px;
  border-radius: 50%;
  object-fit: contain;
  background: #fff;
  border: 2px solid var(--accent, #5eead4);
  box-shadow: 0 0 8px rgba(94,234,212,.3);
}

/* card */
.tl-card {
  flex: 1;
  background: var(--card-bg, rgba(255,255,255,.04));
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 12px;
  padding: 16px;
  max-width: calc(50% - 20px);
  transition: border-color .2s;
}
.tl-card:hover { border-color: var(--accent, #5eead4); }
.tl-card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 8px;
}
.tl-card-header h3 {
  margin: 0;
  font-size: .95rem;
  line-height: 1.3;
}
.tl-card-header .date-badge {
  font-size: .72rem;
  color: var(--accent, #5eead4);
  background: rgba(94,234,212,.1);
  padding: 2px 8px;
  border-radius: 10px;
  white-space: nowrap;
}
.tl-card p { font-size: .85rem; line-height: 1.55; margin: 0 0 8px; }
.tl-card a.ext-link {
  font-size: .78rem;
  color: var(--accent, #5eead4);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 4px;
  opacity: .8;
  transition: opacity .15s;
}
.tl-card a.ext-link:hover { opacity: 1; }

/* carousel inside card */
.award-media-wrapper {
  position: relative;
  border-radius: 8px;
  overflow: hidden;
  margin-top: 10px;
  aspect-ratio: 16/9;
  background: #000;
}
.award-slider {
  display: flex;
  height: 100%;
  transition: transform .35s ease;
}
.award-slide {
  flex: 0 0 100%;
  height: 100%;
}
.award-slide img, .award-slide video {
  width: 100%; height: 100%;
  object-fit: cover;
  object-position: center;
}
.carousel-btn {
  position: absolute;
  top: 50%; transform: translateY(-50%);
  background: rgba(0,0,0,.55);
  color: #fff;
  border: none;
  width: 28px; height: 28px;
  border-radius: 50%;
  cursor: pointer;
  font-size: .9rem;
  z-index: 5;
  display: flex; align-items: center; justify-content: center;
  transition: background .15s;
}
.carousel-btn:hover { background: rgba(0,0,0,.85); }
.carousel-btn.prev { left: 6px; }
.carousel-btn.next { right: 6px; }

@media(max-width: 640px) {
  .timeline-container::before { left: 20px; }
  .tl-item, .tl-item.left { flex-direction: column; }
  .tl-dot { padding-top: 0; }
  .tl-card { max-width: 100%; margin-left: 8px; }
}
"""

def make_carousel(media_list):
    """media_list: list of relative asset paths (img or mp4)"""
    wrapper = '<div class="award-media-wrapper">'
    if len(media_list) > 1:
        wrapper += '<button class="carousel-btn prev" onclick="prevSlide(this)"><</button>'
    wrapper += '<div class="award-slider" data-idx="0">'
    for m in media_list:
        if m.endswith('.mp4'):
            wrapper += f'<div class="award-slide"><video src="{m}" autoplay muted loop playsinline></video></div>'
        else:
            wrapper += f'<div class="award-slide"><img src="{m}" loading="lazy"/></div>'
    wrapper += '</div>'
    if len(media_list) > 1:
        wrapper += '<button class="carousel-btn next" onclick="nextSlide(this)">></button>'
    wrapper += '</div>'
    return wrapper

def make_card(title, date_str, body_html, link=None, link_label=None):
    link_html = ''
    if link:
        label = link_label or link
        link_html = f'<a class="ext-link" href="{link}" target="_blank">↗ {label}</a>'
    return f'''<div class="tl-card">
  <div class="tl-card-header">
    <div>
      <span class="date-badge">{date_str}</span>
      <h3>{title}</h3>
    </div>
  </div>
  {body_html}
  {link_html}
</div>'''

def make_item(side, logo, title, date_str, body_html, link=None, link_label=None):
    dot = f'<div class="tl-dot"><img src="{logo}" alt="logo"/></div>'
    card = make_card(title, date_str, body_html, link, link_label)
    return f'<div class="tl-item {side}">{card}{dot}<div style="flex:1"></div></div>'

def year_marker(y):
    return f'<div class="tl-year-marker"><span>{y}</span></div>'

# ── Journey data ──────────────────────────────────────────────────────────────
JOURNEY_ITEMS = [
    # (year_marker_before, side, logo, title, date, body_html, link, link_label)
    (2026, 'right', 'assets/hubio-logo.png',
     '🔬 Undergraduate Researcher at Biological Data Science Lab', 'Aug 2025 →',
     '<p>Working as a TÜBİTAK Undergraduate Researcher under Prof. Dr. Tunca Doğan at Hacettepe University. Adapting state-of-the-art LLMs to protein generation.</p>',
     'https://hubiodatalab.github.io/', 'HuBio Data Lab'),

    (None, 'left', 'assets/nanomindsai_logo.jpeg',
     '💼 AI Engineering Intern at nanominds', 'Jul 2025',
     '<p>Researched AI workflows in Venture Capital and analyzed AI use cases across the investment process.</p>',
     None, None),

    (None, 'right', 'assets/aybu.png',
     '✏️ Part-Time Art Instructor at AYBU', 'Mar 2025',
     '<p>Taught students the fundamentals of pencil drawing — perspective to anatomical sketches.</p>',
     None, None),

    (2025, 'left', 'assets/ZenithAI.png',
     '🚀 AI Team Lead at BİLTEK AI & Zenith AI', 'Sep 2024',
     '<p>Founded Zenith AI competition team and led the TEKNOFEST 2025 AI in Aviation challenge — built YOLO + ORB visual odometry for flying cars.</p>'
     + make_carousel(['assets/ZenithAI.png', 'assets/zenith.jpg']),
     None, None),

    (2024, 'right', 'assets/aybu.png',
     '💻 Computer Engineering at AYBU', 'Oct 2023',
     '<p>Transferred to Computer Engineering at Ankara Yıldırım Beyazıt University, fulfilling a childhood dream.</p>',
     None, None),

    (2023, 'left', 'assets/firat uni.jpeg',
     '🦷 Dropped Out of Dentistry to Pursue Engineering', 'Sep 2021',
     '<p>Made the radical decision to leave dentistry after two years to follow my true passion in engineering and technology.</p>'
     + make_carousel(['assets/fu-dhf-pic.jpg', 'assets/fu-dhf-pic2.jpg', 'assets/fu-dhf.mp4']),
     None, None),
]

# ── Voluntary data ────────────────────────────────────────────────────────────
VOLUNTARY_ITEMS = [
    (2026, 'right', 'assets/servi_logo.jpg',
     '🌐 Open Source Contributor at Servi', 'Jan 2026 →',
     '<p>Developing the backend of a full-stack open-source project focused on promoting technological awareness. Building TechTipsWiki to explain technologies transparently.</p>',
     'https://www.linkedin.com/company/servi-ekibi/', 'Servi on LinkedIn'),

    (None, 'left', 'assets/milget_logo.jpg',
     '🤝 Head of Education Coordination at Milli Gençlik Topluluğu (AGD)', 'Jun 2024',
     '<p>Co-founded this university club from just 2 members and grew it into the most active AGD branch in Ankara.</p>'
     + make_carousel(['assets/483906555_18261403669286834_4706971470279356965_n.webp', 'assets/milget_logo.jpg']),
     'https://www.linkedin.com/company/milgetybu/', 'LinkedIn'),

    (2025, 'right', 'assets/hhs_logo.jpg',
     '💻 R&D Member at Happy Hacking Space', 'Jan 2025 →',
     '<p>After placing 2nd in the first-ever community Code Jam, I joined their R&D team to contribute to the hackerspace ecosystem.</p>'
     + make_carousel(['assets/hhs_mmet.jpg', 'assets/hhs_logo.jpg']),
     'https://www.linkedin.com/company/happyhackingspace', 'LinkedIn'),
]

# ── Build page from template ──────────────────────────────────────────────────

def build_timeline_html(items):
    html = '<div class="timeline-container">'
    prev_year = None
    for (yr, side, logo, title, date, body, link, link_label) in items:
        if yr and yr != prev_year:
            html += year_marker(yr)
            prev_year = yr
        html += make_item(side, logo, title, date, body, link, link_label)
    html += '</div>'
    return html

def build_page(src_file, dst_file, page_title, intro, items, active_nav):
    with open(src_file, 'r') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Update active nav
    for a in soup.find_all('a'):
        a_href = a.get('href','')
        classes = a.get('class', [])
        if isinstance(classes, str):
            classes = classes.split()
        else:
            classes = list(classes)

        # Remove any existing 'active' class to prevent duplicates
        classes = [c for c in classes if c != 'active']

        if a_href == active_nav:
            classes.append('active')

        if classes:
            a['class'] = classes
        elif 'class' in a.attrs:
            del a.attrs['class']

    # Pre-clean existing Timeline CSS & Carousel JS to prevent duplicates
    for tag in soup.find_all('style'):
        text = tag.get_text()
        if '/* ── Timeline Layout ── */' in text or '.timeline-container' in text:
            tag.decompose()

    for tag in soup.find_all('script'):
        text = tag.get_text()
        if 'function prevSlide' in text or 'function nextSlide' in text:
            tag.decompose()

    # Inject timeline CSS (prepend to body since no <head>)
    style_tag = soup.new_tag('style')
    style_tag.string = TIMELINE_CSS
    soup.body.insert(0, style_tag)

    # Inject carousel JS
    script_tag = soup.new_tag('script')
    script_tag.string = CAROUSEL_JS
    soup.body.append(script_tag)

    # Replace about-section content
    section = soup.find('div', class_='about-section')
    if section:
        title_html = f'<h1><span class="title-hashtag">#</span> {page_title}</h1>'
        section.clear()
        section.append(BeautifulSoup(title_html, 'html.parser'))
        section.append(BeautifulSoup(f'<p>{intro}</p>', 'html.parser'))
        section.append(BeautifulSoup(build_timeline_html(items), 'html.parser'))

    with open(dst_file, 'w') as f:
        f.write(str(soup))
    print(f'✓ Written: {dst_file}')

# ── Run ───────────────────────────────────────────────────────────────────────

JOURNEY_INTRO = "Welcome to my personal journey. Here are the important milestones in my life — from career growth to bold life decisions."
VOLUNTARY_INTRO = "During my university years, I have actively participated in various voluntary communities to share knowledge, foster technological awareness, and build strong, collaborative networks."

build_page('journey.html',  'journey.html',  'Journey',   JOURNEY_INTRO,   JOURNEY_ITEMS,   'journey.html')
# voluntary reads fresh from the ORIGINAL journey (before it was overwritten above would be stale, but since build_page reads src_file each time and journey.html was written first, re-read is fine)
build_page('journey.html',  'voluntary.html', 'Voluntary', VOLUNTARY_INTRO, VOLUNTARY_ITEMS, 'voluntary.html')
