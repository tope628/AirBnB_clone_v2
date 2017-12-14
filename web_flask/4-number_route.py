#!/usr/bin/python3
""" Flask application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """greetings hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """greetings hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """C blank"""
    text2 = text.replace("_", " ")
    return 'C %s' % text2


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text='is cool'):
    """Python is blank"""
    text2 = text.replace("_", " ")
    return 'Python %s' % text2


@app.route('/number/<int:n>', strict_slashes=False)
def numbers(n):
    """N as int"""
    return '%s is a number' % n

if __name__ == '__main__':
    app.run(host="0.0.0.0")
