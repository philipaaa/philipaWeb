# Philip Papadatos – Personal Website

This repo contains the source for my personal site and portfolio.

- **Live site**: `https://philipaaa.live`
- **GitHub Pages repo** (deployment): `https://github.com/philipaaa/philipaaa.github.io`

The site is built with **HTML, CSS, and vanilla JavaScript** and showcases my background in **Computer Science (AI/ML)** and **Biomedical Sciences**, along with selected projects and a peer‑reviewed publication.

## Features

- **Modern, responsive layout** – Works on desktop, tablet, and mobile
- **Dark / light mode** – Theme toggle with preference saved in `localStorage`
- **Smooth navigation** – Fixed navbar with active‑section highlighting and smooth scrolling
- **Scroll‑in animations** – Sections and timeline items animate into view via `IntersectionObserver`
- **Project detail pages** – Dedicated write‑ups for key projects under `projects/`
- **Publications section** – Highlights my prostate MRI publication with a link to PubMed

## Site Structure

Main sections on `index.html`:

1. **Hero** – Intro, tagline, and primary CTAs
2. **About** – Bio, skills & technologies, and languages
3. **Portfolio** – Cards linking to detailed project pages:
   - Q‑Learning IQ Tester  
   - Let’s Train  
   - TalkToMe  
   - Pokémon Party Web Application  
   - Passion XI
4. **Courses & Education** – Computer Science (AI/ML) at Carleton and Biomedical Sciences at uOttawa
5. **Work Experience** – Student Intern role at Conseil des Écoles catholiques du Centre‑Est
6. **Publications** –  
   *Comparison of 5 Rectal Preparation Strategies for Prostate MRI and Impact on Image Quality*  
   with a card linking to PubMed (PMID: 34404240)
7. **Get In Touch** – Email, LinkedIn, GitHub, and downloadable CV

Each portfolio card links to a corresponding page in `projects/` (e.g. `projects/q-learning-iq-tester.html`, `projects/passion-xi.html`) styled with `projects/project.css`.

## Tech Stack

- **HTML5** – Semantic sections and accessible structure
- **CSS3** – Custom design system with CSS variables, grid/flexbox layout, and responsive breakpoints
- **JavaScript** – Theme toggle, scroll animations, mobile navigation, and active‑link highlighting

No frontend framework is used; everything is hand‑rolled for performance and control.

## Running Locally

1. Clone this repository.
2. Open `index.html` directly in your browser **or** start a simple local server:

Using Python:

```bash
python -m http.server 8000
```

Then visit `http://localhost:8000`.

## Project Layout

```text
philipaWeb/
├── index.html          # Main single-page site
├── styles.css          # Global styling and layout
├── script.js           # Theme, navigation, and animations
├── projects/           # Individual project detail pages + project.css
├── assets/             # Images and other static assets
├── resume.pdf          # Downloadable CV linked from the site
├── extract_pdf.py      # Helper script used during resume/content generation
└── README.md           # This file
```

## Deployment

The site is deployed via **GitHub Pages** from `philipaaa/philipaaa.github.io` and served through the custom domain `philipaaa.live`. When I update this repo, I mirror relevant changes into the GitHub Pages repo and redeploy.

