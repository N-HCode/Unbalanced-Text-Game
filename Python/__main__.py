

import sys #Default built in module that let you add more pathways for modules
import os #Default built in module that let you find current pathway

    

#print(sys.path)
import overworld
import random
import fighting
from Class import Player
import monsters

print("Hello")

start = overworld.question("Do you wish to start the game?")

def game(start):
    print("Look at this game")
    x = 20
    y = 20
    location = [x, y]
    battle = False
    Encounter_rate = [1,2,3]
    min_rate =1
    max_rate =20
    name = input("Enter your name\n")
    player = Player(name)

    print("\nlet us start this adventure " + name +"!\n")
    print("You can move by typing a, s, d, or w then hitting enter")
    print("commands: inv, equip(e), equipment(ee), use(u), stat, inspect (equip/items) (ie/ii). Use /help to get these commands again")
    print("I try to make the command the first letter, so you can try that. ")
    print("\nhint: go to (21,21) and talk to the shopkeeper a couple of times\n")

    while start == True and battle == False:

        overworld.map(player,x,y)

        action = str.lower(input())

        if action in ["location", "check location", "here"]:
            print("Current position", location)
        if action in ["quit game", "quit"]:
            print("Quiting Game")
            start = False
        if action in ["w", "up", "north"]:
            y = y + 1
            location = [x, y]
            print(location)
            Encounter = random.randint(min_rate,max_rate)
            #print(Encounter)
            if Encounter in Encounter_rate:
                battle = True

        if action in ["s", "down", "south"]:
            y -= 1
            location = [x, y]
            print(location)
            Encounter = random.randint(min_rate,max_rate)
            #print(Encounter)
            if Encounter in Encounter_rate:
                battle = True

        if action in ["d", "right", "east"]:
            x += 1
            location = [x, y]
            print(location)
            Encounter = random.randint(min_rate,max_rate)
            #print(Encounter)
            if Encounter in Encounter_rate:
                battle = True

        if action in ["a", "left", "west"]:
            x -= 1
            location = [x, y]
            print(location)
            Encounter = random.randint(min_rate,max_rate)
            #print(Encounter)
            if Encounter in Encounter_rate:
                battle = True

        if action in ["stat","stats","Stat","Stats","Status"]:
            stats = vars(player) #stores the attribute
            print("name :",stats["name"], "|exp :",stats["exp"], "|level :",stats["level"], "|hp :",stats["hp"],"/",stats["maxhp"], "|str :",stats["str"], "|int :",stats["int"], "|def :",stats["defense"], "|atk :",stats["atk"], "|dex :",stats["dex"], "|gold :", stats["gold"])
            #print (", ".join("%s: %s" % item for item in stats.items()) #print the attributes
        if action in ["inv"]:
            stats = vars(player)
            print("|equipment :",stats["inv"])
            print("|items :", stats["uinv3"])
            #print("|items :", stats["uinv2"])
            #print("|items :", stats["uinv"])
           # print("|items :", player.uinv2[0].stack)

        if action in ["equip","e"]:
            player.equip()

        if action in ["equipment","ee"]:
            player.equipment()
        
        if action in ["use","u"]:
            try:
                player.use()
            except:
                print("Not sure what you're trying to use")
        if action in ["inspect equip","inspect equips","inspect item", "inspect equipment","inspect equipments","inspect items", "ii","ie"]:
            if action in ["inspect equip","inspect equips","inspect equipment", "inspect equipments", "ie"]:
                for p in range(len(player.inv)):
                    #print("|{}|{}|{}".format(x,  str(player.vinv[x].atk) + " atk" if player.vinv[x].atk > 0 else str(player.vinv[x].deff) + " def", player.vinv[x].name))
                    print("|{}|{}:{}|{}".format(p,"atk:" + str(player.vinv[p].atk), "def:" + str(player.vinv[p].deff), player.vinv[p].name))
            if action in ["inspect item","inspect items", "ii"]:
                for p in range(len(player.uinv)):
                    print("|{}|{}|{}".format(p, player.uinv[p], player.uinv2[p].desc))
                    
            
        if action in ["/help","help"]:
            print("commands: inv(i), equip(e), equipment(ee), use(u), stat, inspect (equip/items)(ie/ii) you can use ii or ie")
            print("For some things I use the first letter to make things easier")

        if battle == True:
            battle = fighting.Fighting(battle, player, x, y)
            


def game_start(start):
    if start == True:
        print("Alright lets start")
        game(start)
    else:
        print("goodbye")
        raise SystemExit

game_start(start)