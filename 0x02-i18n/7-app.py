#!/usr/bin/env python3
"""
A Flask application configured with Flask-Babel for i18n support.
Includes a mock user login system.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional
import pytz


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
    Select the best match for supported languages based on user preferences.

    Returns:
        str: The best match for supported languages.
    """
    # Check locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # Check locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Select the time zone based on user preferences or default to UTC.

    Returns:
        str: The selected time zone.
    """
    # Check timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Check timezone from user settings
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    # Default to UTC
    return 'UTC'


def get_user() -> Optional[dict]:
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
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(debug=True)
