#!/usr/bin/env python3
"""
A Flask application configured with Flask-Babel for i18n support.
Includes a mock user login system.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict


class Config:
    """
    Configuration class for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


app: Flask = Flask(__name__)
app.config.from_object(Config)

babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Select the best match for supported languages.

    Returns:
        str: The best match for supported languages.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Optional[Dict[str, str]]:
    """
    Get user information based on the login_as parameter.

    Returns:
        dict: User information or None if not found.
    """
    try:
        user_id = int(request.args.get('login_as'))
    except (TypeError, ValueError):
        return None
    return users.get(user_id)


@app.before_request
def before_request() -> None:
    """
    Executed before each request to find the logged-in user.
    """
    g.user = get_user()


@app.route('/')
def index() -> str:
    """
    Route that renders the index page.

    Returns:
        str: The rendered HTML content of the index page.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(debug=True)
