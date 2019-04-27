import sys
import random
from DropTable import *
from Class import*
import fighting
import monsters

global boss_x
boss_x = random.randint(20,40)
global boss_y
boss_y = random.randint(20,40)
paper_prince = False
paper_princex = None
paper_princey = None
paid_prince = 0
pay_sign = 0
mid_boss = 0
mid_bossx = random.randint(20,40)
mid_bossy = random.randint(10,30)
van_y = random.randint(10,60)
van_x = random.randint(10,60)
van_meme = 0

def question(ask):
    answer = str.lower(input(repr(ask) + "\n [Y/N]\n"))
    if answer in ["Y","Yes","y","yes"]:
        return True
    else:
        return False

def shop(player):

    enter_shop = str.lower(input("You see a shop here, do you want to enter? "))

    if enter_shop in ["yes","y"]:
        shopin = True

        print("\nThe name's Kendall. Welcome to my shop! I got a bunch of random stuff what do you want?\n")
        while shopin == True:

            buy_sell = str.lower(input("Buy, Sell, Talk?(leave) "))

            if buy_sell in ["sell"]:
                selling = True

                while selling == True:
                    selling_what = str.lower(input("What you want to sell?(equipment or items(back)) "))

                    if selling_what in ["equipment", "equip","e"]:
                        selling_e = True
                        while selling_e == True:
                            try:
                                print(list(enumerate(player.inv)))
                                selling_this = int(input("What equipment?(enter number) "))
                                player.gold = player.gold + player.vinv[selling_this].price
                                print("You got " + str(player.vinv[selling_this].price) +" for " + player.vinv[selling_this].name)

                                del player.inv[selling_this]
                                del player.vinv[selling_this]

                            except:
                                print("Not selling anymore?")
                                selling_e = False

                            #print("Not sure what you're trying to sell")
                            #break


                    if selling_what in ["item","items","i"]:
                        selling_i = True
                        while selling_i == True:
                            try:
                                print(list(enumerate(player.uinv3)))
                                selling_this = int(input("What item?(enter number) "))
                                player.gold = player.gold + player.uinv2[selling_this].price
                                print("You got " + str(player.uinv2[selling_this].price) +" for " + player.uinv2[selling_this].name)
                                
                                player.uinv2[selling_this].reduce_stack(player, selling_this)


                            except:
                                print("Not selling anymore?\n")
                                selling_i = False

                    if selling_what in ["back","leave","esc","escape","exit"]:
                        selling = False
                
            if buy_sell in ["buy","Buy"]:
                print("I got all of these stuff from Omazon. All high quality!")
                buying = True
                while buying == True:
                    shop = [item_1,item_2,item_3, equip_3, equip_4]
                    shop_price = [10,30,100, 25,30]
                    for shopIndex in range(len(shop)):
                        print("|{}| {} {}g| {}".format(shopIndex, shop[shopIndex].name, shop_price[shopIndex], shop[shopIndex].desc if shop[shopIndex].equipable == False else "atk:" + str(shop[shopIndex].atk) +" def:"+  str(shop[shopIndex].deff)))
                    #Hi, your first name is {0} and your last name is {1}".format("foo", "bar")
                    #print (", ".join("%s: %s" % item for item in stats.items()) #print the attributes
                    print("\nYour Gold: {}".format(player.gold))
                    try:
                        buying_this = int(input("What do you want to buy?(put number) "))
                        if player.gold >= shop_price[buying_this]:
                            player.gold = player.gold - shop_price[buying_this]
                            player.buying(shop[buying_this])
                        else:
                            print("You can't afford this.\n")
                    except:
                        print("Not buying anymore?\n")
                        buying = False

            if buy_sell in ["talk"]:
                talking_shop = random.randint(1,3)
                if talking_shop == 1:
                    print("I heard the final boss was at (%s,%s)" % (boss_x,boss_y) )
                if talking_shop == 2:
                    print("I heard the mid boss was at (%s,%s)" % (mid_bossx,mid_bossy) )
                if talking_shop == 3:
                    print("I heard there is a disgusting weeb at (%s,%s)" % (van_x,van_y) )

            if buy_sell in ["leave","Leave","exit","Exit"]:

                print("Kendall: I'll see you later")
                return
    else:
        print("You decided not to enter the shop")
        
