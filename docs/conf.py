# Sphinx documentation configuration for the `update-dotdee' package.
#
# Author: Peter Odding <peter@peterodding.com>
# Last Change: March 25, 2018
# URL: https://github.com/xolox/python-update-dotdee

"""Sphinx documentation configuration for the `update-dotdee` package."""

import os
import sys

# Add the update-dotdee source distribution's root directory to the module path.
sys.path.insert(0, os.path.abspath(os.pardir))

# -- General configuration -----------------------------------------------------

# Sphinx extension module names.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'humanfriendly.sphinx',
]

# Sort members by the source order instead of alphabetically.
autodoc_member_order = 'bysource'

# Paths that contain templates, relative to this directory.
templates_path = ['templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'update-dotdee'
copyright = '2018, Peter Odding'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# Find the package version and make it the release.
from update_dotdee import __version__ as update_dotdee_version  # noqa

# The short X.Y version.
version = '.'.join(update_dotdee_version.split('.')[:2])

# The full version, including alpha/beta/rc tags.
release = update_dotdee_version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['build']

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Refer to the Python standard library.
# From: http://twistedmatrix.com/trac/ticket/4582.
intersphinx_mapping = dict(
    humanfriendly=('https://humanfriendly.readthedocs.io/en/latest', None),
    propertymanager=('https://property-manager.readthedocs.io/en/latest', None),
    python=('https://docs.python.org/2', None),
)

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'nature'

# Output file base name for HTML help builder.
htmlhelp_basename = 'updatedotdeedoc'
