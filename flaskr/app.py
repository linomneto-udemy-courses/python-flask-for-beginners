#!python3

from flask import Flask, request, render_template
from classes.Calculator import Calculator

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=["POST"])
def calculate():
    n1 = float(request.form.get("n1"))
    n2 = float(request.form.get("n2"))
    op = request.form.get("op")
    calc = Calculator(n1, op, n2)
    calc.run()
    return str(calc.result)

app.run()