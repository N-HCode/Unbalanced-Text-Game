import sys
import os
import random
from monsters import*
from time import sleep




def Fighting(battle, player, x, y):

    Monster = spawn(x,y)
    #Mstats = vars(Monster)

    while battle == True:
        print("\n| %s : %s/%s " % (player.name, str(player.hp),str(player.maxhp)))
        print("|[{}][{}][{}]".format("Atk","Use","Run"))

        if player.hp <= 0:
            "You Died"
            raise SystemExit

        action = str.lower(input())

        if action in ["check monster", "chk", "check"]:
            #print (Mstats)
            print("|name: %s |hp: %s |des: %s" % (Monster.name, str(Monster.hp), Monster.des))
        if action in ["atk","hit","fight","attack", "a"]:
            damage = player.atk
           
            print("\n" + str(Monster.name) + " received " + str(damage) + " damage!\n" )
            Monster.hp = Monster.hp - damage

            Monster.cry()

            if Monster.hp > 0:
                Monster.attack(player)

        if Monster.hp <= 0:
            print(str(Monster.name) + " was defeated! You gained " + str(Monster.exp) + " exp!")
            print("You got %s gold!" % (str(Monster.gold)))
            player.get_loot(Monster.item)
            player.gold = player.gold + Monster.gold     
            player.exp = player.exp + Monster.exp
            player.lvlup(player.exp, player.level)
            return False
        
        if action in ["use", "u", "item", "items", "use item", "use items"]:
            try:
                player.use()
            except:
                continue
            
            Monster.attack(player)

        if action in ["run","escape","get on outta here", "r"]:
            escape = random.randint(1,10)
            attempt_escape = 1
            if attempt_escape == escape:
                print("You ran away successfully!")
                return False
            else:
                print("You couldn't escape")
                Monster.attack(player)

#-----------------------------------
def final_fight(Monster, player):


    battle = True

    while battle == True:
        print("\n| %s : %s/%s " % (player.name, str(player.hp),str(player.maxhp)))
        print("|[{}][{}][{}]".format("Atk","Use","Run"))

        if player.hp <= 0:
            "You Died"
            raise SystemExit

        action = str.lower(input())

        if action in ["check monster", "chk", "check"]:
            #print (Mstats)
            print("|name: %s |hp: %s |des: %s" % (Monster.name, str(Monster.hp), Monster.des))
        if action in ["atk","hit","fight","attack", "a"]:
            damage = player.atk
           
            print("\n" + str(Monster.name) + " received " + str(damage) + " damage!\n" )
            Monster.hp = Monster.hp - damage

            Monster.cry()

            if Monster.hp > 0:
                Monster.attack(player)

        if Monster.hp <= 0:
            Monster = spawn_lboss2()
            battle = final_fight2(battle, Monster, player)
            
        
        if action in ["use", "u", "item", "items", "use item", "use items"]:
            try:
                player.use()
            except:
                continue
            
            Monster.attack(player)

            if action in ["run","escape","get on outta here"]:
                print("Nah, you ain't backing down now")
                
def final_fight2(battle, Monster, player):

    while battle == True:
        print("\n| %s : %s/%s " % (player.name, str(player.hp),str(player.maxhp)))
        print("|[{}][{}][{}]".format("Atk","Use","Run"))

        if player.hp <= 0:
            "You Died"
            raise SystemExit

        action = str.lower(input())

        if action in ["check monster", "chk", "check","c"]:
            #print (Mstats)
            print("|name: %s |hp: %s |des: %s" % (Monster.name, str(Monster.hp), Monster.des))
        if action in ["atk","hit","fight","attack", "a"]:
            damage = player.atk
           
            print("\n" + str(Monster.name) + " received " + str(damage) + " damage!\n" )
            Monster.hp = Monster.hp - damage

            Monster.cry()

            if Monster.hp > 0:
                Monster.attack(player)

        if Monster.hp <= 0:
            print(str(Monster.name) + " was defeated! You gained " + str(Monster.exp) + " exp!")
            print("You got %s gold!" % (str(Monster.gold)))
            player.get_loot(Monster.item)
            player.gold = player.gold + Monster.gold     
            player.exp = player.exp + Monster.exp
            player.lvlup(player.exp, player.level)
            
            print("Congrats you won the game! Thank you for playing!\n\n\n\n")
            sleep(20)
            raise SystemExit
            return False
        
        if action in ["use", "u", "item", "items", "use item", "use items"]:
            try:
                player.use()
            except:
                continue
            
            Monster.attack(player)

            if action in ["run","escape","get on outta here"]:
                print("Nah, you ain't backing down now")
                
def Midboss(Monster, player):
    battle = True
    
    while battle == True:
        print("\n| %s : %s/%s " % (player.name, str(player.hp),str(player.maxhp)))
        print("|[{}][{}][{}]".format("Atk","Use","Run"))

        if player.hp <= 0:
            "You Died"
            raise SystemExit

        action = str.lower(input())

        if action in ["check monster", "chk", "check"]:
            #print (Mstats)
            print("|name: %s |hp: %s |des: %s" % (Monster.name, str(Monster.hp), Monster.des))
        if action in ["atk","hit","fight","attack", "a"]:
            damage = player.atk
           
            print("\n" + str(Monster.name) + " received " + str(damage) + " damage!\n" )
            Monster.hp = Monster.hp - damage

            Monster.cry()

            if Monster.hp > 0:
                Monster.attack(player)

        if Monster.hp <= 0:
            Monster.defeat()
            print(str(Monster.name) + " was defeated! You gained " + str(Monster.exp) + " exp!")
            print("You got %s gold!" % (str(Monster.gold)))
            player.get_loot(Monster.item)
            player.gold = player.gold + Monster.gold     
            player.exp = player.exp + Monster.exp
            player.lvlup(player.exp, player.level)
            
            battle = False
            return 1
        
        if action in ["use", "u", "item", "items", "use item", "use items"]:
            try:
                player.use()
            except:
                continue
            
            Monster.attack(player)

        if action in ["run","escape","get on outta here","r"]:
            print("Can't, you just can't")