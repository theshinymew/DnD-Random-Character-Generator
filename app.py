from flask import Flask, render_template, request, redirect
import requests
import json
import random
app = Flask(__name__, static_url_path='/static')
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/character/", methods = ["POST"])
def character():
    with open("static/CharacterData.json") as loop:
        character = json.load(loop)

    player_race = random.choice(character["playerRaces"])
    player_class = random.choice(character["playerClasses"])
    return render_template("character.html", race = player_race, class_and_level = (player_class + " 1"))

if __name__ == '__main__':
    app.run