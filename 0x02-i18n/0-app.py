#!/usr/bin/env python3
"""
A basic Flask application that serves a simple web page.
"""

from flask import Flask, render_template

app: Flask = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Route that renders the index page.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
