from pathlib import Path
import re

files = [
    'index.html', 'about.html', 'journey.html', 'voluntary.html',
    'awards.html', 'art.html', 'captures.html', 'projects.html'
]

force_css = '''\n<style id="codex-font-consistency">\nhtml,body,button,input,select,textarea{font-family:JetBrains Mono,Courier New,Monaco,Menlo,monospace !important;}\nh1,h2,h3,h4,h5,h6,p,a,span,li,div,strong,small,code,pre,nav{font-family:inherit !important;}\n.name-link,.nav-links a,.about-section,.about-section p,.about-section h1,.project-title,.project-title-link,.project-desc,.project-tag,.project-date{font-family:inherit !important;}\n</style>\n'''

for file in files:
    path = Path(file)
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'<style id="codex-font-consistency">.*?</style>\s*', '', text, flags=re.S)
    if '</head>' in text:
        text = text.replace('</head>', force_css + '</head>', 1)
    path.write_text(text, encoding='utf-8')
    print(f'updated: {file}')
