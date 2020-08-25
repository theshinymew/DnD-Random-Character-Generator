import random
import json

class PlayerCharacter:
    standard_array = [15, 14, 13, 12, 10, 8]

    def __init__(self):
        self.pc_stats = self.generateStats()

        with open("static/CharacterData.json") as json_file:
            data = json.load(json_file)

        self.pc_race = random.choice(data["playerRaces"])
        self.pc_class = random.choice(data["playerClasses"])
        
    def generateStats(self) -> list:
        stats = []
        for i in range(6):
            stat_min = 7
            stat_sum = 0
            for j in range(4):
                n = random.randint(1, 6)
                if n < stat_min:
                    stat_min = n
                stat_sum += n
            s = stat_sum - stat_min
            if s < 6:
                stats = standard_array
                random.shuffle(stats)
                return stats
            else:
                stats.append(s)

        return stats

mychar = PlayerCharacter()

print(mychar.pc_stats)
print(mychar.pc_class)
print(mychar.pc_race)