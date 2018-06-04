from globalvars import *
import random
'''
INTRODUCTION
'''

print("Welcome to the game!")
print("You are traveling mercenary in a large valley called Tarenggel")
print("You heard from your hometown's tavern owner that Tarenggel needed help")
print("The great dragon Scethe the Scaleless was on the loose")
print("You show up and offer your help, but you don't have any equipment.")
commands()
print("Good luck on your journey traveler, and may you bring great honor to your name")

'''
"City"
"Forest"
"NWForest"
"Merchant"
"Blacksmith"
"Cave"
"Logger"
"Lakefront"
"Dungeon"
'''

    
'''
TRAVELING MECHANICS
'''
print("Would you like to start playing?")
print("Y / N")
command = input("")
if command == "Y" or command == "Y":
    game = on
elif command == "N" or command == "n":
    game = off
else:
    print("Yes or No, not " + command)
    print("Restart the game")
    game = off

while game == on:
#1    
    while location == "City":
        stars()
        print("You are in the City")
        print("You look around you and see that someone left a couple coins on the ground")
        if "gold" not in items:
            print("You can loot the area")
        print("To your NORTH is the forest.")
        print("To your SOUTH is a traveling Merchant")
        print("To your EAST is a hardworking Blacksmith.")
        print("To your WEST is a cave as old as the land itself")
        print("What would you like to do?")
        command = input("")
        stars()
        if command == "C" or command == "c":
            commands()
        if command == "N" or command == "n":
            print("You traveled North and came across a thick forest")
            location = "Forest"
        elif command == "S" or command == "s":
            print("You traveled South and stumbled into the camp of a shifty merchant, be aware")
            
            location = "Merchant"
        elif command == "E" or command == "e":
            print("You traveled East and came across the most accomplished blacksmith in the land, He can forge the best of the best, but for a price")
            location = "Blacksmith"
        elif command == "W" or command == "w":
            print("You traveled West and found a large Cave opening as tall as a building, and as dark as night. Old scaffolding from a mineshaft make it safe to walk in.")
            location = "Cave"
        elif command == "L" or command == "l":
            if "gold" not in items:
                print("You searched the area and found 1 GOLD")
                items.append("gold")
            else:
                print("You already searched the area")
        else:
            print("INVALID OPTION")

#2
    while location == "Forest":
        stars()
        stars()
        print("You are in a thick forest")
        print("There are many trees that with the right tool, you can harvest the trees for logs.")
        print("To the WEST is more forest, even thicker than the one you stand in now.")
        print("To the SOUTH is the capital city, Grand and luxurious, with lot's of shops and food to eat!")
        print("To the EAST is a lonely Logger, for a price, he will make you anything wood related")
        print("What would you like to do?")
        command = input("")
        stars()
        if command == "C" or command == "c":
            commands()
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
            location = "NWForest"
        elif command == "S" or command == "s":
            print("You travel SOUTH and enter the Capital City")
            location = "City"
        elif command == "E" or ocmmand == "e":
            print("You travel to the EAST and find a small log house")
            location = "Logger"
        else:
            print("INVALID OPTION")
#3
    while location == "NWForest":
        stars()
        stars()
        print("You are deep into the forest, visibility is very limited and very few trees are avaiable to chop down.")
        print("The trees in this land are thicker than the towers of a castle, and as tall as one.")
        print("This forest has been a boundary line for expansion of the city for years as it is too beautiful and too thick to clear")
        print("To the SOUTH is the mouth of the cave")
        print("To the EAST is more forest, thinner and younger than this portion.")
        print("You can search for a young tree to harvest.")
        print("What would you like to do?")
        command = input("")
        stars()
        if command == "C" or command == "c":
            commands()
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
#4
    while location == "Cave":
        stars()
        stars()
        print("You enter a cave, an old mineshaft shut down after an economic meltdown.")
        print("As you enter your eyes adjust and small amounts of light that make it throw expose nodes of metal")
        print("With the right tools, and a good amount of luck, you can harvest the metal")
        print("SOUTH of the cave is the lakefront of the prettiest lake you've ever layed eyes upon")
        print("To the NORTH is the old NWForest, with trees older than time itself")
        print("To the EAST is the capital city, bustling with activity")
        print("What would you like to do?")
        command = input("")
        stars()
        if command == "C" or command == "c":
            commands()
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
            location = "City"
        elif command == "N" or command == "n":
            print("You traveled NORTH into the NWForest, where the trees are older than the mountains surrounding it")
            location = "NWForest"
