# Sphinx configuration for validation.huira.space
# Same toolchain as docs.huira.space: Sphinx with the Furo theme.

project = "Huira Validation"
copyright = "2026, Christopher Gnam"
author = "Christopher Gnam"

extensions = [
    "sphinx.ext.mathjax",
]

html_theme = "furo"
html_title = "Huira Validation"
html_static_path = ['_static']
html_favicon = '_static/logo/icon/icon_blue_on_white.svg'
templates_path = ['_templates']

# Custom sidebar structure:
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/website_link.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}

# Custom CSS overrides:
html_css_files = [
    'css/custom.css',
]

# Custom JavaScript:
html_js_files = []

# Furo theme options:
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2980b9",
        "color-brand-content": "#2980b9",
    },
    "dark_css_variables": {
        "color-brand-primary": "#5ba3d0",
        "color-brand-content": "#5ba3d0",
    },
    "sidebar_hide_name": True,
    "light_logo": "logo/full/blue_on_transparent.svg",
    "dark_logo": "logo/full/white_on_transparent.svg",
}

numfig = True
math_numfig = True

exclude_patterns = ["_build", "README.md", ".github", ".venv"]
