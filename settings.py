import os

REPO_NAME = "personal_flask"

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_REMOVE_EXTRA_FILES = False
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_EXTENSION_CONFIG = {
    'codehilite': {
        'linenums': True,
        'use_pygments': True
    }
}
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
