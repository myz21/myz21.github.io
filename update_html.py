import re
import sys

def modify_html():
    with open('/home/neo/Desktop/GITHUB MYZ21/myz21.github.io/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Task 1 & 2: Fix Contents and Add Gallery back.
    old_toc = '<li><a href="#art-work"><span class="wikipedia-module__8TSorq__wikiTocNum">5</span>Art Work</a></li><li><a href="#references"><span class="wikipedia-module__8TSorq__wikiTocNum">6</span>References</a></li><li><a href="#contact-ext"><span class="wikipedia-module__8TSorq__wikiTocNum">7</span>External links</a></li>'
    new_toc = '<li><a href="#gallery"><span class="wikipedia-module__8TSorq__wikiTocNum">5</span>Gallery</a></li><li><a href="#art-work"><span class="wikipedia-module__8TSorq__wikiTocNum">6</span>Art Work</a></li><li><a href="#references"><span class="wikipedia-module__8TSorq__wikiTocNum">7</span>References</a></li><li><a href="#contact-ext"><span class="wikipedia-module__8TSorq__wikiTocNum">8</span>External links</a></li>'
    if old_toc in html:
        html = html.replace(old_toc, new_toc)
    else:
        # Fallback
        html = re.sub(r'<li><a href="#art-work"><span class="wikipedia-module__8TSorq__wikiTocNum">\d+</span>Art Work</a></li>', '<li><a href="#gallery"><span class="wikipedia-module__8TSorq__wikiTocNum">5</span>Gallery</a></li><li><a href="#art-work"><span class="wikipedia-module__8TSorq__wikiTocNum">6</span>Art Work</a></li>', html)
        html = re.sub(r'<li><a href="#references"><span class="wikipedia-module__8TSorq__wikiTocNum">\d+</span>References</a></li>', '<li><a href="#references"><span class="wikipedia-module__8TSorq__wikiTocNum">7</span>References</a></li>', html)
        html = re.sub(r'<li><a href="#contact-ext"><span class="wikipedia-module__8TSorq__wikiTocNum">\d+</span>External links</a></li>', '<li><a href="#contact-ext"><span class="wikipedia-module__8TSorq__wikiTocNum">8</span>External links</a></li>', html)


    # Task 3: Remove Phone from infobox
    html = re.sub(r'<tr><td class="wikipedia-module__8TSorq__wikiInfoboxLabel">Phone</td><td class="wikipedia-module__8TSorq__wikiInfoboxValue">[^<]+</td></tr>', '', html)


    # Add Gallery Section before Art Work
    gallery_section = """
<section class="wikipedia-module__8TSorq__wikiSection" id="gallery"><h2 class="wikipedia-module__8TSorq__wikiH2">Gallery</h2><div style="margin-top:1rem"><div aria-roledescription="carousel" class="relative w-full max-w-2xl mx-auto" role="region"><div class="overflow-hidden"><div class="flex -ml-4" style="transition: transform 0.5s ease-in-out;">
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="Vodafone Bi Düşünsene Final" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/featured_0.png" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">Group photo of winners at the Vodafone Bi' Düşünsene Büyük Final.</figcaption></figure></div>
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="Online Meeting" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/featured_1.png" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">Online video call with team members.</figcaption></figure></div>
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="Working at Chamber of Commerce" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/featured_2.png" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">Working on a laptop at the Diyarbakır Ticaret ve Sanayi Odası.</figcaption></figure></div>
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="Hacettepe AI Datathon" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/featured_3.png" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">Winning 2nd place and a 12,500₺ prize at the Hacettepe AI Club Datathon.</figcaption></figure></div>
<div aria-roledescription="slide" class="min-w-0 shrink-0 grow-0 basis-full flex justify-center p-4" role="group"><figure style="margin:0;text-align:center;border:1px solid #c8ccd1;padding:6px;background-color:#f8f9fa"><img alt="Zenith AI Finalist" data-nimg="1" decoding="async" height="350" loading="lazy" src="/images/featured_4.png" style="color:transparent;display:block;object-fit:contain;width:100%;height:350px" width="600"/><figcaption class="wikipedia-module__8TSorq__wikiThumbCaption">Zenith AI Team poster celebrating as Artificial Intelligence in Aviation Finalists.</figcaption></figure></div>
</div></div><button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground absolute h-8 w-8 rounded-full -left-12 top-1/2 -translate-y-1/2" disabled=""><svg aria-hidden="true" class="lucide lucide-arrow-left h-4 w-4" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="m12 19-7-7 7-7"></path><path d="M19 12H5"></path></svg><span class="sr-only">Previous slide</span></button><button class="inline-flex items-center justify-center whitespace-nowrap text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 border border-input bg-background hover:bg-accent hover:text-accent-foreground absolute h-8 w-8 rounded-full -right-12 top-1/2 -translate-y-1/2" disabled=""><svg aria-hidden="true" class="lucide lucide-arrow-right h-4 w-4" fill="none" height="24" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M5 12h14"></path><path d="m12 5 7 7-7 7"></path></svg><span class="sr-only">Next slide</span></button></div></div></section><div class="wikipedia-module__8TSorq__clearBoth"></div>
"""

    # We need to add transition to the Art Work carousel as well to fulfill "geçiş efekti olsun"
    # Find the Art Work section and inject the transition style
    # the original `<div class="flex -ml-4">` might have already been modified if run multiple times, 
    # but let's replace all `<div class="flex -ml-4">` inside the html just in case (the only ones are in the carousels)
    html = html.replace('<div class="flex -ml-4">', '<div class="flex -ml-4" style="transition: transform 0.5s ease-in-out;">')

    if 'id="gallery"' not in html:
        html = html.replace('<section class="wikipedia-module__8TSorq__wikiSection" id="art-work">', gallery_section.replace('\n', '') + '<section class="wikipedia-module__8TSorq__wikiSection" id="art-work">')

    with open('/home/neo/Desktop/GITHUB MYZ21/myz21.github.io/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    modify_html()
