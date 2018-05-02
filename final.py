'''
Basic Definitions:
test
'''
import random
items = []

#Item DEFINITIONS
gold  = 1
log = 2
metal = 3
axe = 4
pickaxe = 5
sword = 6

on = 90

off = 91
win = 92
lose = 93
game = on
alive = True
'''
Defining all the locations:
'''
city = "City"
forest = "Forest"
forest_nw = "Northwestern Forest"
logger = "Logger's Shack"
blacksmith = "Blacksmith's shop"
cave = "Mined out Cave"
lakefront = "Lakefront"
merchanthut = "Merchant Hut"
bossdungeon = "Dragon's Dungeon"

command = ""

location = city

items.append(log)
'''
TRAVELING MECHANICS
'''

'''
CITY
'''
while game == on:
    while location == city:
        print("You are in the " + location)
        print("To the North there is a Forest")
        print("To the South is a travelling merchant's hut")
        print("To the West is a Blacksmith's shop")
        print("To the East is an abandoned mineshaft")
        print("Input using N , W , S , or E")
        command = input("")
        if command == "N" or command == "n":
            location = forest
            print("You have traveled to the " + location)
        elif command == "S" or command == "s":
            location = merchanthut
            print("You have traveled to the " + location)
        elif command == "E" or command == "e":
            location = blacksmith
            print("You have traveled to the " + location)
        elif command == "W" or command == "w":
            location = cave
            print("You have traveled to the " + location)
        elif command == "EX" or command == "ex" or command == "eX" or command == "Ex":
            if "gold" not in items:
                print("You can explore the area for gold")
                print("Y / N")
                command = input("")
                if command == "Y" or command == "y":
                    print("You explored the area and found one peice of gold.")
                    items.append("gold")
                elif command == "N" or command == "n":
                    print("You didn't explore")
                else:
                    print("Invalid Option")
            else:
                print("You've already explored!")
        else:
            print("Invalid Option")
    while location == forest:
        print("You are in the " + location)
        print("To the South is the City")
        print("To the West is more forest")
        print("To the East is the Logger's Shack")
        
        print("Choose your direction using S , W , or E.")
        command = input("")
        if command == "S" or command == "s":
            location = city
            print("You have traveled to the " + location)
        elif command == "W" or command == "w":
            location = forest_nw
            print("You have traveled to the " + location)
        elif command == "E" or command == "e":
            location = logger
            print("You have traveled to the " + location)
        elif command == "H" or command == "h":
            if "log" not in items:
                print("You can harvest wood")
                print("Y / N")
                command = input("")
                if command == "Y" or command == "y":
                    print("You harvested wood")
                    items.append("log")
                elif command == "N" or command == "n":
                    print("You didn't harvest wood")
                else:
                    print("Invalid Option")
            else:
                print("You already harvested from this location! Try another one")
        else:
            print("Invalid Option")
#NORTHWEST FOREST
    while location == forest_nw:
        print("You are in the " + location)
        print("To the South is the Cave")
        print("To the East is the Forest")
        
        print("Choose your direction using S ,  or E.")
        command = input("")
        if command == "S" or command == "s":
            location = cave
            print("You have traveled to the " + location)
        elif command == "E" or command == "e":
            location = forest
            print("You have traveled to the " + location)
        elif command == "H" or command == "h":
            if "log" not in items:
                print("You can harvest wood")
                print("Y / N")
                command = input("")
                if command == "Y" or command == "y":
                    print("You harvested wood")
                    items.append("log")
                elif command == "N" or command == "n":
                    print("You didn't harvest wood")
                else:
                    print("Invalid Option")
            else:
                print("You already harvested from this location! Try another one")
        else:
            print("Invalid Option")
#CAVE
    while location == cave:
        print("You're in the " + location)
        print("To the South is the lake front")
        print("To the North is the Northwestern Forest")
        print("To the West is the City center")
        
        print("Choose your direction using N , S , or E")
        command = input("")
        if command == "S" or command == "s":
            location = lakefront
            print("You have traveled to the " + cave)
        elif command == "N" or command == "n":
            location = forest_nw
            print("You have traveled to the " + cave)
        elif command == "E" or command == "e":
            location = city
        else:
            print("Invalid Option")
#LAKEFRONT
    while location == lakefront:
        print("You're in the " + location)
        print("To the North is the Cave")
        print("To the West is the Merchant's hut")
        
        print("Choose your direction using N or E")
        command = input("")
        if command == "N" or command == "n":
            location = cave
            print("You have traveled to the " + location)
        elif command == "E" or command == "e":
            location = merchanthut
            print("You have traveled to the " + location)
        else:
            print("Invalid Option")
