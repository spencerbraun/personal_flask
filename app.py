#!/usr/bin/env python

import argparse
import os
import shutil
import sys
from pathlib import Path

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

app = Flask(__name__)
app.config.from_pyfile("settings.py")
pages = FlatPages(app)
freezer = Freezer(app)


def customcopy(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            try:
                shutil.copytree(s, d, symlinks, ignore)
            except FileExistsError:
                shutil.rmtree(d)
                shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


@app.route("/")
def index():
    posts = [page for page in pages if "date" in page.meta]
    sorted_posts = sorted(posts, reverse=True, key=lambda page: page.meta["date"])
    return render_template("index.html", pages=sorted_posts)


@app.route("/about/")
def about():
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
        "--build",
        action="store_true",
        help="Freezes flask application into build directory",
    )
    parser.add_argument(
        "--live",
        action="store_true",
        default=False,
        help="Freezes flask application and builds to github directory",
    )
    parser.add_argument(
        "--path",
        default=os.path.join(Path().resolve().parent, "spencerbraun.github.io"),
        help="build live version to custom path",
    )
    args = parser.parse_args()

    if args.build:
        freezer.freeze()
    elif args.live:
        customcopy("build", args.path)
    else:
        app.run(host="localhost", port=8000)


if __name__ == "__main__":
    main()