#5
    while location == "lakefront":
        stars()
        stars()
        print("You follow a path that leads to the beach of a beautiful lake.")
        print("There isn't much to do hear but it certainly is magnificent.")
        print("To the NORTH is the deep, dark cave, it's enterance as dark as night")
        print("To the EAST is a wandering Merchant, be careful around him as he may not be trusty")
        print("What would you like to do?")
        command = input("")
        if command == "C" or command == "c":
            commands()
        if command == "E" or command == "e":
            print("You walk EAST to the Merchant and sit down around the campfire.")
            location = "Merchant's Hut"
        elif command == "N" or command == "n":
            print("You walk NORTH to the cave, it's eeriness sends chills down your spine")
            location = "Cave"
#6
    while location == "Merchant":
        stars()
        stars()
        print("You are sitting around the campfire of a Traveling Merchant")
        print("He's willing to trade, but his prices may be expensive.")
        print("To the NORTH is the city center, as vibrant as ever")
        print("To the WEST is the lakefront, a nice place to relaxe")
        print("To the EAST you will find an old dungeon, the known lair of Scethe The Scaleless")
        print("What would you like to do?")
        command = input("")
        stars()
        if command == "C" or command == "c":
            commands()
        if command == "T" or command == "t":
            if "pickaxe" not in items and "log" in items:
                print("The Merchant offers you a pickaxe in exchange for a log for his fire. What a steal!")
                print("Would you like to trade?")
                print("Y / N")
                command = input("")
                if command == "Y" or command == "y":
                    print("You traded one log for a pickaxe")
                    print("It feels and looks sturdy, this should work well.")
                    print("You trade thanks and you sit down, planning your next move.")
                elif command == "N" or command == "n":
                    print("You didn't trade for the pickaxe")
                    print("The man glares at you with a frustrated face, claiming you wasted his precious time")
                    print("You sit back down and plan your next move.")
                else:
                    print("Invalid Option")
            else:
                print("The Merchant has no interest in trading with you if you don't have anything to bring to the table")
        if command == "N" or command == "n":
            print("You return NORTH and enter the city, blazing with activity")
            location = "City"
        if command == "W" or command == "w":
            print("You travel WEST and enter the lakefront")
            location = "lakefront"
        if command == "E" or command == "e":
            print("You walk EAST towards the lair of Scethe The Scaleless")
            print("You could swear that the temperature dropped 20 degrees in a couple seconds")
            location = "Dungeon"
        else:
            print("Invalid Option")
#7
    while location == "Dungeon":
        items.append("sword")
        print("You walk into the lair of Scethe The Scaleless, the infamous dragon that has been terrorising the land")
        print("The reason you're here.")
        print("You see the massive, scaleless dragon, sitting as if it was waiting for you")
        print("It notices you and prepares to attack")
        if "sword" in items:
            print("You have your trusty sword at your side.")
            print("do you want to attack or run?")
            print("A / R")
            command = input("")
            if command == "A" or command == "a":
                if "sword" in items:    
                    attack()
                    bossattack()
                    if bosshealth <= 0:
                        print("You Killed the dragon!")
                        print("You return back to the city with it's head in hand and a smile on your face.")
                        location = "City"
                        game = win
                    elif health <= 0:
                        print("The dragon killed you.")
                        print("Your quest has come to a conclusion.")
                        location = "City"
                        game = lose
                else:
                    print("You can't fight.")

            else:
                print("You decide to leave the dragon's dungeon.")
                print("You remember the Blacksmith being north of here")
                print("and the merchan'ts hut is to the east")
                print("What would you like to do?")
                command = input("")
                if command == "N" or command == "n":
                    print("You traveled north to the Blacksmith, the best in the land")
                    print("He will make you one hell of a blade, for a price.")
                    location = "Blacksmith"
                elif command == "W" or command == "w":
                    print("You walk WEST to the camp of a traveling merchant.")
                    print("He loves to barder and will trade just about any trinket he owns")
                    location = "Merchant"
                else:
                    print("Invalid Option")
    while location == "Blacksmith":
        print("You walk into the shop of strong blacksmith.")
        print("He makes the best in the land. Known for his swords and armor.")
        print("To the north is the Logger's hut, he'll trade you for the best axes in the land")
        print("To the West is the City, bustling with activity as always, day and night")
        print("To the South is the evil layer of Scethe the scaleless, out for blood")
        if "metal" in items:
            print("You could  trade your metal for a sword to fight the dragon")
            print("
            
                    
                
            
