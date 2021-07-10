


from flask import Flask # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response


@app.route('/dojo')
def dojo():
    return 'Dojo!'
    
@app.route('/flask')
def flask():
    flask = "Hi Flask!"
    print(type(flask))
    return flask

@app.route('/micheal')
def micheal():
    micheal = "Hi Micheal"
    print(type(micheal))
    return micheal
    
@app.route('/john')
def john():
    john = "Hi John!"
    print(type(john))
    return john

@app.route('/repeat/<int:num>/name')
def repeat_35(num):

    return 'Hello!' * num

@app.route('/repeat/<int:num>/bye')
def repeat_80(num):
    return 'Bye' * num

@app.route('/repeat/<int:num>/dogs')
def repeat_90(num):
    return 'Dogs' * num

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.


