from os import name
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."


# The default request method is a GET Request
@app.route("/")
def index():
    return render_template("index.html")


# This will be the POST method route
@app.route("/process", methods = ["POST"])
def dojo_Survey():
    print(request.form) 
    # request.form is a dictionary
    # keys and values
    # session is dictionary
    session['name'] = request.form['name']
    session['locations'] =request.form['locations']
    session['language'] =request.form['language']
    session['comments_optional'] =request.form['comments_optional'] 
    return redirect("/result") # redirect makes a new GET request to a different route



@app.route('/result')
def display_result():
        return render_template("result.html")



if __name__ == "__main__":
    app.run(debug = True)