#!/usr/bin/env python

import os

REPO_NAME = "personal_flask"  # Used for FREEZER_BASE_URL
DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

FREEZER_DESTINATION = APP_DIR
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = f"http://localhost/"
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'
FLATPAGES_AUTO_RELOAD = DEBUG
