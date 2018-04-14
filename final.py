'''
Basic Definitions:
test
'''
import random
items = []

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
huntershack = "Hunter's Shack"
blacksmith = "Blacksmith's shop"
cave = "Mined out Cave"
lakefront = "Lakefront"
merchanthut = "Merchant Hut"
bossdungeon = "Dragon's Dungeon"

command = ""

location = city

items.append("sword")
'''
TRAVELING MECHANICS
'''
while game == on:
    while location == city:
        print("You are in the " + location)
        print("To the North there is a Forest")
        print("To the South is a travelling merchant's hut")
        print("To the West is a Blacksmith's shop")
        print("To the East is an abandoned mineshaft")
        print("Where would you like to go?")
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
        else:
            print("Invalid Option")
            
    while location == forest:
        print("You are in the " + location)
        print("To the South is the City")
        print("To the West is more forest")
        print("To the East is the Hunter's shack")
        print("Where would you like to go?")
        print("Choose your direction using S , W , or E.")
        command = input("")
        if command == "S" or command == "s":
            location = city
            print("You have traveled to the " + location)
        elif command == "W" or command == "w":
            location = forest_nw
            print("You have traveled to the " + location)
        elif command == "E" or command == "e":
            location = huntershack
            print("You have traveled to the " + location)
        else:
            print("Invalid Option")

    while location == forest_nw:
        print("You are in the " + location)
        print("To the South is the Cave")
        print("To the East is the Forest")
        print("Where would you like to go?")
        print("Choose your direction using S ,  or E.")
        command = input("")
        if command == "S" or command == "s":
            location = cave
            print("You have traveled to the " + location)
        elif command == "E" or command == "e":
            location = forest
            print("You have traveled to the " + location)
        else:
            print("Invalid Option")

    while location == cave:
        print("You're in the " + location)
        print("To the South is the lake front")
        print("To the North is the Northwestern Forest")
        print("To the West is the City center")
        print("Where would you like to go?")
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

    while location == lakefront:
        print("You're in the " + location)
        print("To the North is the Cave")
        print("To the West is the Merchant's hut")
        print("Where would you like to go?")
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

    while location == merchanthut:
        print("You are in the " + location)
        print("To the North is the City")
        print("To the West is the Lake Front")
        print("To the East is the Boss' Dungeon")
        print("Where would you like to go?")
        print("Choose your direction using N, W, or E")
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
        else:
            print("Invalid Option")

    while location == huntershack:
        print("You are in the " + location)
        print("To the West is the Forest")
        print("To the South is the Blacksmith's Shop")
        print("Where would you like to go?")
        print("Choose your direction using W , or S")
        command = input("")
        if command == "S" or command == "s":
            location = blacksmith
            print("You have traveled to the " + location)
        elif command == "W" or command == "w":
            location = forest
            print("You have traveled to the " + location)
        else:
            print("Invalid Option")

    while location == blacksmith:
        print("You are in the " + location)
        print("To the West is the City")
        print("To the South is the Boss Dungeon")
        print("To the North is the Hunter's Shack")
        print("Where would you like to go?")
        print("Choose your direction using N , S , or W")
        command = input("")
        if command == "S" or command == "s":
            location = bossdungeon
            print("You have traveled to the " + location)
        elif command == "W" or command == "w":
            location = city
            print("You have traveled to the " + location)
        elif command == "N" or command == "n":
            location = huntershack
            print("You have traveled to the " + location)
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
                print("Where would you like to go?")
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
            else:a
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

    
    
