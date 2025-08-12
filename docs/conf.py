"""Configuration file for the Sphinx documentation builder."""

from datetime import datetime

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Hans Spaans'
copyright = f"{datetime.now().year}, {project}"
author = 'Hans Spaans'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'ablog',
    'myst_parser',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx_toolbox.github',
    'sphinx_toolbox.wikipedia',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton',
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_baseurl = 'https://hspaans.github.io/'
html_title = project
html_theme = 'furo'
html_static_path = ['_static']

if html_theme == "alabaster":
    html_theme_options = {}
elif html_theme == "furo":
    html_theme_options = {}
else:
    html_theme_options = {}

if html_theme == "alabaster":
    html_css_files = [
        'custom.css',
    ]
    html_theme_options = {
        'description': 'GitOps || BizDevSecOps || FinOps',
        'logo': 'logo.png',
        'logo_name': True,
    }
    html_sidebars = {
        "*": [
            'about.html',
            'searchfield.html',
            'navigation.html',
            'relations.html',
        ]
    }
elif html_theme == "furo":
    html_sidebars = {}
else:
    html_sidebars = {
        "**": [
            "sidebar-field.html",
            "sidebar-nav.html",
        ]
    }

# -- Extension configuration -------------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

if 'ablog' in extensions:
    blog_path = 'posts'
    blog_title = project
    blog_baseurl = html_baseurl + blog_path + '/'
    blog_feed_archives = True
    blog_feed_fulltext = False
    blog_feed_length = 10
    blog_feed_author = author
    blog_feed_language = 'en'
    blog_feed_domain = html_baseurl

if 'sphinx.ext.intersphinx' in extensions:
    intersphinx_mapping = {
        'ansible': ('https://docs.ansible.com/ansible/latest/', None),
        'python': ('https://docs.python.org/3/', None),
        'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    }

if 'sphinx_toolbox.github' in extensions:
    github_username = 'hspaans'
    github_repository = 'hspaans.github.io'

if 'sphinx_toolbox.wikipedia' in extensions:
    wikipedia_lang = 'en'

if 'sphinx_sitemap' in extensions:
    sitemap_locales = [None]
    sitemap_url_scheme = "{link}"
    exclude_patterns = [
        'posts/drafts*',
    ]
