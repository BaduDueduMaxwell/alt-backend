#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Retrieve a user dictionary by ID or return None if not found."""
    try:
        return users.get(int(user_id))
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Set g.user to the logged-in user if login_as is in the request args."""
    user_id = request.args.get("login_as")
    g.user = get_user(user_id)

    # Set a default locale based on the user or the default to 'en'
    g.locale = g.user['locale'] if g.user and g.user.get('locale') else 'en'


@app.route('/')
def index():
    """Render the index template with user data."""
    return render_template("6-index.html")


def get_locale():
    """Get user's preferred local if it is supported
    The order of priority should be:
        1 - Locale from URL parameters
        2 - Locale from user settings
        3 - Locale from request header
        4 - Default locale
    """

    # Get locale from URL parameters (highest priority)
    locale = request.args.get('locale')
    if locale:
        return locale

    # Get local from user settings
    if g.user and g.user.get('locale'):
        return g.user['locale']

    # Get local from request headers
    user_language = request.accept_languages.best_match(
        ['en', 'fr', 'kg', 'es']
    )
    if user_language:
        return user_language

    return 'en'
