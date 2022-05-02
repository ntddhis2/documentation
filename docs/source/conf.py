# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'NTD DHIS2 Documentation'
copyright = '2021, RTI'
author = 'Adam Preston'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']


def setup(app):
    app.add_css_file('css/custom.css')

# -- Options for EPUB output
epub_show_urls = 'footnote'


# Build PDF & ePub
formats:
  - epub
  - pdf
