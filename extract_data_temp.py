import re
import json
from urllib.parse import urlparse
import os

CV_TEX_CONTENT = """
%-------------------------
% Resume in LaTeX - ATS Optimized
% Optimized for: AI/ML Engineering Internship in Industry
% Author : Muhammed Yıldız
%-------------------------

\documentclass[letterpaper,11pt]{article}

\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\input{glyphtounicode}

\pagestyle{fancy}
\fancyhf{}
\fancyfoot}{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

\addtolength{\oddsidemargin}{-0.5in}
\addtolength{\evensidemargin}{-0.5in}
\addtolength{\textwidth}{1in}
\addtolength{\topmargin}{-.6in}
\addtolength{\textheight}{1.1in}

\urlstyle{same}
\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Section formatting
\titleformat{\section}{
  \vspace{-10pt}\scshape\raggedright\large
}{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]

\pdfgentounicode=1

% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-7pt}
}

\newcommand{\resumeItemListStart}{\begin{itemize}}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}

%-------------------------------------------
\begin{document}

%----------HEADING----------
\begin{center}
    \textbf{\Huge\scshape Muhammed Yıldız} \\ \vspace{2pt}
    \small
    \href{mailto:mhmmdyildiz@proton.me}{\underline{mhmmdyildiz@proton.me}} $|$ 
    \href{https://linkedin.com/in/myzz}{\underline{linkedin.com/in/myzz}} $|$
    \href{https://github.com/myz21}{\underline{github.com/myz21}} $|$
    \href{tel:+905551926713}{+90 555 192 6713}
\end{center}

%-----------PROFESSIONAL SUMMARY-----------
\section{Summary}
    \small{\textbf{AI Researcher} and Computer Engineering undergraduate skilled in \textbf{NLP, computer vision, and generative AI}. Proven ability to train deep learning models and \textbf{deploy AI web services}. Recognized \textbf{hackathon winner} and technical event organizer}


%-----------EDUCATION-----------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Ankara Yildirim Beyazit University}{Ankara, Turkey}
      {B.Sc. in Computer Engineering; GPA: 3.24/4.0}{Oct. 2023 -- June 2027 (Expected)}
  \resumeSubHeadingListEnd

%-----------EXPERIENCE-----------
\section{Experience}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Hacettepe Biological Data Science Lab}{Aug. 2025 -- Present}
      {Undergraduate Researcher}{Ankara, Turkey}
\vspace{0.5pt}
      \resumeItemListStart
\resumeItem{Developed \textbf{ProtMamba}, a \textbf{State-Space Model} for generative protein language modeling, bypassing Transformer quadratic bottlenecks for linear-time inference.}
\resumeItem{Engineered scalable \textbf{PyTorch} data pipelines for 60M+ sequences, utilizing \textbf{Hugging Face} for tokenization and dynamically tracking large-scale training/hyperparameter optimization experiments via \textbf{Weights & Biases (W&B)}.}

      \resumeItemListEnd
\vspace{5pt}
    \resumeSubheading
      {Nanominds}{July 2025 - August 2025}
      {Intern}{İstanbul, Turkey}
\vspace{0.5pt}
\resumeItemListStart
\resumeItem{Researched \textbf{AI workflows in Venture Capital} and analyzed AI use cases across the investment process. I also studied \textbf{Hybrid RAG}, focusing on combining \textbf{dense} and \textbf{sparse retrieval} for improved knowledge systems. The results were presented as a strategic report to the venture capital firm.}

      \resumeItemListEnd
\vspace{5pt}
    \resumeSubheading
      {Zenith AI Team}{March 2025 -- Present}
      {Team Lead & Computer Vision Engineer}{Ankara, Turkey}
\vspace{0.5pt}
      \resumeItemListStart
        \resumeItem{Engineered a vision-based navigation system for a GPS-denied UAV challenge (TEKNOFEST), securing \textbf{finalist} status with the \textbf{highest semi-final trajectory score (0.894)} via \textbf{ORB odometry}; optimized \textbf{YOLO} models via \textbf{data augmentation} to robustly detect objects from challenging aerial imagery.}
        
    \resumeItemListEnd
  \resumeSubHeadingListEnd

%-----------PROJECTS-----------
\section{Technical Projects}
    \resumeSubHeadingListStart

      \resumeProjectHeading
          {\textbf{nanoGPT} $:$ \emph{\textbf{Pytorch/Numpy}} \href{https://github.com/myz21/GPT}{(Click for project - GitHub)}}{Jan. 2026}
          \resumeItemListStart
            \resumeItem{Built a \textbf{GPT language model from scratch} using decoder-only transformer architecture with character-level tokenization, trained for 50 epochs on RTX A5000 GPU over 53 hours to generate contextual text descriptions.}
          \resumeItemListEnd
    \vspace{0.1pt}

      \resumeProjectHeading
          {\textbf{DoctorGPT: Medical Assistant} \href{https://github.com/myz21/DoctorGPT}{(Click for project - GitHub)}}{July 2025}
          \resumeItemListStart
            \resumeItem{Engineered an intelligent conversational AI web service utilizing \textbf{LangChain, Gemini, FastAPI, and Pydantic} to deliver highly responsive, context-aware, and structured natural language interactions for users. }
          \resumeItemListEnd
\vspace{0.1pt}


      \resumeProjectHeading
          {\textbf{E-Corp Customer Insight Analysis} $|$ \emph{\href{https://lnkd.in/dAXxunMu}{2nd Place - Click for post} }}{Mar. 2025}
          \resumeItemListStart
            \resumeItem{Awarded \textbf{2nd Place} by achieving \textbf{0.92 R-squared score} in revenue prediction via optimized \textbf{AdaBoost} and extensive EDA using \textbf{Pandas} and \textbf{Matplotlib}.}
          \resumeItemListEnd
\vspace{0.1pt}

      
    \resumeProjectHeading
        {\textbf{The Traitor — Client/Server Game (C++/SFML)} \href{https://github.com/M-Enes/OOP_Group19}{(Click for project - GitHub)}}{Dec. 2025}
        \resumeItemListStart
          \resumeItem{Built SFML client UI (menu/lobby/action), avatar selection/rendering, and game-over/win screens.}
          \resumeItem{Integrated with \textbf{TCP client--server networking} and \textbf{packet-based messaging} for multiplayer gameplay.}
        \resumeItemListEnd
        
    \resumeSubHeadingListEnd

%-----------LEADERSHIP & AWARDS-----------
\section{Leadership & Awards}
  \resumeSubHeadingListStart

    \resumeProjectHeading
      {\textbf{Vodafone AI Ideathon (Bi' Düşünsene)} $|$ \href{https://lnkd.in/dZVzU3Wx}{\textbf{3rd Place Winner - Click for post}}}{Dec. 2024}
      \resumeItemListStart
        \resumeItem{Conceptualized an early Earthquake Warning System integrated into the Vodafone ecosystem, leveraging Fiber Optic Sensing technology to detect seismic vibrations via existing telecommunication infrastructure.}
      \resumeItemListEnd

    \vspace{4pt}



    \resumeProjectHeading
      {\textbf{Happy Hacking Space Code Jam} $|$ \href{https://www.linkedin.com/posts/myzz_dear-connections-i-finished-the-code-jam-activity-7290399937270308865-ghH9/}{\textbf{2nd Place Winner - Click for post}}}{Jan. 2025}
      \resumeItemListStart
\vspace{0.2pt}
        \resumeItem{Ranked 2nd among competitors by solving complex algorithmic challenges under strict time constraints.}
      \resumeItemListEnd

  \resumeSubHeadingListEnd

%-----------SKILLS-----------
\section{Technical Skills}
 \begin{itemize}[leftmargin=0.15in, label={}]
    \small{\item{
     \textbf{AI/ML Frameworks}{: PyTorch, TensorFlow, Scikit-learn, LangChain, HuggingFace, OpenCV, YOLO} \\
     \textbf{Tools & DevOps}{: Git, Docker, FastAPI, Streamlit, Pandas, NumPy, Matplotlib, Linux} \\
     \textbf{Languages}{: Python, C++, Java, SQL}
    }}
 \end{itemize}

\end{document}
"""

