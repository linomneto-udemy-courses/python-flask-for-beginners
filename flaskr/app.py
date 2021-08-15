#!python3

from flask import Flask, request, render_template, session, redirect
from classes.Calculator import Calculator

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = "simpleCalculator"

@app.route('/reset')
def reset():
    session.clear()
    return redirect("/")

@app.route('/')
def index():
    if ("historic" in session):
        return render_template("index.html", historic = session["historic"])
    else:
        return render_template("index.html")

@app.route('/calculate', methods=["POST"])
def calculate():
    n1 = float(request.form.get("n1"))
    n2 = float(request.form.get("n2"))
    op = request.form.get("op")
    calc = Calculator(n1, op, n2)
    calc.run()
    calcToHistoric(calc)
    return redirect("/")

def calcToHistoric(calc):
    list = []
    if not("historic" in session):
        session["historic"] = list
    else:
        list = session["historic"] 
    item = { "n1": calc.n1, "op": calc.op, "n2": calc.n2, "result": calc.result }
    list.insert(0, item)
    session["historic"] = list

app.run()