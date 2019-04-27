import random
from time import sleep
import sys

class Player:


    def __init__(self, name):

        self.name = name
        self.exp = 0
        self.level = 0
        self.maxhp = 100
        self.hp = 100
        self.str = 0
        self.int = 0
        self.defense = 0
        self.atk = 7
        self.dex = 0
        self.gold = 0
        self.inv = []
        self.uinv = []
        self.uinv2 = []
        self.uinv3 = []
        self.vinv = []
        self.rhand = None
        self.head = None
        self.body = None
        self.leg = None
        self.lhand = None

    def lvlup(self, exp, level):
        lvl = [50,100,300,400,800,1500,3000,5000,8000,12000,15000,20000,25000,32000,40000,50000,62000,80000,100000,130000]
        if len([x for x in lvl if exp > x]) > level:
            lvl_to = len([x for x in lvl if exp > x])

            self.maxhp = self.maxhp + 50 * (lvl_to - self.level)
            self.hp = self.hp + 50 * (lvl_to - self.level)
            self.str = self.str + 1 * (lvl_to - self.level)
            self.int = self.int + 1 * (lvl_to - self.level)
            self.defense = self.defense + 1 * (lvl_to - self.level)
            self.atk = self.atk + 2 * (lvl_to - self.level)
            self.dex = self.dex + 1 * (lvl_to - self.level)

            self.level = lvl_to

            print("You leveled up to " + str(lvl_to))


    def get_loot(self, item):
        if item != None:
            for loot in range(len(item)):
                chance = random.randint(1,item[loot].rarity)
                #print("This was your chance" + str(chance))
                
                if chance == 1:
                
                    if item[loot].equipable == True:
                        #Equipments:: name, atk, deff, equipable, place, price, desc, rarity
                        c = item[loot]
                        looted = equipitem(c.name, c.atk, c.deff, c.equipable, c.place, c.price, c.desc, c.rarity)
                        looted.reroll(random.randint(round(looted.atk * .8), round(looted.atk * 1.2)), random.randint(round(looted.deff * .8), round(looted.deff * 1.2)))
                        print("You got equipable item " + str(looted.name) +"!")
                        self.inv.append(looted.name)
                        self.vinv.append(looted)
                    if item[loot].equipable == False:
                        print("You got usable item " + str(item[loot].name) +"!")
                    #try:
                        if item[loot].name in vars(self)["uinv"]:
                            index = vars(self)["uinv"].index(item[loot].name)
                            self.uinv2[index].increase_stack(self, index)
                    #except:
                        else:
                            self.uinv.append(item[loot].name)
                            self.uinv2.append(item[loot])
                            self.uinv3.append(item[loot].uname)
                            
    def buying(self, item):
        if item != None:
            if item.equipable == True:
                #Equipments:: name, atk, deff, equipable, place, price, desc, rarity
                looted = item
                print("You got " + str(looted.name) +"!\n")
                self.inv.append(looted.name)
                self.vinv.append(looted)
            if item.equipable == False:
                print("You got " + str(item.name) +"!\n")
            #try:
                if item.name in vars(self)["uinv"]:
                    index = vars(self)["uinv"].index(item.name)
                    self.uinv2[index].increase_stack(self, index)
            #except:
                else:
                    self.uinv.append(item.name)
                    self.uinv2.append(item)
                    self.uinv3.append(item.uname)
    def equip(self):

        #print (", ".join("%s " % item for item in self.inv))
        print(list(enumerate(self.inv)))
        try:
            equip = int(input("what would you like to equip or chk? (enter the number) "))

            if self.vinv[equip].place == 'hand':

                which_hand = str.lower(input("which hand?(right or left)"))

                if which_hand in ["left","l"]:
                    if self.lhand != None:

                        print("You already have " + self.lhand.name +" equipped.")
                        print("Name:{} | Atk:{} Def:{} | Desc:{}".format(self.lhand.name,self.lhand.atk,self.lhand.deff,self.lhand.desc))
                        print("Name:{} | Atk:{} Def:{} | Desc:{}".format(self.vinv[equip].name,self.vinv[equip].atk,self.vinv[equip].deff,self.vinv[equip].desc))
                        equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                        if equip_that in ["yes","y","equip"]:
                            self.inv.append(self.lhand.name)
                            self.vinv.append(self.lhand)

                            self.defense = self.defense + (self.vinv[equip].deff - self.lhand.deff)
                            self.atk = self.atk + (self.vinv[equip].atk - self.lhand.atk)

                            self.lhand = self.vinv[equip]

                            del self.inv[equip]
                            del self.vinv[equip]
                            print("equipped "+self.lhand.name)
                        return

                    else:
                        print("Name:{} | Atk:{} Def:{} | Desc:{}".format(self.vinv[equip].name,self.vinv[equip].atk,self.vinv[equip].deff,self.vinv[equip].desc))

                        equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                        if equip_that in ["yes", "y"]:
                            self.lhand = self.vinv[equip]
                            self.defense = self.defense + self.lhand.deff
                            self.atk = self.atk + self.lhand.atk
                            del self.inv[equip]
                            del self.vinv[equip]
                            print("equipped "+self.lhand.name)
                        return
        #--------------------------------------------------------------------
                if which_hand in ["right","r"]:
                    if self.rhand != None:

                        print("You already have " + self.rhand.name +" equipped.")
                        print("Name:{} | Atk:{} Def:{} | Desc:{}".format(self.rhand.name,self.rhand.atk,self.rhand.deff,self.rhand.desc))
                        print("Name:{} | Atk:{} Def:{} | Desc:{}".format(self.vinv[equip].name,self.vinv[equip].atk,self.vinv[equip].deff,self.vinv[equip].desc))
                        equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                        if equip_that in ["yes","y","equip"]:
                            self.inv.append(self.rhand.name)
                            self.vinv.append(self.rhand)

                            self.defense = self.defense + (self.vinv[equip].deff - self.rhand.deff)
                            self.atk = self.atk + (self.vinv[equip].atk - self.rhand.atk)

                            self.rhand = self.vinv[equip]

                            del self.inv[equip]
                            del self.vinv[equip]
                            print("equipped "+self.rhand.name)
                        return

                    else:
                        print("Atk: {} Def:{} | Desc:{}".format(self.vinv[equip].name,self.vinv[equip].atk,self.vinv[equip].deff,self.vinv[equip].desc))

                        equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                        if equip_that in ["yes", "y"]:
                            self.rhand = self.vinv[equip]
                            self.defense = self.defense + self.rhand.deff
                            self.atk = self.atk + self.rhand.atk
                            del self.inv[equip]
                            del self.vinv[equip]
                            print("equipped "+self.rhand.name)
                        return
        #--------------------------------------------------------------------
            if self.vinv[equip].place == 'head':

                if self.head != None:

                    print("You already have " + self.head.name +" equipped.")
                    print("Name:{} | Def:{} | Desc:{}".format(self.head.name,self.head.deff,self.head.desc))
                    print("Name:{} | Def:{} | Desc:{}".format(self.vinv[equip].name,self.vinv[equip].atk,self.vinv[equip].desc))
                    equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                    if equip_that in ["yes","y","equip"]:
                        self.inv.append(self.head.name)
                        self.vinv.append(self.head)

                        self.defense = self.defense + (self.vinv[equip].deff - self.head.deff)
                        self.atk = self.atk + (self.vinv[equip].atk - self.head.atk)

                        self.head = self.vinv[equip]

                        del self.inv[equip]
                        del self.vinv[equip]
                        print("equipped "+self.head.name)
                    return

                else:
                    print(vars(self.vinv[equip]))

                    equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                    if equip_that in ["yes", "y"]:
                        self.head = self.vinv[equip]
                        self.defense = self.defense + self.head.deff
                        self.atk = self.atk + self.head.atk
                        del self.inv[equip]
                        del self.vinv[equip]
                        print("equipped "+ self.head.name)
                    return
        #--------------------------------------------------------------------
            if self.vinv[equip].place == 'body':

                if self.body != None:

                    print("You already have " + self.body.name +" equipped.")
                    print("Name:{} | Def:{} | Desc:{}".format(self.body.name,self.body.deff,self.body.desc))
                    print("Name:{} | Def:{} | Desc:{}".format(self.vinv[equip].name,self.vinv[equip].atk,self.vinv[equip].desc))
                    equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                    if equip_that in ["yes","y","equip"]:
                        self.inv.append(self.body.name)
                        self.vinv.append(self.body)

                        self.defense = self.defense + (self.vinv[equip].deff - self.body.deff)
                        self.atk = self.atk + (self.vinv[equip].atk - self.body.atk)

                        self.body = self.vinv[equip]

                        del self.inv[equip]
                        del self.vinv[equip]
                        print("equipped "+self.body.name)
                    return

                else:
                    print(vars(self.vinv[equip]))

                    equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                    if equip_that in ["yes","y"]:
                        self.body = self.vinv[equip]
                        self.defense = self.defense + self.body.deff
                        self.atk = self.atk + self.body.atk
                        del self.inv[equip]
                        del self.vinv[equip]
                        print("equipped "+self.body.name)
                    return
        #--------------------------------------------------------------------
            if self.vinv[equip].place == 'leg':

                if self.leg != None:

                    print("You already have " + self.leg.name +" equipped.")
                    print("Name:{} | Def:{} | Desc:{}".format(self.leg.name,self.leg.deff,self.leg.desc))
                    print("Name:{} | Def:{} | Desc:{}".format(self.vinv[equip].name,self.vinv[equip].atk,self.vinv[equip].desc))
                    equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                    if equip_that in ["yes","y","equip"]:
                        self.inv.append(self.leg.name)
                        self.vinv.append(self.leg)

                        self.defense = self.defense + (self.vinv[equip].deff - self.leg.deff)
                        self.atk = self.atk + (self.vinv[equip].atk - self.leg.atk)

                        self.leg = self.vinv[equip]

                        del self.inv[equip]
                        del self.vinv[equip]
                        print("equipped "+self.leg.name)
                    return

                else:
                    print(vars(self.vinv[equip]))

                    equip_that = str.lower(input("Would you like to equip {} (yes)? ".format(self.vinv[equip].name)))

                    if equip_that in ["yes","y"]:
                        self.leg = self.vinv[equip]
                        self.defense = self.defense + self.leg.deff
                        self.atk = self.atk + self.leg.atk
                        del self.inv[equip]
                        del self.vinv[equip]
                        print("equipped "+self.leg.name)
                    return
        except:
            print("Did not understand")

    def equipment(self):
        if self.lhand != None:
            print("Left Hand : " + str(vars(self.lhand)))
        if self.rhand != None:
            print("Right Hand : " + str(vars(self.rhand)))
        if self.head != None:
            print("Head : " + str(vars(self.head)))
        if self.body != None:
            print("Body : " + str(vars(self.body)))
        if self.leg != None: 
            print("Legs : " + str(vars(self.leg)))
        return

    def healed(self, amt):
        old_hp = self.hp
        
        healed_to = self.hp + amt
        self.hp = max(min(self.maxhp, healed_to), 0)
        print("you healed " + str(self.hp - old_hp)+"!")

    def use(self):

        print(list(enumerate(self.uinv3)))
        #try:
        use_item = int(input("what would you like to use?"))

        if self.uinv2[use_item].effect == "heal":
            old_hp = self.hp
            amt_healed = self.uinv2[use_item].amt
            self.healed(amt_healed)
            self.uinv2[use_item].reduce_stack(self, use_item)

        else:
            print("Can't use that")

        #except:
        #    print("Not sure what you're trying to use")

