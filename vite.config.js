import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    open: false
  },
  build: {
    rollupOptions: {
      input: {
        index: 'index.html',
        about: 'about.html',
        journey: 'journey.html',
        voluntary: 'voluntary.html',
        awards: 'awards.html',
        art: 'art.html',
        captures: 'captures.html',
        projects: 'projects.html'
      }
    }
  }
});
