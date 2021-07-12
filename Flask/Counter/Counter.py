from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

app.secret_key = "This is to keep a session"


@app.route('/')
def index():
    session['amount'] += 1 # Session is a dictionary and we are setting a key with the value += 1

    return render_template("index.html")

@app.route('/destroy_session')
def reset():
    session.clear()		# clears all keys
    session['amount'] = 0
    # session.pop('secret_key')
    return render_template('index.html')




if __name__=="__main__":      
    app.run(debug=True)    # Run the app in debug mode.