LINKEDIN_MYZ_JSON_CONTENT = """
[{
  "basic_info": {
    "fullname": "Muhammed Yıldız",
    "first_name": "Muhammed",
    "last_name": "Yıldız",
    "headline": "Undergraduate Researcher",
    "public_identifier": "myzz",
    "profile_url": "https://linkedin.com/in/myzz",
    "profile_picture_url": "https://media.licdn.com/dms/image/v2/D4D03AQF-EzlVAlRENg/profile-displayphoto-shrink_800_800/B4DZSM0oBNGUAc-/0/1737529393670?e=1779321600&v=beta&t=yoC0twkRVwAeXHYuuhC1uhHsGLVajDkMhzna94dEs58",
    "about": "https://www.github.com/myz21\n\nHi, I’m Muhammed Yıldız from Diyarbakır, Turkey. I’m a Computer Engineering student at Ankara Yıldırım Beyazıt University, passionate about designing AI-powered tools to solve routine problems. My experiences range from leading AI projects with my friends to developing machine learning solutions for various applications. I also actively contribute to the AI team through workshops and collaborative projects.\n\nI am particularly interested in advancing the field of AI, with a focus on world models and physical AI, and I aspire to work at leading global companies to innovate in these areas. With a creative background in drawing, I strive to leverage both my technical and artistic skills to bring new ideas to life across AI and other disciplines.\n\nDeep work is all you need!",
    "location": {
      "country": "Türkiye",
      "city": "Ankara",
      "full": "Ankara, Türkiye",
      "country_code": "TR"
    },
    "creator_hashtags": [],
    "is_creator": false,
    "is_influencer": false,
    "is_premium": true,
    "open_to_work": false,
    "created_timestamp": 1628586800389,
    "show_follower_count": false,
    "background_picture_url": "https://media.licdn.com/dms/image/v2/D4D16AQEzOHsQh-wJzw/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1708412644225?e=1779321600&v=beta&t=bYM2z4qTvifMbl-cP0jQWh-51nA6sVq_XHvECyxbFQg",
    "urn": "ACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI",
    "follower_count": 992,
    "connection_count": 967,
    "current_company": "Hacettepe University",
    "current_company_urn": "21486",
    "current_company_url": "https://www.linkedin.com/company/hacettepe-university",
    "top_skills": [],
    "email": null
  },
  "experience": [
    {
      "title": "Undergraduate Researcher at Biological Data Science Lab",
      "company": "Hacettepe Üniversitesi",
      "location": "Ankara, Türkiye",
      "description": "Adapting state-of-the-art LLMs to protein generation and downstream tasks. Specifically working on the state space model Mamba.",
      "duration": "Aug 2025 - Present · 9 mos",
      "start_date": {
        "year": 2025,
        "month": "Aug"
      },
      "is_current": true,
      "company_linkedin_url": "https://www.linkedin.com/company/21486/",
      "company_logo_url": "https://media.licdn.com/dms/image/v2/D4D0BAQGR4I1T9kjcjg/company-logo_400_400/B4DZxQ_QdjIwAg-/0/1770885286131/hacettepe_university_logo?e=1779321600&v=beta&t=hb5YN_UXZWwN9-5vhcru1uELXD5OYPGwNDeWaNesgDU",
      "location_type": "Hybrid",
      "skills": [
        "Pytorch",
        "Transformer Models and +1 skill"
      ],
      "company_id": "21486",
      "skills_url": "https://www.linkedin.com/in/myzz/overlay/urn:li:fsd_profilePosition:(ACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI,2729147266)/skill-associations-details?profileUrn=urn%3Ali%3Afsd_profile%3AACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI"
    },
    {
      "title": "AI Engineering Intern",
      "company": "nanominds",
      "location": "Istanbul, Türkiye",
      "description": "- Researched AI workflows in Venture Capital and analyzed AI use cases across the investment process.\n- I also studied Hybrid RAG, focusing on combining dense and sparse retrieval for improved knowledge systems. \n- The results were presented as a strategic report to AI Startup Factory @isbankasi Group.",
      "duration": "Jul 2025 - Aug 2025 · 2 mos",
      "start_date": {
        "year": 2025,
        "month": "Jul"
      },
      "end_date": {
        "year": 2025,
        "month": "Aug"
      },
      "is_current": false,
      "company_linkedin_url": "https://www.linkedin.com/company/106623630/",
      "company_logo_url": "https://media.licdn.com/dms/image/v2/D4D0BAQGilLZ2_6V4dw/company-logo_400_400/B4DZViLuOTHkAY-/0/1741108995444/nanomindsai_logo?e=1779321600&v=beta&t=IAHaGuzgApUOmVBnVZdC1r8UBGPhFYTeYgPNWxLBYSI",
      "employment_type": "Full-time",
      "location_type": "Remote",
      "skills": [
        "Almayla Artırılmış Üretim (RAG) and Girişimcilik"
      ],
      "company_id": "106623630",
      "skills_url": "https://www.linkedin.com/in/myzz/overlay/urn:li:fsd_profilePosition:(ACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI,2876092728)/skill-associations-details?profileUrn=urn%3Ali%3Afsd_profile%3AACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI"
    },
    {
      "title": "Part Time Working Student",
      "company": "Ankara Yıldırım Beyazıt Üniversitesi",
      "description": "I was hired for this role due to my personal interest and talent in meaningful cartoon drawings and pencil sketching. I taught students the fundamentals of pencil drawing and provided key advice to help them develop their 3D thinking skills. I created tutorials using various drawing books and YouTube resources. My lessons covered a wide range of topics, starting from perspective drawing to anatomical sketches. Currently, I continue to draw with my students, and we have formed a small but active drawing community.",
      "duration": "Mar 2025 - May 2025 · 3 mos",
      "start_date": {
        "year": 2025,
        "month": "Mar"
      },
      "end_date": {
        "year": 2025,
        "month": "May"
      },
      "is_current": false,
      "company_linkedin_url": "https://www.linkedin.com/company/16196522/",
      "company_logo_url": "https://media.licdn.com/dms/image/v2/D4D0BAQEjDwjEPrv2Xg/company-logo_400_400/company-logo_400_400/0/1723661781036?e=1779321600&v=beta&t=KyHxGwWg1AUcqmfjMI55NmAjf32vy5xPJSUfBCj5jWk",
      "skills": [
        "Sanat"
      ],
      "company_id": "16196522",
      "skills_url": "https://www.linkedin.com/in/myzz/overlay/urn:li:fsd_profilePosition:(ACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI,2665313808)/skill-associations-details?profileUrn=urn%3Ali%3Afsd_profile%3AACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI"
    },
    {
      "title": "Team Lead",
      "company": "BİLTEK AI",
      "location": "Ankara, Türkiye",
      "description": "I took over the leadership of the newly founded AI team in one of the most established clubs at my university. I founded a competition team called Zenith AI, and with this team, we are currently preparing for the semi-finals of the TEKNOFEST 2025 Artificial Intelligence in Aviation competition.\nWe also organized the club’s first-ever AI conference, which focused on Explainable AI.\nThis experience has been a valuable step in improving my leadership skills.\nCurrently, I continue to lead the Zenith AI team independently from the club.",
      "duration": "Sep 2024 - Mar 2025 · 7 mos",
      "start_date": {
        "year": 2024,
        "month": "Sep"
      },
      "end_date": {
        "year": 2025,
        "month": "Mar"
      },
      "is_current": false,
      "company_linkedin_url": "https://www.linkedin.com/company/105204708/",
      "company_logo_url": "https://media.licdn.com/dms/image/v2/D4E0BAQGFAX6akFXmrA/company-logo_400_400/company-logo_400_400/0/1728499905877/biltek_ai_logo?e=1779321600&v=beta&t=JOXXSe_9NO89LMuvT1baawNWL2bK-u3rs3lhRA_7Gb8",
      "skills": [
        "Proje Yönetimi and Liderlik"
      ],
      "company_id": "105204708",
      "skills_url": "https://www.linkedin.com/in/myzz/overlay/urn:li:fsd_profilePosition:(ACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI,2494785251)/skill-associations-details?profileUrn=urn%3Ali%3Afsd_profile%3AACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI"
    },
    {
      "title": "Core Team Member of AI Department",
      "company": "AYBÜ Bilim ve Teknoloji Topluluğu",
      "duration": "May 2024 - Mar 2025 · 11 mos",
      "start_date": {
        "year": 2024,
        "month": "May"
      },
      "end_date": {
        "year": 2025,
        "month": "Mar"
      },
      "is_current": false,
      "company_linkedin_url": "https://www.linkedin.com/company/5167630/",
      "company_logo_url": "https://media.licdn.com/dms/image/v2/D4D0BAQH6TkPx7w1JUw/company-logo_400_400/B4DZoR.dADKQAc-/0/1761238176608?e=1779321600&v=beta&t=idJzhAWOBCXO4uFvM7YDaKtRNnbTLneKJaBtpbTuHQE",
      "company_id": "5167630"
    },
    {
      "title": "Member of Cyber Department ",
      "company": "AYBÜ Bilim ve Teknoloji Topluluğu",
      "duration": "Nov 2023 - May 2024 · 7 mos",
      "start_date": {
        "year": 2023,
        "month": "Nov"
      },
      "end_date": {
        "year": 2024,
        "month": "May"
      },
      "is_current": false,
      "company_linkedin_url": "https://www.linkedin.com/company/5167630/",
      "company_logo_url": "https://media.licdn.com/dms/image/v2/D4D0BAQH6TkPx7w1JUw/company-logo_400_400/B4DZoR.dADKQAc-/0/1761238176608?e=1779321600&v=beta&t=idJzhAWOBCXO4uFvM7YDaKtRNnbTLneKJaBtpbTuHQE",
      "company_id": "5167630"
    }
  ],
  "education": [
    {
      "school": "Ankara Yıldırım Beyazıt Üniversitesi",
      "degree": "Lisans Derecesi, Bilgisayar Mühendisliği",
      "degree_name": "Lisans Derecesi",
      "field_of_study": "Bilgisayar Mühendisliği",
      "duration": "Oct 2023 - Jun 2027",
      "school_linkedin_url": "https://www.linkedin.com/company/16196522/",
      "skills": "C, Java and +3 skills",
      "school_logo_url": "https://media.licdn.com/dms/image/v2/D4D0BAQEjDwjEPrv2Xg/company-logo_400_400/company-logo_400_400/0/1723661781036?e=1779321600&v=beta&t=KyHxGwWg1AUcqmfjMI55NmAjf32vy5xPJSUfBCj5jWk",
      "start_date": {
        "year": 2023,
        "month": "Oct"
      },
      "end_date": {
        "year": 2027,
        "month": "Jun"
      },
      "school_id": "16196522"
    },
    {
      "school": "Firat University",
      "degree": "Lisans Derecesi, Dentistry",
      "degree_name": "Lisans Derecesi",
      "field_of_study": "Dentistry",
      "duration": "Sep 2021 - Aug 2023",
      "school_linkedin_url": "https://www.linkedin.com/company/142443/",
      "description": "dropped out to pursue my dreams",
      "activities": "FÜ Foreign Language Club",
      "school_logo_url": "https://media.licdn.com/dms/image/v2/C510BAQE3p1j1WWn1Fg/company-logo_400_400/company-logo_400_400/0/1631329825242?e=1779321600&v=beta&t=IIV1wja86Yk_aFV-2BfbVJFpoydWGxYbqrHV0p7KFrM",
      "start_date": {
        "year": 2021,
        "month": "Sep"
      },
      "end_date": {
        "year": 2023,
        "month": "Aug"
      },
      "school_id": "142443"
    }
  ],
  "certifications": [
    {
      "name": "Deep Learning Study Group",
      "issuer": "inzva",
      "issued_date": "Issued Apr 2026"
    },
    {
      "name": "AI Club Datathon'25 Second Prize",
      "issuer": "Hacettepe Üniversitesi Yapay Zeka Topluluğu",
      "issued_date": "Issued Mar 2025"
    }
  ],
  "featured": [
    {
      "type": "post",
      "description": "TR:\n\nVodafone Bi' Düşünsene Fikir Yarışması'nda FiberSense takımımız ile 198 üniversiteden, 2200 başvuru arasından finallere kalarak finalde\u00a0üçüncülük\u00a0elde ettik.\n\nVodafone Yanımda uygulamasına entegre etmeyi düşündüğümüz FiberSense'in ülkemiz için stratejik önemini, Vodafone'a olacak katkısını, uygulanabilirliğini Vodafone Genel Müdürlüğü'nde ekip arkadaşım Evran Can Aras ile jürilere sunduk.\n\nFikrimize gösterdikleri ilgiden dolayı başta sayın Engin Aksoy'a ve sayın Akan Abdula'ya,  Nazlı Tlabar Güler'e,  DENİZ SAĞDIÇ'a , Ayşegül Arıcan Şeker'e,  Meltem Bakiler Sahin'e , ELİF ERGU DEMİRAL'e  Mehmet Keteloglu'na, süreçte bizi bilgilendiren sayın Fatma Bal'a, yarışmadaki arkadaşlarıma ve tabii ki çok değerli Vodafone ailesine teşekkürlerimi sunarım. Azimle çalışmaya, çabalamaya devam edeceğiz.\u00a0 \n\nEN:\n\nWe made it to the finals and won\u00a0third place\u00a0among 2200 applications from 198 universities in the Vodafone Bi' Düşünsene Ideathon.\n\nI am thankful for the great interest and support shown for our idea during this challenging but rewarding process. My thanks go to the esteemed jury members, all the participants in the competition, and the valuable Vodafone family. We will continue to work and strive with determination.",
      "url": "https://www.linkedin.com/feed/update/urn:li:activity:7406752769224663042?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7406752769224663042%29",
      "image_url": "https://media.licdn.com/dms/image/v2/D5622AQGnIKS1YQe5bA/feedshare-shrink_2048_1536/B56ZsoSY5uJ8Aw-/0/1765907468948?e=1779321600&v=beta&t=4pky9az-Y69jkp1YiQvi31Isi_bhEMB4PYLyu3jtoCA",
      "social_counts": {
        "likes": 136,
        "comments": 20,
        "reaction_counts": [
          {
            "type": "like",
            "count": 129
          },
          {
            "type": "praise",
            "count": 6
          },
          {
            "type": "empathy",
            "count": 1
          }
        ]
      }
    },
    {
      "type": "post",
      "description": "Global AI Hub tarafından gerçekleştirilen Aygaz A.Ş. Yapay Zekaya Giriş Bootcamp programına katılmaktan büyük bir memnuniyet duydum. \n\nGururla belirtmek isterim ki, projem ilk 3 proje arasına seçildi ve proje sunumumu başarıyla gerçekleştirdim.\n\nBu inanılmaz yolculukta beni destekleyen ve süreci yöneten Community Lead ve mentörlerimiz Ayşenur Dedecan, İsmail AÇAR, Göker Güner, Hayatı Can AYDIN, Gunnur Senturk, Uğurcan Uzunkaya, İBRAHİM ENES ULUSOY, Mert Yasin Bozkır ve Buldan Karahan'a sonsuz teşekkürlerimi sunuyorum.\n\nYouTube Yayın Linki: https://lnkd.in/dzPcf-uJ\nProjemin linki: https://lnkd.in/dZPajgkh",
      "url": "https://www.linkedin.com/feed/update/urn:li:activity:7213269522361815042?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7213269522361815042%29",
      "image_url": "https://media.licdn.com/dms/image/v2/D4D22AQERz42Ea13g9A/feedshare-shrink_2048_1536/feedshare-shrink_2048_1536/0/1719777469166?e=1779321600&v=beta&t=nP7sAw1MQTz72uiY2uUV9vcVnU7Cz7aSRLNf8zIBiEg",
      "social_counts": {
        "likes": 26,
        "comments": 5,
        "reaction_counts": [
          {
            "type": "like",
            "count": 18
          },
          {
            "type": "praise",
            "count": 7
          },
          {
            "type": "appreciation",
            "count": 1
          }
        ]
      }
    },
    {
      "type": "post",
      "description": "Dear connections,\n\nI finished the Code Jam, organized by Happy Hacking Space, in second place \ud83e\udd48. In this three-stage competition, we solved competitive programming questions. It was a fun and exciting experience. First and foremost, I would like to thank Dogan Can Bakir and the esteemed moderators. I hope to achieve even greater successes in the future.\n\n---\n\nDeğerli bağlantılarım merhaba,\n\n25 Ocak'ta Happy Hacking Space ve .. tarafından düzenlenen Code Jam'i 2. olarak tamamladım. 3 aşamalı bu yarışmada competitive programming sorularını çözdük. Eğlenceli bir etkinlikti. Başta topluluk kurucusu Dogan Can Bakir'a ve değerli moderatörlere teşekkürler. İleriki süreçte daha büyük başarılara imza atmam ümidiyle.\n",
      "url": "https://www.linkedin.com/feed/update/urn:li:activity:7290399937270308865?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7290399937270308865%29",
      "image_url": "https://media.licdn.com/dms/image/v2/D4D22AQHRa5M9kejYHg/feedshare-shrink_1280/B4DZSy0GQCGkAw-/0/1738166791943?e=1779321600&v=beta&t=xcRlX27zRmHyppEY9zAeUgzMh9tceVkiMiAzgV1N_cQ",
      "social_counts": {
        "likes": 63,
        "comments": 4,
        "reaction_counts": [
          {
            "type": "like",
            "count": 60
          },
          {
            "type": "praise",
            "count": 2
          },
          {
            "type": "empathy",
            "count": 1
          }
        ]
      }
    },
    {
      "type": "post",
      "description": "Hacettepe Üniversitesi Yapay Zeka Topluluğu'nun düzenlediği Datathon’da ekibimizle \ud83d\udfdf\ud83d\udfdf\ud83d\udfdf takım / \ud83d\udfdf\ud83d\udfdf\ud83d\udfdf katılımcı arasından finalist olup, final sunumumuzda \ud835\udc22\ud835\udc24\ud835\udc22\ud835\udc27\ud835\udc1c\ud835\udc22\ud835\udc25\ud835\udc22\ud835\udc24 ödülünü kazanmanın gururunu yaşadık! \ud83c\udf89\nTakım arkadaşlarım Fırat Özcan ve Mustafa Özcan ile, Adaboost gibi güçlü makine öğrenmesi modellerini kullanarak, keşifsel veri analizleri yaptık. \n\nSponsor firma Insider için geleceğin pazarlama stratejilerine yönelik öngörüler sunduk. Jürilerden Ahmet Önol ve Prof. Dr. Ali Serhan Koyuncugil'e ayrıca teşekkürler. \n\n Gerçek \"\ud835\udc01\ud835\udc22\ud835\udc25\ud835\udc22\ud835\udc26 \ud835\udc2f\ud835\udc1e \ud835\udc2d\ud835\udc1e\ud835\udc24\ud835\udc27\ud835\udc28\ud835\udc25\ud835\udc28\ud835\udc20\ud835\udc22\" ışığında gerçekleştirdiğimiz bu çalışma, teknik bilgi ve azimle neler başarabileceğimizin somut bir kanıtıdır. Ekibimdeki her bireye teşekkür eder, gelecekte daha büyük başarılara imza atmayı dilerim!\n\n#AI #MachineLearning #Datathon #Adaboost #Insider #Innovation #Hakikat\n\nEnglish:\n\nAt the Datathon organized by Hacettepe University AI Club, our team proudly became finalists among 228 teams and had the honor of winning second place in the final presentation! \ud83c\udf89\n\nIn our presentation, we conducted exploratory data analyses using powerful machine learning models like Adaboost, and provided insights into future marketing strategies for our sponsor, Insider.\n\nThis work, carried out in the true light of \"Science and Technology,\" is a tangible testament to what can be achieved with technical knowledge and determination. I thank every individual on my team and look forward to even greater accomplishments in the future!\n\nhttps://lnkd.in/dAXxunMu",
      "url": "https://www.linkedin.com/feed/update/urn:li:activity:7308571251696984064?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7308571251696984064%29",
      "image_url": "https://media.licdn.com/dms/image/v2/D4D22AQGRB-7q3y1dkA/feedshare-shrink_2048_1536/B4DZW1Cr4AGcA0-/0/1742499156865?e=1779321600&v=beta&t=krhzwTV4MTE1d4XHnJ0ObY-I0fvOgvYF8v8LVUff8ho",
      "social_counts": {
        "likes": 147,
        "comments": 6,
        "reaction_counts": [
          {
            "type": "like",
            "count": 136
          },
          {
            "type": "praise",
            "count": 10
          },
          {
            "type": "empathy",
            "count": 1
          }
        ]
      }
    },
    {
      "type": "post",
      "description": "Türkiye’nin en prestijli teknoloji festivali TEKNOFEST'te Ankara Yıldırım Beyazıt Üniversitesi öğrencileri olarak, Havacılıkta Yapay Zeka yarışmasında 2025’te kurduğumuz Zenith AI takımımız ile kısıtlı imkânlara ve teknik engellere rağmen takım arkadaşlarım Emre Akpınar, Musab Demir ve Yunus Emre Ceran  ile birlikte verdiğimiz beş aylık yoğun çalışmanın sonunda çevrimiçi yarışma simülasyonunda 10. sırayı elde ederek büyük bir başarıya imza attık.\n\nNesne tanıma (object detection) ve konum kestirimi (visual odometry) üzerine çalıştık; konum kestirimi algoritmamız 0.894 rpg_trajectory_evaluation puanı ile ilk sırayı aldı. Uykusuz gecelerimizin meyvesini böylece almış olduk.\n\nBu yalnızca bir başlangıç. Çabamız sürecek, bu yolculukta finalde çok daha iyisini yapmayı hedefliyoruz. Hedefimiz birincilik. Fettah olan Allah, galip gelmeyi nasip etsin.\n\nİleriki gelişmelerimizden haberdar olabilmek için Next hesabımızı buradan takip edebilirsiniz: https://lnkd.in/d4ngM75x\n\n#TEKNOFEST #YapayZeka #havacılıktayapayzeka #YıldırımBeyazıtÜniversitesi #ROCKY",
      "url": "https://www.linkedin.com/feed/update/urn:li:activity:7365358690230501376?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7365358690230501376%29",
      "image_url": "https://media.licdn.com/dms/image/v2/D4D22AQGRsf9Y9T51vQ/feedshare-shrink_2048_1536/B4DZjcCsJjGsA0-/0/1756038352608?e=1779321600&v=beta&t=AU1NeIcUb_VHgAesHKkAoX3KyPftF0D90rGfON9lL98",
      "social_counts": {
        "likes": 131,
        "comments": 20,
        "reaction_counts": [
          {
            "type": "like",
            "count": 118
          },
          {
            "type": "praise",
            "count": 11
          },
          {
            "type": "appreciation",
            "count": 2
          }
        ]
      }
    }
  ]
}]"""

