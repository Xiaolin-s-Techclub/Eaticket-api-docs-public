# Configuration file for the Sphinx documentation builder

project = 'Eaticket'
copyright = '2024, Eaticket'
author = 'Eaticket Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# Add any Sphinx extension module names here
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinxcontrib.openapi'
]

# Add any paths that contain templates here
templates_path = ['_templates']

# The theme to use for HTML and HTML Help pages
html_theme = 'sphinx_rtd_theme'

# The suffix of source filenames
source_suffix = '.rst'

# The master toctree document
master_doc = 'index'

# Add any paths that contain custom static files (such as style sheets) here
html_static_path = ['_static']

# These paths are either relative to html_static_path or fully qualified paths
html_css_files = [
    'custom.css',
]

# Custom sidebar templates
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'style_nav_header_background': '#2980B9',
}