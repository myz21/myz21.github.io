from pathlib import Path
from bs4 import BeautifulSoup

PROJECTS = [
    {
        'title': 'TechTipsWiki',
        'href': 'https://github.com/myz21/TechTipsWiki',
        'date': '2026-05',
        'tech': ['Next.js', 'TypeScript', 'Tailwind', 'FastAPI'],
        'desc': 'Open-source full-stack platform focused on explaining modern technologies clearly, transparently, and fast for curious learners.'
    },
    {
        'title': 'ZenithAI',
        'href': 'https://github.com/myz21',
        'date': '2025-09',
        'tech': ['Python', 'YOLO', 'ORB', 'Computer Vision'],
        'desc': 'Competition-oriented aviation AI work combining object detection and visual odometry experiments for autonomous systems.'
    },
    {
        'title': 'Medical Assistant Chatbot',
        'href': 'https://github.com/myz21',
        'date': '2025-04',
        'tech': ['FastAPI', 'LangChain', 'Pydantic'],
        'desc': 'Personalized conversational AI assistant shaped by demographics and chat history, served through a practical web interface.'
    },
    {
        'title': 'micrograd',
        'href': 'https://github.com/myz21/micrograd',
        'date': '2025-04',
        'tech': ['Python', 'NumPy'],
        'desc': 'A from-scratch neural network learning project inspired by Andrej Karpathy to understand core backpropagation mechanics.'
    },
    {
        'title': 'Spikeflight',
        'href': 'https://github.com/myz21/Spikeflight',
        'date': '2025-02',
        'tech': ['C#', 'Unity'],
        'desc': '2D platformer prototype with enemy baiting, spike traps, and scene-based gameplay foundations built in Unity.'
    },
    {
        'title': 'The Traitor',
        'href': 'https://github.com/myz21/The-Traitor',
        'date': '2025-01',
        'tech': ['C++', 'SFML'],
        'desc': 'Multiplayer strategy game project where hidden-role deduction meets country management and collaborative gameplay design.'
    },
]

STYLE_BLOCK = '''
.projects-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:30px;width:100%;max-width:960px;margin:30px 0 0}
.project-card{background:var(--color-bg-primary);border:1px solid var(--color-border-primary);border-radius:12px;box-shadow:0 2px 6px var(--shadow-light);padding:20px 20px 14px;transition:border-color .25s ease,box-shadow .25s ease,transform .25s ease;min-height:100%}
.project-card:hover{border-color:var(--color-secondary);box-shadow:0 8px 22px var(--shadow-light);transform:translateY(-2px)}
.project-card-head{display:flex;align-items:flex-start;justify-content:space-between;gap:16px;margin-bottom:8px}
.project-link-icon{display:inline-flex;align-items:center;justify-content:center;width:38px;height:38px;border-radius:10px;border:1px solid var(--color-border-primary);background:var(--color-bg-secondary);flex-shrink:0}
.project-link-icon img{width:18px;height:18px;display:block}
.project-title{font-size:1.3rem;font-weight:700;line-height:1.3;margin:0}
.project-title-link{color:var(--color-text-primary);text-decoration:underline;text-decoration-color:var(--color-secondary)!important;text-decoration-thickness:3px;text-underline-offset:4px}
.project-tags{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 12px}
.project-tag{display:inline-flex;align-items:center;padding:4px 8px;border-radius:16px;font-size:.8rem;font-weight:400;line-height:1.8;background:var(--color-bg-light);color:var(--color-text-tertiary);border:1px solid var(--color-border-primary)}
.project-desc{font-size:1rem;font-weight:600;line-height:1.8;color:var(--color-text-tertiary);margin:0 0 12px}
.project-meta{display:flex;justify-content:flex-end;align-items:center;margin-top:auto}
.project-date{font-size:.8rem;font-weight:300;line-height:1.8;color:var(--color-text-light)}
[data-theme="dark"] .project-card{background:#1c1c1e;border-color:#333;box-shadow:0 2px 6px rgba(255,255,255,.08)}
[data-theme="dark"] .project-link-icon{background:#2c2c2e;border-color:#333}
[data-theme="dark"] .project-tag{background:#58585c;border-color:#333;color:#aaa}
[data-theme="dark"] .project-desc{color:#aaa}
[data-theme="dark"] .project-date{color:#999}
@media (max-width: 900px){.projects-grid{grid-template-columns:1fr;max-width:100%}}
@media (max-width: 640px){.project-card{padding:18px}.project-card-head{gap:12px}.project-title{font-size:1.15rem}}
'''


def make_card(project):
    tags = ''.join(f'<span class="project-tag">{tag}</span>' for tag in project['tech'])
    return f'''
    <article class="project-card">
      <div class="project-card-head">
        <div>
          <h2 class="project-title"><span class="title-hashtag">##</span><a class="project-title-link" href="{project['href']}" target="_blank" rel="noopener">{project['title']}</a></h2>
        </div>
        <a class="project-link-icon" href="{project['href']}" target="_blank" rel="noopener" aria-label="Visit {project['title']}">
          <img src="assets/icon_340d47e3.svg" alt="external link icon" />
        </a>
      </div>
      <div class="project-tags">{tags}</div>
      <p class="project-desc">{project['desc']}</p>
      <div class="project-meta"><span class="project-date">{project['date']}</span></div>
    </article>'''


path = Path('projects.html')
soup = BeautifulSoup(path.read_text(encoding='utf-8'), 'html.parser')

for style in soup.find_all('style'):
    text = style.get_text()
    if '.projects-grid' in text or '.project-card{' in text:
        style.decompose()

main = soup.find('main', class_='main-content')
section = main.find('div', class_='about-section') if main else None
if not section:
    raise SystemExit('about-section not found')

section.clear()
section.append(BeautifulSoup('''
<h1><span class="title-hashtag">#</span> Projects</h1>
<p>Selected work across AI, software engineering, and creative experimentation.</p>
<div class="projects-grid"></div>
''', 'html.parser'))

grid = section.find('div', class_='projects-grid')
for project in PROJECTS:
    grid.append(BeautifulSoup(make_card(project), 'html.parser'))

style_tag = soup.new_tag('style')
style_tag.string = STYLE_BLOCK
soup.head.append(style_tag)

path.write_text(str(soup), encoding='utf-8')
print('updated: projects.html')
