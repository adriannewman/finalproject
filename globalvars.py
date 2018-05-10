import random
items = []
on = 90
off = 91
game = on
command = ""

health = 5
damage = 5
bossdamage = 1
bosshealth = 25
location = "City"

#combat defs:

def attack():
    attackhit = random.randint(1,3)
    if attackhit == 1 or attackhit == 2:
        print("You hit the dragon, dealing 5 damage")
        bosshealth = bosshealth - damage
        print(bosshealth)
    elif attackhit == 3:
        print("Your attack missed!")

def bossattack():
    bossattackhit = random.randint(1,5)
    if bossattackhit == 1 or bossattackhit == 2:
        print("The dragon hit you and dealt 1 damage")
        health = health - bossdamage
        print(health)
    elif bossatackhit == 3 or bossatackhit == 4 or bossatackhit == 5:
        print("The Dragon's attack missed!")
    




def stars():
    print("*")
    print("*")
    print("*")
    print("*")
 
    
def commands():
    print("COMMANDS:")
    print("S for SOUTH")
    print("N for NORTH")
    print("E for EAST")
    print("W for WEST")
    print("H for HARVEST")
    print("Ex for EXPLORE")
    print("T for TRADE / BUY")
    print("A for ATTACK")
    print("R for RUN")
    print("C for COMMANDS")
    print("Be warned, these commands are situational")
    print("Should only be used when they are useful")
    
