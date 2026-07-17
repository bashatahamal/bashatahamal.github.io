# bashatahamal.github.io

My personal site: portfolio, engineering notes, and CV. Live at [bashatahamal.github.io](https://bashatahamal.github.io).

Built with Jekyll on GitHub Pages. No CSS or JS frameworks: the design system, layouts, and interactions are hand-rolled (about 1,000 lines of CSS on design tokens, and a small vanilla JS file). Editorial look: Charter serif, warm off-white paper, one green accent, gold hairlines, full dark mode.

## Running locally

With Docker (or Podman):

```
docker compose up
```

Or with Ruby installed:

```
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000. Restart the server after editing `_config.yml` (the one file Jekyll does not live-reload).

## Editing content

Everything editable is documented in [docs/README.md](docs/README.md), which has an "I want to change..." table covering projects, blog posts, the experience timeline, the CV, and site settings.

Quick switches live at the top of [_config.yml](_config.yml): the availability chip, the writing section toggle, and hiding unfinished work cards.

## Structure

```
_includes/v2/     atoms, molecules, organisms (the component library)
_layouts/         v2.html (base), project.html, post.html
_data/            experience.yml, skills.yml (content, separated from markup)
_posts/           blog posts (markdown, mermaid diagrams supported)
projects/         one file per project: card + detail page
assets/v2/        css/main.css (design tokens down to organisms), js/main.js, fonts
docs/             maintenance guides
```

## Checks

```
bundle exec rake test
```

Builds the site and runs html-proofer against the output (broken links, missing images).

## License

Code is MIT licensed (see [LICENSE](LICENSE)). Site content is mine: text, images, project descriptions, and the CV are not licensed for reuse.

The repo started life on the Freelancer Jekyll theme years ago; the current site is a from-scratch rebuild and no theme code remains.