LINKEDIN_MYZ2_JSON_CONTENT = """
[{
  "about": "https://www.github.com/myz21\n\nHi, I’m Muhammed Yıldız from Diyarbakır, Turkey. I’m a Computer Engineering student at Ankara Yıldırım Beyazıt University, passionate about designing AI-powered tools to solve routine problems. My experiences range from leading AI projects with my friends to developing machine learning solutions for various applications. I also actively contribute to the AI team through workshops and collaborative projects.\n\nI am particularly interested in advancing the field of AI, with a focus on world models and physical AI, and I aspire to work at leading global companies to innovate in these areas. With a creative background in drawing, I strive to leverage both my technical and artistic skills to bring new ideas to life across AI and other disciplines.\n\nDeep work is all you need!",
  "address": null,
  "addressCountryOnly": "Türkiye",
  "addressWithCountry": "Ankara, Türkiye Türkiye",
  "addressWithoutCountry": "Ankara, Türkiye",
  "backgroundPicture": "https://media.licdn.com/dms/image/v2/D4D16AQEzOHsQh-wJzw/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1708412644225?e=1779321600&v=beta&t=bYM2z4qTvifMbl-cP0jQWh-51nA6sVq_XHvECyxbFQg",
  "backgroundPictureAllDimentions": [
    {
      "expiresAt": 1779321600000,
      "height": 199,
      "image": "https://media.licdn.com/dms/image/v2/D4D16AQEzOHsQh-wJzw/profile-displaybackgroundimage-shrink_200_800/profile-displaybackgroundimage-shrink_200_800/0/1708412644225?e=1779321600&v=beta&t=kOZ96WlSHArFtm_41TshDfqZkLHVMGnwahO5yenNEvU",
      "width": 800
    },
    {
      "expiresAt": 1779321600000,
      "height": 349,
      "image": "https://media.licdn.com/dms/image/v2/D4D16AQEzOHsQh-wJzw/profile-displaybackgroundimage-shrink_350_1400/profile-displaybackgroundimage-shrink_350_1400/0/1708412644225?e=1779321600&v=beta&t=bYM2z4qTvifMbl-cP0jQWh-51nA6sVq_XHvECyxbFQg",
      "width": 1400
    }
  ],
  "companyNameOnProfileTopCardShown": false,
  "creator": false,
  "current_company": "Hacettepe University",
  "current_company_description": "Founded on the foundations of the Chair of Child Health established in 1954 by Prof. Dr. İhsan Doğramacı, Hacettepe rapidly became one of Türkiye’s most prominent institutions in the fields of health and science. With the establishment of the Children’s Hospital and the Institute of Child Health, a strong academic structure was formed that integrated education, research, and public service. This pioneering approach in health sciences was further institutionalized with the establishment of the Faculty of Medicine and the Faculty of Health Sciences.\n\nWith the official establishment of Hacettepe University in 1967, this accumulated academic heritage was consolidated under a single university structure. Since then, Hacettepe has taken its place among Türkiye’s most respected and leading higher education institutions.\n\nCelebrating its 50th anniversary in 2017 with pride, Hacettepe University today continues to contribute to social development and universal values in the fields of science, technology, and the arts through its 17 faculties, 15 institutes, 4 vocational schools, 2 schools of higher education, 1 conservatory, and 98 research and application centers.\n\nFor tens of thousands of students, alumni, and staff members, being a member of Hacettepe means being part of a distinguished academic tradition, a strong institutional culture, and a vision that shapes the future.",
  "current_company_domain": "hacettepe.edu.tr",
  "current_company_employee_count": "7648",
  "current_company_followers": 177420,
  "current_company_headquarters": "Ankara, TR",
  "current_company_industry": "Higher Education",
  "current_company_linkedin_url": "https://tr.linkedin.com/school/hacettepe-university/",
  "current_company_name": "Hacettepe University",
  "current_company_organization_type": "Educational",
  "current_company_url": "https://tr.linkedin.com/school/hacettepe-university/",
  "current_company_website": "http://hacettepe.edu.tr/",
  "educationOnProfileTopCardShown": false,
  "educations": [
    {
      "caption": "Oct 2023 - Jun 2027",
      "companyId": "16196522",
      "companyLink1": "https://www.linkedin.com/school/ybuankara/",
      "companyUrn": "urn:li:fsd_company:16196522",
      "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQEjDwjEPrv2Xg/company-logo_400_400/company-logo_400_400/0/1723661781036?e=1779321600&v=beta&t=KyHxGwWg1AUcqmfjMI55NmAjf32vy5xPJSUfBCj5jWk",
      "subComponents": [],
      "subtitle": "Lisans Derecesi, Bilgisayar Mühendisliği",
      "title": "Ankara Yıldırım Beyazıt Üniversitesi"
    },
    {
      "caption": "Sep 2021 - Aug 2023",
      "companyId": "142443",
      "companyLink1": "https://www.linkedin.com/school/firat-university/",
      "companyUrn": "urn:li:fsd_company:142443",
      "logo": "https://media.licdn.com/dms/image/v2/C510BAQE3p1j1WWn1Fg/company-logo_400_400/company-logo_400_400/0/1631329825242?e=1779321600&v=beta&t=IIV1wja86Yk_aFV-2BfbVJFpoydWGxYbqrHV0p7KFrM",
      "subComponents": [
        {
          "text": "78.73",
          "type": "insightComponent"
        }
      ],
      "subtitle": "Lisans Derecesi, FÜ Foreign Language Club",
      "title": "Fırat Üniversitesi"
    },
    {
      "caption": "Sep 2017 - Jun 2021",
      "subComponents": [
        {
          "text": "92.45",
          "type": "insightComponent"
        }
      ],
      "subtitle": "High School Diploma, Yok",
      "title": "Nevzat Ayaz Anadolu Lisesi"
    }
  ],
  "experiences": [
    {
      "breakdown": false,
      "caption": "Aug 2025 - Present · 5 mos",
      "companyId": "21486",
      "companyLink1": "https://www.linkedin.com/school/hacettepe-university/",
      "companyUrn": "urn:li:fsd_company:21486",
      "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQGR4I1T9kjcjg/company-logo_100_100/B4DZxQ_QdjIwAY-/0/1770885286131/hacettepe_university_logo?e=1779321600&v=beta&t=P3pqP3sG0s9lvwfKcbuQN_rzNREJGW-hsRPriyArGzg",
      "metadata": "Ankara, Türkiye",
      "subComponents": [
        {
          "description": {
            "text": "Adapting state-of-the-art LLMs to protein generation and downstream tasks. Specifically working on the state space model Mamba.",
            "type": "textComponent"
          }
        }
      ],
      "subtitle": "Hacettepe Üniversitesi",
      "title": "Undergraduate Researcher at Biological Data Science Lab"
    },
    {
      "breakdown": false,
      "caption": "Jul 2025 - Aug 2025 · 1 mo",
      "companyId": "106623630",
      "companyLink1": "https://www.linkedin.com/company/nanomindsai/",
      "companyUrn": "urn:li:fsd_company:106623630",
      "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQGilLZ2_6V4dw/company-logo_100_100/B4DZViLuOTHkAQ-/0/1741108995444/nanomindsai_logo?e=1779321600&v=beta&t=yQEiwESZ7H3n0yBfIYYpEcJTxCUKR68mP65l_DUm4ac",
      "metadata": "İstanbul, Türkiye",
      "subComponents": [
        {
          "description": {
            "text": "- Researched AI workflows in Venture Capital and analyzed AI use cases across the investment process.\n- I also studied Hybrid RAG, focusing on combining dense and sparse retrieval for improved knowledge systems. \n- The results were presented as a strategic report to AI Startup Factory @isbankasi Group.",
            "type": "textComponent"
          }
        }
      ],
      "subtitle": "nanominds · Full-time",
      "title": "AI Engineering Intern"
    },
    {
      "breakdown": false,
      "caption": "Mar 2025 - May 2025 · 2 mos",
      "companyId": "16196522",
      "companyLink1": "https://www.linkedin.com/school/ybuankara/",
      "companyUrn": "urn:li:fsd_company:16196522",
      "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQEjDwjEPrv2Xg/company-logo_400_400/company-logo_400_400/0/1723661781036?e=1779321600&v=beta&t=KyHxGwWg1AUcqmfjMI55NmAjf32vy5xPJSUfBCj5jWk",
      "subComponents": [
        {
          "description": {
            "text": "I was hired for this role due to my personal interest and talent in meaningful cartoon drawings and pencil sketching. I taught students the fundamentals of pencil drawing and provided key advice to help them develop their 3D thinking skills. I created tutorials using various drawing books and YouTube resources. My lessons covered a wide range of topics, starting from perspective drawing to anatomical sketches. Currently, I continue to draw with my students, and we have formed a small but active drawing community.",
            "type": "textComponent"
          }
        }
      ],
      "subtitle": "Ankara Yıldırım Beyazıt Üniversitesi",
      "title": "Part Time Working Student"
    },
    {
      "breakdown": false,
      "caption": "Sep 2024 - Mar 2025 · 7 mos",
      "companyId": "105204708",
      "companyLink1": "https://www.linkedin.com/company/biltek-ai/",
      "companyUrn": "urn:li:fsd_company:105204708",
      "logo": "https://media.licdn.com/dms/image/v2/D4E0BAQGFAX6akFXmrA/company-logo_100_100/B4DZjcCsJjGsA0-/0/1756038352608?e=1779321600&v=beta&t=AU1NeIcUb_VHgAesHKkAoX3KyPftF0D90rGfON9lL98",
      "metadata": "Ankara, Türkiye",
      "subComponents": [
        {
          "description": {
            "text": "I took over the leadership of the newly founded AI team in one of the most established clubs at my university. I founded a competition team called Zenith AI, and with this team, we are currently preparing for the semi-finals of the TEKNOFEST 2025 Artificial Intelligence in Aviation competition.\nWe also organized the club’s first-ever AI conference, which focused on Explainable AI.\nThis experience has been a valuable step in improving my leadership skills.\nCurrently, I continue to lead the Zenith AI team independently from the club.",
            "type": "textComponent"
          }
        }
      ],
      "subtitle": "BİLTEK AI",
      "title": "Team Lead"
    },
    {
      "breakdown": true,
      "companyId": "5167630",
      "companyLink1": "https://www.linkedin.com/company/aybubiltek/",
      "companyUrn": "urn:li:fsd_company:5167630",
      "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQH6TkPx7w1JUw/company-logo_100_100/B4DZoR.dADKQAU-/0/1761238176608?e=1779321600&v=beta&t=Fjw0o85mKDm-Ct8jQK3CvCiYLhNAXtpc2jVnM6hKzHU",
      "subComponents": [
        {
          "caption": "May 2024 - Mar 2025 · 10 mos",
          "description": [],
          "title": "Core Team Member of AI Department"
        },
        {
          "caption": "Nov 2023 - May 2024 · 6 mos",
          "description": [],
          "title": "Member of Cyber Department "
        }
      ],
      "subtitle": "undefined · 1 yr 4 mos",
      "title": "AYBÜ Bilim ve Teknoloji Topluluğu"
    }
  ],
  "firstName": "Muhammed",
  "fullName": "Muhammed Yıldız",
  "geoLocationBackfilled": false,
  "headline": "Undergraduate Researcher",
  "honorsAndAwards": [],
  "industry": "Computer Software",
  "influencer": false,
  "interests": [],
  "languages": [],
  "lastName": "Yıldız",
  "licenseAndCertificates": [
    {
      "breakdown": false,
      "companyId": "28184006",
      "companyLink1": "https://www.linkedin.com/company/inzva/",
      "companyUrn": "urn:li:fsd_company:28184006",
      "logo": "https://media.licdn.com/dms/image/v2/C560BAQGUg-3pKJ16og/company-logo_400_400/company-logo_400_400/0/1631398857864?e=1779321600&v=beta&t=60TxJgAWZhnmIV_cO4q6M7Dq7ZqmzVU7caJub88jI1E",
      "subComponents": [
        {
          "description": []
        }
      ],
      "subtitle": "inzva",
      "title": "Deep Learning Study Group"
    },
    {
      "breakdown": false,
      "companyId": "12622420",
      "companyLink1": "https://www.linkedin.com/company/hacettepeaiclub/",
      "companyUrn": "urn:li:fsd_company:12622420",
      "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFXxGf86xywRA/company-logo_400_400/company-logo_400_400/0/1630497284466/hacettepeaiclub_logo?e=1779321600&v=beta&t=Hrl-E8dwP6zunRV9bLNHICDAL5MwfG21OLexHbuwzic",
      "subComponents": [
        {
          "description": []
        }
      ],
      "subtitle": "Hacettepe Üniversitesi Yapay Zeka Topluluğu",
      "title": "AI Club Datathon'25 Second Prize"
    },
    {
      "breakdown": false,
      "companyId": "14025979",
      "companyLink1": "https://www.linkedin.com/company/ai-business-school/",
      "companyUrn": "urn:li:fsd_company:14025979",
      "logo": "https://media.licdn.com/dms/image/v2/D4E0BAQFDZnLYhTfU4Q/company-logo_400_400/company-logo_400_400/0/1719921413341/ai_business_school_logo?e=1779321600&v=beta&t=z9Ck6iWUjF0S7mI6ro9qpQGwQtnIGhhrzzwJs7HYX7E",
      "subComponents": [
        {
          "description": []
        }
      ],
      "subtitle": "AI Business School",
      "title": "Deep Learning Bootcamp"
    },
    {
      "breakdown": false,
      "companyId": "34917076",
      "companyLink1": "https://www.linkedin.com/company/btk-akademi/",
      "companyUrn": "urn:li:fsd_company:34917076",
      "logo": "https://media.licdn.com/dms/image/v2/D560BAQFzhoINQt47kw/company-logo_400_400/company-logo_400_400/0/1733413650231?e=1779321600&v=beta&t=GwU0PQnpikk7MY1R1f5lN_cfRn61Rxf_Bx0PcoF0fZM",
      "subComponents": [
        {
          "description": []
        }
      ],
      "subtitle": "BTK Akademi",
      "title": "Introduction to 2D Game Development with Unity"
    },
    {
      "breakdown": false,
      "companyId": "18094181",
      "companyLink1": "https://www.linkedin.com/company/milliegitimbakanligi/",
      "companyUrn": "urn:li:fsd_company:18094181",
      "logo": "https://media.licdn.com/dms/image/v2/D4E0BAQFGBeYphcyqBg/company-logo_400_400/B4EZh.zLtkGUAc-/0/1754474004095/milliegitimbakanligi_logo?e=1779321600&v=beta&t=rNYGgp0Sqy95d_AUoZSbTLVneejOVcSpUvAahoE5ANs",
      "subComponents": [
        {
          "description": []
        }
      ],
      "subtitle": "Millî Eğitim Bakanlığı",
      "title": "Oil Painting and Charcoal Drawing Course"
    },
    {
      "breakdown": false,
      "companyId": "14025979",
      "companyLink1": "https://www.linkedin.com/company/ai-business-school/",
      "companyUrn": "urn:li:fsd_company:14025979",
      "logo": "https://media.licdn.com/dms/image/v2/D4E0BAQFDZnLYhTfU4Q/company-logo_400_400/company-logo_400_400/0/1719921413341/ai_business_school_logo?e=1779321600&v=beta&t=z9Ck6iWUjF0S7mI6ro9qpQGwQtnIGhhrzzwJs7HYX7E",
      "subComponents": [
        {
          "description": []
        }
      ],
      "subtitle": "AI Business School",
      "title": "Introduction to Artificial Intelligence"
    }
  ],
  "maidenName": null,
  "memorialized": false,
  "organizations": [],
  "premium": true,
  "primaryLocale": {
    "country": "TR",
    "language": "tr"
  },
  "profilePic": "https://media.licdn.com/dms/image/v2/D4D03AQF-EzlVAlRENg/profile-displayphoto-shrink_800_800/B4DZSM0oBNGUAc-/0/1737529393670?e=1779321600&v=beta&t=yoC0twkRVwAeXHYuuhC1uhHsGLVajDkMhzna94dEs58",
  "profilePicAllDimensions": [
    {
      "expiresAt": 1779321600000,
      "height": 200,
      "image": "https://media.licdn.com/dms/image/v2/D4D03AQF-EzlVAlRENg/profile-displayphoto-shrink_200_200/B4DZSM0oBNGUAY-/0/1737529393665?e=1779321600&v=beta&t=md5glZc9mhhNovtcmqmBG9Il-LdoaVf3y3qDwsWNAhw",
      "width": 200
    },
    {
      "expiresAt": 1779321600000,
      "height": 400,
      "image": "https://media.licdn.com/dms/image/v2/D4D03AQF-EzlVAlRENg/profile-displayphoto-shrink_400_400/B4DZSM0oBNGUAg-/0/1737529393665?e=1779321600&v=beta&t=qcPGOOlv5cCy6sXIbtLoQUpSi5Lari5XafzkEJpNhd8",
      "width": 400
    },
    {
      "expiresAt": 1779321600000,
      "height": 100,
      "image": "https://media.licdn.com/dms/image/v2/D4D03AQF-EzlVAlRENg/profile-displayphoto-shrink_100_100/B4DZSM0oBNGUAU-/0/1737529393665?e=1779321600&v=beta&t=BtQIWWg3QGsJuqQRKTAjCYJ-Ow4NjkKooAd3GoktwsQ",
      "width": 100
    },
    {
      "expiresAt": 1779321600000,
      "height": 560,
      "image": "https://media.licdn.com/dms/image/v2/D4D03AQF-EzlVAlRENg/profile-displayphoto-shrink_800_800/B4DZSM0oBNGUAc-/0/1737529393670?e=1779321600&v=beta&t=yoC0twkRVwAeXHYuuhC1uhHsGLVajDkMhzna94dEs58",
      "width": 560
    }
  ],
  "projects": [],
  "publicIdentifier": "myzz",
  "showPremiumSubscriberBadge": true,
  "skills": [
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "CNN"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Diffusion Models"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Girişimcilik"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Almayla Artırılmış Üretim (RAG)"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Pytorch"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Transformer Models"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Huggingface"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Sanat"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Proje Yönetimi"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Liderlik"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Veri Yapıları"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Algoritmalar"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Veri Analizi"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Makine Öğrenimi"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Uygulamalı Matematik"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Java"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Oyun Geliştirme"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "C"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Çizim"
    },
    {
      "subComponenets": [
        {
          "description": []
        }
      ],
      "title": "Yağlı Boya"
    }
  ],
  "tempStatus": null,
  "urn": "ACoAADcSzyMBUV7aSeCnnR1DXVqPlaswLOi6EJI",
  "volunteerAndAwards": [
    {
      "breakdown": false,
      "caption": "Jan 2026 - Present · ",
      "companyId": "111101223",
      "companyLink1": "https://www.linkedin.com/company/servi-ekibi/",
      "companyUrn": "urn:li:fsd_company:111101223",
      "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQG5OSdHH0kIwQ/company-logo_100_100/B4DZvNldRuIAAU-/0/1768680707724/servi_community_logo?e=1779321600&v=beta&t=Fd2297sBU7W-Xc3H5uyAuS_nFOdK-xpLHmpC5iJjhkE",
      "subComponenets": [
        {
          "description": []
        }
      ],
      "subtitle": "Servi",
      "title": "Open Source Contributor"
    },
    {
      "breakdown": false,
      "caption": "Jan 2025 - Present · 1 yr",
      "companyId": "105137266",
      "companyLink1": "https://www.linkedin.com/company/happyhackingspace/",
      "companyUrn": "urn:li:fsd_company:105137266",
      "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQH_AlrAMxnFyw/company-logo_400_400/B4DZoINMq0GsAg-/0/1761074269292/happyhackingspace_logo?e=1779321600&v=beta&t=72jYkxRnbV_tsfoBcc1p7N0dLYdwfGZvVW1rBD-AUpU",
      "subComponenets": [
        {
          "description": []
        }
      ],
      "subtitle": "Happy Hacking Space",
      "title": "Research and Development Member"
    },
    {
      "breakdown": false,
      "caption": "Jun 2024 - Present · 1 yr 7 mos",
      "companyId": "105382247",
      "companyLink1": "https://www.linkedin.com/company/milgetybu/",
      "companyUrn": "urn:li:fsd_company:105382247",
      "logo": "https://media.licdn.com/dms/image/v2/D4D0BAQEMRUe-zaE_8g/company-logo_400_400/company-logo_400_400/0/1729019631925?e=1779321600&v=beta&t=ExCOkYoMOjBcYLN3Vt4sgEIUPFFyY85aM_WgHJZ9oAg",
      "subComponenets": [
        {
          "description": []
        }
      ],
      "subtitle": "Milli Gençlik Topluluğu",
      "title": "AYBÜ Komisyonu Eğitim Koordinatörü"
    }
  ],
  "profileUrl": "https://www.linkedin.com/in/myzz",
  "input": "myzz",
  "username": "myzz",
  "success": true
}]"""

