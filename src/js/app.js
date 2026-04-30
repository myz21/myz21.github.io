/**
 * Wikipedia-Style Portfolio - Main Application
 * 
 * Design Patterns Used:
 * - Module Pattern for encapsulation
 * - Observer Pattern for theme switching
 * - Factory Pattern for component creation
 * - Template Method for rendering sections
 * 
 * Architecture:
 * - Separation of concerns (data, rendering, interaction)
 * - Event-driven architecture
 * - Progressive enhancement
 */

(function() {
  'use strict';

  // ============================================
  // Configuration & State
  // ============================================
  const CONFIG = {
    selectors: {
      themeToggle: '.theme-toggle',
      themeIcon: '.theme-toggle__icon',
      searchInput: '.wiki-header__search-input',
      tocToggle: '.wiki-toc__toggle',
      tocList: '.wiki-toc__list',
      sections: '.wiki-section',
      infobox: '.wiki-infobox'
    },
    storage: {
      themeKey: 'wiki-portfolio-theme',
      tocOpenKey: 'wiki-portfolio-toc-open'
    },
    themes: {
      light: 'light',
      dark: 'dark'
    }
  };

  // Application state
  const state = {
    currentTheme: CONFIG.themes.light,
    tocOpen: true,
    profileData: null
  };

  // ============================================
  // Theme Manager (Observer Pattern)
  // ============================================
  const ThemeManager = {
    /**
     * Initialize theme from storage or system preference
     */
    init() {
      const savedTheme = localStorage.getItem(CONFIG.storage.themeKey);
      const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      
      state.currentTheme = savedTheme || (systemPrefersDark ? CONFIG.themes.dark : CONFIG.themes.light);
      this.apply(state.currentTheme);
      this.setupListeners();
    },

    /**
     * Apply theme to document
     */
    apply(theme) {
      document.documentElement.setAttribute('data-theme', theme);
      state.currentTheme = theme;
      localStorage.setItem(CONFIG.storage.themeKey, theme);
      this.updateIcon(theme);
    },

    /**
     * Toggle between light and dark themes
     */
    toggle() {
      const newTheme = state.currentTheme === CONFIG.themes.light 
        ? CONFIG.themes.dark 
        : CONFIG.themes.light;
      this.apply(newTheme);
    },

    /**
     * Update theme toggle button icon
     */
    updateIcon(theme) {
      const iconEl = document.querySelector(CONFIG.selectors.themeIcon);
      if (!iconEl) return;

      if (theme === CONFIG.themes.dark) {
        // Sun icon for dark mode (clicking will switch to light)
        iconEl.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>';
      } else {
        // Moon icon for light mode (clicking will switch to dark)
        iconEl.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
      }
    },

    /**
     * Setup event listeners for theme toggle
     */
    setupListeners() {
      const toggleBtn = document.querySelector(CONFIG.selectors.themeToggle);
      if (toggleBtn) {
        toggleBtn.addEventListener('click', () => this.toggle());
      }

      // Listen for system theme changes
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem(CONFIG.storage.themeKey)) {
          this.apply(e.matches ? CONFIG.themes.dark : CONFIG.themes.light);
        }
      });
    }
  };

  // ============================================
  // Table of Contents Manager
  // ============================================
  const TocManager = {
    /**
     * Initialize TOC functionality
     */
    init() {
      this.setupToggle();
      this.highlightOnScroll();
      this.generateTocFromSections();
    },

    /**
     * Setup TOC toggle button
     */
    setupToggle() {
      const toggleBtn = document.querySelector(CONFIG.selectors.tocToggle);
      const tocList = document.querySelector(CONFIG.selectors.tocList);
      
      if (toggleBtn && tocList) {
        toggleBtn.addEventListener('click', () => {
          state.tocOpen = !state.tocOpen;
          tocList.style.display = state.tocOpen ? 'block' : 'none';
          toggleBtn.textContent = state.tocOpen ? 'hide' : 'show';
          localStorage.setItem(CONFIG.storage.tocOpenKey, state.tocOpen);
        });
      }
    },

    /**
     * Highlight current section in TOC on scroll
     */
    highlightOnScroll() {
      const sections = document.querySelectorAll(CONFIG.selectors.sections);
      const tocLinks = document.querySelectorAll('.wiki-toc__item a');

      const observerOptions = {
        root: null,
        rootMargin: '-20% 0px -60% 0px',
        threshold: 0
      };

      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const id = entry.target.id;
            tocLinks.forEach(link => {
              link.parentElement.classList.remove('wiki-toc__item--active');
              if (link.getAttribute('href') === `#${id}`) {
                link.parentElement.classList.add('wiki-toc__item--active');
              }
            });
          }
        });
      }, observerOptions);

      sections.forEach(section => observer.observe(section));
    },

    /**
     * Generate TOC entries from page sections
     */
    generateTocFromSections() {
      const tocList = document.querySelector(CONFIG.selectors.tocList);
      if (!tocList) return;

      const sections = document.querySelectorAll('.wiki-section[id]');
      let sectionNumber = 0;

      sections.forEach(section => {
        sectionNumber++;
        const heading = section.querySelector('h2');
        if (!heading) return;

        const li = document.createElement('li');
        li.className = 'wiki-toc__item';
        li.innerHTML = `
          <a href="#${section.id}">
            <span class="wiki-toc__number">${sectionNumber}.</span>
            <span class="wiki-toc__text">${heading.textContent}</span>
          </a>
        `;
        tocList.appendChild(li);
      });
    }
  };

  // ============================================
  // Search Manager
  // ============================================
  const SearchManager = {
    /**
     * Initialize search functionality
     */
    init() {
      const searchInput = document.querySelector(CONFIG.selectors.searchInput);
      if (searchInput) {
        searchInput.addEventListener('input', (e) => this.handleSearch(e.target.value));
        searchInput.addEventListener('keydown', (e) => {
          if (e.key === 'Enter') {
            e.preventDefault();
            this.handleSearch(e.target.value);
          }
        });
      }
    },

    /**
     * Handle search input
     */
    handleSearch(query) {
      if (!query.trim()) {
        this.clearHighlights();
        return;
      }

      this.highlightMatches(query);
    },

    /**
     * Highlight matching text in content
     */
    highlightMatches(query) {
      this.clearHighlights();
      const regex = new RegExp(`(${query})`, 'gi');
      const content = document.querySelector('.wiki-content');
      
      if (!content) return;

      // Simple highlight implementation
      const walker = document.createTreeWalker(
        content,
        NodeFilter.SHOW_TEXT,
        null,
        false
      );

      const nodes = [];
      let node;
      while (node = walker.nextNode()) {
        if (node.textContent.toLowerCase().includes(query.toLowerCase())) {
          nodes.push(node);
        }
      }

      nodes.forEach(textNode => {
        const span = document.createElement('span');
        span.innerHTML = textNode.textContent.replace(regex, '<mark class="search-highlight">$1</mark>');
        textNode.parentNode.replaceChild(span, textNode);
      });
    },

    /**
     * Clear search highlights
     */
    clearHighlights() {
      document.querySelectorAll('.search-highlight').forEach(mark => {
        mark.parentNode.replaceChild(
          document.createTextNode(mark.textContent),
          mark
        );
      });
    }
  };

  // ============================================
  // Smooth Scroll Handler
  // ============================================
  const ScrollManager = {
    /**
     * Initialize smooth scrolling for anchor links
     */
    init() {
      document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
          const targetId = anchor.getAttribute('href');
          if (targetId === '#') return;

          const targetElement = document.querySelector(targetId);
          if (targetElement) {
            e.preventDefault();
            targetElement.scrollIntoView({
              behavior: 'smooth',
              block: 'start'
            });
          }
        });
      });
    }
  };

  // ============================================
  // Accessibility Manager
  // ============================================
  const AccessibilityManager = {
    /**
     * Initialize accessibility features
     */
    init() {
      this.setupKeyboardNavigation();
      this.setupAriaLabels();
    },

    /**
     * Setup keyboard navigation
     */
    setupKeyboardNavigation() {
      document.addEventListener('keydown', (e) => {
        // Escape key to close any open modals/dropdowns
        if (e.key === 'Escape') {
          document.activeElement.blur();
        }
      });
    },

    /**
     * Setup ARIA labels for interactive elements
     */
    setupAriaLabels() {
      const themeToggle = document.querySelector(CONFIG.selectors.themeToggle);
      if (themeToggle && !themeToggle.hasAttribute('aria-label')) {
        themeToggle.setAttribute('aria-label', 'Toggle dark mode');
        themeToggle.setAttribute('role', 'button');
        themeToggle.setAttribute('tabindex', '0');
      }
    }
  };

  // ============================================
  // Data Loader (Factory Pattern)
  // ============================================
  const DataLoader = {
    /**
     * Load profile data from JSON file
     */
    async load() {
      try {
        const response = await fetch('src/data/profile.json');
        if (!response.ok) throw new Error('Failed to load profile data');
        state.profileData = await response.json();
        return state.profileData;
      } catch (error) {
        console.error('Error loading profile data:', error);
        return null;
      }
    }
  };

  // ============================================
  // Component Renderer (Template Method Pattern)
  // ============================================
  const ComponentRenderer = {
    /**
     * Render infobox component
     */
    renderInfobox(data) {
      const infobox = document.querySelector(CONFIG.selectors.infobox);
      if (!infobox || !data) return;

      const basicInfo = data.basicInfo;
      
      infobox.innerHTML = `
        <div class="wiki-infobox__title">${basicInfo.fullName}</div>
        <div class="wiki-infobox__subtitle">${basicInfo.headline}</div>
        <img 
          src="${basicInfo.profilePictureUrl}" 
          alt="${basicInfo.fullName}" 
          class="wiki-infobox__image"
          width="220"
          height="270"
          loading="lazy"
        />
        <div class="wiki-infobox__caption">${basicInfo.firstName}, ${new Date().getFullYear()}</div>
        <table class="wiki-infobox__table">
          <tbody>
            ${this.renderInfoboxRows(data)}
          </tbody>
        </table>
        ${data.skills ? this.renderSkillsSection(data.skills) : ''}
      `;
    },

    /**
     * Render infobox data rows
     */
    renderInfoboxRows(data) {
      const rows = [];
      const basicInfo = data.basicInfo;

      // GitHub link
      if (basicInfo.githubUrl) {
        rows.push(`
          <tr>
            <td class="wiki-infobox__label">GitHub</td>
            <td class="wiki-infobox__value">
              <a href="${basicInfo.githubUrl}" class="wiki-link" target="_blank" rel="noopener">
                ${basicInfo.publicIdentifier}
              </a>
            </td>
          </tr>
        `);
      }

      // LinkedIn link
      if (basicInfo.profileUrl) {
        rows.push(`
          <tr>
            <td class="wiki-infobox__label">LinkedIn</td>
            <td class="wiki-infobox__value">
              <a href="${basicInfo.profileUrl}" class="wiki-link" target="_blank" rel="noopener">
                ${basicInfo.publicIdentifier}
              </a>
            </td>
          </tr>
        `);
      }

      // Location
      if (basicInfo.location) {
        rows.push(`
          <tr>
            <td class="wiki-infobox__label">Location</td>
            <td class="wiki-infobox__value">${basicInfo.location.full}</td>
          </tr>
        `);
      }

      // Education
      if (data.education && data.education.length > 0) {
        const currentEdu = data.education.find(e => e.current) || data.education[0];
        rows.push(`
          <tr>
            <td class="wiki-infobox__label">Education</td>
            <td class="wiki-infobox__value">
              ${currentEdu.degree}, ${currentEdu.institution}<br>
              <span class="wiki-small">(${currentEdu.duration})</span>
            </td>
          </tr>
        `);
      }

      return rows.join('');
    },

    /**
     * Render skills section in infobox
     */
    renderSkillsSection(skills) {
      let skillsHtml = '<div class="wiki-infobox__section-header">Skills</div>';
      skillsHtml += '<table class="wiki-infobox__table"><tbody>';

      if (skills.technical) {
        skillsHtml += `
          <tr>
            <td class="wiki-infobox__label">Technical</td>
            <td class="wiki-infobox__value">${skills.technical.join(', ')}</td>
          </tr>
        `;
      }

      if (skills.tools) {
        skillsHtml += `
          <tr>
            <td class="wiki-infobox__label">Tools</td>
            <td class="wiki-infobox__value">${skills.tools.join(', ')}</td>
          </tr>
        `;
      }

      skillsHtml += '</tbody></table>';
      return skillsHtml;
    },

    /**
     * Render experience section
     */
    renderExperience(experience) {
      const section = document.getElementById('experience');
      if (!section || !experience) return;

      const list = section.querySelector('.wiki-list') || section.querySelector('ul');
      if (!list) return;

      list.innerHTML = experience.map(exp => `
        <li class="wiki-list__item">
          <span class="wiki-bold">${exp.title}</span>, 
          <span class="wiki-link">${exp.company}</span>
          <span class="wiki-small">(${exp.duration})</span>
          <span class="wiki-emdash"></span>
          ${exp.description}
        </li>
      `).join('');
    },

    /**
     * Render education section
     */
    renderEducation(education) {
      const section = document.getElementById('education');
      if (!section || !education) return;

      const list = section.querySelector('.wiki-list') || section.querySelector('ul');
      if (!list) return;

      list.innerHTML = education.map(edu => `
        <li class="wiki-list__item">
          <span class="wiki-bold">${edu.degree} in ${edu.field}</span>, 
          ${edu.institution}
          <span class="wiki-small">(${edu.duration})</span>
          ${edu.note ? `<br><em>${edu.note}</em>` : ''}
        </li>
      `).join('');
    },

    /**
     * Render projects section
     */
    renderProjects(projects) {
      const section = document.getElementById('projects');
      if (!section || !projects) return;

      const list = section.querySelector('.wiki-list') || section.querySelector('ul');
      if (!list) return;

      list.innerHTML = projects.map(proj => `
        <li class="wiki-list__item">
          <span class="wiki-bold">${proj.name}</span> — ${proj.description}
          ${proj.technologies ? `<br><span class="wiki-small">Technologies: ${proj.technologies.join(', ')}</span>` : ''}
        </li>
      `).join('');
    },

    /**
     * Render achievements section
     */
    renderAchievements(achievements) {
      const section = document.getElementById('achievements');
      if (!section || !achievements) return;

      const list = section.querySelector('.wiki-list') || section.querySelector('ul');
      if (!list) return;

      list.innerHTML = achievements.map(ach => `
        <li class="wiki-list__item">
          <span class="wiki-bold">${ach.title}</span>
          <span class="wiki-small">(${ach.year})</span>
          <span class="wiki-emdash"></span>
          ${ach.description}
        </li>
      `).join('');
    }
  };

  // ============================================
  // Main Application Controller
  // ============================================
  const App = {
    /**
     * Initialize the application
     */
    async init() {
      // Initialize core functionality
      ThemeManager.init();
      ScrollManager.init();
      AccessibilityManager.init();

      // Load and render profile data
      const profileData = await DataLoader.load();
      if (profileData) {
        ComponentRenderer.renderInfobox(profileData);
        ComponentRenderer.renderExperience(profileData.experience);
        ComponentRenderer.renderEducation(profileData.education);
        ComponentRenderer.renderProjects(profileData.projects);
        ComponentRenderer.renderAchievements(profileData.achievements);
      }

      // Initialize interactive components
      TocManager.init();
      SearchManager.init();

      // Add search highlight styles
      this.addSearchHighlightStyles();

      console.log('Portfolio application initialized successfully');
    },

    /**
     * Add dynamic styles for search highlights
     */
    addSearchHighlightStyles() {
      const style = document.createElement('style');
      style.textContent = `
        mark.search-highlight {
          background-color: #ffeb3b;
          color: #000;
          padding: 0 2px;
          border-radius: 2px;
        }
        [data-theme="dark"] mark.search-highlight {
          background-color: #f9a825;
          color: #000;
        }
        .wiki-toc__item--active a {
          font-weight: 600;
          color: var(--color-link);
        }
      `;
      document.head.appendChild(style);
    }
  };

  // ============================================
  // Initialize on DOM Ready
  // ============================================
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => App.init());
  } else {
    App.init();
  }

  // Expose for debugging (optional)
  window.WikiPortfolio = {
    ThemeManager,
    TocManager,
    SearchManager,
    ComponentRenderer,
    state
  };

})();
