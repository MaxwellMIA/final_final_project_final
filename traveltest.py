class Area:
    def __init__(self, name, description, exits, look, interact):
        self.name = name
        self.description = description
        self.exits = exits
        self.look = look
        self.interact = interact
 
def print_area(current_area):
    print(f"You are in the {current_area.name}.")
    print("What would you like to do?")
    command = input("~Travel, Look, Interact, Inventory, Stats~ ").lower()

    if command == "travel":
        print("Where do you want to go?")
        command = input(f"~{current_area.exits}, back~ ").lower()
        if command == "bedroom" and current_area == hallway:
            current_area = bedroom
            print(f"You walk to your bedroom\n")
            print_area(current_area)

        if command == "hallway" and (current_area == bedroom or current_area == bathroom or current_area == stairs):
            current_area = hallway
            print(f"You walk to the hallway\n")
            print_area(current_area)

        if command == "bathroom" and current_area == hallway:
            current_area = bathroom
            print(f"You walk to the bathroom\n")
            print_area(current_area)

        if command == "stairs" and (current_area == hallway or current_area == livingroom):
            current_area = stairs
            print(f"You walk to the stairs\n")
            print_area(current_area)

        if command == "living room" and (current_area == stairs or current_area == kitchen or current_area == yard or current_area == frontdoor):
            current_area = livingroom
            print(f"You walk to the living room\n")
            print_area(current_area)

        if command == "kitchen" and current_area == livingroom:
            current_area = kitchen
            print(f"You walk to the kitchen\n")
            print_area(current_area)

        if command == "yard" and current_area == livingroom:
            if yardkey == True:
                current_area = yard
                print(f"You walk to out to the yard\n")
                print_area(current_area)
            else:
                print(f"You go to back door, but you realize you don't have your key.")
                print(f"You'll need to find your key first before going out back.")
                print_area(current_area)

        if command == "front door" and current_area == livingroom:
            current_area = frontdoor
            print(f"You walk to the front door\n")
            print_area(current_area)

        if command == "plaza" and (current_area == frontdoor or current_area == park or current_area ==  grocery or current_area == jewelry or current_area == sports):
            current_area = plaza
            print(f"You walk to the plaza\n")
            print_area(current_area)

        if command == "home" and current_area == plaza:
            current_area = frontdoor
            print(f"You walk back home")
            print("You walk back inside\n")
            print_area(current_area)
        
        if command == "park" and (current_area == plaza or current_area == field):
            current_area = park
            print(f"You walk to the park\n")
            print_area(current_area)

        if command == "field" and (current_area == park or current_area == woods):
            current_area = field
            print(f"You walk to the open field\n")
            print_area(current_area)

        if command == "woods" and current_area == field:
            current_area = woods
            print(f"You walk into the woods\n")
            print_area(current_area)

        if (command == "grocery" or command == "grocery store") and current_area == plaza:
            current_area = grocery
            print(f"You walk to the grocery store\n")
            print_area(current_area)

        if (command == "jewelry" or command == "jewelry store") and current_area == plaza:
            current_area = jewelry
            print(f"You walk to the jewlry store\n")
            print_area(current_area)

        if (command == "sports" or command == "sports store") and current_area == plaza:
            current_area = sports
            print(f"You walk to the sports store\n")
            print_area(current_area)

        if command == "back":
            print_area(current_area)

        if command != "bedroom" or command != "bathroom" or command != "hallway" or command != "stairs" or command != "living room" or command != "kitchen" or command != "yard" or command != "front door" or command !="plaza" or command !="home" or command !="park" or command !="field" or command !="woods" or command !="grocery" or command !="grocery store" or command !="jewelry" or command !="jewelry store" or command !="sports" or command !="sports store":
            print_area(current_area)

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

yardkey = False
current_area = bathroom
print_area(current_area)