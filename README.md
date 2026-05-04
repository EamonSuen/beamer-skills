# Beamer Skills

This is the canonical repository for a Beamer academic-presentation skill. It contains both the Agent Skill and a bundled Beamer starter template.

Agent Skill for creating, adapting, and maintaining Chinese/English academic Beamer presentations.

The skill is compatible with tools that support the Agent Skills `SKILL.md` convention, including Codex and Claude Code.

## What It Does

- Guides agents through building academic Beamer decks for research talks, thesis defenses, course reports, seminars, and paper presentations.
- Uses `XeLaTeX + ctex + biblatex` assumptions from the source template.
- Documents the expected project layout: `main.tex`, `sections/`, `tables/`, `figures/`, and bibliography files.
- Preserves the template's Chinese/English font setup and academic slide conventions.
- Bundles the full MIT-licensed sample template, including the slide gallery, figures, tables, bibliography, and preview PDF.
- Provides a safe helper script for creating a new deck working directory without overwriting existing paths.

## Repository Layout

```text
beamer/
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
git clone https://github.com/EamonSuen/beamer-skills.git ~/.codex/skills/beamer
```

If `~/.codex/skills/beamer` already exists, inspect it first and use the update command below instead of cloning over it.

Use it in Codex with:

```text
Use $beamer to create or adapt an academic Beamer presentation.
```

To create a new deck working directory from the bundled template:

```bash
python ~/.codex/skills/beamer/scripts/create_deck.py /absolute/path/to/new-deck
```

Use `--parents` when the parent folders should be created too:

```bash
python ~/.codex/skills/beamer/scripts/create_deck.py --parents ~/Documents/BeamerProjects/research-talk-2026
```

If the skill already exists, update it with:

```bash
git -C ~/.codex/skills/beamer pull --ff-only
```

## Install For Claude Code

Claude Code discovers personal skills from `~/.claude/skills/<skill-name>/SKILL.md`.

Install this skill with:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/EamonSuen/beamer-skills.git ~/.claude/skills/beamer
```

If `~/.claude/skills/beamer` already exists, inspect it first and use the update command below instead of cloning over it.

Use it in Claude Code either naturally:

```text
Help me create a Chinese/English academic Beamer deck for my research presentation.
```

or invoke it directly:

```text
/beamer
```

To create a new deck working directory from the bundled template:

```bash
python ~/.claude/skills/beamer/scripts/create_deck.py /absolute/path/to/new-deck
```

Use `--parents` when the parent folders should be created too:

```bash
python ~/.claude/skills/beamer/scripts/create_deck.py --parents ~/Documents/BeamerProjects/research-talk-2026
```

If Claude Code was already running before installation, restart Claude Code or ask it to list available skills.

Update the installed skill with:

```bash
git -C ~/.claude/skills/beamer pull --ff-only
```

For a project-local Claude Code installation, clone or vendor this repository under the target project:

```text
.claude/skills/beamer/SKILL.md
```

Then commit `.claude/skills/beamer/` to that project if the skill should be shared with collaborators.

## Font Dependency

The bundled Beamer template uses `fontspec` paths rather than system font names. It expects `main.tex` to define `\FontRoot` as the directory containing a clone of:

```text
https://github.com/Haixing-Hu/latex-chinese-fonts
```

The bundled default is the project-local path:

```text
fonts/latex-chinese-fonts
```

The Beamer template points to that location through `main.tex`:

```tex
\newcommand{\FontRoot}{fonts/latex-chinese-fonts}
```

For the default setup, clone the font repository into the generated deck:

```bash
git clone https://github.com/Haixing-Hu/latex-chinese-fonts.git fonts/latex-chinese-fonts
```

Alternatively, clone it elsewhere and update `\FontRoot` before compiling.

## Bundled Template

This skill includes a bundled copy of the Beamer template at:

```text
assets/beamer-universal-academic-template
```

The bundled copy intentionally excludes generated LaTeX auxiliary files, `output/`, `.texpadtmp`, `.DS_Store`, and `tmp1.tmp`.

The older standalone template repository is retained only as an archived historical reference:

```text
https://github.com/EamonSuen/beamer-universal-academic-template
```

Prefer this repository for new installs, issues, and future updates.

## Validate

Codex skill validation:

```bash
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/beamer
```

If your default Python does not include PyYAML, run the validator from a Python environment that has `PyYAML` installed.

## References

- Claude Code skills documentation: `https://code.claude.com/docs/en/skills`
- Font repository: `https://github.com/Haixing-Hu/latex-chinese-fonts`

## License

MIT License. See `LICENSE`.
