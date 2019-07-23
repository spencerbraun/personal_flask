#!/usr/bin/env python

import argparse
import os
import shutil
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
FLATPAGES_EXTENSION = ".md"
FREEZER_REMOVE_EXTRA_FILES = False
FLATPAGES_MARKDOWN_EXTENSIONS = ["codehilite"]
FLATPAGES_EXTENSION_CONFIG = {"codehilite": {"linenums": "True"}}
FLATPAGES_ROOT = os.path.join(APP_DIR, "pages")

app = Flask(__name__)
app.config.from_pyfile("settings.py")
app.url_map.strict_slashes = False
# app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

#
# @app.before_request
# def clear_trailing():
#     from flask import redirect, request
#
#     rp = request.path
#     if rp != "/" and rp.endswith("/"):
#         return redirect(rp[:-1])


@app.route("/")
def index():
    posts = [page for page in pages if "date" in page.meta]
    sorted_posts = sorted(posts, reverse=True, key=lambda page: page.meta["date"])
    return render_template("index.html", pages=sorted_posts)


@app.route("/about/")
def about():
    # about = [page for page in pages if "About" == page.meta['title']]
    # return render_template("page.html", page=about)
    return render_template("about.html")


@app.route("/writing/")
def writing():
    posts = [
        page for page in pages if all([tag in page.meta for tag in ["date", "writing"]])
    ]
    sorted_posts = sorted(posts, reverse=True, key=lambda page: page.meta["date"])
    return render_template("writing.html", pages=sorted_posts)


@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--build',
        action='store_true',
        help='Freezes flask application into build dir'
    )
    parser.add_argument(
        '--build_live',
        action='store_true',
        help='Freezes flask application and build to docs dir'
    )
    args = parser.parse_args()

    if args.build or args.build_live:
        freezer.freeze()
        if args.build_live:
            shutil.copytree('build', 'docs')
    else:
        app.run(host="localhost", port=8000)


if __name__ == "__main__":
    main()
