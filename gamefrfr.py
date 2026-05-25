import time
def slowprint(text, delay=0): #0.07
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class Area:
    def __init__(self, name, description, look="", interact=""):
        self.name = name
        self.description = description
        self.look = look
        self.interact = interact
        self.exits = {}

    def moving(self, direction, area, locked=False, key=None):
        self.exits[direction.lower()] = {
            "area": area,
            "locked": locked,
            "key": key
        }

#----------------------------------------------------------------------- Variables

game = {
    "day": 1,
    "inventory": [],
    "gift": "none",
    "stats": {"health": 100, "stress": 0, "money": 50},
    "flags": {
        "photo_album": True,
        "drawer_money": True,
    }
}

#----------------------------------------------------------------------- areas 

bedroom = Area(
    "Bedroom",
    "It's your messy childhood bedroom.",
    look = "",
    interact = ""
)

hallway = Area(
    "Hallway",
    "A narrow hallway with faded walls.",
    look = "",
    interact = ""
)

bathroom = Area(
    "Bathroom",
    "A plain bathroom.",
    look = "",
    interact = ""
)

stairs = Area(
    "Stairs",
    "You're always afraid of slipping.",
    look = "",
    interact = ""
)

livingroom = Area(
    "Living Room",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

kitchen = Area(
    "kitchen",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

yard = Area(
    "yard",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

frontdoor = Area(
    "frontdoor",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

plaza = Area(
    "plaza",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

park = Area(
    "park",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

grocery = Area(
    "grocery",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

jewelry = Area(
    "jewelry",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

sports = Area(
    "sports",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

field = Area(
    "field",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

woods = Area(
    "woods",
    "The TV hasn't been turned on in days.",
    look = "",
    interact = ""
)

#------------------------ traveling 

bedroom.moving("hallway", hallway)
hallway.moving("bedroom", bedroom)
hallway.moving("bathroom", bathroom)
hallway.moving("stairs", stairs)
bathroom.moving("hallway", hallway)
stairs.moving("hallway", hallway)
stairs.moving("living room", livingroom)
livingroom.moving("stairs", stairs)
livingroom.moving("kitchen", kitchen)
livingroom.moving("yard", yard, locked=True, key="yard key")
livingroom.moving("front door", frontdoor)
kitchen.moving("living room", livingroom)
yard.moving("living room", livingroom)
frontdoor.moving("living room", livingroom)
frontdoor.moving("plaza", plaza)
plaza.moving("home", frontdoor)
plaza.moving("park", park)
plaza.moving("grocery store", grocery)
plaza.moving("jewelry store", jewelry)
plaza.moving("sports store", sports)
park.moving("plaza", plaza)
park.moving("field", field)
field.moving("park", park)
field.moving("woods", woods)
woods.moving("field", field)
grocery.moving("plaza", plaza)
jewelry.moving("plaza", plaza)
sports.moving("plaza", plaza)

slowprint("~~Starting game~~")

def naming():
    while True:
        name = input("What is your name? ").capitalize()
        if name == "Scarlet":
            slowprint("I'm glad you still think of me, but you can't use my name!")
        else:
            return name
        
playername = naming()

def print_day(day, gift, name):
    if day == 1:
        slowprint("Day one.")
        slowprint("Three days left.")
        slowprint("You open your eyes, looking at the ceiling above you.")
        slowprint("You slowly sit up, rubbing your eyes.")
        slowprint("You look over at your calendar, frowning as you see what the date is.")
        slowprint("It's the eighth, and Scarlet's birthday is the eleventh.")
        slowprint("You promised her you would meet up with her, but you want to get a gift before then.")
        slowprint("But first, you need something to eat.")
        slowprint("Goals:")
        slowprint("Find a gift for Scarlet before the eleventh.")
        slowprint("Find something to eat")
    elif day == 2:
        slowprint("Day two.")
        slowprint("Two days left.")
        slowprint("You wake up, today is now the ninth.")
        slowprint("You stretch and get out of bed.")
        slowprint("You hear your computer ping, you should really check it out.")
        slowprint("Goals:")
        if gift == "none":
            slowprint("Find a gift for Scarlet before the eleventh.")
        else:
            slowprint("Give Scarlet your gift on the eleventh.")
        slowprint("Check the notification on you computer.\n")
    elif day == 3:
        slowprint("Day three.")
        slowprint("One days left.")
        slowprint("You wake up. It's the tenth.")
        slowprint("You're supposed to meet with Scarlet tomorrow.")
        slowprint("You feel like you should clean yourself up before that.")
        slowprint("Goals:")
        if gift == "none":
            slowprint("Find a gift for Scarlet before the tomorrow.")
        else:
            slowprint("Give Scarlet your gift tomorrow.")
        slowprint("Take a shower.")
        slowprint("Brush your hair.")
        slowprint("Do some laundry.\n")
    else:
        slowprint("Day four.")
        slowprint("Zero days left.")
        slowprint("You wake up, looking at your calendar.")
        slowprint("It's the 7th. Today is finally the day.")
        slowprint("You grab your bag as you make your way to the front door.")
        slowprint("You can barely step outside before you hear your name being called.")
        slowprint(f"'{name}! I haven't seen you in forever!'")
        slowprint("You look up at Scarlet, a smile slowly showing on your face.")
        slowprint("Scarlet makes her way up to you, standing face to face in the matter of seconds.")
        endings(gift)

# endings 2-5 than 1
   
def endings(finalgift):    
    if finalgift == "none":
        slowprint("'Do you know what day it is?' She beamed, looking at you with hope.")
        slowprint("Your smile quickly turns to a frown before you can stop yourself.")
        slowprint("'Oh, yah.'")
        slowprint("You notice Scarlets shoulders slump, despite how upbeat she trys to stay.")
        slowprint("She opens her mouth to say something, but she changes her mind before she can.")
        slowprint("There's an uncomfortable pause between you two, before she lets out a sigh.")
        slowprint("'Well, atleast I got to finally see you.'")
        slowprint("Before you gain the courage to say anything she turns and leaves.")
        slowprint("You watch helplessly as she walks to her car, looking glum as she drives away.")
        slowprint("You make your way back inside, the sound of rain starts up as you make your way back into the house.")
        slowprint("You to your bedroom, tossing your bag to the floor as you slump onto your bed.")
        slowprint("You lay there for a while, at least it feels that way.")
        slowprint("You hear your computer beep, but you don't bother to look at it.")
        slowprint("Theres always next year.\n")
        slowprint("\nEnding 2/5")
        slowprint("Hopefully next time you can bring yourself to care enough.")
    elif finalgift == "Necklace" or finalgift == "Silver earrings":
        slowprint("Ending 3/5")
    elif finalgift == "Soccerball":
        slowprint("Ending 4/5")
    else:
        slowprint("Ending 5/5")
# ---------------- GAME FUNCTIONS ----------------
def show_area(area):
    slowprint(f"\n=== {area.name} ===")
    slowprint(area.description)


def travel(area):
    slowprint("\nYou can go to:")
    for d in area.exits:
        print("-", d)

    choice = input("Where? ").lower()

    if choice in area.exits:
        exit_data = area.exits[choice]

        if exit_data["locked"]:
            slowprint("It's locked.")
            return area

        return exit_data["area"]

    slowprint("You can't go there.")
    return area


def interact(area):
    choice = input(f"What do you interact with? ({area.interact}) ").lower()
    if area == bedroom and choice == "desk":
        slowprint("You sit at your desk.")
        if game["flags"]["drawer_money"]:
            slowprint("You find $50.")
            game["stats"]["money"] += 50
            game["flags"]["drawer_money"] = False

    elif area == bathroom and choice == "mirror":
        slowprint("You look into the mirror.")
        game["stats"]["stress"] += 5

    else:
        slowprint("Nothing happens.")


# ---------------- MAIN LOOP ----------------

def gameplay(current_area):
    while True:
        show_area(current_area)

        slowprint("\nActions: travel / interact / stats / quit")
        command = input("> ").lower()

        if command == "travel":
            current_area = travel(current_area)

        elif command == "interact":
            interact(current_area)

        elif command == "stats":
            slowprint(game["stats"])

        elif command == "quit":
            break

print_day(game["day"], game["gift"], playername)
current_area = bedroom
gameplay(current_area)
