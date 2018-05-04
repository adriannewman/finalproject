'''
INTRODUCTION
'''

print("Welcome to the game!")
print("You are traveling mercenary in a large valley called Tarenggel")
print("You heard from your hometown's tavern owner that Tarenggel needed help")
print("The great dragon Scethe the Scaleless was on the loose")
print("You show up and offer your help, but you don't have any equipment.")
print("You can Loot the area using 'L'")
print("You can harvest maaterials in an area with 'H' if you have the required tool")
print("You can Travel using N / W / S / E")
print("Good lcuk on your journey traveler, and may you bring great honor to your name")



'''
BASIC DEFINITIONS
'''
import random
items = []
on = 90
off = 91
game = on
command = ""

location = "City"

'''
TRAVELING MECHANICS
'''

while game == on:
    while location == "City":
        print("You are in the City")
        print("You look around you and see that someone left a couple coins on the ground")
        print("You can loot the area")
        print("To your NORTH is the forest.")
        print("To your SOUTH is a traveling merchant's camp")
        print("To your EAST is a hardworking blacksmith's Shop.")
        print("To your WEST is a cave as old as the land itself")
        print("What would you like to do?")
        command = input("")
        if command == "N" or command == "n":
            print("You traveled North and came across a thick forest")
            location = "Forest"
        elif command == "S" or command == "s":
            print("You traveled South and stumbled into the camp of a shifty merchant, be aware")
            location = "Merchant's Camp"
        elif command == "E" or command == "e":
            print("You traveled East and came across the most accomplished blacksmith in the land, He can forge the best of the best, but for a price")
            location = "Blacksmith's Shop"
        elif command == "W" or command == "w":
            print("You traveled West and found a large Cave opening as tall as a building, and as dark as night. Old scaffolding from a mineshaft make it safe to walk in.")
            location = "Cave"
        elif command == "L" or command == "l":
            if "gold" not in inventory:
                print("You searched the area and found 1 GOLD")
                items.append("gold")
            else:
                print("You already searched the area")
        else:
            print("INVALID OPTION")


    while location == "Forest"
        print("You are in a thick forest")
        print("There are many trees that with the right tool, you can harvest the trees for logs.")
        print("To the WEST is more forest, even thicker than the one you stand in now.")
        print("To the SOUTH is the capital city, Grand and luxurious, with lot's of shops and food to eat!")
        print("To the EAST is a lonely logger's hut, for a price, he will make you anything wood related")
        print("What would you like to do?")
        command = input("")
        if command == "H" or command == "h":
            if "axe" in items:
                print("You can harvest a recently felled tree to get a log")
                print("Would you like to do so?")
                print("Y / N")
                command = input("")
                if command == "Y" or command == "y":
                    print("You chopped tirelessly at the recently felled tree, and finally manage to get a usable log from the trunk.")
                    items.append("log")
                elif command == "N" or command == "n":
                    print("You did not harvest the wood")
                else:
                    print("Invalid Option")
        elif command == "W" or command == "w":
            print("You travel WEST, deeper into the forest, visibilty is limited and the trees appear to be very old; This land has been untouched for hundreds of years.")
            location = "Northwestern Forest"
        elif command == "S" or command == "s":
            print("You travel SOUTH and enter the Capital City")
            location = "City"
        elif command == "E" or ocmmand == "e":
            print("You travel to the EAST and find a small log house")
            location = "Logger's Hut"
        else:
            print("INVALID OPTION")

    while location == "Northwestern Forest":
        print("You are deep into the forest, visibility is very limited and very few trees are avaiable to chop down.")
        print("The trees in this land are thicker than the towers of a castle, and as tall as one.")
        print("This forest has been a boundary line for expansion of the city for years as it is too beautiful and too thick to clear")
        print("To the SOUTH is the mouth of the cave")
        print("To the EAST is more forest, thinner and younger than this portion.")
        print("You can search for a young tree to harvest.")
        print("What would you like to do?")
        command = input("")
        if command == "H" or command == "h":
            findtree = random.randint(1,3)
            if findtree > 3:
                print("You found a small tree")
                if "axe" in items:
                    print("You can harvest the tree")
                    print("Y / N")
                    command = input("")
                    if command == "Y" or command == "y":
                        print("You chopped down the small tree and cut it into smaller chunks to carry on you")
                        items.append("log")
                    elif command == "N" or command == "n":
                        print("You did not chop down the tree")
                    else:
                        print("INVALID OPTION")
                else:
                    print("You don't have the required tool to chop down the tree, come back with an AXE")
            else:
                print("You could not find a small enough tree to harvest in the area, try your luck again")
        elif command == "S" or command == "s":
            print("You traveled West and found a large Cave opening as tall as a building, and as dark as night. Old scaffolding from a mineshaft make it safe to walk in.")
            location = "Cave"
        elif command == "E" or command == "e":
            print("You travel out of the thick forest, back towards the EAST and the trees begin to thin")

    while location = "Cave":
        print("You enter a cave, an old mineshaft shut down after an economic meltdown.")
        print("As you enter your eyes adjust and small amounts of light that make it throw expose nodes of metal")
        print("With the right tools, and a good amount of luck, you can harvest the metal")
        print("SOUTH of the cave is the lakefront of the prettiest lake you've ever layed eyes upon")
        print("To the NORTH is the old Northwestern Forest, with trees older than time itself")
        print("To the EAST is the capital city, bustling with activity")
        print("What would you like to do?")
        command = input("")
        if command == "H" or command == "h":
            if "pickaxe" in items:
                findnode = random.randint(1,5)
                if findnode > 3:
                    print("You see a sparking light and investigate it")
                    print("It's a metal node!")
                    print("Would you like to mine it?")
                    print("Y / N")
                    command = input("")
                    if command == "Y" or command == "y":
                        print("You mined the node, being sure not to hit your foot as you mine")
                        items.append("metal")
                    elif command == "N" or command == "n":
                        print("You chose to stay safe and avoided hitting your toe with a pickaxe")
                        print("You walked away, leaving the node behind")
                    else:
                        print("INVALID COMMAND")
                else:
                    print("You searched and searched but couldn't find any nodes in the area.")
            else:
                print("There's no point in searching for a node if you don't have a pickaxe!")
        elif command == "S" or command == "s":
            print("You traveled SOUTH and stumbled across a beach that puts heaven to shame.")
            location = "lakefront"
        elif command == "E" or command == "e":
            print("You walked EAST back into the capital city. As you enter a man tells you to try out the fish")
            location = "City")
        elif command == "N" or command == "n":
            print("You traveled NORTH into the Northwestern Forest, where the trees are older than the mountains surrounding it")
            location = "Northwestern Forest")

    while location = "lakefront":
        print("You follow a path that leads to the beach of a beautiful lake.")
        print("
        
            
            
            




        
        
