#!/usr/bin/env python3
"""
A Flask application configured with Flask-Babel for i18n support.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)

babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages.

    Returns:
        str: The best match language.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Route that renders the index page.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