class equipitem():
    def __init__(self, name, atk, deff, equipable, place, price, desc, rarity):
        self.name = name
        self.atk = atk
        self.deff = deff
        self.equipable = equipable
        self.place = place
        self.price = price
        self.desc = desc
        self.rarity = rarity
        
    def reroll(self, atk, deff):
        self.atk = atk
        self.deff = deff

class item():
    def __init__(self, name, equipable, price, effect, amt, desc, rarity):
        self.stack = 1
        self.name = name
        self.uname = self.name + "(" + str(self.stack) + ")"
        self.equipable = equipable
        self.price = price
        self.effect = effect
        self.amt = amt
        self.desc = desc
        self.rarity = rarity

    def increase_stack(self, player, index):
        self.stack = self.stack + 1
        player.uinv3[index] = player.uinv2[index].name + "(" + str(player.uinv2[index].stack) + ")"
    
    def reduce_stack(self, player, index):
        self.stack = self.stack - 1
        player.uinv3[index] = player.uinv2[index].name + "(" + str(player.uinv2[index].stack) + ")"
        if self.stack <= 0:
            #print("deleting itself")
            del player.uinv2[index]
            del player.uinv[index]
            del player.uinv3[index]



class Monsters():

    def __init__(self, name, hp, atk, gold, exp, des, item):
        self.name = name
        # To override specific attributes, assign new values here.
        self.hp = hp
        self.atk = atk
        self.gold = gold
        self.exp = exp
        self.des = des
        self.item = item

    def attack(self, player):
        Mdamage = max(0,self.atk - int(.25 * player.defense))
        print(str(self.name) + " attacks! You took " + str(Mdamage) + " damage!" )
        player.hp = player.hp - Mdamage

    def cry(self):
        pass

    def intro(self):
        print("\n%s appeared" % (self.name))


