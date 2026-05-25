

def print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name):
    print(f"You are in the {current_area.name}.")
    print("What would you like to do?")
    command = input("~Travel, Look, Interact, Inventory, Stats~ ").lower()

    if command == "look":
        print(current_area.description)
        print(current_area.look)
        print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)

    if command == "interact":
        print(current_area.interact)
        command = input("What would you like to interact with? ").lower()

        if command == "bed" and current_area == bedroom:
            if day == 1 and day1task == False or day == 2 and day2task == False or day == 3 and day3task == False:
                print("You look at your bed.")
                print("You want to sleep, but you still have things to do.\n")
                print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
            if day == 1 and day1task == True:
                print("You look at your bed.")
                print("You yawn and climb in, going to sleep.\n")
                day = 2
                print_day(day)
                print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
            if day == 2 and day2task == True:
                print("You look at your bed.")
                print("You yawn and climb in, going to sleep.\n")
                day = 3
                print_day(day)
                print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
            if day == 3 and day3task == True:
                if gift == "none":
                    print("WARNING!")
                    print("You don't have a gift for tomorrow.")
                    print("Do you want to move onto the next day?")
                    command = input("Yes, No").lower()
                    if command == "yes":
                        print("You look at your bed.")
                        print("You yawn and climb in, going to sleep.\n")
                        day = 4
                        print_day(day)
                    if command == "no":
                        print("You look at your bed.")
                        print("You want to sleep but you still have things to do.\n")
                        print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
                if gift != "none":
                    print("You look at your bed.")
                    print("You yawn and climb in, going to sleep.\n")
                    day = 4
                    print_day(day)

        if command == "desk" and current_area == bedroom:
            print("You walk over to your desk, sitting down.")
            print("What would you like to do?")
            command = input("~Computer, Drawer, Notes, Back~ ").lower()
            if command == "computer":
                if day != 2:
                    print("You go to your computer, but you don't have any messages.\n")
                    print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
                if day == 2:
                    print("You open your computer, opening up your messages.\n")
                    # messages
                    print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
            if command == "drawer":
                if drawermoney == True:
                    print("You open the drawer, grabbing your wallet.")
                    print("You now have $50.\n")
                    drawermoney = False
                    print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
                if drawermoney == False:
                    print("You open the drawer, but there isn't anything left inside.\n")
                    print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
            if command == "notes":
                print("You look at the sticky notes that scatter your desk.")
                print("Most of them aren't useful anymore, but you look at the one your mom left you before she left.")
                print(f"'I'll be gone until the 13th. I made you dinner for tonight. Love you {name}.'")
                print("You sigh and put the note back.\n")
                print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)

        if command == "bookshelf" and current_area == bedroom:
            print("You go to your bookshelf, looking at the few books you haven't bothered to move yet.")
            print("What book would you like to look at?")
            if photoalbumshelf == True:
                command = input("~Photo album, Book set, Diary, Back~ ").lower()
                if command == "photo album":
                    print("You grab the photo album, looking at the first few photos.")
                    print("They are all photos of you and Scarlet.")
                    print("You wonder if this would be a good birthday gift.")
                    print("Do you want to give Scarlet this gift?")
                    command = input("Yes, No").lower()
                    if command == "yes":
                        print("You put the photo album in your bag.\n")
                        gift = "photo album"
                        photoalbumshelf == False
                        print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
                    if command == "no":
                        print("You put the photo album back.\n")
                        print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
                if command == "book set":
                    print("You grab the first book from the book set.")
                    print("It's in a language you don't understand.")
                    print("You think one of your older friends gave this to you before she moved.")
                    print("You frown and put the book back.\n")
                    print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
                if command == "diary":
                    print("You look at your diary for a few minutes.")
                    print("You can't remember the last time you wrote in it.")
                    print("You continue to look at your diary.")
                    print("You suddenly feel sick to your stomach.")
                    print("You finally look away, feeling your heart pounding in your chest.\n")
                    player_stats["Stress"] += 10
                    if player_stats["Stress"] >= 100:
                        stressdeath()
                    print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)

        if command == "drawer" and current_area == hallway:
            print("You open the drawer, but all that's inside is a few pens and paper clips.")
            print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)

        if command == "mirror" and current_area == bathroom:
            if randomfear == False:
                num = random.randint(1, 50)
                if num == 25:
                    print("You look at the mirror for a few seconds.")
                    print("It doesn't look like you anymore.")
                    print("You raise your hand, hitting the mirror as hard as you can.")
                    print("The mirror shatters as you hit it, cutting your hand.\n")
                    randomfear == True
                    player_stats["Stress"] += 30
                    if player_stats["Stress"] >= 100:
                        stressdeath()
                    player_stats["Health"] -= 10
                    if player_stats["Stress"] >= 100:
                        healthdeath()
                print("You look at the mirror, but something feels off.")
                print("Your stomach starts to ache.\n")
                player_stats["Stress"] += 5
                if player_stats["Stress"] >= 100:
                    stressdeath()
            if randomfear == True:
                print("The mirror is shattered.")
                print("It doesn't bother you anymore.\n")
            # Washer & Drier, Bathtub
        
        if (command == "washer & drier" or command == "washer" or command == "drier" or command == "washer + drier" or command == "washer&drier") and current_area == bathroom:
            if day != 3:
                print("You should probably do some laundry soon, but you don't feel like it now.")
            if day == 3:
                if laundrytask == False:
                    print("You turn on the washing machine,")

        if command == "" and current_area == "hi":
            print("i")

        if command == "" and current_area == "hi":
            print("i")

        if command == "" and current_area == "hi":
            print("i")

        if command == "back":
            print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)
        
        if command != "bed" or command != "desk" or command != "bookshelf" or command != "drawer" or command != "":
            print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)

    if command == "inventory":
        if inventory == "empty":
            print("You don't have anything in your bag currently.")
        if inventory != "empty":
            print("You open up your backpack and look at whats inside.")
            print(inventory)

    if command == "stats":
        print(f"{name}'s stats. Health:{player_stats['Health']} Stress:{player_stats['Stress']} Money:{player_stats['Money']}")


def stressdeath():
    print("you die via stress")

def healthdeath():
    print("you die via brian death")
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

# hi
photoalbumshelf = True
yardkey = False
gift = "none"
day1task = False
day2task = False
day3task = False
drawermoney = True
invsalad = False
invsteak = False
inventory = "empty"
player_stats = {"Health": 100, "Stress": 0, "Money": 50}
day = 1
randomfear = False
current_area = bathroom
laundrytask = False
name = ''
naming(name)
print_day(day)
print_area(current_area, day, gift, photoalbumshelf, player_stats, drawermoney, name)