#MERCHANT HUT
    while location == merchanthut:
        print("You are in the " + location)
        print("To the North is the City")
        print("To the West is the Lake Front")
        print("To the East is the Boss' Dungeon")
       
        command = input("")
        if command == "N" or command == "n":
            location = city
            print("You have traveled to the " + location)
        elif command == "W" or command == "w":
            location = lakefront
            print("You have traveled to the " + location)
        elif command == "E" or command == "e":
            location = bossdungeon
            print("You have traveled to the " + location)
        elif command == "t" or command == "T":
            if "log" in items:
                print("You can purchase an pickaxe")
                print("The axe will cost 'log'")
                print("Would you like to purchase the pickaxe?")
                print("Y / N")
                command = input("")
                if command == "Y" or command == "y":
                    print("You have purchased the pickaxe!")
                    items.remove("log")
                    items.append("pickaxe")
                elif command == "N" or command == "n":
                    print("You didn't purchase the pickaxe..")
                else:
                    print("Invalid option")
                
        else:
            print("Invalid Option")
          
    while location == logger:
        print("You are in the " + location)
        print("To the West is the Forest")
        print("To the South is the Blacksmith's Shop")
        
        print("Choose your direction using W , or S")
        
        command = input("")
        if command == "S" or command == "s":
            location = blacksmith
            print("You have traveled to the " + location)
        elif command == "W" or command == "w":
            location = forest
            print("You have traveled to the " + location)
        elif command == "T" or command == "t":
            if "gold" in items:
                print("You can purchase the the axe")
                print("It will cost 1 gold")
                print("Y / N")
                command = input("")
                if command == "Y" or command == "y":
                    print("You purchased the axe")
                    items.remove("gold")
                    items.append("axe")
                    print(items)
                elif command == "N" or command == "n":
                    print("You didn't purchase the axe")
            else:
                print("You can't purchase the axe")
        else:
            print("Invalid Option")

    while location == blacksmith:
        print("You are in the " + location)
        print("To the West is the City")
        print("To the South is the Boss Dungeon")
        print("To the North is the Logger's Shack")
        command = input("")
        if command == "S" or command == "s":
            location = bossdungeon
            print("You have traveled to the " + location)
        elif command == "W" or command == "w":
            location = city
            print("You have traveled to the " + location)
        elif command == "N" or command == "n":
            location = logger
            print("You have traveled to the " + location)
        elif command == "t" or command == "T":
            if "metal" and "log" in items:
                print("You have enough resources to purchase a sword!")
                print("It costs one metal and one log")
                print("Y / N")
                command == input("")
                if command == "Y" or command == "y":
                    print("You purchased the sword!")
                    items.remove("metal")
                    items.remove("log")
                    items.append("sword")
                    print(items)
                elif command == "N" or command == "n":
                    print("You didn't buy the sword.. ")
                else:
                    print("Invalid Option")
        else:
            print("Invalid Option")

    while location == bossdungeon:
        if "sword" in items:
            print("You can fight the dragon!")
            print("To fight it, type A or Attack")
            print("To Run, type R or Run")
            print("What would you like to do?")
            command = input("")
            if command == "A" or command == "a" or command == "Attack" or command == "attack":
                battle = random.randint(1,2)
                if battle == 1:
                    print("You killed the Dragon!")
                    print("You return to the City, to claim your prize for slaying the Dragon that has terrorized the land")
                    location = city
                    game = win
                elif battle == 2:
                    print("You were killed.")
                    game = lose
            elif command == "R" or command == "r" or command == "Run" or command == "run":        
                print("You are in the " + location)
                print("To the North is the Blacksmith Shop")
                print("To the West is the Merchant's hut")
                
                print("Choose your direction using N or W")
                command = input("")
                if command == "N" or command == "n":
                    location = blacksmith
                    print("You have traveled to the " + location)
                elif command == "W" or command == "w":
                    location = merchanthut
                    print("You have traveled to the " + location)
                else:
                    print("Invalid Option")
            else:
                print("Invalid Option")



'''
GAME FINISH MECHANICS
'''
while game == win:
    game = off
    print("''''''''''''''''''''''''''''''''''''''''''''''")
    print("''''''''''''''''''''''''''''''''''''''''''''''")
    print("''''''''''''''''''''''''''''''''''''''''''''''")
    print("You have completed the game!")
    print("Feel free to restart and do it again!")

while game == lose:
    game = off
    print("''''''''''''''''''''''''''''''''''''''''''''''")
    print("''''''''''''''''''''''''''''''''''''''''''''''")
    print("''''''''''''''''''''''''''''''''''''''''''''''")
    print("You have lost.")
    print("Restart to try again")

    
    