class Crazy_Hooman():


    def __init__(self, name, item):
        self.name = name
        self.hp = random.randint(20, 45)
        self.attk = random.randint(1, 1)
        self.gold = random.randint(2, 5)
        self.exp = 420
        self.des = "It's your boi " + str(name)
        self.item = item
    

    def attack(self, player):
        Mdamage = max(0,self.attk - int(.25 * player.defense))
        print(str(self.name) + " attacks! You took " + str(Mdamage) + " damage!" )
        player.hp = player.hp - Mdamage

    def drop_loot(self, player):
        #loot_drop = random.randint(1,2)
        #if loot_drop == 1:
        pass

    def cry(self): 
        last_boss = random.randint(1,5)

        if last_boss == 1 and self.hp > 0:
            print(str(self.name) +": Ow! That hurts! You're a bully")
        if last_boss == 2 and self.hp > 0:
            print(str(self.name) +": It's 6:00 and work ends at 6:30. Let me go to the bathroom for 30 minutes")
        if last_boss == 3 and self.hp > 0:
            print(str(self.name) +": Now that's just rude")
        if last_boss == 4 and self.hp > 0:
            print(str(self.name) +": Did you really just put my in your text adventure game?")
        if self.hp <= 0:
            print(str(self.name) +": Welp I'm out of hp. Guess I'll go now.")    

    def intro(self):
        print("\n" + self.name + ": It's your boi!!! " + self.name + ", the last boss, SIR")

