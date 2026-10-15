# Sphinx configuration for validation.huira.space
# Same toolchain as docs.huira.space: Sphinx with the Furo theme.

project = "Huira Validation"
author = "Christopher Gnam"
copyright = "2026, Christopher Gnam"

extensions = [
    "sphinx.ext.mathjax",
]

html_theme = "furo"
html_title = "Huira Validation"

numfig = True
math_numfig = True

exclude_patterns = ["_build", "README.md", ".github", ".venv"]
