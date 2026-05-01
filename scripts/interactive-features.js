(function() {
    // Feature 1: +1 and Emoji Interaction
    const emojiList = [
        128293, 128640, 10024, 127919, 127775, 129504, 128161, 127881, 128079,
        128588, 127942, 127774, 128526, 128175, 128293, 129412, 129322, 128126,
        129408, 129430, 129488, 127752, 127922, 127918, 128142, 129292, 129761,
        129392
    ];

    let clickCount = 0;
    const fxLayer = document.querySelector('.wiki-inactive-fx-layer') || document.body;

    document.addEventListener('click', function(event) {
        const target = event.target;
        const interactiveElement = target.closest('[data-inactive-action="1"]');

        if (!interactiveElement) return;

        // Prevent default for links if they are just for interaction
        if (interactiveElement.tagName === "A" && (interactiveElement.getAttribute('href') === "#" || interactiveElement.getAttribute('href') === "")) {
            event.preventDefault();
        }

        clickCount++;

        const clientX = event.clientX;
        const clientY = event.clientY;

        // Add "+1" effect
        createFloatingItem(clientX + 12, clientY - 20, "+1", "plus");

        // Add emoji effect every 5 clicks
        if (clickCount % 5 === 0) {
            const randomEmoji = String.fromCodePoint(
                emojiList[Math.floor(Math.random() * emojiList.length)]
            );
            createFloatingItem(clientX + 44, clientY - 36, randomEmoji, "emoji");
        }
    }, true);

    function createFloatingItem(x, y, text, kind) {
        const item = document.createElement('span');
        item.className = `wiki-inactive-fx-item ${kind === "emoji" ? "wiki-inactive-fx-emoji" : "wiki-inactive-fx-plus"}`;
        item.style.left = `${x}px`;
        item.style.top = `${y}px`;
        item.textContent = text;
        
        fxLayer.appendChild(item);

        setTimeout(() => {
            item.remove();
        }, 1100);
    }

    // Feature 2: Talk Section (Contact Dropdown)
    const personalData = {
        name: "Muhammed Yıldız",
        email: "mhmmdyildiz@proton.me",
        linkedin: "https://linkedin.com/in/myzz",
        github: "https://github.com/myz21",
    };

    function createDropdown(trigger) {
        // Remove existing dropdown if any
        const existing = document.querySelector('.custom-contact-dropdown');
        if (existing) existing.remove();

        const dropdown = document.createElement('div');
        dropdown.className = 'custom-contact-dropdown';
        // Wikipedia-like styling
        Object.assign(dropdown.style, {
            position: 'fixed',
            backgroundColor: 'white',
            border: '1px solid #a2a9b1',
            boxShadow: '0 2px 2px 0 rgba(0,0,0,0.25)',
            zIndex: '2000',
            padding: '8px 0',
            borderRadius: '2px',
            minWidth: '180px',
            fontFamily: 'sans-serif'
        });

        const rect = trigger.getBoundingClientRect();
        // Position dropdown below the trigger, aligned to the left or right depending on space
        let top = rect.bottom + 5;
        let left = rect.left;
        
        if (left + 180 > window.innerWidth) {
            left = rect.right - 180;
        }

        dropdown.style.top = `${top}px`;
        dropdown.style.left = `${left}px`;

        const menuList = document.createElement('ul');
        Object.assign(menuList.style, {
            listStyle: 'none',
            margin: '0',
            padding: '0'
        });

        const items = [
            { label: 'Email', href: `mailto:${personalData.email}`, icon: '✉️' },
            { label: 'LinkedIn', href: personalData.linkedin, icon: '🔗' },
            { label: 'GitHub', href: personalData.github, icon: '💻' }
        ];

        items.forEach(itemData => {
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = itemData.href;
            a.target = "_blank";
            a.rel = "noopener noreferrer";
            Object.assign(a.style, {
                display: 'flex',
                alignItems: 'center',
                padding: '8px 16px',
                textDecoration: 'none',
                color: '#36c', // Wikipedia blue
                fontSize: '14px',
                transition: 'background-color 0.1s'
            });
            
            const iconSpan = document.createElement('span');
            iconSpan.textContent = itemData.icon;
            iconSpan.style.marginRight = '10px';
            iconSpan.style.fontSize = '16px';
            
            const textSpan = document.createElement('span');
            textSpan.textContent = itemData.label;

            a.appendChild(iconSpan);
            a.appendChild(textSpan);

            a.onmouseover = () => {
                a.style.backgroundColor = '#eaecf0';
                a.style.textDecoration = 'underline';
            };
            a.onmouseout = () => {
                a.style.backgroundColor = 'transparent';
                a.style.textDecoration = 'none';
            };
            
            li.appendChild(a);
            menuList.appendChild(li);
        });

        dropdown.appendChild(menuList);
        document.body.appendChild(dropdown);

        // Close dropdown when clicking outside
        const closeDropdown = (e) => {
            if (!dropdown.contains(e.target) && !trigger.contains(e.target)) {
                dropdown.remove();
                document.removeEventListener('click', closeDropdown);
            }
        };
        // Use a small timeout to avoid immediate closing from the same click
        setTimeout(() => document.addEventListener('click', closeDropdown), 10);
    }

    // Attach to "Talk" buttons
    document.addEventListener('click', function(event) {
        const target = event.target;
        // Check if it's a "Talk" button or inside one
        const talkButton = target.closest('button');
        if (talkButton && talkButton.textContent.trim() === 'Talk') {
            event.preventDefault();
            event.stopPropagation();
            createDropdown(talkButton);
        }
    });

    // Feature 3: Carousel fallback navigation (for static export)
    function initCarouselFallback(carousel) {
        const slides = Array.from(carousel.querySelectorAll('[aria-roledescription="slide"]'));
        if (slides.length <= 1) return;

        const track = slides[0].parentElement;
        if (!track) return;

        const buttons = Array.from(carousel.querySelectorAll('button'));
        const prevBtn = buttons.find((btn) => btn.textContent.trim().toLowerCase().includes('previous slide'));
        const nextBtn = buttons.find((btn) => btn.textContent.trim().toLowerCase().includes('next slide'));
        if (!prevBtn || !nextBtn) return;

        let index = 0;

        const setDisabled = () => {
            prevBtn.disabled = index <= 0;
            nextBtn.disabled = index >= slides.length - 1;
        };

        const update = () => {
            const slideWidth = slides[0].getBoundingClientRect().width;
            track.style.transform = `translateX(${-slideWidth * index}px)`;
            track.style.transition = 'transform 0.3s ease';
            setDisabled();
        };

        const goPrev = () => {
            if (index > 0) {
                index -= 1;
                update();
            }
        };

        const goNext = () => {
            if (index < slides.length - 1) {
                index += 1;
                update();
            }
        };

        prevBtn.addEventListener('click', (event) => {
            event.preventDefault();
            goPrev();
        });

        nextBtn.addEventListener('click', (event) => {
            event.preventDefault();
            goNext();
        });

        window.addEventListener('resize', update);
        update();
    }

    function enableCarouselFallbacks() {
        const carousels = Array.from(document.querySelectorAll('[aria-roledescription="carousel"]'));
        carousels.forEach((carousel) => {
            const buttons = Array.from(carousel.querySelectorAll('button'));
            const prevBtn = buttons.find((btn) => btn.textContent.trim().toLowerCase().includes('previous slide'));
            const nextBtn = buttons.find((btn) => btn.textContent.trim().toLowerCase().includes('next slide'));
            if (!prevBtn || !nextBtn) return;
            if (prevBtn.disabled && nextBtn.disabled) {
                initCarouselFallback(carousel);
            }
        });
    }

    const runCarouselFallbacks = () => {
        setTimeout(enableCarouselFallbacks, 0);
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', runCarouselFallbacks);
    } else {
        runCarouselFallbacks();
    }

})();
    // Dark Mode Toggle
    function initDarkMode() {
        const appearanceBtns = document.querySelectorAll('.wikipedia-module__8TSorq__wikiAppearanceBtn');
        
        // Check if user has a preference saved in localStorage or prefers dark mode
        const savedMode = localStorage.getItem('wiki-dark-mode');
        if (savedMode === '1' || (!savedMode && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
            document.documentElement.setAttribute('data-wiki-dark', '1');
        }

        appearanceBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const isDark = document.documentElement.getAttribute('data-wiki-dark') === '1';
                if (isDark) {
                    document.documentElement.removeAttribute('data-wiki-dark');
                    localStorage.setItem('wiki-dark-mode', '0');
                } else {
                    document.documentElement.setAttribute('data-wiki-dark', '1');
                    localStorage.setItem('wiki-dark-mode', '1');
                }
            });
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initDarkMode);
    } else {
        initDarkMode();
    }
