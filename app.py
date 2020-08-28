from flask import Flask, render_template, request, redirect
import requests
import json
import random
from static import character_generator
app = Flask(__name__, static_url_path='/static')
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/character/", methods = ["POST"])
def character():
    pc = character_generator.PlayerCharacter()
    
    return render_template("character.html", race = pc.pc_race, class_and_level = (pc.pc_class + " 1"), 
                           strength = pc.pc_stats["Strength"], dexterity = pc.pc_stats["Dexterity"], 
                           constitution = pc.pc_stats["Constitution"], intelligence = pc.pc_stats["Intelligence"],
                           wisdom = pc.pc_stats["Wisdom"], charisma = pc.pc_stats["Charisma"])

if __name__ == '__main__':
    app.run