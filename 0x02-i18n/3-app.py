#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask import Flask, render_template
from flask_babel import Babel, _


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@app.route('/')
def home():
    """Route to render 3-index.html"""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
