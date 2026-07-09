# Maintaining this site

A practical guide to editing bashatahamal.github.io. The site is **Jekyll** (static site generator) using a small, framework-free template system. You edit content in a few predictable places and Jekyll rebuilds the HTML.

> Writing/design rules live in the repo's [REDESIGN.md](../REDESIGN.md) §2. The one you'll break most often: **never use em dashes (—) or en dashes (–) in copy.** Use commas, periods, colons, parentheses, or plain hyphens for dates.

## "I want to change..." (start here)

| I want to change... | Edit this | Guide |
|---|---|---|
| Availability chip ("Open to new roles") | `_config.yml` → `availability:` | [site-settings.md](site-settings.md) |
| Show/hide the Writing section | `_config.yml` → `show_writing:` | [site-settings.md](site-settings.md) |
| Hero headline, intro, proof paragraph | `_includes/v2/organisms/hero.html` | plain HTML, edit the text |
| About text | `_includes/v2/organisms/about.html` | plain HTML, edit the text |
| Skills lists | `_data/skills.yml` | [add-experience.md](add-experience.md) |
| Experience timeline (jobs) | `_data/experience.yml` | [add-experience.md](add-experience.md) |
| A project card or its detail page | `projects/<n>_<name>.md` | [add-project-card.md](add-project-card.md) |
| Blog posts | `_posts/YYYY-MM-DD-slug.md` | [add-blog-post.md](add-blog-post.md) |
| Contact email / footer text | `_includes/v2/organisms/footer.html` | plain HTML |
| Social links (GitHub, LinkedIn, WA...) | `_includes/v2/atoms/social-links.html` | plain HTML |
| Nav menu items | `_includes/v2/organisms/nav.html` | plain HTML |
| Profile photo | replace `img/profile.png` (square image) | used by hero + CV link previews |
| The CV PDF people download | `cv/basha-tahamal-cv.pdf` | [update-cv.md](update-cv.md) |
| Colors, fonts, spacing | `assets/v2/css/main.css` (tokens at top) | [Look and feel](#look-and-feel-colors-fonts-favicon) below |
| Favicon | run `scripts/make_favicon.py` | [Look and feel](#look-and-feel-colors-fonts-favicon) below |
| SEO title/description/social preview | `_layouts/v2.html` `<head>` + `_config.yml` `description:` | plain HTML |

## Task guides
- [Add or edit a blog post](add-blog-post.md)
- [Add or edit a project card](add-project-card.md)
- [Add or edit an experience entry](add-experience.md)
- [Update the CV PDF (LaTeX workflow)](update-cv.md)
- [Site settings: availability chip + writing toggle](site-settings.md)
- [Analysis: what's left and what's worth doing](recommendations.md)

## Look and feel (colors, fonts, favicon)

All styling is one file, `assets/v2/css/main.css`, and every color/font is a **design token** (CSS variable) defined in the `:root` block at the very top:

- Light palette in `:root { ... }`, dark palette in the `[data-theme="dark"]` block right below it. Change a hex once and it updates everywhere, both themes.
- Key tokens: `--accent` (the green `#0e6e55`), `--gold` (`#a16f0b` hairlines), `--bg`, `--ink`, `--serif`, `--sans`.
- **Never hard-code a color in a component.** Always use `var(--token)` so dark mode keeps working.

Favicon: `scripts/make_favicon.py` regenerates the "B." monogram (favicon.ico + PNG sizes). Edit the colors/letter in the script, then `pip install pillow` and `python3 scripts/make_favicon.py`.

## How the template system fits together

```
_layouts/            page skeletons (templates)
  v2.html              base: <head>, nav, footer, theme/JS. Everything wraps this.
  project.html         a project detail page
  post.html            a blog post page

_includes/v2/         reusable building blocks (atomic design)
  atoms/               smallest pieces: section-heading, tag, social-links, theme-toggle
  molecules/           small combos: project-card, timeline-item, skill-group
  organisms/           whole sections: hero, work-grid, experience, about, writing, footer, nav

_data/                content as data (no HTML)
  experience.yml       the Experience timeline
  skills.yml           the About > skills lists

projects/*.md          one file per project card + its detail page
_posts/*.md            one file per blog post

assets/v2/
  css/main.css         all styling (design tokens at the top)
  js/main.js           theme toggle, mobile menu, gallery lightbox

images/thumbnails/     project card thumbnails
images/<name>/         a project's gallery images
cv/basha-tahamal-cv.pdf the downloadable CV
index.html             the homepage (just assembles the organisms)
```

**The idea:** content lives in `_data` files and `projects/` + `_posts/` markdown. You rarely touch HTML/CSS. Layouts and includes render that content the same way every time, so everything stays consistent (spacing, fonts, dark mode) automatically.

## Preview your changes locally

From the repo folder (`bashatahamal.github.io/`):

```bash
bundle exec jekyll serve
```

Open http://localhost:4000. Jekyll watches files and rebuilds on save (refresh the browser). Stop with Ctrl-C.

First time on a new machine: `bundle install` once, first.

## Publish

The live site is the `main` branch on GitHub (GitHub Pages builds it automatically on push). Ongoing work is on the `redesign-v2` branch. To publish:

```bash
git add -A
git commit -m "describe your change"
git push
```

If you're on `redesign-v2`, merge it into `main` when ready (`git checkout main && git merge redesign-v2 && git push`).

## Golden rules (so the site stays consistent)
1. **No em/en dashes in copy.** Plain hyphens for date ranges: `January 2026 - July 2026`.
2. **3 tags per project.** Keep them consistent in style (domain + key tech).
3. **Keep experience in sync with the CV** (`cv_docs/cv/latest/main.tex`). If you add a job to one, add it to the other.
4. **Dark mode is automatic.** Use the existing CSS variables (`var(--ink)`, `var(--accent)`, etc.); never hard-code colors.
5. **Newest first.** Ordering is by filename (see the project + post guides).
