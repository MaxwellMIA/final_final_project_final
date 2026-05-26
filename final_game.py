import time
import sys
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
    "gift": "none",
    "computer": False,
    "task3": False,
    "painting": False,
    "key": False,
    "baseballcap": False,
    "stats": {"health": 100, "stress": 0, "money": 50},
    "flags": {
        "photoalbum": True,
        "drawermoney": True,
        "sleep": False,
    }
}

#----------------------------------------------------------------------- areas 

bedroom = Area(
    "Bedroom",
    "It's your bedroom. It seems messier then it was yesterday.",
    look = "It's your childhood bedroom, the walls have faded in color over the years. Trash litters your desk and the floor, while your bed is covered in dirty clothes you haven't feel like moving.",
    interact = "Bed, Desk, Bookshelf, Hunter"
)

hallway = Area(
    "Hallway",
    "A short hallway.",
    look = "There is spots of paint missing from the wall where paintings used to hang. Most of the photos got taken down after the divorce. Atleast you don't have to look at them anymore.",
    interact = "Drawer"
)

bathroom = Area(
    "Bathroom",
    "A plain bathroom, but it's cleaner then your room.",
    look = "The mirror on the wall taunts you, making you feel a wave of dread wash over you.",
    interact = "Mirror, Washer & Drier, Shower"
)

stairs = Area(
    "Stairs",
    "You're always afraid of slipping.",
    look = "You look at the painting on the wall, but you don't know what it is.",
    interact = "Painting"
)

livingroom = Area(
    "Living Room",
    "The living room seems darker then normal. The TV hasn't been turned on in days.",
    look = "The TV is covered in dust, but even if you wanted to watch it, you don't know where the remote is. Atleast the plant looks happy near the window.",
    interact = "Plant"
)

kitchen = Area(
    "Kitchen",
    "The kitchen smells faintly like stale coffee and mold.",
    look = "Dirty dishes sit piled in the sink, and a few unopened bills clutter the counter beside the microwave. The refrigerator hums quietly in the corner while rain taps softly against the window above the sink.",
    interact = "Fridge"
)

yard = Area(
    "Yard",
    "Your backyard stretches out behind the house, quiet and slightly overgrown.",
    look = "The grass is uneven and a little too long, as if no one has bothered to take care of it recently. A worn path leads toward a rickety old treehouse near the fence. The air feels colder out here, and the house behind you looks smaller than it should.",
    interact = ""
)

treehouse = Area(
    "Treehouse",
    "Your old treehouse full of memories, both good and bad.",
    look = "The wood is old, and the walls are covered in old paint thats chipping now. You miss having time with your friends here, before everything happened.",
    interact = "Photo album, Baseball cap, Weird can"
)

frontdoor = Area(
    "Front Door",
    "The front door stands between you and the outside world.",
    look = "The paint on the door is slightly chipped, and the doorknob feels cold to the touch. A small mat sits on the floor, worn down from years of use.",
    interact = ""
)

plaza = Area(
    "Plaza",
    "A small town plaza that feels oddly empty for this time of day.",
    look = "The pavement is slightly cracked in places, and a few benches sit scattered around the open space. A faded fountain sits at the center, barely trickling water. Shops surround the plaza, their windows reflecting a dull, gray sky.",
    interact = "Fountain"
)

park = Area(
    "Park",
    "A quiet park with winding paths and too much open space.",
    look = "Tall trees line the walking paths, their leaves rustling softly in the wind. The grass is patchy in places, but the benches look like they are used daily.",
    interact = "Robert"
)

grocery = Area(
    "Grocery Store",
    "A small neighborhood grocery store with flickering fluorescent lights.",
    look = "The aisles are mostly quiet, with a faint hum from the refrigerators in the back. Shopping carts sit scattered near the entrance, some slightly bent or rusted.",
    interact = "Salad"
)

