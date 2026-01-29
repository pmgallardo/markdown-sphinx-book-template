# docs/conf.py

from datetime import date

project = "My Book"
author = "Pablo Gallardo"
release = "1.0"
copyright = f"{date.today().year}, {author}"

extensions = [
    "myst_parser",                 # Markdown support
    "sphinx.ext.autosectionlabel", # Cross-refs to section titles
    "sphinx.ext.intersphinx",
]

# Make section labels unique across files
autosectionlabel_prefix_document = True

# MyST (Markdown) options
myst_enable_extensions = [
    "colon_fence",     # ::: fenced blocks
    "deflist",         # definition lists
    "linkify",         # auto-link URLs
]

# Optional: make heading anchors more predictable
myst_heading_anchors = 3

# Theme
html_theme = "sphinx_book_theme"

# Static and templates
html_static_path = ["_static"]
templates_path = ["_templates"]

# Optional: show logo/cover in the sidebar if you add one
# html_logo = "_static/cover.png"

# Intersphinx example (optional)
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

# Source file types
source_suffix = {
    ".md": "markdown",
}

# Master document (Sphinx 5+ generally uses root_doc)
root_doc = "index"

html_use_index = True

# = Only HTML configuration =
# If you want a nicer “index” page label in HTML
html_title = project

# = Only PDF configuration =
latex_engine = "xelatex"  # better Unicode/font support (also works: "pdflatex", "lualatex")

latex_elements = {
    "papersize": "a4paper",   # or "letterpaper"
    "pointsize": "11pt",
}