data = {
    'fullname': '',
    'firstname': '',
    'lastname': '',
    'email': '',
    'phone': '',
    'linkedin': '',
    'github': '',
    'summary': '',
    'education': [],
    'experience': [],
    'projects': [],
    'leadership_awards': [],
    'skills': {'AI/ML Frameworks': '', 'Tools & DevOps': '', 'Languages': ''},
    'images': {}
}

# --- Process cv.tex content ---
tex_content = CV_TEX_CONTENT

# Full Name
name_match = re.search(r'\\textbf{{\\Huge\\scshape (.*?)}}', tex_content)
if name_match:
    data['fullname'] = name_match.group(1).strip()
    parts = data['fullname'].split()
    data['firstname'] = parts[0] if parts else ''
    data['lastname'] = parts[-1] if len(parts) > 1 else ''

# Contact Info
email_match = re.search(r'\\href{{mailto:(.*?)}}', tex_content)
if email_match: data['email'] = email_match.group(1).strip()
linkedin_match = re.search(r'linkedin.com/in/(.*?)}', tex_content)
if linkedin_match: data['linkedin'] = linkedin_match.group(1).strip()
github_match = re.search(r'github.com/(.*?)}', tex_content)
if github_match: data['github'] = github_match.group(1).strip()
phone_match = re.search(r'\\href{{tel:\\+\\d{{10,12}}}}{{(\\+\\d{{10,12}})}}', tex_content)
if phone_match: data['phone'] = phone_match.group(1).strip()

