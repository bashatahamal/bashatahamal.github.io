# Update the CV PDF

The CV is LaTeX, kept in a **separate repo**: `~/space/portfolio/cv_docs/cv/latest/`.

- `main.tex` = the master CV (real contact info). **This is the one the site publishes.**
- `public_safe.pdf` / `public_safe.tex` = older scrubbed variant. As of 2026-07-09 it lags behind main (missing the HDCE-TIB block). Prefer maintaining `main.tex` only.
- `basha.jpg` = the photo used in the header.

## The workflow (edit → compile → publish)

```bash
cd ~/space/portfolio/cv_docs/cv/latest

# 1. Edit main.tex (see "Where things are in main.tex" below)

# 2. Compile (run twice is handled automatically by latexmk)
latexmk -C main.tex          # clean old build state (important after errors)
latexmk -pdf main.tex        # produces main.pdf

# 3. Check main.pdf looks right (open it), then publish to the site:
cp main.pdf ~/space/portfolio/bashatahamal.github.io/cv/basha-tahamal-cv.pdf

# 4. Commit both repos
cd ~/space/portfolio/cv_docs && git add -A && git commit -m "update cv"
cd ~/space/portfolio/bashatahamal.github.io && git add cv/ && git commit -m "refresh cv pdf" && git push
```

## Where things are in main.tex

| Section | Look for |
|---|---|
| Contact strip | `\documentTitles{` (phone, email, LinkedIn, city) |
| Summary paragraph | `\tinysection{Summary}` |
| A job entry | `\headingBf{Company}{Dates}` then `\headingIt{Title}{Location}` |
| Job bullets | the `\begin{resume_list} ... \end{resume_list}` under it |
| Education / Skills | `\section{Education}`, `\section{Skills}` |

To add a new job: copy an existing block from `\headingBf` through `\end{resume_list}` and edit. Newest jobs go first. Keep dates as `January 2026 -- July 2026` (the `--` is LaTeX for a dash; fine here, the no-dash rule is for the website copy).

**Keep the website timeline in sync**: same change goes in `_data/experience.yml` (see [add-experience.md](add-experience.md)).

## Troubleshooting (learned 2026-07-08, keep for reference)

**`command not found: latexmk`**
TeX isn't on your shell's PATH. Open a new terminal window, or run:
`export PATH="/Library/TeX/texbin:$PATH"`

**`! LaTeX Error: File 'something.sty' not found.`**
Your BasicTeX is missing a package. Install it by name:
`sudo tlmgr install <something>`
(If sudo is a hassle: `tlmgr init-usertree` once, then `tlmgr --usermode install <something>`.)

**`Font ... not loadable: Metric (TFM) file not found` or thousands of `Missing character: There is no X in font nullfont!`**
A font package's actual font files are missing (the PDF will silently drop text!). Find the owner and install it:
```bash
tlmgr search --global --file "<fontname>"   # e.g. bchr7t
sudo tlmgr install <package>                 # e.g. charter
```
The Charter body font is already installed in your user tree (`~/Library/texmf`), so this specific one shouldn't recur on this machine.

**latexmk says "up-to-date" but you know it failed before**
It caches failures. `latexmk -C main.tex` then compile again.

**Nuclear option**: compile on [Overleaf](https://overleaf.com) instead. Upload `main.tex` + `basha.jpg`; it has every package preinstalled.

## Rules for CV content
- Same voice rules as the site: plain sentences, no fluff.
- Summary says "over 5 years of professional experience"; bump it as time passes.
- It's 4 pages as of July 2026. For applications, consider a trimmed 2-page variant (flagged in docs/recommendations.md).
