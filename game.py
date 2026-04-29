print("~~GAME NAME~~")

name = input("What is your name? ").capitalize()
if name == "Scarlet":
    print("Sorry, that names not available")

class Area:
    def __init__(self):
        self.name = 0
        self.description = 0
        self.exits = 0

    def print_area(self):
        print(f"You are in {self.name}.")
        print(self.description)
        print("What would you like to do?")
        command = input("~Travel, Look, Interact~ ").lower()

        if command == "travel":
            print("Where do you want to go?")
            command = input(f"~{self.exits}, back~ ").lower()
            if command == self.exits:
                print(f"You walk to {self.exits}")
                current_area = {self.exits}
                # add smt to print out next areas stuff
            if command == "back":
                print("You've changed your mind.")
                # make it avaible to redo the "what would you like to do" to run though these 3 if statments again

        if command == "look":
            print(self.look)
            # make it avaible to redo Nhe "what would you like to do" to run though these 3 if statments again

        if command == "interact":
            print(self.interact)

current_area = "bedroom"

bedroom = Area()
bedroom.name = "Bedroom"
bedroom.description = "It's your bedroom. It seems messier then it was yesterday."
bedroom.exits = "Hallway"
bedroom.look = "It's your childhood bedroom, the walls have faded in color over the years. Trash litters your desk and the floor, while your bed is covered in dirty clothes you haven't feel like moving."
bedroom.interact = "Bed, Computer, Bookshelf"

hallway = Area()
hallway.name = "Hallway"
hallway.description = "A short hallway."
hallway.exits = "Bedroom, Bathroom, Stairs"
hallway.look = "There is spots of paint missing from the wall where paintings used to hang. Most of the photos got taken down after the divorce"
hallway.interact = "Plant"

bathroom = Area()
bathroom.name = "Bathroom"
bathroom.description = "A plain bathroom. It's cleaner then your room."
bathroom.exits = "Hallway"
bathroom.look = "The mirror on the wall taunts you, you feel a wave of dread come over you."
bathroom.interact = "Mirror"

stairs = Area()
stairs.name = "Stairs"
stairs.description = "You're always afriad of slipping"
stairs.exits = "Hallway, Living room"
stairs.look = "You look at the painting on the wall, but you don't know what it is."
stairs.interact = "There is nothing to interact with."

livingroom = Area()
livingroom.name = "Living room"
livingroom.description = "The living room seems darker then normal."
livingroom.exits = "Stairs, Kitchen, Yard,"

player_stats = {"Health": 100, "Stress": 0, "Money": 50}

if command == "stats":
    print(f"{name}'s stats. Health:{player_stats['Health']} Stress:{player_stats['Stress']} Money:{player_stats['Money']}")