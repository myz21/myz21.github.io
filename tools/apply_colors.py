import os
import re
import glob

# The style block to inject
style_content = """<style>
    :root, [data-theme="dark"], body {
        --color-bg-primary: #18181b !important;
        --color-bg-secondary: #27272a !important;
        --color-primary: rgb(0, 108, 176) !important;
        --color-primary-dark: rgb(1, 46, 89) !important;
        --color-text-primary: #f4f4f5 !important;
        --color-text-secondary: #a1a1aa !important;
    }
    body {
        background-color: var(--color-bg-primary) !important;
        color: var(--color-text-primary) !important;
    }
    .experience-card {
        background: var(--color-bg-secondary);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 24px;
        margin-bottom: 30px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .experience-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }
    .experience-header {
        display: flex;
        align-items: center;
        gap: 16px;
        margin-bottom: 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        padding-bottom: 16px;
    }
    .experience-logo {
        width: 64px;
        height: 64px;
        object-fit: contain;
        border-radius: 12px;
        background: #fff;
        padding: 6px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        flex-shrink: 0;
    }
    .experience-title-area h3 {
        margin: 0 0 6px 0;
        font-size: 1.25em;
        font-weight: 600;
        color: var(--color-text-primary);
    }
    .experience-title-area .date {
        font-size: 0.85em;
        color: var(--color-text-secondary);
        font-weight: 500;
        letter-spacing: 0.5px;
    }
    .experience-body p {
        margin: 0 0 16px 0;
        line-height: 1.65;
        color: #d4d4d8;
    }
    .carousel {
        position: relative;
        width: 100%;
        border-radius: 12px;
        background: rgba(0,0,0,0.2);
        display: flex;
        align-items: center;
        margin-top: 20px;
        box-shadow: inset 0 2px 10px rgba(0,0,0,0.2);
    }
    .carousel-track {
        display: flex;
        width: 100%;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        gap: 16px;
        padding: 16px;
        scrollbar-width: thin;
        scrollbar-color: rgba(255,255,255,0.2) transparent;
    }
    .carousel-track::-webkit-scrollbar {
        height: 8px;
    }
    .carousel-track::-webkit-scrollbar-track {
        background: transparent;
    }
    .carousel-track::-webkit-scrollbar-thumb {
        background-color: rgba(255,255,255,0.2);
        border-radius: 4px;
    }
    .carousel-track > * {
        flex: 0 0 80%;
        max-height: 400px;
        object-fit: cover;
        border-radius: 8px;
        scroll-snap-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
</style>"""

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Clean up any extraneous <style> blocks appended at the end of index.html by VisBug
    if filepath == 'index.html':
        # Remove all <style> blocks EXCEPT the first one (the huge minified one)
        # We can split by <style> and </style>
        # A simpler way: we know VisBug appended them after </div></div>
        content = re.sub(r'(</div></div>\s*)<style>.*?</style>', r'\1', content, flags=re.DOTALL)
        content = re.sub(r'<style>.*?</style>', '', content, flags=re.DOTALL) # Wait, this removes everything!
        
    # More robust cleanup for index.html: 
    # Just read the original index.html, find the first match of <style>...</style> which is ~4MB,
    # keep it, and remove all other <style> tags.
    if filepath == 'index.html':
        with open(filepath, 'r', encoding='utf-8') as f:
            content_original = f.read()
        matches = list(re.finditer(r'<style>.*?</style>', content_original, flags=re.DOTALL))
        if len(matches) > 1:
            # Reconstruct content keeping only the first style block
            # Actually, the user's modifications are just a lot of <style> blocks at the end.
            last_valid_pos = matches[1].start()
            content = content_original[:last_valid_pos]

    # Inject style_content into <head> or before </body>
    if '</head>' in content:
        content = content.replace('</head>', f'{style_content}\n</head>')
    else:
        content = content.replace('</body>', f'{style_content}\n</body>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Update CSS files too
css_files = glob.glob('css/*.css')
css_vars = """
:root, [data-theme="dark"], body {
    --color-bg-primary: #18181b !important;
    --color-bg-secondary: #27272a !important;
    --color-primary: rgb(0, 108, 176) !important;
    --color-primary-dark: rgb(1, 46, 89) !important;
    --color-text-primary: #f4f4f5 !important;
    --color-text-secondary: #a1a1aa !important;
}
"""

for filepath in css_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Prepend the CSS variables to ensure they apply
    content = css_vars + "\n" + content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Applied colors to all HTML and CSS files.")
