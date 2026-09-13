const STORAGE_KEY = 'site-theme';

function preferredTheme() {
  const requested = new URLSearchParams(window.location.search).get('theme');
  if (requested === 'light' || requested === 'dark') return requested;
  const saved = localStorage.getItem(STORAGE_KEY);
  if (saved === 'light' || saved === 'dark') return saved;
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
}

function applyTheme(theme) {
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem(STORAGE_KEY, theme);
  document.querySelector('meta[name="theme-color"]')?.setAttribute('content', theme === 'dark' ? '#18181b' : '#f3f4f6');
  const button = document.querySelector('.theme-toggle-button');
  if (button) {
    const nextTheme = theme === 'dark' ? 'light' : 'dark';
    button.setAttribute('aria-label', `Switch to ${nextTheme} theme`);
    button.setAttribute('title', `Switch to ${nextTheme} theme`);
  }
}

export function initialiseTheme() {
  applyTheme(preferredTheme());
  document.querySelector('.theme-toggle-button')?.addEventListener('click', () => {
    applyTheme(document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark');
  });
}
