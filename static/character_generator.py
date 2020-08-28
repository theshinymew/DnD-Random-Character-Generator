import random
import json

class PlayerCharacter:
    standard_array = [15, 14, 13, 12, 10, 8]

    def __init__(self):
        self.pc_stats = self.generateStats()

        with open("static/player_races.json") as races:
            racedata = json.load(races)
        
        with open("static/player_classes.json") as classes:
            classdata = json.load(classes)

        self.pc_race = random.choice(list(racedata))
        self.pc_class = random.choice(list(classdata))
        
    def generateStats(self) -> dict:
        keys = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
        stats = [sum(sorted([random.randint(1,6) for x in range(4)])[1:]) for y in range(6)]
        return dict(zip(keys, stats))