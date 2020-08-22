from flask import Flask, render_template, request, redirect
import requests
app = Flask(__name__, static_url_path='/static')
@app.route("/")
def index():
    return render_template("index.html", pstyleColor = "#F3EFE0", style = "display:none")
@app.route("/character/", methods = ["POST"])
def character():
    class_and_level = "Mage"
    class_background = ""
    player_name = "Mudkip_warrior_69"
    race = "Mudkip"
    alignment = ""
    return render_template("character.html", 
    class_and_level = class_and_level,
    class_background = class_background, 
    player_name = player_name,
    race = race,
    alignment = alignment)

if __name__ == '__main__':
    app.run