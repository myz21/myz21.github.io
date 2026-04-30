# Muhammed Yıldız - Wikipedia-Style Portfolio

A clean, professional portfolio website designed in the style of Wikipedia, showcasing the background, skills, and achievements of Muhammed Yıldız.

## 🎯 Design Philosophy

> "One goal: what would be the most effective structure for a recruiter to parse and understand my background and skills?"

Wikipedia is perhaps the **MOST** easily recognized interface on the internet. It has iterated through hundreds of designs to create the perfect balance of information density and readability. This portfolio leverages that familiarity to present information in a way that any reader's mind is instantly familiar with.

## 🏗️ Project Structure

```
myz21.github.io/
├── index.html              # Main HTML page
├── README.md               # This file
├── src/
│   ├── css/
│   │   └── styles.css      # Main stylesheet (BEM methodology)
│   ├── js/
│   │   └── app.js          # Main JavaScript application
│   ├── data/
│   │   └── profile.json    # Profile data configuration
│   └── schemas/
│       └── profile.schema.json  # JSON schema for profile data
└── assets/
    └── images/             # Image assets (if needed)
```

## 🎨 Design Patterns Used

### CSS
- **BEM (Block Element Modifier)**: Consistent naming convention for CSS classes
- **CSS Custom Properties**: Design tokens for theming (colors, spacing, typography)
- **Mobile-First Responsive Design**: Progressive enhancement for all screen sizes

### JavaScript
- **Module Pattern**: Encapsulation of functionality
- **Observer Pattern**: Theme switching with system preference detection
- **Factory Pattern**: Component creation
- **Template Method Pattern**: Section rendering

### Architecture Principles
- **Separation of Concerns**: Data, rendering, and interaction are decoupled
- **Event-Driven Architecture**: Responsive user interactions
- **Progressive Enhancement**: Works without JavaScript, enhanced with it

## ✨ Features

- 🌓 **Dark/Light Theme Toggle** with system preference detection
- 📱 **Fully Responsive** design for all devices
- 🔍 **Search Functionality** with text highlighting
- 📑 **Auto-Generated Table of Contents** with scroll highlighting
- ♿ **Accessible** with ARIA labels and keyboard navigation
- 🚀 **Performance Optimized** with lazy loading and minimal dependencies
- 📄 **Print-Friendly** styles

## 🚀 Getting Started

### Prerequisites
- A modern web browser (Chrome, Firefox, Safari, Edge)
- A local web server (for development)

### Running Locally

1. Clone the repository:
```bash
git clone https://github.com/myz21/myz21.github.io.git
cd myz21.github.io
```

2. Start a local server:
```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve .

# Using PHP
php -S localhost:8000
```

3. Open your browser to `http://localhost:8000`

### Deployment

This portfolio is designed to be deployed as a static site. Recommended platforms:
- GitHub Pages
- Netlify
- Vercel
- Cloudflare Pages

## 📊 Performance

- **No external dependencies** (vanilla HTML, CSS, JS)
- **Minimal file size** for fast loading
- **Lazy loading** for images
- **CSS containment** for rendering optimization

## 🛠️ Customization

### Updating Profile Data

Edit `src/data/profile.json` to update:
- Personal information
- Education history
- Work experience
- Skills
- Projects
- Achievements
- Certifications

### Styling Changes

Modify `src/css/styles.css` to:
- Change color scheme (update CSS custom properties in `:root`)
- Adjust typography
- Modify spacing and layout

### Adding New Sections

1. Add section HTML in `index.html`
2. Add corresponding styles in `styles.css`
3. (Optional) Add data rendering logic in `app.js`

## 📜 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📧 Contact

- **GitHub**: [myz21](https://github.com/myz21)
- **LinkedIn**: [myzz](https://linkedin.com/in/myzz)

---

*Built with ❤️ using clean code principles*
