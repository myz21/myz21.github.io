from pathlib import Path
import re

HTML_FILES = [
    'index.html', 'about.html', 'journey.html', 'voluntary.html',
    'awards.html', 'art.html', 'captures.html', 'projects.html'
]

FONT_FACE_RE = re.compile(r'@font-face\s*\{[^{}]*font-family\s*:\s*JetBrains Mono;[^{}]*\}', re.IGNORECASE)
STYLE_RE = re.compile(r'<style[^>]*>(.*?)</style>', re.IGNORECASE | re.DOTALL)

CANONICAL_FONT_BLOCK = '''@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Thin_0756e8e8.ttf) format("truetype");font-weight:100;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-ExtraLight_8391e7ec.ttf) format("truetype");font-weight:200;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Light_60c18d7d.ttf) format("truetype");font-weight:300;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Regular_a0bf60ef.ttf) format("truetype");font-weight:400;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Medium_31c92d01.ttf) format("truetype");font-weight:500;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-SemiBold_1b3bfa1e.ttf) format("truetype");font-weight:600;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Bold_5590990c.ttf) format("truetype");font-weight:700;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Regular_9d0a1f7a.ttf) format("truetype");font-weight:400;font-style:italic}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Medium_4477fda6.ttf) format("truetype");font-weight:500;font-style:italic}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-SemiBold_3b300050.ttf) format("truetype");font-weight:600;font-style:italic}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Bold_4039d5ce.ttf) format("truetype");font-weight:700;font-style:italic}'''


def normalize_file(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    changed = False

    def repl(match: re.Match[str]) -> str:
        nonlocal changed
        style_body = match.group(1)
        found = FONT_FACE_RE.findall(style_body)
        if not found:
            return match.group(0)
        stripped = FONT_FACE_RE.sub('', style_body)
        stripped = re.sub(r'\n\s*\n+', '\n', stripped).strip()
        new_body = CANONICAL_FONT_BLOCK + ('\n' + stripped if stripped else '')
        if new_body != style_body.strip():
            changed = True
        return match.group(0).replace(style_body, new_body)

    new_text = STYLE_RE.sub(repl, text, count=1)
    if new_text != text:
        path.write_text(new_text, encoding='utf-8')
        return True
    return changed


for rel in HTML_FILES:
    path = Path(rel)
    if not path.exists():
        continue
    updated = normalize_file(path)
    print(f"{'updated' if updated else 'ok'}: {rel}")
