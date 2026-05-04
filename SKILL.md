---
name: beamer
description: Create, adapt, and maintain Chinese/English academic Beamer presentations using the local beamer-universal-academic-template project. Use when Codex needs to make course reports, thesis defenses, research talks, seminars, academic slide decks, XeLaTeX Beamer files, bibliography-enabled presentations, or slides based on this reusable template.
---

# Beamer Academic Template

## Overview

Use the bundled Beamer template in `assets/beamer-universal-academic-template` as the source of truth for academic slide projects. The template is built around `XeLaTeX + ctex + biblatex`, supports Chinese/English mixed typesetting, and keeps content split across `main.tex`, `sections/`, `tables/`, `figures/`, and bibliography files.

## Quick Start

1. Inspect the user's target deck or requested topic.
2. Read `references/template-guide.md` when you need project structure, bundled sample-library details, compile commands, font repository assumptions, or common edit patterns.
3. For a new deck, copy the bundled template with `scripts/create_deck.py <target-directory>`; the script refuses to overwrite an existing target.
4. For an existing deck, modify the relevant `main.tex`, `sections/*.tex`, `tables/*.tex`, `figures/`, and bibliography files directly.
5. Use `sections/00_slide_gallery.tex` as the built-in sample library when selecting layouts.
6. Compile with:

```bash
latexmk -xelatex -outdir=output main.tex
```

## Editing Workflow

- Update title metadata in `main.tex`: `\title`, `\subtitle`, `\author`, `\institute`, and `\date`.
- Keep main narrative slides in `sections/01_intro.tex` through `sections/05_conclusion.tex`.
- Keep backup material in `sections/99_appendix.tex`.
- Use the bundled `sections/00_slide_gallery.tex` as a pattern library for Beamer layouts; include it only when the user wants examples compiled into the deck.
- Put reusable table fragments in `tables/*.tex` and include them with `\input{tables/name}`.
- Put figures under `figures/`, preserving relative paths from `main.tex`.
- Maintain references in `references.bib` unless the user asks to consolidate with `bib/references.bib`.

## Style Guidance

- Prefer concise research-talk slides: one claim per slide, short bullets, and details in appendix.
- Use Chinese/English mixed text naturally; the template already configures `ctex`, `fontspec`, and CJK fonts.
- Treat `/Users/eamonsuen/Documents/GitHub/latex-chinese-fonts` as a local clone of `https://github.com/Haixing-Hu/latex-chinese-fonts`; if the clone is missing, restore that path or update `\FontRoot` in `main.tex`.
- Use the provided academic boxes for emphasis when appropriate: `findingbox`, `methodbox`, `regressionbox`, `robustbox`, `policybox`, and `cautionbox`.
- Use `booktabs` style tables and avoid dense tables unless they are central to the talk.
- Keep captions, citations, and appendix material formal enough for academic presentation.

## Validation

After edits, run the compile command from the deck root. If compilation fails, inspect the first LaTeX error and fix source files before retrying. Do not delete build directories or generated files as a cleanup shortcut.

## Reference

Read `references/template-guide.md` for detailed structure, file roles, compile behavior, fonts, and common task recipes.

## Bundled Resources

- `assets/beamer-universal-academic-template/`: complete MIT-licensed starter template with sample slide gallery, figures, tables, bibliography, preview PDF, and README.
- `scripts/create_deck.py`: safely copy the bundled template to a new target directory.
