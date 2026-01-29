# Template for technical book using Markdown + Sphinx

Template for a technical book using Markdown as markup language and Sphinx for building it.

The template includes:

- Cover
- Table of contents
- Cross-chapter references
- Index

## Pre-requisites

- Python
- Sphinx
- ST-parser
- linkify-it-py
- TeX engine:
  - MiKTeX (Windows)
  - MacTeX (macOS)
  - Texlive (Linux)
- Other LaTeX support packages:
  - latexmk (Linux)

### Windows Pre-requisites

```shell
python -m venv .venv
.venv\Scripts\activate
# Just once
pip install -U sphinx myst-parser sphinx-book-theme
# Command to install MikTeX
```

### macOS Pre-requisites

From the project folder:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -U sphinx myst-parser sphinx-book-theme
# If you create PDFs
# Command to install MacTeX
```

### Linux Pre-requisites

From the project folder:

```shell
python3 -m venv .venv
source .venv/bin/activate
pip install -U sphinx myst-parser sphinx-book-theme linkify-it-py
# If you create PDFs
apt install texlive-full latexmk
```

## Build instructions

### Linux

Run these commands from the project root folder.

```shell
# PDF
source .venv/bin/activate
sphinx-build -W -b latex docs docs/_build/latex
latexmk -pdf -cd -xelatex -interaction=nonstopmode docs/_build/latex/mybook.tex
makeindex -s docs/_build/latex/python.ist -o docs/_build/latex/mybook.ind docs/_build/latex/mybook.idx
latexmk -pdf -cd -xelatex -interaction=nonstopmode docs/_build/latex/mybook.tex
```

Note: the last two commands were added to add an index to the document.

```shell
# HTML
source .venv/bin/activate
sphinx-build -n -W -b html docs docs/_build/html
```

## Authoring instructions

Modify the template files in folder `docs` as desired.

## Presentation instructions

Configure the `docs/conf.py` file as in any other Sphinx project.

## License

The template is licensed under CC0-1.0.

Please update (or remove) the [`REUSE.toml`](REUSE.toml) and [`LICENSES`](LICENSES/) folder.
