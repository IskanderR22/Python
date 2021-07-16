
import re
from flask import Flask,render_template, redirect, request

from flask_app import app   

from flask_app.models.user import User # Importing the MODEL and the class Dog


@app.route("/")
def index():
    return render_template("index.html", all_users = User.get_all()) 


@app.route("/new/user", methods = ['POST'])
def new_user():
    newest_user = User.create(request.form)

    
    return redirect(f'/user/{newest_user}')


@app.route("/create/user")
def create_user():

    return render_template("create_new_user.html")


# Every function  expect for get_all() requires a dictionary 
@app.route('/user/<int:user_id>')
def display_user(user_id):
    return render_template("one_user.html", user = User.get_one({"id": user_id}))



# This displays the form to edit a User
@app.route("/edit/<int:user_id>")
def edit_user(user_id):
    return render_template("edit_user.html", user = User.get_one({"id": user_id})) 


# Performs the UPDATE process
@app.route("/edit/<int:user_id>/update", methods = ['POST'])
def update_user(user_id):
    new_dict = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        'id': user_id
    }
    print(new_dict)
    User.update(new_dict) # Make sure to pass the new dictionary with the ID number

    return redirect("/")


# Performs the DELETE process
@app.route("/delete/user/<int:user_id>")
def delete(user_id):
    User.delete({"id": user_id})
    return redirect("/")



