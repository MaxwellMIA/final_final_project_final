# Before game functions
import time

def slowprint(text, delay=0):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# starting zone

slowprint("~~GAME NAME~~")

name = input("What is your name? ").capitalize()
if name == "Scarlet":
    slowprint("Sorry, that names not available")

def print_day(day):
    if day == 1:
        slowprint("intro stuff and name and quest for day one and four")
        slowprint("You open your eyes, ")
        time.sleep(0.3)
    if day == 2:
        slowprint("quest for day two and four")
    if day == 3:
        slowprint("quest for day three and four")
    if day == 4:
        if day == 4:
            slowprint("You wake up, looking at your calendar.")
            time.sleep(0.3)
            slowprint("It's the 7th. Today is finally the day.")
            time.sleep(0.3)
            slowprint("You grab your bag as you make your way to the front door.")
            time.sleep(0.3)
            slowprint("You can barely step outside before you hear your name being called.")
            time.sleep(0.3)
            slowprint(f"'{name}! I haven't seen you in forever!'")
            time.sleep(0.3)
            slowprint("You look up at Scarlet, a smile slowly showing on your face.")
            time.sleep(0.3)
            slowprint("Scarlet makes her way up to you, standing face to face in the matter of seconds.")
            time.sleep(0.3)

        if gift == "none":
            slowprint("'Do you know what day it is?' She beamed, looking at you with hope.")
            time.sleep(0.3)
            slowprint("Your smile quickly turns to a frown before you can stop yourself.")
            time.sleep(0.3)
            slowprint("'Oh, yah.'")
            time.sleep(0.3)
            slowprint("You notice Scarlets shoulders slump, despite how upbeat she trys to stay.")
            time.sleep(0.3)
            slowprint("She opens her mouth to say something, but she changes her mind before she can.")
            time.sleep(0.3)
            slowprint("There's an uncomfortable pause between you two, before she lets out a sigh.")
            time.sleep(0.3)
            slowprint("'Well, atleast I got to finally see you.'")
            time.sleep(0.3)
            slowprint("Before you gain the courage to say anything she turns and leaves.")
            time.sleep(0.3)
            slowprint("You watch helplessly as she walks to her car, looking glum as she drives away.")
            time.sleep(0.3)
            slowprint("You make your way back inside, the sound of rain starts up as you make your way back into the house.")
            time.sleep(0.3)
            slowprint("You to your bedroom, tossing your bag to the floor as you slump onto your bed.")
            time.sleep(1)
            slowprint("You lay there for a while, at least it feels that way.")
            time.sleep(0.3)
            slowprint("You hear your computer beep, but you don't bother to look at it.")
            time.sleep(0.3)
            slowprint("Theres always next year.")
            time.sleep(0.3)
            slowprint("Ending 1")
            slowprint("Giftless and lonely")

        if gift == "Necklace" or gift == "Silver earrings":
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            time.sleep(0.3)
            slowprint("")
            
        if gift == "book":
            slowprint("hi")

class Area:
    def __init__(self, name, description, exits, look, interact):
        self.name = name
        self.description = description
        self.exits = exits
        self.look = look
        self.interact = interact
 
def print_area(current_area):
    slowprint(f"You are in the {current_area.name}.")
    slowprint(current_area.description)
    
    slowprint("What would you like to do?")
    command = input("~Travel, Look, Interact, stats~ ").lower()

    if command == "travel":
        slowprint("Where do you want to go?")
        command = input(f"~{current_area.exits}, back~ ").lower()
        if command == "bedroom" and current_area == hallway:
            current_area = bedroom
            slowprint(f"You walk to your bedroom")
            print_area(current_area)

        if command == "hallway" and (current_area == bedroom or current_area == bathroom or current_area == stairs):
            current_area = hallway
            slowprint(f"You walk to the hallway")
            print_area(current_area)

        if command == "bathroom" and current_area == hallway:
            current_area = bathroom
            slowprint(f"You walk to the bathroom")
            print_area(current_area)

        if command == "stairs" and (current_area == hallway or current_area == livingroom):
            current_area = stairs
            slowprint(f"You walk to the stairs")
            print_area(current_area)

        if command == "living room" and (current_area == stairs or current_area == kitchen or current_area == yard or current_area == frontdoor):
            current_area = livingroom
            slowprint(f"You walk to the living room")
            print_area(current_area)

        if command == "kitchen" and current_area == livingroom:
            current_area = kitchen
            slowprint(f"You walk to the kitchen")
            print_area(current_area)

        if command == "yard" and current_area == livingroom:
            if yardkey == True:
                current_area = yard
                slowprint(f"You walk to out to the yard")
                print_area(current_area)
            else:
                slowprint(f"You go to back door, but you realize you don't have your key.")
                slowprint(f"You'll need to find your key first before going out back.")
                print_area(livingroom)

        if command == "front door" and current_area == livingroom:
            current_area = frontdoor
            slowprint(f"You walk to your front door")
            print_area(current_area)

        if command == "back":
            print_area(current_area)

        if command != "bedroom" or command != "bathroom" or command != "hallway" or command != "stairs" or command != "living room" or command != "kitchen" or command != "yard" or command != "front door":
            print_area(current_area)

    if command == "look":
        slowprint(current_area.look)
        print_area(current_area)

    if command == "interact":
        slowprint(current_area.interact)

    if command == "stats":
        slowprint(f"{name}'s stats. Health:{player_stats['Health']} Stress:{player_stats['Stress']} Money:{player_stats['Money']}")


# Areas

bedroom = Area("Bedroom", "It's your bedroom. It seems messier then it was yesterday.", "Hallway", "It's your childhood bedroom, the walls have faded in color over the years. Trash litters your desk and the floor, while your bed is covered in dirty clothes you haven't feel like moving.", "Bed, Computer, Bookshelf")

hallway = Area("Hallway", "A short hallway.", "Bedroom, Bathroom, Stairs", "There is spots of paint missing from the wall where paintings used to hang. Most of the photos got taken down after the divorce", "Plant")

bathroom = Area("Bathroom", "A plain bathroom. It's cleaner then your room.", "Hallway", "The mirror on the wall taunts you, you feel a wave of dread come over you.", "Mirror")

stairs = Area("Stairs", "You're always afriad of slipping", "Hallway, Living room", "You look at the painting on the wall, but you don't know what it is.", "Painting")

livingroom = Area("Living room", "The living room seems darker then normal.", "Stairs, Kitchen, Yard, frontdoor", "Livingroomlook", "Livingroominteract")

kitchen = Area("Kitchen", "walking in", "living room", "look", "interact")

yard = Area("Yard", "walking in", "exits", "living room", "interact")

frontdoor = Area("Front door", "walking in", "living room, plaza", "look", "interact")

# Key and non-key items

yardkey = True
gift = "none"

invsalad = False
invsteak = False

# Changing variables

player_stats = {"Health": 100, "Stress": 0, "Money": 50}
inventory = "empty"

day = 1
current_area = bedroom
print_day(day)
print_area(current_area)