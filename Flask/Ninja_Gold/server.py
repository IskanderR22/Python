from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe."

@app.route("/")
def index():
    if "newGold" not in session:
        session['newGold'] = 0
    if "goldCount" not in session:
        session['goldCount'] = 0
    return render_template("index.html")


@app.route("/getrich", methods = ["POST"])
def get_rich():
    if request.form['source'] == 'farm':
        session['currentGold'] = session['goldCount']
        session['newGold'] = random.randint(10,20)
        session['goldCount'] += session['newGold']
    if request.form['source'] == 'cave':
        session['currentGold'] = session['goldCount']
        session['newGold'] = random.randint(5,10)
        session['goldCount'] += session['newGold']
    if request.form['source'] == 'house':
        session['currentGold'] = session['goldCount']
        session['newGold'] = random.randint(2,5)
        session['goldCount'] += session['newGold']
    if request.form['source'] == 'casino':
        session['currentGold'] = session['goldCount']
        session['newGold'] = random.randint(-50,50)
        session['goldCount'] += session['newGold']
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)