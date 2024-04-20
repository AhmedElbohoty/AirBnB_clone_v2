#!/usr/bin/python3
'''
script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
    - /: display “Hello HBNB!”
    - /hbnb: display “HBNB”
    - /c/<text>: display “C ” followed by the value of the text variable
      (replace underscore _ symbols with a space)
    - /python/<text>: display “Python ”, followed by the value of the text
      variable (replace underscore _ symbols with a space)
      The default value of text is “is cool”
    - /number/<n>: display “n is a number” only if n is an integer
    - /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
'''

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Display “Hello HBNB!”'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display "HBNB”'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    '''Display “C ” followed by the value of the text variable
      (replace underscore _ symbols with a space )
    '''
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    '''Display “Python ”, followed by the value of the text'''
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''Display “n is a number” only if n is an integer'''
    return f"{n:d} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY'''
    if not isinstance(n, int):
        return ""
    return render_template('5-number.html', number=number)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
