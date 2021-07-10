
import re
from flask import Flask
from flask.templating import render_template


app = Flask(__name__) 

# @app.route('/')          # The "@" decorator associates this route with the function immediately following
# def hello_world():
#     return 'Hello World!'

# @app.route('/play')
# def hello():
#     return render_template("index.html")

# @app.route('/play/<int:x>')
# def add(x):
#     return render_template('index.html', x = x)
@app.route('/')
@app.route('/play')
@app.route('/play/<int:x>')
@app.route('/play/<int:x>/<string:color>')
def color(x = 3, color = "blue"):
    return render_template('index.html', x = x, color = color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.