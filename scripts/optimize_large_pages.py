import re
import os
import bs4

font_face_replacements = """@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Thin_0756e8e8.ttf)format("truetype");font-weight:100;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-ExtraLight_8391e7ec.ttf)format("truetype");font-weight:200;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Light_60c18d7d.ttf)format("truetype");font-weight:300;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Regular_a0bf60ef.ttf)format("truetype");font-weight:400;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Medium_31c92d01.ttf)format("truetype");font-weight:500;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-SemiBold_1b3bfa1e.ttf)format("truetype");font-weight:600;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Bold_5590990c.ttf)format("truetype");font-weight:700;font-style:normal}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Regular_9d0a1f7a.ttf)format("truetype");font-weight:400;font-style:italic}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Medium_4477fda6.ttf)format("truetype");font-weight:500;font-style:italic}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-SemiBold_3b300050.ttf)format("truetype");font-weight:600;font-style:italic}
@font-face{font-family:JetBrains Mono;src:url(assets/fonts/JetBrainsMono-Bold_4039d5ce.ttf)format("truetype");font-weight:700;font-style:italic}
"""

def remove_base64_font_faces(css_content):
    result = []
    i = 0
    n = len(css_content)
    removed_count = 0
    while i < n:
        idx = css_content.find('@font-face', i)
        if idx == -1:
            result.append(css_content[i:])
            break
        result.append(css_content[i:idx])
        
        start_block = css_content.find('{', idx)
        if start_block == -1:
            result.append(css_content[idx:])
            break
            
        end_block = css_content.find('}', start_block)
        if end_block == -1:
            result.append(css_content[idx:])
            break
            
        block_content = css_content[idx:end_block+1]
        if 'data:font' in block_content or 'data:application' in block_content or 'data:x-font' in block_content:
            removed_count += 1
            i = end_block + 1
        else:
            result.append(block_content)
            i = end_block + 1
            
    return "".join(result), removed_count

def optimize_file(filename):
    print(f"Optimizing {filename}...")
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return
        
    initial_size = os.path.getsize(filename) / (1024 * 1024)
    print(f"  Initial Size: {initial_size:.2f} MB")
    
    with open(filename, 'r', encoding='utf-8') as f:
        soup = bs4.BeautifulSoup(f, 'html.parser')
        
    styles = soup.find_all('style')
    total_removed = 0
    font_injected = False
    
    # We want to process each style tag
    # Some style tags might be duplicates or empty, let's keep track of clean style contents
    style_tags_to_keep = []
    seen_styles = set()
    
    for style_tag in styles:
        content = style_tag.string or ''
        # Remove base64 font-faces
        clean_content, removed = remove_base64_font_faces(content)
        total_removed += removed
        
        # Deduplicate identical or empty style tags (common in about.html bloat)
        stripped = clean_content.strip()
        if not stripped:
            style_tag.decompose()
            continue
            
        if stripped in seen_styles:
            print("  Removed duplicate style tag.")
            style_tag.decompose()
            continue
            
        seen_styles.add(stripped)
        
        # Inject standard font-face definitions at the beginning of the first style tag that contains CSS
        if not font_injected and ('body' in clean_content or ':root' in clean_content or 'html' in clean_content):
            clean_content = font_face_replacements + "\n" + clean_content
            font_injected = True
            
        style_tag.string = clean_content
        
    # If no font was injected to existing styles, create a new style tag for fonts
    if not font_injected:
        new_style = soup.new_tag('style')
        new_style.string = font_face_replacements
        soup.head.insert(0, new_style)
        print("  Injected font-face definitions into a new style tag.")
        
    # Save the optimized file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    final_size = os.path.getsize(filename) / (1024 * 1024)
    print(f"  Removed {total_removed} base64 font-face definitions.")
    print(f"  Final Size: {final_size:.4f} MB (Reduced by {(initial_size - final_size) / initial_size * 100:.1f}%)")

if __name__ == "__main__":
    optimize_file('index.html')
    optimize_file('about.html')
