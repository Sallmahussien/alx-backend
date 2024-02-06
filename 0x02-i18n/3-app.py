#!/usr/bin/env python3
"""Defines flask app"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Function to get the locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """Render 3-index.html"""
    home_title = gettext('home_title')
    return render_template('3-index.html', home_title=home_title)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
