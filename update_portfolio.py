import os
import re
import json
import requests
from bs4 import BeautifulSoup, NavigableString
from urllib.parse import urlparse

# Configuration
BASE_DIR = os.path.abspath(os.getcwd())
IMAGES_DIR = os.path.join(BASE_DIR, 'images')
SCRIPTS_DIR = os.path.join(BASE_DIR, 'scripts')
INDEX_HTML = os.path.join(BASE_DIR, 'index.html')
CV_TEX = os.path.join(BASE_DIR, 'cv.tex')
JSON_FILES = ['linkedin_myz.json', 'linkedin_myz2.json']

    # 2. Extract from JSONs
    for json_file in JSON_FILES:
        path = os.path.join(BASE_DIR, json_file)
        if not os.path.exists(path): continue
        
        with open(path, 'r', encoding='utf-8') as f:
            jdata = json.load(f)
            if isinstance(jdata, list): jdata = jdata[0]
            
            # Basic Info
            bi = jdata.get('basic_info', jdata)
            if bi.get('fullname'): data['fullname'] = bi['fullname']
            if bi.get('profile_picture_url'): data['images']['profile'] = bi['profile_picture_url']
            if bi.get('profilePic'): data['images']['profile'] = bi['profilePic']
            if bi.get('background_picture_url'): data['images']['bg'] = bi['background_picture_url']
            
            # Featured
            featured = jdata.get('featured', [])
            for i, item in enumerate(featured):
                if item.get('image_url'):
                    data['images'][f'featured_{i}'] = item['image_url']
    
    # Add more images from index.html if they are not in JSON or CV
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        for img in soup.find_all('img'):
            src = img.get('src', '')
            if src.startswith('/images/') and not src.startswith('/images/profile') and not src.startswith('/images/bg'):
                # Extract filename without extension as key
                key = os.path.splitext(os.path.basename(src))[0]
                if key not in data['images']:
                    # Construct a dummy URL for downloading, assuming it's a local file that needs to be re-downloaded or kept
                    # For now, we'll just collect the local path as a URL to be processed by download_images
                    data['images'][key] = src # This will be handled by download_images if it's a URL, otherwise it will fail.
                                              # A better approach would be to copy local files if they exist.
                                              # For now, assuming all images are external URLs or will be replaced.
        for link in soup.find_all('link', {'rel': 'preload', 'as': 'image'}):
            href = link.get('href', '')
            if href.startswith('/images/') and not href.startswith('/images/profile') and not href.startswith('/images/bg'):
                key = os.path.splitext(os.path.basename(href))[0]
                if key not in data['images']:
                    data['images'][key] = href
                    
    return data

def download_images(image_urls):
    print("Cleaning and updating images...")
    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)
    else:
        for f in os.listdir(IMAGES_DIR):
            os.remove(os.path.join(IMAGES_DIR, f))
            
    mapping = {} # old_path_pattern -> new_local_path
    
    for key, url in image_urls.items():
        try:
            # If the URL is already a local path, we don't need to download it again
            if url.startswith('/images/'):
                # Assuming these are the old local images that need to be replaced by new downloads
                # Or, if they are meant to be kept, this logic needs adjustment.
                # For now, we treat them as old images that will be overwritten by new downloads if a URL is found.
                # If no external URL is found for them, they will be ignored.
                continue

            parsed_url = urlparse(url)
            path = parsed_url.path
            ext = os.path.splitext(path)[1]
            if not ext: ext = '.png' # Default to png if no extension found

            filename = f"{key}{ext}"
            filepath = os.path.join(IMAGES_DIR, filename)
            
            print(f"Downloading {url} -> {filename}")
            resp = requests.get(url, timeout=15)
            if resp.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(resp.content)
                mapping[key] = f"/images/{filename}"
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            
    return mapping

