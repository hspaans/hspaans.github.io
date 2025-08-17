"""Configuration file for the Sphinx documentation builder."""

from datetime import datetime
import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Hans Spaans'
project_title = 'GitBiz evangelist that follows the enlightenment path of CI/CD towards FinOps'
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
html_extra_path = ['robots.txt']

if html_theme == "alabaster":
    html_css_files = [
        'alabaster.css',
    ]
    html_sidebars = {
        "*": [
            'about.html',
            'searchfield.html',
            'navigation.html',
            'relations.html',
        ]
    }
    html_theme_options = {
        'description': 'GitBiz evangelist that follows the enlightenment path of CI/CD towards FinOps',
        'logo': 'logo-light.jpg',
        'logo_name': True,
    }
elif html_theme == "furo":
    html_css_files = [
        'furo.css',
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    ]
    html_sidebars = {}
    html_theme_options = {
        "light_logo": "logo-light.jpg",
        "dark_logo": "logo-dark.jpg",
        "footer_icons": [
            {
                "name": "RSS",
                "url": "https://hspaans.github.io/blog/atom.xml",
                "html": "",
                "class": "fas fa-rss",
            },
            {
                "name": "GitHub",
                "url": "https://github.com/hspaans/hspaans.github.io",
                "html": "",
                "class": "fa-brands fa-github",
            },
        ],
        "source_repository": "https://github.com/hspaans/hspaans.github.io/",
        "source_branch": "master",
        "source_directory": "docs/",
        # "announcement": "test",
    }
else:
    # Make sure everything is reset if html_theme is unknown
    html_css_files = []
    html_theme_options = {}
    html_sidebars = {}

# -- Extension configuration -------------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

if 'ablog' in extensions:
    blog_path = 'blog'
    blog_title = project
    blog_baseurl = html_baseurl
    blog_feed_archives = True
    blog_feed_fulltext = True
    blog_feed_length = 10
    blog_feed_author = author
    blog_feed_language = 'en'
    blog_post_pattern = "blog/*.rst"

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

if os.getenv("GITHUB_ACTIONS"):
    extensions.append("sphinxcontrib.googleanalytics")
    googleanalytics_id = "G-N7F9Y9PQSX"
