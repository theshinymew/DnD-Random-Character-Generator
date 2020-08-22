from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__, static_url_path='/static')
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/character/", methods = ["POST"])
def character():
    class_and_level = "Mage"
    class_background = ""
    race = "Mudkip"
    alignment = ""
    return render_template("character.html", 
    class_and_level = class_and_level,
    class_background = class_background, 
    race = race,
    alignment = alignment)

if __name__ == '__main__':
    app.run