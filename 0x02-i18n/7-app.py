#!/usr/bin/env python3
"""
A Flask application that handles timezone selection.
"""

from flask import Flask, request, g
from flask_babel import Babel
import pytz
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Retrieve a user from the users dictionary
    based on the login_as parameter."""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@babel.timezoneselector
def get_timezone():
    """Determine the best timezone to use based
    on URL parameter, user settings, or default to UTC."""
    # 1. Check for timezone in URL parameters
    tz_param = request.args.get('timezone')
    if tz_param:
        try:
            # Validate the timezone
            return pytz.timezone(tz_param).zone
        except UnknownTimeZoneError:
            pass  # Continue to the next source

    # 2. Check user settings for a timezone
    if g.user and g.user.get("timezone"):
        try:
            # Validate the user's timezone setting
            return pytz.timezone(g.user["timezone"]).zone
        except UnknownTimeZoneError:
            pass  # Continue to the default

    # 3. Default to UTC
    return "UTC"


@app.before_request
def before_request():
    """Set user and other global variables before handling the request."""
    g.user = get_user()


@app.route('/')
def index():
    """Display a simple HTML page with a greeting and user info."""
    return render_template('7-index.html')


if __name__ == "__main__":
    app.run()
