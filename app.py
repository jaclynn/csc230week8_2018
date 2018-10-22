from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    weather = "sunny"
    rainy=True
    names = ["Bob", "Mary", "Bart", "Kathy", "Susan", "Stanley"]
    return render_template("home.html",users=names, weather = weather, rainy=rainy)

@app.route('/about')
def about():
    return render_template("about.html")

app.run('0.0.0.0',port='8080')