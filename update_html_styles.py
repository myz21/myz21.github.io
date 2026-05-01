import re

def update_html():
    with open('/home/neo/Desktop/GITHUB MYZ21/myz21.github.io/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove disabled="" from carousel buttons so they can loop infinitely on the first slide
    # The buttons look like: <button class="... absolute h-8 w-8 rounded-full -left-12 top-1/2 -translate-y-1/2" disabled="">
    # We will just remove `disabled=""` from all carousel buttons.
    html = re.sub(r'(<button class="[^"]*lucide-arrow-[^"]*) disabled=""(>)', r'\1\2', html)
    html = re.sub(r' disabled=""(><svg aria-hidden="true" class="lucide lucide-arrow-)', r'\1', html)

    # 2. Make caption text black and cooler
    # Change <figcaption class="wikipedia-module__8TSorq__wikiThumbCaption"> to add inline styles
    html = html.replace(
        '<figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">',
        '<figcaption class="wikipedia-module__8TSorq__wikiThumbCaption" style="color: #000; font-weight: 600; font-size: 14px; text-shadow: 0px 0px 1px rgba(0,0,0,0.2);">'
    )

    with open('/home/neo/Desktop/GITHUB MYZ21/myz21.github.io/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    update_html()
