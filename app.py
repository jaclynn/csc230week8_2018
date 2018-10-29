import requests
from flask import Flask, render_template

weatherapi = "8ad8c7132e7c59ef510f95727999c43e"
response = requests.get("https://samples.openweathermap.org/data/2.5/weather?zip=21901,us&appid="+weatherapi)
weather = response.json()
htmlweather = weather["weather"][0]["description"].title()
temp = int((weather["main"]["temp"]-273.15)*9/5+32)
print(temp)
print(htmlweather)

app = Flask(__name__)

@app.route('/')
def index():
    names = ["Bob", "Mary", "Bart", "Kathy", "Susan", "Stanley"]
    return render_template("home.html",users=names, weather = htmlweather, temp=temp)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/chat')
def chat():

    return render_template("chat.html")

app.run('0.0.0.0',port='8080')