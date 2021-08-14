#!python3

from flask import Flask, request, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/calculate', methods=["POST"])
def calculate():
    return "calculate method"

app.run()