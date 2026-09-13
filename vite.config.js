import { defineConfig } from 'vite';

export default defineConfig({
  base: './',
  server: {
    open: false
  },
  build: {
    rollupOptions: {
      input: {
        index: 'index.html',
        journey: 'journey.html',
        voluntary: 'voluntary.html',
        awards: 'awards.html',
        art: 'art.html',
        projects: 'projects.html'
      }
    }
  }
});
