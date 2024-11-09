#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Config class to configure available languages"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate Flask app, set config, and initialize Babel
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Function to determine the best match with supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Route to render the index page"""
    return render_template('3-index.html', title=_('home_title'))


if __name__ == "__main__":
    app.run(debug=True)
