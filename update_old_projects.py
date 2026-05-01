import re

def update_old_projects():
    with open('/home/neo/Desktop/GITHUB MYZ21/myz21.github.io/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Replacements for old projects
    html = html.replace(
        '<span class="wikipedia-module__8TSorq__wikiBold">nanoGPT - Pytorch/Numpy</span>',
        '<a href="https://github.com/myz21" target="_blank" rel="noopener noreferrer" class="wikipedia-module__8TSorq__wikiBold" style="color:#0645ad;text-decoration:none;">nanoGPT - Pytorch/Numpy</a>'
    )
    
    html = html.replace(
        '<span class="wikipedia-module__8TSorq__wikiBold">DoctorGPT: Medical Assistant - LangChain · Gemini · FastAPI</span>',
        '<a href="https://github.com/myz21" target="_blank" rel="noopener noreferrer" class="wikipedia-module__8TSorq__wikiBold" style="color:#0645ad;text-decoration:none;">DoctorGPT: Medical Assistant - LangChain · Gemini · FastAPI</a>'
    )
    
    html = html.replace(
        '<span class="wikipedia-module__8TSorq__wikiBold">E-Corp Customer Insight Analysis - 2nd Place</span>',
        '<a href="https://github.com/myz21" target="_blank" rel="noopener noreferrer" class="wikipedia-module__8TSorq__wikiBold" style="color:#0645ad;text-decoration:none;">E-Corp Customer Insight Analysis - 2nd Place</a>'
    )
    
    html = html.replace(
        '<span class="wikipedia-module__8TSorq__wikiBold">The Traitor — Client/Server Game - C++/SFML</span>',
        '<a href="https://github.com/myz21" target="_blank" rel="noopener noreferrer" class="wikipedia-module__8TSorq__wikiBold" style="color:#0645ad;text-decoration:none;">The Traitor — Client/Server Game - C++/SFML</a>'
    )

    with open('/home/neo/Desktop/GITHUB MYZ21/myz21.github.io/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    update_old_projects()
