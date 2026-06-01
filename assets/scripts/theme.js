(() => {
  const STORAGE_KEY = 'site-theme';
  const root = document.documentElement;

  const getPreferredTheme = () => {
    const paramTheme = new URLSearchParams(window.location.search).get('theme');
    if (paramTheme === 'light' || paramTheme === 'dark') return paramTheme;
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved === 'light' || saved === 'dark') return saved;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const applyTheme = (theme) => {
    root.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#18181b' : '#f3f4f6');
    const button = document.querySelector('.theme-toggle-button');
    if (button) {
      const nextTheme = theme === 'dark' ? 'light' : 'dark';
      button.setAttribute('aria-label', `Switch to ${nextTheme} theme`);
      button.setAttribute('title', `Switch to ${nextTheme} theme`);
    }
  };

  const toggleTheme = () => {
    applyTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
  };

  document.addEventListener('DOMContentLoaded', () => {
    applyTheme(getPreferredTheme());
    const button = document.querySelector('.theme-toggle-button');
    if (button) button.addEventListener('click', toggleTheme);
  });
})();
