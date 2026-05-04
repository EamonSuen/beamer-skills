# Beamer Universal Academic Template

一个通用的学术 `beamer` 演示模板，适合课程汇报、论文答辩、研究展示和 seminar。

This repository is a reusable Chinese/English academic Beamer template for
research talks, thesis defenses, course reports, and seminars.

## 特点

- 基于 `XeLaTeX + ctex + biblatex`
- 支持中英文混排
- 按章节拆分内容，便于长期维护
- 预留 `figures/`、`tables/`、`bib/` 和 `fonts/` 目录
- 使用 `output/` 统一存放编译产物
- 内置 `sections/00_slide_gallery.tex` 样例库，便于复制常见学术幻灯片布局
- 提供示例图、示例表格、参考文献和 appendix 结构

## 目录

```text
beamer-universal-academic-template/
├── README.md
├── LICENSE
├── .gitignore
├── main.tex
├── references.bib
├── sections/
├── figures/
├── tables/
├── bib/
├── fonts/
└── output/
```

核心文件：

- `main.tex`: 文档入口、字体、主题、metadata、章节顺序和参考文献。
- `sections/`: 正文和附录幻灯片。
- `sections/00_slide_gallery.tex`: 样例库，包含常见布局、表格、图片、数学、代码和强调框。
- `tables/`: 可复用表格片段。
- `figures/`: 示例图、图表和 logo。
- `references.bib`: 默认文献库。
- `bib/references.bib`: 备用文献库路径。

## 编译

推荐使用：

```bash
latexmk -xelatex -outdir=output main.tex
```

如需清理辅助文件，优先使用 `latexmk` 自带清理：

```bash
latexmk -c -outdir=output main.tex
```

不要手动递归删除编译目录。

## 使用说明

1. 修改 `main.tex` 中的标题、作者、机构和日期。
2. 按需编辑 `sections/` 下各章节文件。
3. 将图片和 logo 放入 `figures/`。
4. 将表格片段放入 `tables/`。
5. 将文献维护在 `references.bib` 或 `bib/references.bib`。
6. 正式汇报前，通常应注释掉或删除 `\input{sections/00_slide_gallery}`，除非你想展示样例库。

## 样例库

`sections/00_slide_gallery.tex` 是本模板的核心样例库，包含：

- 文字、列表、description 和强调格式。
- 多栏布局。
- 图片、表格和 caption 样式。
- 数学公式、定理、证明和模型展示。
- `tcolorbox` 学术强调框。
- 代码 listings。
- TikZ 图示。
- appendix 和 backup slide 模式。

建议把样例库当作复制和改写的模式库，而不是最终汇报内容。

## 字体说明

模板默认直接使用本机固定路径下的字体仓库。该目录应为
[`Haixing-Hu/latex-chinese-fonts`](https://github.com/Haixing-Hu/latex-chinese-fonts)
的本地 clone：

- `/Users/eamonsuen/Documents/GitHub/latex-chinese-fonts`

如果你在新机器上使用本模板，可选择：

```bash
git clone https://github.com/Haixing-Hu/latex-chinese-fonts.git /Users/eamonsuen/Documents/GitHub/latex-chinese-fonts
```

或者修改 `main.tex` 中的：

```tex
\newcommand{\FontRoot}{/Users/eamonsuen/Documents/GitHub/latex-chinese-fonts}
```

当前默认配置：

- 英文正文字体：`TimesNewRoman.ttf`
- 英文无衬线：`Helvetica.ttf`
- 英文等宽：`Courier.ttf`
- 中文正文字体：`FangSong.ttf`
- 中文无衬线：`STHeiti.ttf`
- 中文等宽替代：`SimHei.ttf`

这样做比依赖系统字体名更稳定，原因是：

- 不依赖 Fontconfig 或系统字体注册状态
- 字体粗体、斜体映射可以显式控制
- 换机器后只要该仓库路径不变，编译结果更一致

如果你希望针对单个项目使用自带字体，也可以把字体文件放入：

- `fonts/serif/`
- `fonts/sans/`
- `fonts/mono/`

然后在 [main.tex](/Users/eamonsuen/Documents/GitHub/beamer-universal-academic-template/main.tex) 中取消对应注释并调整文件名。

## 建议

- 若是正式汇报，建议把 `logo/logo.pdf` 替换为你的学校或机构标识。
- 若文献库只保留一个版本，建议统一使用根目录的 `references.bib`。
- 若要公开分发修改版，请保留 MIT license，并确认没有真实姓名、邮箱、机构内部数据或未授权图片。

## Agent Skill

配套 Agent Skill：

- <https://github.com/EamonSuen/beamer-academic-template>

该 skill 可安装到 Codex 或 Claude Code，用于让 agent 按本模板创建和维护学术 Beamer 幻灯片。

## License

MIT License. See [LICENSE](LICENSE).
