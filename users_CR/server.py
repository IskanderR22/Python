

import re
from flask import Flask, app, render_template, redirect, request

from user import User # Importing the MODEL and the class Dog


app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route("/")
def index():
    return render_template("index.html", all_users = User.get_all()) 


@app.route("/new/user", methods = ['POST'])
def new_user():
    User.create(request.form)
    return redirect('/')

@app.route("/create/user")
def create_user():
    return render_template("create_new_user.html")

# Every function  expect for get_all() requires a dictionary 
@app.route('/user/<int:user_id>')
def display_user(user_id):
    return render_template("one_user.html", user = User.get_one({"id": user_id}))



if __name__ == "__main__":
    app.run(debug=True)