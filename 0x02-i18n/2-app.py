#!/usr/bin/env python3
"""  Get locale from request """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ configure available languages """
    LANGUAGES =  ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route("/")
def index():
    """ display content of 2-index.html """
    return render_template("2-index.html")


@babel.localeselector
def get_locale():
    """ determine the best match with our supported languages. """
    return request.accept_languages.best_match(Config.LANGUAGES)


if __name__ == "__main__":
    app.run(debug=True)
