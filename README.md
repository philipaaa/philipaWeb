# Personal Portfolio Website

A clean, modern, and responsive personal website showcasing your portfolio, courses, and work experience.

## Features

- 🎨 **Modern Design** - Clean and professional UI with smooth animations
- 📱 **Fully Responsive** - Works perfectly on desktop, tablet, and mobile devices
- ⚡ **Fast & Lightweight** - Pure HTML, CSS, and JavaScript (no frameworks)
- 🎯 **Easy to Customize** - Well-organized code with clear comments
- ✨ **Smooth Animations** - Intersection Observer for scroll-triggered animations
- 🧭 **Smooth Navigation** - Fixed navbar with active section highlighting

## Sections

1. **Hero/Home** - Introduction with your name and tagline
2. **About** - Personal information and skills
3. **Portfolio** - Showcase of your projects
4. **Courses** - Educational background and courses taken
5. **Experience** - Work experience timeline
6. **Contact** - Ways to get in touch

## Getting Started

### Prerequisites

- A modern web browser
- A text editor (VS Code, Sublime Text, etc.)
- Optional: A local web server (for testing)

### Installation

1. Clone or download this repository
2. Open `index.html` in your web browser
3. Start customizing the content!

### Running Locally

You can use any local server. Here are a few options:

**Using Python:**
```bash
python -m http.server 8000
```

**Using Node.js (http-server):**
```bash
npx http-server
```

**Using VS Code Live Server:**
- Install the "Live Server" extension
- Right-click on `index.html` and select "Open with Live Server"

Then open `http://localhost:8000` (or the port shown) in your browser.

## Customization Guide

### 1. Update Personal Information

**In `index.html`:**

- **Name**: Replace "Your Name" throughout the file
- **Hero Section**: Update the title, subtitle, and tagline
- **About Section**: Write your personal bio and add your skills
- **Contact Section**: Update email, LinkedIn, and GitHub links

### 2. Add Your Profile Picture

Replace the SVG placeholder in the hero section:

```html
<div class="hero-image">
    <img src="path/to/your/profile.jpg" alt="Your Name" class="profile-image">
</div>
```

Then add CSS for `.profile-image`:
```css
.profile-image {
    width: 300px;
    height: 300px;
    border-radius: 50%;
    object-fit: cover;
    box-shadow: var(--shadow-xl);
}
```

### 3. Add Portfolio Projects

Edit the portfolio items in `index.html`:

```html
<div class="portfolio-item">
    <div class="portfolio-image">
        <img src="path/to/project-image.jpg" alt="Project Name">
    </div>
    <div class="portfolio-content">
        <h3>Your Project Name</h3>
        <p>Project description...</p>
        <div class="portfolio-links">
            <a href="https://your-demo.com" class="link">Live Demo</a>
            <a href="https://github.com/yourusername/project" class="link">GitHub</a>
        </div>
    </div>
</div>
```

### 4. Update Courses

Modify the course items:

```html
<div class="course-item">
    <div class="course-year">2024</div>
    <div class="course-content">
        <h3>Course Name</h3>
        <p class="course-institution">Institution Name</p>
        <p>Course description...</p>
    </div>
</div>
```

### 5. Update Work Experience

Edit the experience items:

```html
<div class="experience-item">
    <div class="experience-date">2024 - Present</div>
    <div class="experience-content">
        <h3>Your Job Title</h3>
        <p class="experience-company">Company Name</p>
        <ul class="experience-duties">
            <li>Responsibility 1</li>
            <li>Responsibility 2</li>
        </ul>
    </div>
</div>
```

### 6. Customize Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-color: #6366f1;      /* Main brand color */
    --secondary-color: #8b5cf6;   /* Secondary accent color */
    --text-primary: #1f2937;       /* Main text color */
    --text-secondary: #6b7280;     /* Secondary text color */
    /* ... */
}
```

### 7. Add More Skills

In the About section, add more skill tags:

```html
<span class="skill-tag">Your Skill</span>
```

## File Structure

```
philipaWeb/
│
├── index.html          # Main HTML file
├── styles.css          # All styles and animations
├── script.js           # JavaScript for interactivity
└── README.md           # This file
```

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Performance Tips

1. **Optimize Images**: Use compressed images (WebP format recommended)
2. **Lazy Loading**: Images will lazy load automatically if you add the `loading="lazy"` attribute
3. **Minify**: For production, minify CSS and JavaScript files
4. **CDN**: Consider hosting images on a CDN for faster loading

## Deployment

### GitHub Pages

1. Push your code to a GitHub repository
2. Go to Settings → Pages
3. Select the main branch
4. Your site will be live at `https://yourusername.github.io/repository-name`

### Netlify

1. Drag and drop your project folder to [Netlify](https://www.netlify.com)
2. Your site will be live instantly!

### Vercel

1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` in your project directory
3. Follow the prompts

## License

Feel free to use this template for your personal website!

## Credits

- Font: [Inter](https://fonts.google.com/specimen/Inter) by Google Fonts
- Design inspiration: Modern web design trends

## Support

If you have any questions or need help customizing your website, feel free to reach out!

---

Made with ❤️ for showcasing your work
