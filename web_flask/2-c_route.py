#!/usr/bin/python3
"""Module with a flask script"""
from flask import Flask, escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Module that returns Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Module that returns HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Module that display the content of variable text"""
    text = escape(text.replace("_", " "))
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
