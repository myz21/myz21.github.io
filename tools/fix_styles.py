import re
import glob

html_files = glob.glob('*.html')
css_files = glob.glob('css/*.css')

# The user's new style block
new_style = """
    :root, [data-theme="dark"], body {
        --color-primary: rgb(0, 108, 176) !important;
        --color-primary-dark: rgb(1, 46, 89) !important;
    }
    :root, body {
        --color-secondary: rgb(108, 117, 125) !important;
        --color-white: rgb(255, 255, 255) !important;
        --color-black: rgb(0, 0, 0) !important;
        --color-text-primary: rgb(33, 33, 33) !important;
        --color-text-secondary: rgb(33, 37, 41) !important;
        --color-text-tertiary: rgb(85, 85, 85) !important;
        --color-text-light: rgb(91, 91, 91) !important;
        --color-text-muted: rgb(108, 117, 125) !important;
        --color-bg-primary: rgb(255, 255, 255) !important;
        --color-bg-secondary: rgb(251, 251, 255) !important;
        --color-bg-tertiary: rgb(249, 255, 250) !important;
        --color-bg-quaternary: rgb(245, 245, 245) !important;
    }
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's write a cleanup function for HTML
def add_style_to_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We will just inject it into the <head> if possible
    # Wait, the user has existing <style> blocks in index.html starting from line 20 that we want to clean up.
    # If the file is index.html we can clean it up.
    pass

