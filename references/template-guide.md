# Beamer Academic Template Guide

## Source Project

Bundled template root:

`${CLAUDE_SKILL_DIR}/assets/beamer-universal-academic-template`

Local source project used to maintain the bundled copy:

`/Users/eamonsuen/Documents/GitHub/beamer-universal-academic-template`

Use the bundled template as the canonical reference for layout, package choices, font configuration, and example content. When adapting it into another deck, preserve the same structure unless the user requests a different organization.

## Project Structure

- `main.tex`: document preamble, fonts, Beamer theme, metadata, section inputs, bibliography, and final Q&A frame.
- `sections/01_intro.tex`: introduction and motivation.
- `sections/02_background.tex`: literature, context, and descriptive facts.
- `sections/03_model.tex`: model setup and equations.
- `sections/04_empirics.tex`: empirical design, results, and interpretation.
- `sections/05_conclusion.tex`: takeaways and closing.
- `sections/99_appendix.tex`: backup slides after `\appendix`.
- `sections/00_slide_gallery.tex`: reusable layout examples and Beamer component patterns.
- `tables/*.tex`: standalone table fragments intended to be included inside frames.
- `figures/`: charts, diagrams, and logo assets.
- `references.bib`: default bibliography file used by `main.tex`.
- `bib/references.bib`: alternate bibliography location retained by the template.
- `main.pdf`: preview build of the template.

The bundled copy intentionally excludes generated LaTeX auxiliary files, `output/`, `.texpadtmp`, `.DS_Store`, and `tmp1.tmp`.

## Compile

Recommended command from the deck root:

```bash
latexmk -xelatex -outdir=output main.tex
```

The template uses `biblatex` with `biber`, so a normal `latexmk` run should handle bibliography passes. If bibliography entries do not appear, inspect whether `biber` is installed and whether citation keys match `references.bib`.

Avoid cleanup commands unless the user asks. If cleanup is requested, follow local file-safety rules and avoid recursive deletion.

## Font Repository Assumptions

The template uses `XeLaTeX`, `ctex`, and `fontspec` with a fixed local font repository. This directory is expected to be a local clone of `https://github.com/Haixing-Hu/latex-chinese-fonts`:

`/Users/eamonsuen/Documents/GitHub/latex-chinese-fonts`

Current defaults:

- English serif: `TimesNewRoman.ttf`
- English sans: `Helvetica.ttf`
- English mono: `Courier.ttf`
- Chinese serif/main: `FangSong.ttf`
- Chinese sans: `STHeiti.ttf`
- Chinese mono substitute: `SimHei.ttf`

If the target machine does not have this font repository, either clone `https://github.com/Haixing-Hu/latex-chinese-fonts` to the same path, ask the user for the intended font path, or switch `main.tex` to project-local fonts under `fonts/serif/`, `fonts/sans/`, and `fonts/mono/`.

The project-level font setting lives in `main.tex`:

```tex
\newcommand{\FontRoot}{/Users/eamonsuen/Documents/GitHub/latex-chinese-fonts}
```

When moving the deck to another machine, update only `\FontRoot` if the cloned font repository is stored elsewhere.

## Preamble Features

The template includes common academic presentation packages:

- `graphicx` for figures.
- `booktabs` and `colortbl` for tables.
- `amsmath` and `amssymb` for equations.
- `multicol` for two-column outlines.
- `tikz` with arrows, shapes, positioning, calc, and fit libraries.
- `csquotes`, `biblatex`, and `hyperref` for references.
- `appendixnumberbeamer` so appendix slides do not affect main slide numbering.
- `listings` for code snippets.
- `tcolorbox` for academic callout boxes.
- `ccicons` for the Creative Commons mark on the final frame.

Available callout boxes:

- `regressionbox`
- `findingbox`
- `methodbox`
- `robustbox`
- `policybox`
- `cautionbox`

Use these for compact emphasis, not for every slide.

## Common Tasks

### Create a New Deck From the Bundled Template

Use the helper script when a user wants a new deck directory:

```bash
python scripts/create_deck.py /absolute/path/to/new-deck
```

The target directory must not already exist. If it exists, inspect it and ask the user how to proceed instead of overwriting.

### Create a New Research Talk

1. Set title metadata in `main.tex`.
2. Replace the five main section files with the talk narrative.
3. Put backup details in `sections/99_appendix.tex`.
4. Add citations to `references.bib`.
5. Use `sections/00_slide_gallery.tex` as the sample library for layouts and LaTeX patterns.
6. Replace example figures and tables with project-specific assets.
7. Decide whether to comment out `\input{sections/00_slide_gallery}` for a formal deck.
8. Compile and fix the first LaTeX error before addressing downstream errors.

### Add a Figure Slide

Use `figure` with `\includegraphics`, keep paths relative to the deck root, and prefer `keepaspectratio`:

```tex
\begin{frame}{Descriptive Evidence}
  \begin{figure}
    \centering
    \includegraphics[width=0.78\linewidth,height=0.58\textheight,keepaspectratio]{figures/my-chart.pdf}
    \caption{Short, informative caption.}
  \end{figure}
\end{frame}
```

### Add a Table Slide

For reusable tables, place the table in `tables/name.tex` and include it:

```tex
\begin{frame}{Main Results}
  \input{tables/main-results}
\end{frame}
```

Use `booktabs` rules and reduce font size locally with `{\small ...}` or `{\scriptsize ...}` when needed.

### Add Citations

Use `\textcite{key}` for narrative citations and `\parencite{key}` for parenthetical citations. Add entries to `references.bib` and compile with `latexmk -xelatex -outdir=output main.tex`.

### Use the Slide Gallery

Open `sections/00_slide_gallery.tex` when the user asks for layout ideas, example Beamer constructs, multi-column slides, table patterns, boxes, code listings, TikZ diagrams, or appendix patterns. Copy the relevant frame pattern into the real section file and adapt the content. Do not treat the sample gallery as production talk content.

## Editing Preferences

- Keep slides presentation-oriented; avoid paper paragraphs.
- Use one main claim per frame.
- Prefer appendix slides for robustness, derivations, long tables, and secondary figures.
- Keep table and figure filenames stable and descriptive.
- Preserve `\appendix` placement before appendix inputs.
- Avoid changing global font and theme settings unless the user asks or compilation requires it.
