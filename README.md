# Beamer Academic Template Skill

Agent Skill for creating, adapting, and maintaining Chinese/English academic Beamer presentations based on the local `beamer-universal-academic-template` project.

The skill is compatible with tools that support the Agent Skills `SKILL.md` convention, including Codex and Claude Code.

## What It Does

- Guides agents through building academic Beamer decks for research talks, thesis defenses, course reports, seminars, and paper presentations.
- Uses `XeLaTeX + ctex + biblatex` assumptions from the source template.
- Documents the expected project layout: `main.tex`, `sections/`, `tables/`, `figures/`, and bibliography files.
- Preserves the template's Chinese/English font setup and academic slide conventions.
- Bundles the full MIT-licensed sample template, including the slide gallery, figures, tables, bibliography, and preview PDF.
- Provides a safe helper script for creating a new deck directory without overwriting existing paths.

## Repository Layout

```text
beamer-academic-template/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── beamer-universal-academic-template/
├── scripts/
│   └── create_deck.py
├── references/
│   └── template-guide.md
├── LICENSE
└── README.md
```

## Install For Codex

Install as a personal Codex skill:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/EamonSuen/beamer-academic-template.git ~/.codex/skills/beamer-academic-template
```

If `~/.codex/skills/beamer-academic-template` already exists, inspect it first and use the update command below instead of cloning over it.

Use it in Codex with:

```text
Use $beamer-academic-template to create or adapt an academic Beamer presentation.
```

To create a new deck from the bundled template:

```bash
python ~/.codex/skills/beamer-academic-template/scripts/create_deck.py /absolute/path/to/new-deck
```

If the skill already exists, update it with:

```bash
git -C ~/.codex/skills/beamer-academic-template pull --ff-only
```

## Install For Claude Code

Claude Code discovers personal skills from `~/.claude/skills/<skill-name>/SKILL.md`.

Install this skill with:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/EamonSuen/beamer-academic-template.git ~/.claude/skills/beamer-academic-template
```

If `~/.claude/skills/beamer-academic-template` already exists, inspect it first and use the update command below instead of cloning over it.

Use it in Claude Code either naturally:

```text
Help me create a Chinese/English academic Beamer deck for my research presentation.
```

or invoke it directly:

```text
/beamer-academic-template
```

To create a new deck from the bundled template:

```bash
python ~/.claude/skills/beamer-academic-template/scripts/create_deck.py /absolute/path/to/new-deck
```

If Claude Code was already running before installation, restart Claude Code or ask it to list available skills.

Update the installed skill with:

```bash
git -C ~/.claude/skills/beamer-academic-template pull --ff-only
```

For a project-local Claude Code installation, clone or vendor this repository under the target project:

```text
.claude/skills/beamer-academic-template/SKILL.md
```

Then commit `.claude/skills/beamer-academic-template/` to that project if the skill should be shared with collaborators.

## Font Dependency

The source Beamer template expects a local clone of:

```text
https://github.com/Haixing-Hu/latex-chinese-fonts
```

at:

```text
/Users/eamonsuen/Documents/GitHub/latex-chinese-fonts
```

The Beamer template points to that location through `main.tex`:

```tex
\newcommand{\FontRoot}{/Users/eamonsuen/Documents/GitHub/latex-chinese-fonts}
```

On another machine, either clone the font repository to the same path or update `\FontRoot` to the local font repository path.

## Source Template

This skill includes a bundled copy of the Beamer template at:

```text
assets/beamer-universal-academic-template
```

The bundled copy intentionally excludes generated LaTeX auxiliary files, `output/`, `.texpadtmp`, `.DS_Store`, and `tmp1.tmp`.

The source template is maintained at:

```text
https://github.com/EamonSuen/beamer-universal-academic-template
```

When using this skill outside the original machine, provide the target Beamer project path and font path if they differ.

## Validate

Codex skill validation:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/beamer-academic-template
```

If your default Python does not include PyYAML, run the validator from a Python environment that has `PyYAML` installed.

## References

- Claude Code skills documentation: `https://code.claude.com/docs/en/skills`
- Font repository: `https://github.com/Haixing-Hu/latex-chinese-fonts`

## License

MIT License. See `LICENSE`.