def map(player,x,y):
    global paid_prince
    global pay_sign
    global mid_boss
    global van_meme
    
    if x == 21 and y == 21:
        shop(player)
    if x == boss_x and y == boss_y:
        Fight_boss = str.lower(input("You're at the final boss will you fight?"))
        
        if Fight_boss in ["y","yes"] and mid_boss ==0:
            print("\nYou didn't kill the midboss yet. You can't fight the boss before the mid boss. You know the Rulezzzzz")
        elif Fight_boss in ["y","yes"]:
            
            Monster = monsters.spawn_lboss()
            fighting.final_fight(Monster, player)
        else:
            print("You noped on outta there")
    if x == paper_princex and y == paper_princey and paid_prince == 0:
        print("""\nYou found a sign with an sketchy arrow pointing to the ground."Please dig a hole here and put in the money" """)
        digPay = question("Do you abandon all logic and put 60000g into the hole?")
        if "CaSh MoNeY" in player.inv:
            useMoney = question("Wait you have CaSh MoNeY! You can do anything! Want to put CaSh MoNeY in the hole instead??")
            if useMoney == True:
                index1 = vars(player)["inv"].index("CaSh MoNeY")
                #print("{}, {}".format(player.inv[index1],player.vinv[index1]))
                del player.inv[index1]
                del player.vinv[index1]
                print("Abandoning all logic, you buried CaSh MoNeY in the ground...")
                paid_prince = 1
                
                if pay_sign ==0:
                    print("Feeling a little buyer's remorse you did some mental gymnastics to justicify your objective bad decision")
                    print("You gain 1 int from your mental gymnastics!")
                    player.int += 1
                else:
                    print("Really? After you avoided the scam you came back and do it anyways??? Give me back that int point!")
                    print("You lost 1 int!")
                    player.int -= 1
            
            elif digPay == True:
                if player.gold >= 60000:
                    player.gold -= 60000
                    print("How did you get 60,000g?? Anyways, you buried 60,000g in the ground...")
                    paid_prince = 1
                    
                    if pay_sign ==0:
                        print("Feeling a little buyer's remorse you did some mental gymnastics to justify your objective bad decision")
                        print("You gain 1 int from your mental gymnastics!")
                        player.int += 1
                    else:
                        print("Really? After you avoided the scam you came back and do it anyways??? Give me back that int point!")
                        print("You lost 1 int!")
                        player.int -= 1
                else:
                    print("You don't have 60,000g. I mean like, why would you.")
            else:
                if pay_sign == 0:
                    print("You patted yourself on the back and knew you just avoided a scam. You felt that all your years of learning was just for this moment")
                    print("You felt a little bit better about yourself and a bit smarter")
                    print("\nYou got 1 int!\n")
                    player.int += 1
                    pay_sign = 1
                else:
                    print("You came back to the sign just to remember how smart you felt.")
    if paid_prince >= 1 and paid_prince < 10000:
        paid_prince += 1
        if paid_prince == 10000:
            print("\nAn owl came down and perched on your shoulder. You looked around confuzzled. When trying to reach for the owl, it flew away and drop a piece of paper in your hands")
            print(""" "Hey! Its me! The prince of Alestasia! Thanks to your donation I was able to pay some knights and raid the bandits to get the paper! Here is a paper check for 1,000,000g like I promised! Wow there is a lot of paper involving me. I guess you could call me the Paper Prince! Haha!" """)
            print(""" "I never seen you before, but I when I imagine you. I see someone with at least {} int!" """.format(player.int))
            player.buying(quest_1)
            print("I guess you can somehow sell it to a shop and somehow get money????\n")
            if pay_sign ==1:
                print("I also feel like someone took away an int point from you for helping me. So, I'm giving you another one!")
                print("\nYou got 1 int!")
                player.int += 1
    if x == mid_bossx and y == mid_bossy and mid_boss == 0:
        fight_mid_boss = question ("You found the mid boss, fight it?")
        if fight_mid_boss == True:
            Monster = monsters.Mid_boss()
            mid_boss = fighting.Midboss(Monster, player)
        else:
            print("nope")
    if x ==van_x and y == van_y and van_meme == 0:
        print("You saw a guy who is dressed like he is in a japanese anime. You try to avoid him but he noticed you")
        print("\nVan: the name's Van. You're here for the good stuff arn't ya. the bonbi MEMEs REEEEEEEE. Well I'll juice ya for 50g whatyasay??")
        buy_memes = str.lower(input("\nbuy meme from this degenerate?"))
        if buy_memes in ["Y","Yes","y","yes"] and player.gold >= 50:
            print("Van: This Wil MeSs YoU uP")
            print("Lost 50g")
            player.gold -= 50
            player.buying(meme_1)
            van_meme = 1
        elif buy_memes in ["Y","Yes","y","yes"] and player.gold < 500:
            print("You don't have enough for the mEmEs")
        else:
            print("you escape sucessfully")
        
    else:
        random_events(player)
        return

def random_events(player):
    event = random.randint(1,200)
    #print(event)
    global paper_prince
    global paper_princex
    global paper_princey
    
    if event == 1 and paper_prince == False:

        paper_prince = True
        paper_princex=random.randint(-100,100)
        paper_princey=random.randint(-100,100)
        print("""\nYou saw a piece of paper taped to the ground."Hey stranger, if you saw this note, well then you are in luck! I am prince of the north western kingdom of Alestasia. I forgot the 4 digit code to the lock of my treasury to my kingdom! Some bandit stole the paper I wrote those digits on too! They want 60,000g for the paper and my army won't help because I can't pay them! If you help, once I am able to get back into treasury I'll give you 1,000,000g!Please go to ({},{}) and put the money in a hole dug in the ground, so no one will know where it is. I'll come get it personally and you'll hear from me soon after! TY ;)" The piece of paper then burst into flames.{} Besides, the one shop in the game doesn't even have anything costing 1,000,000g???""".format(paper_princex,paper_princey,"You don't have 60,000g and you're not sure if you should even try." if player.gold < 60000 else "You don't have 60,0... wait you have" + str(player.gold) + "g??? why do you have so much???"))
    
    if event == 2:
        
        print("You saw a {}-shaped cloud. The whimsicalness of the world make you feel a bit better".format(random.choice(["dog","cat","whale","cloud","chicken","duck"])))
        player.healed(13)
    if event == 3:
        
        print("You felt a little hungry, but then you remember this isn't a survival game so there is no hunger meter!")
        player.healed(10)
    #if event == 4:
        
    #    drink_it = question("A fountain suddenly appears before you! You feel a bit thirsty looking at it. Do you drink of it?")
    #   what_did_you_just_drink = random.randint(1,5)
    #    if drink_it == True and what_did_you_just_drink == 1:
     #       pass
            