from Class import equipitem,item
from random import randint as roll

#Equipments:: name, atk, deff, equipable, place, price, desc, rarity
#'hand', 'head', 'body', 'leg'

#items:: name, equipable, price, effect, amt, desc, rarity


equip_1 = equipitem("Testing sword",100,0,True,"hand", 20,"sword for testing the game", 5)
equip_2 = equipitem("Testing sword DEF",0,100,True,"hand", 20,"sword for testing the game", 2)
equip_3 = equipitem("broken sword",3,0,True,"hand", 20,"How old could this be?", 5)
equip_4 = equipitem("Plank Shield",0,3,True,"hand", 20,"Pretty sure you can find this on the ground", 5)
OP_1 = equipitem("CaSh MoNeY",5000,3,True,"hand", -80000,"as long as you have CaSh MoNeY you can do AnYtHinG", 100)
OP_2 = equipitem("Test Client Master Degree",0,5,True,"head", 1,"Are you proud yet, Mom?", 50)
item_1 = item("herb", False , 3, "heal", 35, "heals 35",2)
item_2 = item("potion", False , 10, "heal", 55, "heals 55",4)
item_3 = item("High potion", False , 25, "heal", 100, "heals 100",10)
quest_1 = item("Money Check", False , 1000000, None, 55, "It's a check worth 1,000,000. Wowee!", 10000)
meme_1 = equipitem("Bonbi MeMes", 0,250,True,"head",0,"ThEsE ArE somE QuAliTy BonBi memes",50000)