class LastBoss():


    def __init__(self, name):
        self.name = name
        self.hp = random.randint(300, 500)
        self.attk = random.randint(20, 25)
        self.gold = random.randint(1000, 5000)
        self.exp = 50000
        self.des = "Last Boss"
        self.item = []
    

    def attack(self, player):
        Mdamage = max(0, self.attk - int(.25 * player.defense))
        print(str(self.name) + " attacks! You took " + str(Mdamage) + " damage!" )
        player.hp = player.hp - Mdamage

    def drop_loot(self, player):
        #loot_drop = random.randint(1,2)
        #if loot_drop == 1:
        pass

    def cry(self): 
        last_boss = random.randint(1,8)

        if last_boss == 1 and self.hp > 0:
            print(str(self.name) +": Remember if you gotta go, do it on company time")
        if last_boss == 2 and self.hp > 0:
            print(str(self.name) +": Wanna look at a picture of my dog?")
        if last_boss == 3 and self.hp > 0:
            print(str(self.name) +": Ohio better not reject us again")
        if last_boss == 4 and self.hp > 0:
            print(str(self.name) +": Did you find a bug? We gotta get the devs on this")
        if last_boss == 5 and self.hp > 0:
            print(str(self.name) +": Still can't believe I crashed my car")
        if last_boss == 6 and self.hp > 0:
            print(str(self.name) +": Smoke break?")  


    def intro(self):
        print("It looks like the end")

