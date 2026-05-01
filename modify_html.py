import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Instagram from Infobox
html = re.sub(r'<tr><td class="wikipedia-module__8TSorq__wikiInfoboxLabel">Instagram</td><td class="wikipedia-module__8TSorq__wikiInfoboxValue"><a class="" href="https://www\.instagram\.com/delusional\.myz/">www\.instagram\.com/delusional\.myz/</a></td></tr>', '', html)

# 2. Remove Instagram from lead text
html = re.sub(r' Background in drawing and illustration; shares work at instagram\.com/delusional\.myz\.', '', html)

# 3. Change "Gallery" to "Art Work"
html = html.replace('id="gallery"><h2 class="wikipedia-module__8TSorq__wikiH2">Gallery</h2>', 'id="art-work"><h2 class="wikipedia-module__8TSorq__wikiH2">Art Work</h2>')

# Also update the Table of Contents link
html = html.replace('<a href="#gallery"><span class="wikipedia-module__8TSorq__wikiTocNum">5</span>Gallery</a>', '<a href="#art-work"><span class="wikipedia-module__8TSorq__wikiTocNum">5</span>Art Work</a>')

# 4. Replace Gallery Carousel with new artwork
new_carousel_items = """
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="Os Calcaneus" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/os-calcaneus.jpeg" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">A detailed anatomical sketch of the calcaneus bone with color-coded labels in Latin.</figcaption></figure></div>
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="Os Femoris" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/os-femoris.jpeg" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">A meticulous anatomical study of the femur bone with pink and purple ink annotations.</figcaption></figure></div>
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="Sheeps" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/sheeps.jpeg" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">A thought-provoking ink drawing featuring a group of sheep surrounding a butcher.</figcaption></figure></div>
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="What U Consume" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/what-u-consume.jpeg" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">A political cartoon showing a hand sprinkling bombs onto a plate labeled "GAZA".</figcaption></figure></div>
"""

# The carousel is inside <div class="flex -ml-4"> ... </div>
# We need to replace the contents of this div
import re
# Regex to match the contents of <div class="flex -ml-4">...</div><button
html = re.sub(r'(<div class="flex -ml-4">)(.*?)(</div></div><button class="inline-flex)', r'\1' + new_carousel_items.replace('\n', '') + r'\3', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
