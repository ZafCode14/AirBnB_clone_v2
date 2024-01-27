"""Module with a flask script"""
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Method that returns Hello HBNB"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Method that returns HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Method that returns a strig with a variable"""
    text = escape(text.replace("_", " "))
    return "C {}".format(text)

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python/", strict_slashes=False, defaults={"text": "is_cool"})
def python_text(text):
    """Method that returns a string with a variable"""
    text = escape(text.replace("_", " "))
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Method that returns a string with a number"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number_template(n):
    """Method that returns a template"""
    return render_template("5-number.html", number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_odd_or_even(n):
    """Method that returns a template"""
    return render_template("6-number_odd_or_even.html", number=n)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
