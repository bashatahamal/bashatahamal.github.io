# bashatahamal.github.io

Basha Tahamal's portfolio. Jekyll, GitHub Pages, no CSS/JS frameworks. Redesigned July 2026 (branch `redesign-v2`; `main` = live site).

**This repository is public.** Nothing sensitive belongs in it: no internal planning notes, no personal context beyond what the site itself publishes. Working notes live outside the repo in `../notes/` (REDESIGN.md tracker, recommendations).

**Start here:**
- `docs/README.md` — how to edit anything (the "I want to change..." table).
- `../notes/REDESIGN.md` — living tracker: taste contract, decisions log, open items (private, outside the repo).
- `../design-system/` — the **Basha Editorial design system, the master northstar for all design work**. Follow its `readme.md` and `HANDOFF.md`; tokens and classes from its `styles.css`/`css/` are the only styling vocabulary. When something needs a new color, font, or component, use the nearest existing token/class instead of inventing one.

**Hard rules (do not break):**
1. **No em dashes (—) or en dashes (–) anywhere in copy.** Commas, periods, colons, parentheses; plain hyphens for date ranges. Basha flags these as AI-generated tells.
2. Write in Basha's plain, sincere voice (reference: his CV summary). No marketing fluff, no "crafting digital experiences".
3. No gradients, glassmorphism, emoji decoration, skill bars, or heavy shadows. Editorial serif look: green #0e6e55, gold #a16f0b, tokens in `assets/v2/css/main.css`.
4. Only publish content traceable to his CV (`../cv_docs/`) or his explicit input. Old repo files may be theme demo content that is NOT his work.
5. Keep `_data/experience.yml` in sync with the CV (`../cv_docs/cv/latest/main.tex`).
6. Git commits: no Co-Authored-By / AI attribution trailers.

**Build/preview:** `docker compose up` (or `bundle exec jekyll serve`; restart after `_config.yml` changes). Site switches (availability chip, writing toggle, hidden projects) are at the top of `_config.yml`, documented in `docs/site-settings.md`.
