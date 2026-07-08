# Add or edit an experience entry

The Experience timeline is data, not HTML. Edit one file: **`_data/experience.yml`**.

It's a list of jobs, top-to-bottom = newest-to-oldest (order in the file is the order shown). Each entry looks like this:

```yaml
- company: Berning
  role: Software Engineer, AI Systems
  period: January 2026 - July 2026
  location: Remote
  recent: true
  link: /projects/berning
  summary: >
    Built Leadflow, an AI-powered lead generation platform with automated
    lead ingestion and enrichment, multi-client LLM scoring pipelines, and
    AI-driven personalized outreach.
```

## Add a new job
Copy the block above to the **top** of the list (newest first) and edit the fields.

## Field reference
| Field | Required | What it does |
|---|---|---|
| `company` | yes | The bold title on the timeline. |
| `role` | yes | Your title, shown in green next to the company. |
| `period` | yes | `Month Year - Month Year`. Plain hyphen, no dashes. |
| `location` | optional | Shown after the period, e.g. `Remote`, `Bandung, ID`. |
| `recent: true` | optional | Marks the entry with a filled green dot (use it for the most recent role only). |
| `link` | optional | A URL like `/projects/berning`. If set, the whole entry becomes clickable and shows "View project →" on hover. Point it at the matching project detail page. |
| `summary` | yes | 1-3 sentences. The `>` lets you wrap across lines; they join into one paragraph. |

## Linking an experience entry to its project
If the job also has a project card (most do), set `link:` to that project's permalink so people can click through to the detail page. Example: the eFishery entry has `link: /projects/efishery`. A job with no project page (like the career break) simply omits `link`.

## Editing the About > Skills lists
Skill groups are in **`_data/skills.yml`**, same idea:

```yaml
- group: AI / ML
  items: [LLM apps & agents, RAG, Computer Vision, OCR]
- group: Backend
  items: [Python, FastAPI, PostgreSQL, Redis]
```

Add a group by copying a block; add a skill by adding to its `items` list.

## Keep it in sync with the CV
The timeline should match your CV (`cv_docs/cv/latest/main.tex`). When you add or change a job here, make the same change there (and recompile the CV, then copy the new PDF to `cv/basha-tahamal-cv.pdf`).
