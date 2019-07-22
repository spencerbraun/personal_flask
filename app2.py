#!/usr/bin/env python

import os
import sys

from flask import (
    Flask,
    flash,
    Markup,
    redirect,
    render_template,
    request,
    Response,
    session,
    url_for,
)
from flask_flatpages import FlatPages
from flask_frozen import Freezer

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FREEZER_REMOVE_EXTRA_FILES = False
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_EXTENSION_CONFIG = {
    'codehilite': {
        'linenums': 'True'
    }
}
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')

app = Flask(__name__)
app.url_map.strict_slashes = False
# app.config.from_pyfile('settings.py')
app.config.from_object(__name__)
pages = FlatPages(app)
# freezer = Freezer(app)

@app.before_request
def clear_trailing():
    from flask import redirect, request

    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1])

# @freezer.register_generator
# def page_details():
#     for path in pages.iter():
#         yield {'path': path}

@app.route('/')
def index():
    posts = [page for page in pages if 'date' in page.meta]
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)



if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 5000))
    #
    # if len(sys.argv) > 1 and sys.argv[1] == "build":
    #     freezer.freeze()
    # else:
    app.run(host='localhost', port=8000)