# Summary
summary_match = re.search(r'\\section{{Summary}}\\s+\\small{{\\textbf{{(.*?)}}', tex_content, re.DOTALL)
if summary_match:
    summary = summary_match.group(1).replace('\\textbf{{', '').replace('}}', '').strip()
    data['summary'] = summary

# Education
education_section = re.search(r'\\section{{Education}}(.*?)(?=\\section|$)', tex_content, re.DOTALL)
if education_section:
    edu_items = re.findall(r'\\resumeSubheading{{(.*?)}}{{(.*?)}}\s*\\textit{{\\small(.*?)}}{{(.*?)}}', education_section.group(1), re.DOTALL)
    for item in edu_items:
        data['education'].append({'institution': item[0], 'location': item[1], 'degree': item[2], 'period': item[3]})

# Experience
experience_section = re.search(r'\\section{{Experience}}(.*?)(?=\\section|$)', tex_content, re.DOTALL)
if experience_section:
    exp_items = re.findall(r'\\resumeSubheading{{(.*?)}}{{(.*?)}}\s*\\small{{(.*?)}}{{(.*?)}}', experience_section.group(1), re.DOTALL)
    for item in exp_items:
        highlights_block = re.search(r'\\vspace{{0.5pt}}\\s*\\resumeItemListStart(.*?)\\resumeItemListEnd', item[4], re.DOTALL)
        highlights = re.findall(r'\\resumeItem{{(.*?)}', highlights_block.group(1)) if highlights_block else []
        data['experience'].append({'company': item[0], 'period': item[1], 'role': item[2], 'location': item[3], 'highlights': highlights})

