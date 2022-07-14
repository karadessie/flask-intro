"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Start Here</title>
      </head>
      <body>
          What page would you like?
          <p></p>
          <form action="/hello" method='GET'>
          <a href="/hello">Take me to the compliment page</a>
           <input type="submit" value="Submit">
          </form>
          <p></p>
          <form action="/hello-diss" method='GET'>
          <a href="/hello-diss">Take me to the disrespect page</a>
          <input type="submit" value="Submit">
          </form>
      </body>
    </html>
    """

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet" method='GET'>
          What's your name? <input type="text" name="person">
          What compliment would you like?
          <p>
          <input type="radio" name="compliment" value="awesome">Awesome<br>
          <input type="radio" name="compliment" value="terrific">Terrific<br>
          <input type="radio" name="compliment" value="fantastic">Fantastic<br>
          <input type="radio" name="compliment" value="neato">Neato<br>
          <input type="radio" name="compliment" value="fantabulous">Fantabulous<br>
          <input type="radio" name="compliment" value="wowza">Wowza<br>
          <input type="radio" name="compliment" value="oh-so-not-meh">Oh-so-not-meh<br>
          <input type="radio" name="compliment" value="brilliant">Brilliant<br>
          <input type="radio" name="compliment" value="ducky">Ducky<br>
          <input type="radio" name="compliment" value="coolio">Coolio<br>
          <input type="radio" name="compliment" value="incredible">Incredible<br>
          <input type="radio" name="compliment" value="wonderful">Wonderful<br>
          <input type="radio" name="compliment" value="smashing">Smashing<br>
          <input type="radio" name="compliment" value="lovely">Lovely<br>
          </p>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """
@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """
@app.route('/hello-diss')
def say_hello_diss():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss" method='GET'>
          What's your name? <input type="text" name="person">
          What diss would you like?
          <p>
          <input type="radio" name="disrespect" value="gross">Gross<br>
          <input type="radio" name="disrespect" value="lousy">Lousy<br>
          <input type="radio" name="disrespect" value="stupid">Stupid<br>
          <input type="radio" name="disrespect" value="lame">Lame<br>
          <input type="radio" name="disrespect" value="pond scum">Pond Scum<br>
          <input type="radio" name="disrespect" value="meh">Meh<br>
          <input type="radio" name="disrespect" value="boring">Boring<br>
          <input type="radio" name="disrespect" value="annoying">Annoying<br>
          <input type="radio" name="disrespect" value="childish">Childish<br>
          <input type="radio" name="disrespect" value="rat fink">Rat Fink<br>
          <input type="radio" name="disrespect" value="infantile">Infantile<br>
          <input type="radio" name="disrespect" value="worthless">Worthless<br>
          <input type="radio" name="disrespect" value="airhead">Airhead<br>
          <input type="radio" name="disrespect" value="blockhead">Blockhead<br>
          </p>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    disrespect = request.args.get("disrespect")

    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Disrespect</title>
      </head>
      <body>
        Hi, {player}! I think you're {disrespect}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")