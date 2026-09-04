# Add or edit a project card

Each project is one file in `projects/`. That single file produces **both** the card in the "How I Got Here" grid **and** the detail page it links to.

## Add a new project

1. Create `projects/<N>_<name>.md`. The **number prefix controls order**: cards are sorted by filename and shown highest-first (newest). The current highest is `9.3_berning.md`, so a newer project would be `9.4_something.md`.
   > Ordering is a text sort, so keep the numbering scheme consistent (don't jump to `10_`, which would sort before `2_`).

2. Add a thumbnail image to `images/thumbnails/` (see [Thumbnails](#thumbnails) below).

3. Paste this template and fill it in:

```markdown
---
layout: project
type: project

title: Company or Project Name
permalink: projects/short-slug
image: images/thumbnails/your-thumb.png
date: Month Year - Month Year
labels:
    - Tag One
    - Tag Two
    - Tag Three
summary: One sentence, outcome-first. This is the card text.

describe-opening: >
  A short paragraph that opens the detail page. Tell the story:
  what the problem was, what you did, and the outcome.

describe-content:
    - <strong>A bold line becomes a section heading</strong>
    - A plain line becomes a bullet point.
    - Another bullet.
    - <em>An italic line is a smaller sub-heading</em>
    - More bullets under it.

describe-closing: '<strong>Tools used:</strong> Python, FastAPI, Postgres, etc.'

---
```

## Field reference
| Field | Used for | Notes |
|---|---|---|
| `layout: project` / `type: project` | required plumbing | Always include both, exactly as shown. |
| `title` | card + page heading | |
| `permalink` | the URL | `projects/slug` → lives at `/projects/slug`. No file extension. |
| `index` | nothing, currently | Retired from project cards and project pages (August 2026). Existing `P.0N` values are kept as stable identifiers but are not rendered; new projects do not need one. |
| `image` | card thumbnail | Path from repo root, e.g. `images/thumbnails/x.png`. |
| `ogImage` | social-share preview image | Path to a 1200x630 PNG. Generate with `scripts/make_og_images.py` after adding the project (uses `title`/`date`/`summary`/`labels`) rather than making one by hand. |
| `date` | card + page kicker | Plain text. Use hyphens, not dashes: `July 2024 - September 2024`. |
| `labels` | the tags | **Use exactly 3.** Domain + key tech. |
| `summary` | card description | One outcome-first sentence. |
| `describe-opening` | page intro paragraph | Supports markdown/links. |
| `describe-content` | page body | A list. Lines containing `<strong>` or `<em>` render as headings; every other line is a bullet. |
| `describe-closing` | page footer line | Usually the "Tools used" line. |
| `galleryImg` | image gallery | Optional. See [Galleries](#galleries). |
| `galleryCaption` | mono caption under the gallery | Optional. Short, factual. |
| `videoUrl` or `youtubeId` | embedded video | Optional. `youtubeId` is just the ID; `videoUrl` is a full embed URL. |
| `heroImg` | hero media | Optional. Path to the project's single strongest image; renders full-column right under the header (design-system pattern). Clicking opens the lightbox. |
| `videoPoster` | hero video poster | Optional. Path to a poster image; renders in the hero position with a play button, and clicking swaps in the `videoUrl`/`youtubeId` player (video never autoplays). |
| `heroCaption` | mono caption under the hero media | Optional. Short, factual, e.g. "Leadflow pipeline overview". |
| `draft: true` | hide it | Optional. Keeps the file but removes it from the grid (used for the Career Break). Central alternative: `hidden_projects` in `_config.yml` ([site-settings.md](site-settings.md)). |

## Thumbnails
- Put the file in `images/thumbnails/` and point `image:` at it.
- A company logo works. If there's no logo, a simple wordmark on the site's cream/ink/green palette fits (that's what the Berning "Leadflow" thumbnail is).
- The card crops to a 16:10 area and fits the image inside with padding, so exact dimensions don't matter. ~900×560 or a square logo both look fine.

## Galleries
If a project has screenshots:

1. Create a folder `images/<name>/` and drop the images in.
2. Set `galleryImg: /images/<name>` in the front matter.

How it renders on the detail page:
- Shows the **first 3 images** as a strip; if there are more, the 3rd shows a "+N more" overlay.
- Clicking any image opens a full-screen lightbox (arrow keys, Esc, click-outside to close).
- **Order is by filename.** The first 3 files (alphabetically) are the "cover" images. To choose which show, rename your best ones `01-...`, `02-...`, `03-...`.

## Tag guidance
Three tags, describing the project at a glance: a domain (e.g. `Computer Vision`, `LLM`, `Backend`) plus the key tech or role. Keep the style consistent with the other cards.

## Edit an existing project
Open its file in `projects/` and edit. To reorder, rename the number prefix. To hide it without deleting, add `draft: true`.
