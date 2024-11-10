from flask import Flask, render_template, g, request
from flask_babel import Babel, _
import pytz
from datetime import datetime
from pytz.exceptions import UnknownTimeZoneError

app = Flask(__name__)
babel = Babel(app)

# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """Set user and locale before each request"""
    user_id = request.args.get('login_as', type=int)
    if user_id:
        user = users.get(user_id)
        if user:
            g.user = user
            g.locale = user.get("locale", "en")
            g.timezone = user.get("timezone", "UTC")
        else:
            g.user = None
            g.locale = "en"
            g.timezone = "UTC"
    else:
        g.user = None
        g.locale = "en"
        g.timezone = "UTC"


def get_locale():
    """Get the locale based on user settings or the query parameter"""
    return g.locale or request.accept_languages.best_match(
        ['en', 'fr', 'kg', 'es'])


def get_timezone():
    """Get the timezone based on user settings or URL parameter"""
    try:
        # Validate and return timezone
        tz = pytz.timezone(g.timezone)
        return tz
    except UnknownTimeZoneError:
        return pytz.UTC  # Default to UTC if timezone is invalid


babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)


@app.route('/')
def index():
    """Home page displaying user info and current time in local timezone"""
    current_time = datetime.now(
        get_timezone()).strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=current_time)


if __name__ == "__main__":
    app.run(debug=True)
