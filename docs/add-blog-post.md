# Add or edit a blog post

Posts live in `_posts/`. One markdown file per post.

## Add a new post

1. Create a file named `YYYY-MM-DD-a-short-slug.md` in `_posts/`.
   The date and slug come from the filename. Example:
   `_posts/2026-08-01-rag-that-actually-works.md`

2. Paste this template at the top (the `---` block is the "front matter", i.e. the post's settings):

```markdown
---
title: "Your post title in Title Case"
date: 2026-08-01
tags: [LLM, Infrastructure]
excerpt: "One or two sentences shown on the writing list and homepage teaser. Keep it plain."
---

Your first paragraph. Write in plain first-person. No em dashes.

## A section heading

Body text. Use `##` for sections and `###` for sub-sections.

- Bullet points work
- Like this

**Bold** for emphasis. `inline code` and fenced code blocks are styled:

```python
print("code blocks render in a monospace box")
```
```

3. That's it. You do **not** need to set `layout` (it defaults to `post`).

## Where it shows up (automatically)
- Its own page at `/writing/your-short-slug/` (the slug is the filename minus the date).
- Listed on the **/writing/** page, newest first.
- The two newest appear as teasers in the homepage **Writing** section.
- Added to the RSS feed (`/feed.xml`).

## Field reference
| Field | Required | What it does |
|---|---|---|
| `title` | yes | Shown as the H1 and in lists. Wrap in quotes. |
| `date` | yes | `YYYY-MM-DD`. Controls order (newest first) and the displayed date. |
| `excerpt` | recommended | The summary in lists/teasers. If omitted, Jekyll uses the first paragraph. |
| `tags` | optional | 1-3 short tags, shown as chips under the title. Example: `tags: [LLM, Cost]` |

## What renders (markdown reference)

Everything is plain markdown (kramdown). All of these are styled to match the design system:

- Headings (`##`, `###`), **bold**, *italic*, links, lists, blockquotes.
- `inline code` and fenced code blocks. Name the language after the fence
  (` ```python `) to get quiet green/gold syntax colors.
- Tables, images (hairline border + rounded corners), and `---` horizontal
  rules (gold hairline).
- **Mermaid diagrams**: a fenced block with the `mermaid` language renders as
  an SVG diagram in the page, adapting to light/dark mode:

  ~~~markdown
  ```mermaid
  flowchart LR
    A[Request] --> B{Cache hit?}
    B -- yes --> C[Serve cached]
    B -- no --> D[Call LLM]
  ```
  ~~~

  The mermaid library loads from a CDN only on pages that contain a diagram;
  posts without one stay dependency-free.
- **Table of contents**: posts with 3 or more `##` sections automatically get
  a sticky mini-TOC in the left margin on wide screens. Nothing to configure.

## Edit an existing post
Open the file in `_posts/` and edit the body or front matter. To change the URL, rename the file's slug (note: this breaks any existing links to the old URL).

## Notes
- Ordering is by `date`. To bump a post to the top, give it a later date.
- Keep the writing voice plain and sincere. **No em/en dashes.**
- Nothing appears until you save and Jekyll rebuilds (it's automatic while `jekyll serve` is running).
