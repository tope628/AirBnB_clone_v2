#!/usr/bin/python3
""" Flask application"""
from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """N as int"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """N as int"""
    eo = 'odd'
    if n % 2 == 0:
        eo = 'even'
    return render_template('6-number_odd_or_even.html', n=n, eo=eo)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
