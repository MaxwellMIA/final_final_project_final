# Before game functions
import time
from colorama import Fore

def slowprint(text, delay=0): #0.07
    for char in text:
        print(Fore.RED + char, end='', flush=True)
        time.sleep(delay)
    time.sleep(0) #0.3
    print()

# starting zone

slowprint("~~GAME NAME~~")

name = input("What is your name? ").capitalize()
if name == "Scarlet":
    slowprint("Sorry, that names not available")

def print_day(day):
    if day == 1:
        slowprint("Day one.")
        time.sleep(0.7)
        slowprint("Three days left.")
        time.sleep(0.7)
        slowprint("You open your eyes, looking at the ceiling above you.")
        slowprint("You slowly sit up, rubbing your eyes.")
        slowprint("You look over at your calendar, frowning as you see what the date is.")
        slowprint("It's the eighth, and Scarlet's birthday is the eleventh.")
        slowprint("You promised her you would meet up with her, but you want to get a gift before then.")
        slowprint("But first, you need something to eat.")
        time.sleep(0.7)
        slowprint("Goals:")
        slowprint("Find a gift for Scarlet before the eleventh.")
        slowprint("Find something to eat.")
    if day == 2:
        slowprint("Day two.")
        time.sleep(0.7)
        slowprint("Two days left.")
        time.sleep(0.7)
        slowprint("You wake up, today is now the ninth.")
        slowprint("You stretch and get out of bed.")
        slowprint("You hear your computer ping, you should really check it out.")
        time.sleep(0.7)
        slowprint("Goals:")
        if gift == "none":
            slowprint("Find a gift for Scarlet before the eleventh.")
        else:
            slowprint("Give Scarlet your gift on the eleventh.")
        slowprint("Check the notification on you computer.")
    if day == 3:
        slowprint("Day three.")
        time.sleep(0.7)
        slowprint("One days left.")
        time.sleep(0.7)
        slowprint("You wake up. It's the tenth.")
        slowprint("You're supposed to meet with Scarlet tomorrow.")
        slowprint("You feel like you should clean yourself up before that.")
        time.sleep(0.7)
        slowprint("Goals:")
        if gift == "none":
            slowprint("Find a gift for Scarlet before the tomorrow.")
        else:
            slowprint("Give Scarlet your gift tomorrow.")
        slowprint("Take a shower.")
        slowprint("Brush your hair.")
        slowprint("Do some laundry.")
    if day == 4:
        if day == 4:
            slowprint("Day four.")
            time.sleep(0.7)
            slowprint("Zero days left.")
            time.sleep(0.7)
            slowprint("You wake up, looking at your calendar.")
            slowprint("It's the 7th. Today is finally the day.")
            slowprint("You grab your bag as you make your way to the front door.")
            slowprint("You can barely step outside before you hear your name being called.")
            slowprint(f"'{name}! I haven't seen you in forever!'")
            slowprint("You look up at Scarlet, a smile slowly showing on your face.")
            slowprint("Scarlet makes her way up to you, standing face to face in the matter of seconds.")

        if gift == "none":
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
            time.sleep(0.7)
            slowprint("You lay there for a while, at least it feels that way.")
            slowprint("You hear your computer beep, but you don't bother to look at it.")
            slowprint("Theres always next year.")
            time.sleep(0.7)
            slowprint("Ending 1")
            slowprint("Giftless and lonely")

        if gift == "Necklace" or gift == "Silver earrings":
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
    slowprint("What would you like to do?")
    command = input("~Travel, Look, Interact, Inventory, Stats~ ").lower()

    if command == "travel":
        slowprint("Where do you want to go?")
        command = input(f"~{current_area.exits}, back~ ").lower()
        if command == "bedroom" and current_area == hallway:
            current_area = bedroom
            slowprint(f"You walk to your bedroom\n")
            print_area(current_area)

        if command == "hallway" and (current_area == bedroom or current_area == bathroom or current_area == stairs):
            current_area = hallway
            slowprint(f"You walk to the hallway\n")
            print_area(current_area)

        if command == "bathroom" and current_area == hallway:
            current_area = bathroom
            slowprint(f"You walk to the bathroom\n")
            print_area(current_area)

        if command == "stairs" and (current_area == hallway or current_area == livingroom):
            current_area = stairs
            slowprint(f"You walk to the stairs\n")
            print_area(current_area)

        if command == "living room" and (current_area == stairs or current_area == kitchen or current_area == yard or current_area == frontdoor):
            current_area = livingroom
            slowprint(f"You walk to the living room\n")
            print_area(current_area)

        if command == "kitchen" and current_area == livingroom:
            current_area = kitchen
            slowprint(f"You walk to the kitchen\n")
            print_area(current_area)

        if command == "yard" and current_area == livingroom:
            if yardkey == True:
                current_area = yard
                slowprint(f"You walk to out to the yard\n")
                print_area(current_area)
            else:
                slowprint(f"You go to back door, but you realize you don't have your key.")
                slowprint(f"You'll need to find your key first before going out back.")
                print_area(livingroom)

        if command == "front door" and current_area == livingroom:
            current_area = frontdoor
            slowprint(f"You walk to the front door\n")
            print_area(current_area)

        if command == "plaza" and (current_area == frontdoor or current_area == park or current_area ==  grocery or current_area == jewelry or current_area == sports):
            current_area = plaza
            slowprint(f"You walk to the plaza\n")
            print_area(current_area)

        if command == "home" and current_area == plaza:
            current_area = frontdoor
            slowprint(f"You walk back home")
            slowprint("You walk back inside\n")
            print_area(current_area)
        
        if command == "park" and (current_area == plaza or current_area == field):
            current_area = park
            slowprint(f"You walk to the park\n")
            print_area(current_area)

        if command == "field" and (current_area == park or current_area == woods):
            current_area = field
            slowprint(f"You walk to the open field\n")
            print_area(current_area)

        if command == "woods" and current_area == field:
            current_area = woods
            slowprint(f"You walk into the woods\n")
            print_area(current_area)

        if (command == "grocery" or command == "grocery store") and current_area == plaza:
            current_area = grocery
            slowprint(f"You walk to the grocery store\n")
            print_area(current_area)

        if (command == "jewelry" or command == "jewelry store") and current_area == plaza:
            current_area = jewelry
            slowprint(f"You walk to the jewlry store\n")
            print_area(current_area)

        if (command == "sports" or command == "sports store") and current_area == plaza:
            current_area = sports
            slowprint(f"You walk to the sports store\n")
            print_area(current_area)

        if command == "back":
            print_area(current_area)

        if command != "bedroom" or command != "bathroom" or command != "hallway" or command != "stairs" or command != "living room" or command != "kitchen" or command != "yard" or command != "front door" or command !="plaza" or command !="home" or command !="park" or command !="field" or command !="woods" or command !="grocery" or command !="grocery store" or command !="jewelry" or command !="jewelry store" or command !="sports" or command !="sports store":
            print_area(current_area)

    if command == "look":
        slowprint(current_area.description)
        slowprint(current_area.look)
        print_area(current_area)

    if command == "interact":
        slowprint(current_area.interact)
        command = input("What would you like to interact with? ")

        if command == "bed" and current_area == bedroom:
            #do the day tasks and days and day 4 task for 3 and sleep
            slowprint("i")

        if command == "desk" and current_area == bedroom:
            slowprint("You walk over to your desk, sitting down.")
            slowprint("What would you like to do?")
            command = input("~Computer, Drawer, Notes, Back~ ").lower()
            if command == "computer":
                if day != 2:
                    slowprint("You go to your computer, but you don't have any messages.")
                    print_area(current_area)
                if day == 2:
                    slowprint("You open your computer, opening up your messages.")
                    #messages
                    print_area(current_area)

            if command == "drawer":
                if drawermoney == True:
                    slowprint("You open the drawer, grabbing your wallet.")
                    slowprint("You now have $50.")
                    drawermoney = False
                    print_area(current_area)
                if drawermoney == False:
                    slowprint("You open the drawer, but there isn't anything left inside.")
                    print_area(current_area)

            if command == "notes":
                slowprint("You look at the sticky notes that scatter your desk.")
                slowprint("Most of them aren't useful anymore, but you look at the one your mom left you before she left.")
                slowprint(f"'I'll be gone until the 13th. I made you dinner for tonight. Love you {name}.'")
                slowprint("You sigh and put the note back.")
                print_area(current_area)

        if command == "bookshelf" and current_area == bedroom:
            slowprint("")

        if command == "" and current_area == "hi":
            slowprint("i")

        if command == "back":
            print_area(current_area)
        
        if command != "":
            print_area(current_area)

    if command == "inventory":
        if inventory == "empty":
            slowprint("You don't have anything in your bag currently.")
        if inventory != "empty":
            slowprint("You open up your backpack and look at whats inside.")
            slowprint(inventory)

    if command == "stats":
        slowprint(f"{name}'s stats. Health:{player_stats['Health']} Stress:{player_stats['Stress']} Money:{player_stats['Money']}")