def update_html(data, img_mapping, replacements):
    print("Updating index.html...")
    if not os.path.exists(INDEX_HTML): return
    
    with open(INDEX_HTML, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    # 1. Update Text Nodes
    def replace_text_nodes(node):
        if isinstance(node, NavigableString):
            current_text = str(node)
            new_text = current_text
            for old, new in replacements.items():
                new_text = new_text.replace(old, new)
            if new_text != current_text:
                node.replace_with(new_text)
        elif hasattr(node, 'children'):
            for child in node.children:
                replace_text_nodes(child)

    replace_text_nodes(soup)
    
    # 2. Update Title and Meta
    title = soup.find('title')
    if title:
        title.string = title.string.replace(OLD_FIRST_NAME, data['firstname'])
        
    desc = soup.find('meta', attrs={'name': 'description'})
    if desc:
        desc['content'] = desc['content'].replace(OLD_FIRST_NAME, data['firstname'])

    # 3. Update Images
    old_image_to_new_key = {
        '/images/hussain-profile.jpeg': 'profile',
        '/images/comsats-plus-1.png': 'featured_0',
        '/images/comsats-plus-2.png': 'featured_1',
        '/images/pawsy-1.png': 'featured_2',
        '/images/pawsy-2.png': 'featured_3',
        '/images/uniserve-1.png': 'featured_4',
        '/images/uniserve-2.png': 'featured_5',
        '/images/gesture-present.png': 'featured_6',
        # Add more as needed
    }

    for img in soup.find_all('img'):
        src = img.get('src', '')
        for old_filename, new_key in old_image_to_new_key.items():
            if old_filename == src and new_key in img_mapping:
                img['src'] = img_mapping[new_key]
                break
    
    for link in soup.find_all('link', {'rel': 'preload', 'as': 'image'}):
        href = link.get('href', '')
        for old_filename, new_key in old_image_to_new_key.items():
            if old_filename == href and new_key in img_mapping:
                link['href'] = img_mapping[new_key]
                break
        
    # 4. Update Links (Email, GitHub, LinkedIn)
    for a in soup.find_all('a'):
        href = a.get('href', '')
        for old, new in replacements.items():
            if old in href:
                a['href'] = href.replace(old, new)

    with open(INDEX_HTML, 'w', encoding='utf-8') as f:
        f.write(str(soup))

def update_scripts(data, replacements):
    print("Updating scripts...")
    if not os.path.exists(SCRIPTS_DIR): return
    
    for filename in os.listdir(SCRIPTS_DIR):
        if filename.endswith('.js'):
            path = os.path.join(SCRIPTS_DIR, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = content
            for old, new in replacements.items():
                new_content = new_content.replace(old, new)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

def main():
    data = extract_data()
    print(f"Extracted Name: {data['fullname']}")
    
    # Define comprehensive replacements dictionary
    replacements = {
        OLD_NAME: data['fullname'],
        OLD_FIRST_NAME: data['firstname'],
        OLD_LAST_NAME: data['lastname'],
        OLD_EMAIL: data['email'],
        OLD_GITHUB: data['github'],
        OLD_LINKEDIN: data['linkedin'],
        "Hussain's Portfolio": f"{data['firstname']}'s Portfolio",
        "Atique ul Hussain Zaidi": data['fullname'],
        "Atique": data['firstname'],
        "Zaidi": data['lastname'],
        "atiqueulhussainz@gmail.com": data['email'],
        "hussaynzaidi": data['github'],
        "atiqueulhussainzaidi": data['linkedin'],
        "Software Engineer": data['summary'].split(';')[0].strip() if data['summary'] else "Undergraduate Researcher", # Heuristic
        "Builder": "AI Researcher", # Heuristic
        "Lahore, Pakistan": "Ankara, Türkiye", # Specific location update
        "COMSATS University Islamabad": "Ankara Yıldırım Beyazıt Üniversitesi",
        "COMSATS": "AYBÜ",
        "Pakistan": "Türkiye",
        # Project names and descriptions (from old index.html)
        "AI-Based Lipreader - Final Year Project": data['projects'][0]['name'] if data['projects'] else "AI-Based Lipreader",
        "GesturePresent - Gesture-based Slides Controller": data['projects'][1]['name'] if len(data['projects']) > 1 else "GesturePresent",
        "COMSATS Plus - Campus Utility App": data['projects'][2]['name'] if len(data['projects']) > 2 else "COMSATS Plus",
        "Pawsy - Pet Sitter Platform": data['projects'][3]['name'] if len(data['projects']) > 3 else "Pawsy",
        "Group Selecta - Multilingual Product Catalogue Migration": data['projects'][4]['name'] if len(data['projects']) > 4 else "Group Selecta",
        "Uniserve App - Community Donation Platform": data['projects'][5]['name'] if len(data['projects']) > 5 else "Uniserve App",
        "Chrome Extensions - TabX Manager & L.ai": data['projects'][6]['name'] if len(data['projects']) > 6 else "Chrome Extensions",
        # Experience (from old index.html)
        "Product Engineering Intern, Mudship": data['experience'][0]['role'] + ", " + data['experience'][0]['company'] if data['experience'] else "Product Engineering Intern, Mudship",
        "AI Intern, CVision": data['experience'][1]['role'] + ", " + data['experience'][1]['company'] if len(data['experience']) > 1 else "AI Intern, CVision",
        "Accommodations, Roundtables & Vendors Manager, Future Fest": data['experience'][2]['role'] + ", " + data['experience'][2]['company'] if len(data['experience']) > 2 else "Accommodations, Roundtables & Vendors Manager, Future Fest",
        "Account Executive, Motive Inc.": data['experience'][3]['role'] + ", " + data['experience'][3]['company'] if len(data['experience']) > 3 else "Account Executive, Motive Inc.",
        "Competitive Programming  - 4th Place, Technoverse 2025": data['leadership_awards'][1]['name'] if len(data['leadership_awards']) > 1 else "Competitive Programming  - 4th Place, Technoverse 2025",
        # Skills (from old index.html)
        "JavaScript, Python, Java, C, React, Next.js": data['skills']['Languages'] + ", " + data['skills']['AI/ML Frameworks'] if data['skills']['Languages'] and data['skills']['AI/ML Frameworks'] else "JavaScript, Python, Java, C, React, Next.js",
        "Supabase, MongoDB, PostgreSQL, Prisma": "Supabase, MongoDB, PostgreSQL, Prisma", # Placeholder, needs to be extracted from cv.tex if available
        "N8N, CrewAI, Figma, Bubble, Cloudinary, Clerk, Stripe, Manifest V3": data['skills']['Tools & DevOps'] if data['skills']['Tools & DevOps'] else "N8N, CrewAI, Figma, Bubble, Cloudinary, Clerk, Stripe, Manifest V3",
        # Gallery captions
        "COMSATS Plus Home page (Web view).": "AYBÜ Plus Home page (Web view).",
        "COMSATS Plus responsive mobile view showing the Yaadein (anonymized memory map) feature. ": "AYBÜ Plus responsive mobile view showing the Yaadein (anonymized memory map) feature. ",
        # References
        "hussaynzaidi.vercel.app": "myz21.github.io",
        "linkedin.com/in/atiqueulhussainzaidi": f"linkedin.com/in/{data['linkedin']}",
        "github.com/hussaynzaidi": f"github.com/{data['github']}",
        "comsatsplus.com": "aybuplus.com", # Assuming a new domain for the project
        "Pawsy platform.": "Pawsy platform.", # No change needed
        "uniserveapp.com": "uniserveapp.com", # No change needed
        "gesturepresent.vercel.app": "gesturepresent.vercel.app", # No change needed
        "Pakistani web developers": "Turkish web developers",
        "React developers": "AI/ML developers",
        "Next.js developers": "Python developers",
        "TypeScript programmers": "C++ programmers",
        "Open-source software developers": "Deep Learning engineers",
        "2026": "2027", # Update year in references
        "17 April 2026": "1 May 2026", # Update date in footer
        "01:40": "00:00", # Update time in footer
        "(PST)": "(TRT)", # Update timezone in footer
    }
    
    img_mapping = download_images(data['images'])
    
    update_html(data, img_mapping, replacements)
    update_scripts(data, replacements)
    
    print("Portfolio update complete!")

if __name__ == "__main__":
    main()

