name = "health stress cost"
salad = "+20 -10 10"
steak = "-40 +20 0"

class Shop:
    def __init__(self, itemname, cost):
        self.itemname = itemname
        self.cost = cost

class Inv:
    def __init__(self, itemname2, health, stress):
        self.itemname2 = itemname2
        self.health = health
        self.stress = stress

shopsalad = Shop("Sports store", "walking in", "plaza", "look", "interact")




if {player_stats['Health']} == 0:
    print("You died.")

if {player_stats['Stress']} == 100:
    print("you died")