class LastBoss2():


    def __init__(self, name):
        self.name = name
        self.hp = random.randint(5000, 10000)
        self.attk = random.randint(100, 200)
        self.gold = random.randint(10000, 50000)
        self.exp = 500000
        self.des = "OHIOOOOOOOO (Phase 2)"
        self.item = []
    

    def attack(self, player):
        Mdamage = max(0, self.attk - round(int(.25 * player.defense)))
        print(str(self.name) + " attacks! You took " + str(Mdamage) + " damage!" )
        player.hp = player.hp - Mdamage

    def drop_loot(self, player):
        #loot_drop = random.randint(1,2)
        #if loot_drop == 1:
        pass

    def cry(self): 
        last_boss = random.randint(1,8)

        if last_boss == 1 and self.hp > 0:
            print(str(self.name) +": We gotta print out 100 forms in 20 MINUTES")
        if last_boss == 2 and self.hp > 0:
            print(str(self.name) +": NO HUddlInG FoR ToDay")
        if last_boss == 3 and self.hp > 0:
            print(str(self.name) +": Ohio better not rejected us AgAiN")
        if last_boss == 4 and self.hp > 0:
            print(str(self.name) +": Dust 2 is the best map of all time")
        if last_boss == 5 and self.hp > 0:
            print(str(self.name) +": Alright guys lets rush B")
        if last_boss == 6 and self.hp > 0:
            print(str(self.name) +": Smoke break?") 


    def intro(self):
        print("Jark put on his gaming headset. You know it's about to go down. Your arms are heavy.. knees... spaghetti..")
class MidBoss():


    def __init__(self, name):
        self.name = name
        self.hp = random.randint(2000, 3000)
        self.attk = random.randint(60, 100)
        self.gold = random.randint(555, 777)
        self.exp = 3650
        self.des = "The Mezeriak "
        self.item = []
    

    def attack(self, player):
        Mdamage = max(0, self.attk - round(int(.25 * player.defense)))
        print(str(self.name) + " attacks! You took " + str(Mdamage) + " damage!" )
        player.hp = player.hp - Mdamage

    def drop_loot(self, player):
        #loot_drop = random.randint(1,2)
        #if loot_drop == 1:
        pass

    def cry(self): 
        last_boss = random.randint(1,8)
            
        if last_boss == 1 and self.hp > 0:
            print(str(self.name) +": Feel THE POWER OF DARKNESS")
        if last_boss == 2 and self.hp > 0:
            print(str(self.name) +": YOU STILL UNDERSTAND NOTHING")
        if last_boss == 3 and self.hp > 0:
            print(str(self.name) +": I am a NOBODY")
        if last_boss == 4 and self.hp > 0:
            print(str(self.name) +": I am ANYTHING YOU WANT ME TO BE")
        if last_boss == 5 and self.hp > 0:
            print(str(self.name) +": I'll do anything once")
        if last_boss == 6 and self.hp > 0:
            print(str(self.name) +": YOU'RE PRETTY GOOD")


    def intro(self):
        print("\nYour Hope ends here")
        sleep(4)
        print("AND YOUR MEANINGLESS EXISTENCE WITH IT")
        sleep(3)
        print("IT IS I")
        sleep(2)
        
        for c in "THE MIZERAK!\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            sleep(0.1)
        print

    def defeat(self):
        print("You may have defeated me, but..")
        sleep(3)
        for c in "You'll never beat the DARHNESS\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            sleep(0.05)
        print