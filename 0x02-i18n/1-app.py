#!/usr/bin/env python3
""" Task 1 """
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """Languages class"""
    LANGUAGES = ["en", "fr"]
    Babel_locale = "en"
    Babel_timezone = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)

@app.route("/")
def welcomephrase():
    """ Hello page """
    return render_template('1-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