jewelry = Area(
    "Jewelry Store",
    "The jewelry store shines as you walk in. Your wallet feels heavy.",
    look = "Glass cases line the walls, filled with rings, necklaces, and earrings that catch the light. A faint perfume lingers in the air, which burns your nose.",
    interact = "Earrings, Necklace"
)


sports = Area(
    "Sports store",
    "A slightly dusty sports shop filled with old gear and faded posters of athletes.",
    look = "Rows of shelves hold worn-out equipment, from footballs and basketballs to running shoes and gloves. Some of the posters on the wall are peeling at the corners, showing athletes that have retired years ago.",
    interact = "Cashier, Soccer ball"
)

field = Area(
    "Field",
    "An open field stretching far beyond the park, quiet and slightly unsettling in its emptiness.",
    look = "Tall grass sways gently in the wind, moving in slow waves across the land. There are no paths here, only flattened patches where people once walked. In the distance, the edge of a dark forest looms, the trees packed tightly together like a wall.",
    interact = "Sarah"
)

woods = Area(
    "Woods",
    "A dense forest where the sunlight barely reaches the ground.",
    look = "The trees are tightly packed, their branches twisting overhead and blocking most of the sky. The air feels colder here, and every step forward makes the ground softer and less stable",
    interact = ""
)

backwoods = Area(
    "Backwoods",
    "You can't see anything anymore.",
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
yard.moving("tree house", treehouse)
treehouse.moving("yard", yard)
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
woods.moving("Back woods", backwoods)
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

def printday(day, gift, name):
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
    elif day == 4:
        slowprint("Day four.")
        slowprint("Zero days left.")
        slowprint("You wake up, looking at your calendar.")
        slowprint("It's the 11th. Today is finally the day.")
        slowprint("You grab your bag as you make your way to the front door.")
        slowprint("You can barely step outside before you hear your name being called.")
        slowprint(f"'{name}! I haven't seen you in forever!'")
        slowprint("You look up at Scarlet, a smile slowly showing on your face.")
        slowprint("Scarlet makes her way up to you, standing face to face in the matter of seconds.")
        endings(gift)
    else:
        slowprint("You die.")
        sys.exit()

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
        sys.exit()
    elif finalgift == "necklace" or finalgift == "earrings":
        slowprint("'Do you know what day it is?' She beamed, looking at you with hope.")
        slowprint("You hesitate for a moment, then reach into your bag.")
        slowprint("Her eyes widen slightly as you hand her the gift.")
        slowprint("Scarlet carefully takes it, her expression shifting as she sees what it is.")
        slowprint("Theres a quiet pause.")
        slowprint("'Oh... thank you.' she says softly.")
        slowprint("She tries to smile, but there's still a hint of sadness in her eyes.")
        slowprint("She puts on the jewelry despite that.")
        slowprint("'Thank you.'")
        slowprint("She looks like she wants to say more, but she doesn't") 
        slowprint("'I don't wear much jewelry anymore, but it's better than nothing.'")
        slowprint("'I should go. But thanks. Really.'")
        slowprint("Before you can respond, she turns and walks off.")
        slowprint("Ending 3/5")
        sys.exit("At least you got her something.")
    elif finalgift == "soccerball":
        slowprint("'Do you know what day it is?' She beamed, looking at you with hope.")
        slowprint("You hesitate for a second, then pull the soccer ball out of your bag.")
        slowprint("Her eyes light up immediately.")
        slowprint("'Oh wow, we haven't played soccer in a while.'")
        slowprint("Before you can say anything, she grabs the ball from your hands.")
        slowprint("'Come on. You're playing with me.'")
        slowprint("The two of you head to the park.")
        slowprint("The grass is damp, but she doesn't seem to care at all.")
        slowprint("She kicks the ball to you with a grin. 'Don't go easy on me.'")
        slowprint("And you don't")
        slowprint("For a while, nothing else matters.")
        slowprint("Just passing, laughing, chasing the ball across the field like everything is normal again.")
        slowprint("At one point she actually laughs.")
        slowprint("You haven't heard her laugh in years.")
        slowprint("Eventually you both slowly stop, standing there catching your breaths.")
        slowprint("She nudges the ball lightly with her foot.")
        slowprint("'You know, I didn't think you'd actually give me anything.'")
        slowprint("'But I'm glad you did.'")
        slowprint("You smile, but youre not sure if she saw it.")
        slowprint("She looks down at the ball, then back at you.")
        slowprint("'This was a good idea. Really good.'")
        slowprint("'We should do this again sometime. Properly. No excuses.'")
        slowprint("You look shocked, but you can't help but argee.")
        slowprint("Maybe everything will be okay again.")
        slowprint("Ending 4/5")
        sys.exit("Friends again, maybe this time it can last.")
    elif finalgift == "photo album":
        slowprint("'Do you know what day it is?' She beamed, looking at you with hope.")
        slowprint("You don't answer right away. Instead, you carefully pull out a small photo album.")
        slowprint("Her expression flickers with curiosity as you hand it to her.")
        slowprint("She knows what it is, but she doesn't believe it.")
        slowprint("The first page is the two of you from a long time ago.")
        slowprint("Then another. And another.")
        slowprint("Small moments. Random days. Random things that didn't feel important at the time.")
        slowprint("'I can't believe it.' She whispers.")
        slowprint("'I thought you didn't care about any of this.' she says quietly.")
        slowprint("You can only muster up a small sorry, which makes you feel worse after saying it.")
        slowprint("But that doesn't stop her.")
        slowprint("She steps forward and pulls you into a tight hug, holding on longer than you can ever remember.")
        slowprint("For once, there is no distance between you two.")
        slowprint("'I'm so happy.' She says into your shoulder. 'I'm so, so happy.'")
        slowprint("When she finally lets go, she doesn't step back far, and you're thankful for that.")
        slowprint("'I don't even care about the day anymore'")
        slowprint("'I'm just glad it's you.'")
        slowprint("She hugs you again, and you this time you don't want to let go.")
        slowprint("Ending 5/5")
        sys.exit("Best friend again, no matter what.")

def stress():
    if game["stats"]["stress"] >= 100:
        slowprint("\nYou slowly start to feel sick.")
        slowprint("You clutch your chest, which starts to burn, as you fall to your knees.")
        slowprint("You've had panic attacks before, but it was never like this.")
        slowprint("You slowly lose consciousness, and you never will wake up again.")
        slowprint("\nEnding 1/5")
        slowprint("Maybe you should of tried to manage your stress better.")
        sys.exit()

def health():
    if game["stats"]["health"] <= 0:
        slowprint("\nYou slowly start to feel sick.")
        slowprint("Your whole body hurts as you clutch yourself.")
        slowprint("You fall to the floor quickly, passing out before losing your breath.")
        slowprint("\nEnding 1/5")
        slowprint("Maybe you should of tried to manage your health better.")
        sys.exit()

def bear():
    slowprint("You walk into the woods, but you quickly lose your way.")
    slowprint("You stumble around before you hear a loud roar")
    slowprint("At least that was the last thing you heard to.")
    slowprint("\nEnding 1/5")
    slowprint("Maybe you should of not gone in the dark scary woods.")
    sys.exit()

# ---------------- GAME FUNCTIONS ----------------

def showarea(area):
    slowprint(f"\n=== {area.name} ===")
    slowprint(area.description)
    if area == backwoods:
        bear()

def travel(area):
    slowprint("\nYou can go to:")
    for d in area.exits:
        print("-", d)

    command = input("Where? ").lower()

    if command in area.exits:
        exitdata = area.exits[command]

        if exitdata["locked"]:
            required_key = exitdata["key"]

            if required_key == "yard key" and game["key"]:
                slowprint("You use the yard key to unlock the path.")
                exitdata["locked"] = False
            else:
                slowprint("It's locked.")
                slowprint("You think you remember you're mom talking about hiding the key inside on the bottom floor.")
                return area

        return exitdata["area"]

    slowprint("You can't go there.")
    return area


def interact(area):
    command = input(f"What do you interact with? ({area.interact}) ").lower()
    if area == bedroom:
        if command == "bed":
            if game["flags"]["sleep"] == False:
                slowprint("You look at your bed.")
                slowprint("You want to sleep, but you still have things to do.\n")
            elif game["day"] != 4:
                slowprint("You look at your bed.")
                slowprint("You yawn and climb in, going to sleep.\n")
                game["day"] += 1
                game["flags"]["sleep"] = False
                printday(game["day"], game["gift"], playername)
            elif game["day"] == 3 and game["gift"] == "none":
                slowprint("WARNING!")
                slowprint("You don't have a gift for tomorrow.")
                slowprint("Do you want to move onto the next day?")
                command = input("Yes, No ").lower()
                if command == "yes":
                    slowprint("You look at your bed.")
                    slowprint("You yawn and climb in, going to sleep.\n")
                    game["day"] += 1
                    game["flags"]["sleep"] = False
                    printday(game["day"], game["gift"], playername)
                else:
                    slowprint("You look at your bed.")
                    slowprint("You want to sleep but you still have things to do.\n")
        elif command == "desk":
            slowprint("You sit at your desk.")
            if game["flags"]["drawermoney"]:
                slowprint("You find $50.")
                game["stats"]["money"] += 50
                game["flags"]["drawermoney"] = False
            if game["day"] == 2 and game["computer"] == False:
                slowprint("You open your computer, opening up your messages.")
                slowprint("Robert messaged you, which shocks you.")
                slowprint("He asks you to see if you can go to the treehouse in your yard to find his old baseball hat.")
                slowprint("He tells you that you can meet him in the park when you find it, but he will need it today.")
                game["computer"] = True
            else:
                slowprint("You go to your computer, but you don't have any messages.\n")
        elif command == "bookshelf":
            slowprint("You go to your bookshelf, looking at the few books you haven't bothered to move yet.")
            slowprint("What book would you like to look at?")
            command = input("Book set, Diary, Back~ ").lower()
            if command == "book set":
                slowprint("You grab the first book from the book set.")
                slowprint("It's in a language you don't understand.")
                slowprint("You think one of your older friends gave this to you before she moved.")
                slowprint("You frown and put the book back.\n")
            if command == "diary":
                slowprint("You look at your diary for a few minutes.")
                slowprint("You can't remember the last time you wrote in it.")
                slowprint("You continue to look at your diary.")
                slowprint("You suddenly feel sick to your stomach.")
                slowprint("You finally look away, feeling your heart pounding in your chest.\n")
                game["stats"]["stress"] += 5
                stress()
        elif command == "hunter":
            slowprint("You pet Hunter, who sleeps on your bed.")
            slowprint("He meows at you quietly before going back to bed.")
        else:
            slowprint("You can't do that.")
    elif area == hallway:
        if command == "drawer":
            slowprint("You open the drawer, but all that's inside is a few pens and paper clips.")
        else:
            slowprint("You can't do that.")
    elif area == bathroom:
        if command == "mirror":
            slowprint("You look into the mirror, but it makes you feel sick to your stomach.")
            game["stats"]["stress"] += 5
            stress()
        elif command == "washer & drier":
            if game["day"] == 3 and game["task3"] == False:
                slowprint("You decide to do some laundry and take a shower.")
                slowprint("Better to get both done at once.")
                slowprint("After your shower you brush your hair too.")
                game["task3"] = True
                game["flags"]["sleep"] = True
                slowprint("Now you are ready to go to bed.")
            else:
                slowprint("You don't feel like doing your laundry right now.")
        elif command == "shower":
            if game["day"] == 3 and game["task3"] == False:
                slowprint("You decide to do some laundry and take a shower.")
                slowprint("Better to get both done at once.")
                slowprint("After your shower you brush your hair too.")
                game["task3"] = True
                game["flags"]["sleep"] = True
                slowprint("Now you are ready to go to bed.")
            else:
                slowprint("You don't feel like doing your laundry right now.")
        else:
            slowprint("You can't do that.")
    elif area == stairs:
        if command == "painting" and game["painting"] == False:
            slowprint("You look at the painting, thinking to yourself.")
            slowprint("You slightly move the painting, which causes a cockroach to run off.")
            slowprint("You're so startled you almost fall down the stairs, but you caught yourself before you can.")
            game["painting"] = True
            game["stats"]["stress"] += 5
            stress()
        elif command == "painting" and game["painting"] == True:
            slowprint("You don't want to touch the painting.")
        else:
            slowprint("You can't do that.")
    elif area == livingroom:
        if command == "plant" and game["key"] == False:
            slowprint("You look at the plant, but you notice something glimmer in the pot.")
            slowprint("Reaching your hand in the pot, you feel the yard key.")
            slowprint("You now have the yard key.")
            game["key"] = True
        elif command == "plant" and game["key"] == True:
            slowprint("There isn't anything interesting about the plant.")
        else:
            slowprint("You can't do that.") 
    elif area == kitchen:
        if command == "fridge" and game["day"] == 1:
            slowprint("You open the fridge")
            slowprint("Theres salad and a steak.")
            slowprint("You want to eat one, but you will have to throw away the other before it molds.")
            command = input("What do you want to eat? ").lower()
            if command == "salad":
                slowprint("You grab the steak and throw it away, before grabbing the salad.")
                slowprint("You embrace yourself before taking a bite, but it actually isn’t horrible.")
                game["stats"]["stress"] -= 10
                game["stats"]["health"] += 10
                game["flags"]["sleep"] = True
                slowprint("You are full now, and you are ready to go to bed.")
            elif command == "steak":
                slowprint("You grab the salad and throw it away, before grabbing the steak.")
                slowprint("You heat the steak up in the micowave")
                slowprint("You embrace yourself before taking a bite, but it couldn't have prepared you for this horrible taste.")
                game["stats"]["stress"] += 10
                game["stats"]["health"] -= 10
                game["flags"]["sleep"] = True
                stress()
                health()
                slowprint("You aren't full, but your stomach hurts and you just want to go to bed.")
            else:
                slowprint("You've changed your mind.")
        elif game["day"] != 1:
            slowprint("There is nothing in the fridge.")
        else:
            slowprint("You can't do that.")
    elif area == treehouse:
        if command == "photo album" and game["flags"]["photoalbum"] == True:
            slowprint("You look at the photo album, it's mainly pictures of you and Scarlet")
            slowprint("Maybe Scarlet would like this as her gift.")
            command = input("Use the photo album as a gift? (yes / no) ").lower()
            if command == "yes":
                game["gift"] = "photo album"
                game["flags"]["photoalbum"] = False
        elif command == "photo album" and game["flags"]["photoalbum"] == False:
            slowprint("You already took the photo album")
        elif command == "baseball cap" and game["day"] == 2 and game["computer"] == True and game["baseballcap"] == False:
            slowprint("You found Roberts baseball cap. You grab it to give to him later.")
            game["baseballcap"] = True
        elif command == "baseball cap" and game["baseballcap"] == False:
            slowprint("You don't need this right now.")
        elif command == "baseball cap" and game["baseballcap"] == True:
            slowprint("You already took the baseball cap.")
        elif command == "weird can":
            slowprint("You open up the weird can, getting hit in the face by a fake snake.")
            game["stats"]["health"] -= 1
            health()
        else: 
            slowprint("You can't do that.")
    elif area == plaza:
        if command == "fountain":
            slowprint("You look in the fountain, you wonder how many people have put coins in it.")
        else: 
            slowprint("You can't do that.")
    elif area == park:
        if command == "robert":
            if game["day"] != 2:
                slowprint("It's your friend Robert, but he is too focused on his phone to see you.")
            elif game["day"] == 2 and game["baseballcap"] == False:
                slowprint("You go up to Robert, and he looks up at you.")
                slowprint("'Hey! Do you have my hat?'")
                slowprint("You shake your head and look away embarrassed.")
                slowprint("'I'm pretty sure it's in the treehouse, if you could find it, that would be awesome!")
            elif game["day"] == 2 and game["baseballcap"] == True:
                slowprint("You walk up to Robert, holding out the baseball cap.")
                slowprint("'Oh yah bro! This is awesome! Thanks man.'")
                slowprint("Robert puts on the hat.")
                slowprint("'You know, Scarlet misses you, maybe you could give her something from our childhood.'")
                slowprint("You shrug, not really thinking about it much.")
                slowprint("'Anyways, I have to go home. Bye.'")
                game["flags"]["sleep"] = True
                slowprint("You've had a fulfilling day, you are ready to go to bed.")
            else: 
                slowprint("You can't do anything right now.")
        else: 
            slowprint("You can't do that.") 
    elif area == grocery:
        slowprint("Theres some salads for $10")
        if game["stats"]["money"] > 10:
            command = input("Do you want to buy it? (yes / no) ").lower()
            if command == "yes":
                game["stats"]["money"] -= 10
                slowprint("You buy the salad and eat it, you feel better.")
                game["stats"]["stress"] -= 10
                game["stats"]["health"] += 10
            elif command == "no":
                slowprint("You changed your mind.")
            else:
                slowprint("You can't choose that.")
        elif game["stats"]["money"] < 10:
            slowprint("You can't afford it.")
        else:
            slowprint("You can't do that.")
    elif area == jewelry:
        slowprint("Theres some earrings and a necklace for $45 each.")
        slowprint("You could pick one of these to be Scarlets gift.")
        if game["stats"]["money"] > 45:
            command = input("Do you want to buy one? (yes / no) ").lower()
            if command == "yes":
                command = input("Do you want the earrings or the necklace? ").lower()
                if command == "earrings":
                    game["stats"]["money"] -= 45
                    game["gift"] = "earrings"
                    slowprint("You buy the earrings for Scarlet.")
                elif command == "necklace":
                    game["stats"]["money"] -= 45
                    game["gift"] = "necklace"
                    slowprint("You buy the necklace for Scarlet.")
                else:
                    slowprint("You change your mind")
            else:
                slowprint("You aren't too interested.")
        elif game["stats"]["money"] < 45:
            slowprint("You can't afford it.")
        else:
            slowprint("You can't do that.")
    elif area == sports:
        if command == "cashier":
            slowprint("You look at the cashier, who is smoking a cig.")
            slowprint("You're too nervous to say anything, despite how nice she looks.")
        elif command == "soccer ball":
            slowprint("Theres a soccer ball for $20.")
            slowprint("You could pick this to be Scarlets gift.")
            if game["stats"]["money"] > 20:
                command = input("Do you want to buy it? (yes / no) ").lower()
                if command == "yes":
                    game["stats"]["money"] -= 20
                    game["gift"] = "soccer ball"
                    slowprint("You buy the soccer ball for Scarlet.")
                elif command == "no":
                    slowprint("You changed your mind.")
            elif game["stats"]["money"] < 20:
                slowprint("You can't afford it.")
            else:
                slowprint("You can't do that.")
        else:
            slowprint("You can't do that.")
    else:
        slowprint("You can't do that.")

# ---------------- MAIN LOOP ----------------

def gameplay(currentarea):
    while True:
        showarea(currentarea)

        slowprint("\nActions: travel / interact / stats")
        command = input("What do you want to do? ").lower()

        if command == "travel":
            currentarea = travel(currentarea)

        elif command == "interact":
            interact(currentarea)

        elif command == "stats":
            slowprint(game["stats"])

printday(game["day"], game["gift"], playername)
currentarea = bedroom
gameplay(currentarea)