# Areas

bedroom = Area("Bedroom", "It's your bedroom. It seems messier then it was yesterday.", "Hallway", "It's your childhood bedroom, the walls have faded in color over the years. Trash litters your desk and the floor, while your bed is covered in dirty clothes you haven't feel like moving.", "Bed, Desk, Bookshelf, Back")

hallway = Area("Hallway", "A short hallway.", "Bedroom, Bathroom, Stairs", "There is spots of paint missing from the wall where paintings used to hang. Most of the photos got taken down after the divorce. Atleast you don't have to look at them anymore.", "Drawer, Back")

bathroom = Area("Bathroom", "A plain bathroom. It's cleaner then your room.", "Hallway", "The mirror on the wall taunts you, making you feel a wave of dread wash over you.", "Mirror, Washer & Drier, Bathtub, Back")

stairs = Area("Stairs", "You're always afriad of slipping.", "Hallway, Living room", "You look at the painting on the wall, but you don't know what it is.", "Painting, Back")

livingroom = Area("Living room", "The living room seems darker then normal. The TV hasn't been turned on in days.", "Stairs, Kitchen, Yard, Front door", "The TV is covered in dust, but even if you wanted to watch it, you don't know where the remote is. Atleast the plant looks happy near the window.", "Plant, Back")

kitchen = Area("Kitchen", "walking in", "living room", "look", "interact")

yard = Area("Yard", "walking in", "exits", "living room", "interact")

frontdoor = Area("Front door", "walking in", "living room, plaza", "look", "interact")

plaza = Area("Plaza", "walking in", "home, park, grocery, jewelry, sports", "look", "interact")

park = Area("Park", "walking in", "plaza, field", "look", "interact")

field = Area("Field", "walking in", "park, woods", "look", "interact")

woods = Area("Woods", "walking in", "field", "look", "interact")

grocery = Area("Grocery store", "walking in", "plaza", "look", "interact")

jewelry = Area("Jewelry store", "walking in", "plaza", "look", "interact")

sports = Area("Sports store", "walking in", "plaza", "look", "interact")

# Key and non-key items

yardkey = False
gift = "none"
day1task = False
day2task = False
day3task = False
drawermoney = True

invsalad = False
invsteak = False

# Changing variables

player_stats = {"Health": 100, "Stress": 0, "Money": 50}
inventory = "empty"

day = 1
current_area = bedroom
print_day(day)
print_area(current_area)