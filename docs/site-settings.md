# Site settings (switches in _config.yml)

Quick toggles at the top of `_config.yml`. Edit, save, and Jekyll rebuilds. No HTML needed.

> Note: `_config.yml` is the one file `jekyll serve` does NOT auto-reload. After editing it, stop the server (Ctrl-C) and run `bundle exec jekyll serve` again.

## Availability chip (the "Open to new roles" pill in the hero)

```yaml
availability:
  show: true
  text: Open to new roles
  tone: open
```

| Key | What it does |
|---|---|
| `show` | `false` hides the chip entirely. |
| `text` | The label. Keep it short (2-5 words). |
| `tone` | The dot color and text color: `open` = green (available), `busy` = gold (employed but listening), `quiet` = neutral text with no dot (not looking). |

Examples for different life stages:
- Actively looking: `text: Open to new roles`, `tone: open`
- Employed, open to interesting offers: `text: Open to interesting problems`, `tone: busy`
- Heads-down at a job: `show: false` (or `text: Building at CompanyName`, `tone: quiet`)

## Writing section

```yaml
show_writing: false
```

- `false`: the Writing section disappears from the homepage, the nav link is removed, and `/writing/` shows a "coming soon" card. Post files in `_posts/` are kept and still build at their URLs, they just aren't linked anywhere.
- `true`: homepage shows the 2 newest posts, nav gets the Writing link, `/writing/` lists everything.

Flip it to `true` when you're ready to publish. Posts don't need any changes; the toggle only controls visibility.

## Hidden work cards

```yaml
hidden_projects: []
```

Hide a work card while its content (card data, screenshots, detail page) is still in progress, so an unfinished project never blocks publishing a design update. List project slugs, which are the last part of the project's permalink (`projects/berning` -> `berning`):

```yaml
hidden_projects: [berning, wedding]
```

- The card disappears from the "How I Got Here" grid.
- The detail page still renders at its direct URL (existing links keep working) but gets a `noindex` meta tag so search engines drop it.
- To remove a project's page from the built site entirely, add `published: false` to that project file's front matter instead.
- Related: `draft: true` in a project's front matter also hides just the card (older per-file mechanism, still supported).
