#!/usr/bin/env python

from flask import render_template
from app2 import app, pages, freezer

@app.route('/')
def index():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)

@app.route('/<path:path>/')
def page(path):
    # `path` is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
#
# @freezer.register_generator
# def product_details():
#     for product in pages.all():
#         yield {'path': pages.path}
