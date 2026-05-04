# Agent Guide

This repository is a universal academic Beamer template for research talks,
course presentations, defenses, and seminars. It is a template project: the
actual presentation content should be written from the user's talk script,
outline, paper, notes, or other source material rather than from the placeholder
examples in the repository. Agents working here should keep changes small,
preserve the template structure, and avoid modifying generated artifacts unless
explicitly requested.

## Project Overview

- Main entry point: `main.tex`
- Section content: `sections/*.tex`
- Tables: `tables/*.tex`
- Figures and logos: `figures/`
- Bibliography: `references.bib` and `bib/references.bib`
- Build output directory: `output/`
- Primary build tool: `latexmk`
- Expected engine: `XeLaTeX`
- Bibliography backend: `biber`

The template is designed for Chinese and English academic slides using
`ctex`, `fontspec`, `biblatex`, `tikz`, `tcolorbox`, `listings`, and Beamer's
standard layout tools.

## Build Commands

Use this command to compile the presentation:

```bash
latexmk -xelatex -outdir=output main.tex
```

Use this command only when the user explicitly asks to clean LaTeX auxiliary
files:

```bash
latexmk -c -outdir=output main.tex
```

Do not run broad cleanup commands. Do not remove generated files manually with
recursive deletion commands.

## Editing Rules

- Prefer editing `sections/*.tex` for slide content.
- Edit `main.tex` only for global configuration, metadata, packages, theme
  settings, font configuration, bibliography configuration, or section order.
- Put reusable table fragments in `tables/`.
- Put image assets in `figures/`; keep logo assets under `figures/logo/`.
- Keep bibliography entries in BibTeX format and avoid duplicate keys.
- Do not edit `main.pdf` directly.
- Do not modify generated LaTeX files such as `.aux`, `.bbl`, `.bcf`, `.blg`,
  `.fdb_latexmk`, `.fls`, `.log`, `.nav`, `.out`, `.run.xml`, `.snm`,
  `.synctex.gz`, `.toc`, `.vrb`, or `.xdv` unless the user specifically asks.
- Preserve unrelated user edits. Check `git status --short` before making
  changes when the task may overlap with existing work.

## LaTeX Style

- Keep slide source readable and modular.
- Use `\section` and `\subsection` to maintain navigation and outline slides.
- Keep frames focused: one claim, result, figure, or table per slide where
  possible.
- Prefer Beamer-native environments such as `frame`, `columns`, `block`,
  `alertblock`, `exampleblock`, `theorem`, `definition`, and `proof`.
- Use existing custom box environments for academic emphasis:
  `regressionbox`, `findingbox`, `methodbox`, `robustbox`, `policybox`, and
  `cautionbox`.
- Use `\includegraphics` for figures and keep paths relative to the project
  root.
- Use `\input{tables/...}` for larger reusable tables.
- Use `\cite`, `\textcite`, or `\parencite` consistently with `biblatex`.
- Avoid overfull slides. Shorten text, split frames, or use `columns` instead
  of shrinking everything.
- Keep Chinese and English mixed text natural; the project already uses
  `ctex` and explicit font configuration.

## Fonts

The default font root is configured in `main.tex` as:

```tex
\newcommand{\FontRoot}{/Users/eamonsuen/Documents/GitHub/latex-chinese-fonts}
```

Do not change this absolute font path unless the user asks for a portable or
project-local font setup. If adding project-local fonts, place them under:

- `fonts/serif/`
- `fonts/sans/`
- `fonts/mono/`

Then update the relevant `fontspec` declarations in `main.tex`.

## Slide Gallery

`sections/00_slide_gallery.tex` is a rich sample slide library. It contains many
potentially useful styles, layouts, and LaTeX patterns for academic
presentations, including text layouts, columns, math slides, tables, figures,
blocks, theorem-like environments, citations, code listings, and visual
emphasis patterns.

Use the slide gallery as a style and implementation reference. When creating
new slides, first understand the user's talk script or source material, then
select suitable patterns from the gallery and adapt them to that content. Do not
treat the gallery as production content, and do not leave placeholder examples
in final slides unless the user explicitly asks for template demonstration
slides.

## File Safety

This project is used on macOS. Be conservative with filesystem operations.

- Do not use recursive deletion commands.
- Do not use `git clean`, `git reset --hard`, `rm -r`, `rm -rf`, `find -delete`,
  `xargs rm`, `rsync --delete`, or similar cleanup commands.
- Do not delete directories.
- Do not overwrite existing files without checking whether they contain user
  work.
- Prefer read-only inspection commands such as `pwd`, `ls -la`, `rg --files`,
  `git status --short`, and `git diff`.
- If deletion is truly required, stop and ask the user for explicit
  confirmation with the full absolute path.

## Verification

After meaningful LaTeX changes, compile with:

```bash
latexmk -xelatex -outdir=output main.tex
```

If compilation fails, inspect the relevant lines in `main.log` and fix the
source file that caused the error. Report any remaining warnings that affect
the rendered PDF, such as missing fonts, missing figures, undefined citations,
or overfull boxes on important slides.

## Agent Response Expectations

- Summarize what changed and where.
- Mention whether compilation was run.
- If compilation was not run, state why.
- Keep final responses concise and include actionable next steps only when
  useful.
