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
| `tone` | The dot color and text color: `open` = green (available), `busy` = gold (employed but listening), `quiet` = gray (not looking). |

Examples for different life stages:
- Job hunting: `text: Open to new roles`, `tone: open`
- Employed, open to interesting offers: `text: Open to interesting problems`, `tone: busy`
- Heads-down at a job: `show: false` (or `text: Building at CompanyName`, `tone: quiet`)

## Writing section

```yaml
show_writing: false
```

- `false`: the Writing section disappears from the homepage, the nav link is removed, and `/writing/` shows a "coming soon" card. Post files in `_posts/` are kept and still build at their URLs, they just aren't linked anywhere.
- `true`: homepage shows the 2 newest posts, nav gets the Writing link, `/writing/` lists everything.

Flip it to `true` when you're ready to publish. Posts don't need any changes; the toggle only controls visibility.
