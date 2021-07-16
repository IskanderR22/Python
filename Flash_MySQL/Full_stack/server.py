from flask import Flask, app, render_template, redirect, request

from dog import Dog # Importing the MODEL and the class Dog


app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


# Displays all dogs
@app.route("/")
def index():
    return render_template("index.html", all_dogs = Dog.get_all()) 

# Displays the form to create a new dog
@app.route("/dogs/new")
def new_dog():
    return render_template("new_dog.html")

# Performs the action of creating a new dog
@app.route("/dogs/create", methods = ['POST'])
def create_dog():
    # print(request.form)
    Dog.create(request.form)

    return redirect("/") # ALWAYS REDIRECT IN A POST ROUTE

# This one displays a single dog
@app.route('/dogs/<int:dog_id>')
def display_dog(dog_id):
    return render_template("dog.html", dog = Dog.get_one({"id": dog_id}))


# Displays the page to update a dog
@app.route("/dogs/<int:dog_id>/edit")
def edit_dog_form(dog_id):
    return render_template("edit_dog.html", id = dog_id)


# Perform the action of update a single dog
@app.route("/dogs/<int: dog_id>/update", methods = ["POST"])
def update_dog(dog_id):
    new_dict = {
        "name": request.form['name'],
        "age": request.form['age'],
        "hair_color": request.form['hair_color'],
        "id": dog_id
    }

    Dog.update(request.form)

    return redirect("/")


# Perform the action of deleting a single dog
@app.route("dogs/<int:dog_id>/delete")
def delete_dog(dog_id):
    Dog.delete({"id": dog_id})
    return redirect("/")
    

if __name__ == "__main__":
    app.run(debug=True)