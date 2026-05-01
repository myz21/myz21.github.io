import re

def update_index():
    with open('/home/neo/Desktop/GITHUB MYZ21/myz21.github.io/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the TOC sub-items for Projects
    old_toc_sub = '<ul class="wikipedia-module__8TSorq__wikiTocSub"><li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->1</span>AI-Based Lipreader</a></li><li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->2</span>GesturePresent</a></li><li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->3</span>COMSATS Plus</a></li><li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->4</span>Pawsy</a></li><li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->5</span>Group Selecta</a></li><li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->6</span>Uniserve App</a></li></ul>'
    
    new_toc_sub = '<ul class="wikipedia-module__8TSorq__wikiTocSub">' + \
                  '<li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->1</span>nanoGPT</a></li>' + \
                  '<li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->2</span>DoctorGPT</a></li>' + \
                  '<li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->3</span>E-Corp Customer Insight Analysis</a></li>' + \
                  '<li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->4</span>The Traitor</a></li>' + \
                  '<li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->5</span>Deep Learning Fish Classification</a></li>' + \
                  '<li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->6</span>BTK Datathon Regression</a></li>' + \
                  '<li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->7</span>ML Bootcamp</a></li>' + \
                  '<li><a href="#projects"><span class="wikipedia-module__8TSorq__wikiTocNum">4.<!-- -->8</span>Spikeflight</a></li>' + \
                  '</ul>'
    
    html = html.replace(old_toc_sub, new_toc_sub)

    # 2. Add the new projects to the projects list
    new_projects_html = """<li><a href="https://github.com/myz21/bootcampDeepLearning" target="_blank" rel="noopener noreferrer" class="wikipedia-module__8TSorq__wikiBold" style="color:#0645ad;text-decoration:none;">Deep Learning Fish Classification</a> <span class="wikipedia-module__8TSorq__wikiSmall">(Oct. 2024)</span> — TensorFlow/Keras, CNN. Developed a CNN classifier for 18,000 images, implementing data augmentation and dropout layers to enhance model generalization and robustness.</li><li><a href="https://github.com/myz21/BTK_Datathon/blob/main/BTK_Datathon24_rmse6_13.ipynb" target="_blank" rel="noopener noreferrer" class="wikipedia-module__8TSorq__wikiBold" style="color:#0645ad;text-decoration:none;">BTK Datathon Regression</a> <span class="wikipedia-module__8TSorq__wikiSmall">(Sept. 2024)</span> — Kaggle Competition. Processed 65,125 records to forecast network load; reduced RMSE from 9.83 to 6.13 via advanced categorical encoding and feature selection.</li><li><a href="https://github.com/myz21/bootcampAI" target="_blank" rel="noopener noreferrer" class="wikipedia-module__8TSorq__wikiBold" style="color:#0645ad;text-decoration:none;">ML Bootcamp</a> <span class="wikipedia-module__8TSorq__wikiSmall">(Jun. 2024)</span> — Achieved 96.67 percent accuracy by benchmarking 6 ML/DL models (CNN, LightGBM, etc.) on the Fashion MNIST dataset and successfully presented the results live to 450+ participants and industry mentors for the top mentor selection process.</li><li><a href="https://github.com/myz21/Spikeflight" target="_blank" rel="noopener noreferrer" class="wikipedia-module__8TSorq__wikiBold" style="color:#0645ad;text-decoration:none;">Spikeflight (Unity 2D Game)</a> <span class="wikipedia-module__8TSorq__wikiSmall">(March 2024)</span> — Implemented menu and in-game UI flow including play, pause, replay, and home navigation. Applied a persistent global game-state manager (Singleton) to track and display gameplay statistics across scenes.</li>"""

    # We find the end of the Projects list:
    # <li><span class="wikipedia-module__8TSorq__wikiBold">The Traitor — Client/Server Game - C++/SFML</span> <span class="wikipedia-module__8TSorq__wikiSmall">(2025)</span> — Built SFML client UI and integrated TCP client-server networking for multiplayer gameplay.</li></ul></section>
    
    target_str = 'networking for multiplayer gameplay.</li></ul>'
    if target_str in html:
        html = html.replace(target_str, 'networking for multiplayer gameplay.</li>' + new_projects_html + '</ul>')
    else:
        print("Error: Could not find the insertion point for new projects.")

    with open('/home/neo/Desktop/GITHUB MYZ21/myz21.github.io/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == "__main__":
    update_index()
