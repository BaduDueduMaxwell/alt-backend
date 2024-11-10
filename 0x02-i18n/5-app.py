#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask, render_template, request, g


app = Flask(__name__)

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


@app.route('/')
def index():
    """Render the index template with user data."""
    return render_template("5-index.html")