# Projects
projects_section = re.search(r'\\section{{Technical Projects}}(.*?)(?=\\section|$)', tex_content, re.DOTALL)
if projects_section:
    proj_items = re.findall(r'\\resumeProjectHeading{{\\textbf{{(.*?)}}\s*\\$: \\emph{{\\textbf{{(.*?)}}}} \\href{{(.*?)}}{{.*?}}}}{{(.*?)}}\s*\\resumeItemListStart(.*?)\\resumeItemListEnd', projects_section.group(1), re.DOTALL)
    for item in proj_items:
        description = re.findall(r'\\resumeItem{{(.*?)}', item[4])
        data['projects'].append({'name': item[0], 'tech': item[1], 'link': item[2], 'date': item[3], 'description': description})

# Leadership & Awards
leadership_section = re.search(r'\\section{{Leadership & Awards}}(.*?)(?=\\section|$)', tex_content, re.DOTALL)
if leadership_section:
    lead_items = re.findall(r'\\resumeProjectHeading{{\\textbf{{(.*?)}}\s*\\$ \\href{{(.*?)}}{{.*?}}}}{{(.*?)}}\s*\\resumeItemListStart(.*?)\\resumeItemListEnd', leadership_section.group(1), re.DOTALL)
    for item in lead_items:
        description = re.findall(r'\\resumeItem{{(.*?)}', item[3])
        data['leadership_awards'].append({'name': item[0], 'link': item[1], 'date': item[2], 'description': description})

