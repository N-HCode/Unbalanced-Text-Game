from random import randint as roll
from Class import*
from DropTable import*

def spawn(x,y):



    print("\nYou got an encounter!")
    which_monster = roll(1,7)
    print(which_monster)

    if x <= 40 and y <= 40:
        
        if which_monster == 1:

                      #NormalMob ( name, hp, atk, gold, exp, des, item)
            Monster = Monsters("Wolf", roll(25,35),roll(2,5), roll(5,10), roll(10,20),"Looks hungry", [equip_1,equip_2,item_1,item_2])
    

        elif which_monster == 2:

            Monster = Crazy_Hooman("Evan", [OP_2])

        elif which_monster == 3:
            Monster = Monsters("Trash Can", roll(30,45),roll(3,4), roll(5,5), roll(20,21),"You're fighting a trash can...",[OP_1])
        else:
            
            Monster = Monsters("Slimey", roll(10,15),roll(1,2), roll(1,2), roll(5,8),"It's a slime", [equip_1,item_1,item_2])
            

    if x > 40 and x <= 80 or y > 40 and y <= 80:

        if which_monster == 1:

            Monster = Monsters("New Wolf", roll(50,60),roll(9,13), roll(20,25), roll(40,60),"Looks newly hungry?", None)

        else:

            Monster = Monsters("Orge", roll(100,200),roll(10,20), roll(50,100), roll(100,200),"Orge vey!", None)

    if x> 80 or y > 80:
        
        if which_monster in [1,2,3,4,5,6]:
            Monster = Monsters("Nightmare", roll(500,1000),roll(50,100), roll(200,400), roll(1000,3000),"You shouldn't be here", None)
        else:
            Monster = Monsters("True Nightmare", roll(5000,10000),roll(75,125), roll(500,600), roll(7000,10000),"It should be impossible to meet this", None)
              
    Monster.intro()
    return Monster

def spawn_lboss():

    Monster = LastBoss("Jark")
    Monster.intro()
    return Monster

def spawn_lboss2():

    Monster = LastBoss2("Jark The GFS Masterace")
    Monster.intro()
    return Monster

def Mid_boss():

    Monster = MidBoss("The Mizerak")
    Monster.intro()
    return Monster