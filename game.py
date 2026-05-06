# Before game functions
import time

def slowprint(text, delay=0.07):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# starting zone

slowprint("~~GAME NAME~~")

name = input("What is your name? ").capitalize()
if name == "Scarlet":
    slowprint("Sorry, that names not available")

class Area:
    def __init__(self, name, description, exits, look, interact):
        self.name = name
        self.description = description
        self.exits = exits
        self.look = look
        self.interact = interact
 
def print_area(self):
    slowprint(f"You are in the {self.name}.")
    slowprint(self.description)
    #!!!!!!!!!!reask from here
    slowprint("What would you like to do?")
    command = input("~Travel, Look, Interact, stats~ ").lower()

    if command == "travel":
        slowprint("Where do you want to go?")
        command = input(f"~{self.exits}, back~ ").lower()
        if command == self.exits:
            slowprint(f"You walk to {self.exits}")
            current_area = {self.exits}
        if command == "back":
            print("hi")

    if command == "look":
        slowprint(self.look)
        # make it avaible to redo Nhe "what would you like to do" to run though these 3 if statments again

    if command == "interact":
        slowprint(self.interact)

    if command == "stats":
        slowprint(f"{name}'s stats. Health:{player_stats['Health']} Stress:{player_stats['Stress']} Money:{player_stats['Money']}")

# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Lucy", 5)

bedroom = Area("Bedroom", "It's your bedroom. It seems messier then it was yesterday.", "Hallway", "It's your childhood bedroom, the walls have faded in color over the years. Trash litters your desk and the floor, while your bed is covered in dirty clothes you haven't feel like moving.", "Bed, Computer, Bookshelf")

hallway = Area("Hallway", "A short hallway.", "Bedroom, Bathroom, Stairs", "There is spots of paint missing from the wall where paintings used to hang. Most of the photos got taken down after the divorce", "Plant")

bathroom = Area("Bathroom", "A plain bathroom. It's cleaner then your room.", "Hallway", "The mirror on the wall taunts you, you feel a wave of dread come over you.", "Mirror")

stairs = Area("Stairs", "You're always afriad of slipping", "Hallway, Living room", "You look at the painting on the wall, but you don't know what it is.", "Painting")

livingroom = Area("Living room", "The living room seems darker then normal.", "Stairs, Kitchen, Yard,", "Livingroomlook", "Livingroominteract")



player_stats = {"Health": 100, "Stress": 0, "Money": 50}
day = 1
current_area = bedroom
print_area(current_area)