# Skills
skills_section = re.search(r'\\section{{Technical Skills}}(.*?)(?=\\section|$)', tex_content, re.DOTALL)
if skills_section:
    ai_ml_match = re.search(r'\\textbf{{AI/ML Frameworks}}{{: (.*?)}}', skills_section.group(1))
    if ai_ml_match: data['skills']['AI/ML Frameworks'] = ai_ml_match.group(1).strip()
    tools_devops_match = re.search(r'\\textbf{{Tools & DevOps}}{{: (.*?)}}', skills_section.group(1))
    if tools_devops_match: data['skills']['Tools & DevOps'] = tools_devops_match.group(1).strip()
    languages_match = re.search(r'\\textbf{{Languages}}{{: (.*?)}}', skills_section.group(1))
    if languages_match: data['skills']['Languages'] = languages_match.group(1).strip()

# --- Process JSON content ---
json_files_content = [LINKEDIN_MYZ_JSON_CONTENT, LINKEDIN_MYZ2_JSON_CONTENT]

for json_content in json_files_content:
    jdata = json.loads(json_content)
    if isinstance(jdata, list): jdata = jdata[0]

    bi = jdata.get('basic_info', jdata)
    if bi.get('fullname') and not data['fullname']: data['fullname'] = bi['fullname']
    if bi.get('profile_picture_url'): data['images']['profile'] = bi['profile_picture_url']
    if bi.get('profilePic'): data['images']['profile'] = bi['profilePic']
    if bi.get('background_picture_url'): data['images']['bg'] = bi['background_picture_url']

    featured = jdata.get('featured', [])
    for i, item in enumerate(featured):
        if item.get('image_url'):
            data['images'][f'featured_{i}'] = item['image_url']

print(json.dumps(data))
