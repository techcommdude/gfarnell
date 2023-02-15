# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = ''
copyright = '2023, Geoff F'
author = ''
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

html_title = ''
html_short_title = 'test'
html_logo = '_static/python2.jpg'
html_favicon = '_static/favicon-32x32_chipmunk.ico'

templates_path = ['_templates']
exclude_patterns = []

html_sidebars = {
   '**': ['globaltoc.html', 'searchbox.html', 'relations.html']
}



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_theme_options = {
    'fixed_sidebar': 'true',
}

# 'sidebar_width': '20',
