import random
import sys
import time

# Define the starting stats of the player
class Player:
    def __init__(self):
        self.name = "Poka-Poka"
        self.hp = 10
        self.maxHp = 10
        self.atk = 3
        self.mp = 10
        self.maxMp = 10
        self.skills = []
        self.coins = 30
        self.lvl = 1
        self.xpSup = 10
        self.xp = 0
        self.itemList = []
        self.weapon = 0
        self.armor = 0


# Define the basic stats of the enemies
class flying_cabbage:
    def __init__(self):
        self.hp = 1
        self.atk = 1
        self.xp = 2
        self.gold = 1
        self.name = "flying cabbage"
        self.item = food


class giant_frog:
    def __init__(self):
        self.hp = 4
        self.atk = 3
        self.xp = 4
        self.gold = 3
        self.name = "Giant frog"
        self.item = food


# class explosive_rock :
#     def __init__(self) :
#         self.hp = 10
#         self.atk = 0
#         self.xp = 8
#         self.gold = 5
#         self.name = "rocher explosif"
#         self.item = explosive_fragment

class wolf:
    def __init__(self):
        self.hp = 5
        self.atk = 4
        self.xp = 12
        self.gold = 8
        self.name = "wolf"
        self.item = food


class bandit:
    def __init__(self):
        self.hp = 5
        self.atk = 5
        self.xp = 10
        self.gold = 20
        self.name = "bandit"
        self.item = food


class undead:
    def __init__(self):
        self.hp = 10
        self.atk = 6
        self.xp = 20
        self.gold = 18
        self.name = "undead"
        self.item = "undefined"


class skeleton:
    def __init__(self):
        self.hp = 5
        self.atk = 9
        self.xp = 8
        self.gold = 20
        self.name = "skeleton"
        self.item = "undefined"


# Stats of the boss
# class vanir:
#     def __init__(self):
#         self.hp = 250
#         self.atk = 15
#         self.xp = 500
#         self.gold = 300
#         self.name = "Vanir"
#         self.item = "épée ou armure"
class Vanir:
    def __init__(self):
        self.hp = 40
        self.atk = 5


# Define stats of objects
class food:
    def __init__(self):
        self.name = "Provisions"
        self.heal = 5
        self.count = 1


class heal_potion:
    def __init__(self):
        self.name = "healing potion"
        self.heal = 10
        self.count = 1


class mana_stone:
    def __init__(self):
        self.name = "mana stone"
        self.heal = 10
        self.count = 1


class explosive_fragment:
    def __init__(self):
        self.name = "Fragment explosif"
        self.dmg = 5
        self.count = 1


# Define stats of skills and spells
class light_heal:
    def __init__(self):
        self.name = "light heal"
        self.heal = 5
        self.cost = 5

class intermediate_heal:
    def __init__(self):
        self.name = "medium heal"
        self.hp = 10
        self.cost = 10

class advanced_heal:
    def __init__(self):
        self.name = "maximum heal"
        self.heal = 20
        self.cost = 18

class fire_ball:
    def __init__(self):
        self.name = "fire ball"
        self.cost = 6
        self.dmg = 4

class lightning:
    def __init__(self):
        self.name = "lightning"
        self.cost = 9
        self.dmg = 9

class sacred_sanctuary:
    def __init__(self):
        self.name = "sacred sanctuary"
        self.cost = 11
        self.heal = 9
        self.dmg = 4

class drain_touch:
    def __init__(self):
        self.name = "Drain drain_touch"
        self.cost = 11
        self.heal = 4
        self.dmg = 9

class explosive_shoot:
    def init(self):
        self.name = "explosive shoot"
        self.cost = 15
        self.dmg = 11

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

# Display the menu at the start of the game, wich allows the player to start a new game or see the credits.
def mainMenu():
    print("1. Start Game")
    print("2. History & Rules")
    print("3. Credits")
    print("4. Quit")
    #ASKING THE USER WHAT THEY WHANT 
    selecMenu = int(input(">> Please chose from 1, 2, 3 or 4 \n"))
    
    if selecMenu == 1:
        startGame()
    elif selecMenu == 2:
        print(">> Once upon a time a group of powerful adventurers, composed of an Archmage, a Crusader, an Archpriest and a valiant and charismatic hero from another world decided to face the general of the demon king Vanir and became legends...")
        time.sleep(5)
        print(">> But that excitement was short lived...")
        time.sleep(5)
        print(">> The crusader's mission was to kill cabbages in the plains, but being a masochist unable to wield a sword, she failed to kill a single one and the consequences were disastrous, because half of the fields of the city were destroyed.")
        time.sleep(5)
        print(">> Due to his immense debts from the purchase of a large amount of alcohol in the city of Axel, the archpriest decided to flee his debts and take refuge in the forest awakening many beasts.")
        time.sleep(5)
        print(">> To express Megumin's love for explosion magic, the young archmage unleashed her magic on an abandoned castle filled with the living dead or skeleton that slept peacefully. You are the only hope in the face of the demonic and powerful Vanir to restore order and peace in the city of Axel.")
        time.sleep(5)
        print(">> But for Kazuma, it is said that he disappeared and became a merchant in order to live a life of laziness without having to fight.")
        time.sleep(5)
        print("")
        print("--------------------------------------------")
        print("")
        print("")
        print("Your tasks are now to: ")
        print(">> Battle the fiercest of monstres, to gain money, xp and glory.")
        print(">> Use your battle experiance to buy wepons and tools.")
        print("And most of all...")
        print(">> DEFEAT THE DEMON KING")
        print("")
        confirm = str(input(">> Do you wish to continue? y/n"))
        if confirm == "yes" or confirm == "y" or confirm == "Yes" or confirm == "Y" :
            print("okay...")
        else:
            sys.exit()
        mainMenu()
    
    elif selecMenu == 3:
        print("____________________________________________________")
        print("|                                                   |")
        print("|        Contributors to the Kazuquest project :    |")
        print("|                                                   |")
        print("|     ",'\033[36m',"Ambrose Ben Tiba",'\033[39m',"  |")
        print("|     ",'\033[35m',"Cyril Chuzel",'\033[39m',"      |")
        print("|     ",'\033[31m',"Merwan Mahiout",'\033[39m',"    |")
        print("|                                                   |")
        print("|          And thanks also to our professor         |")
        print("|                   Loic Janin                      |")
        print("|            And the Translator... Thinker          |")
        print("|___________________________________________________|")
        mainMenu()
    elif selecMenu == 4:
        print("Alright see ya later Baka")
        sys.exit()


# Initialize the game grid and the stats of the player, and launch the game.
# Also activate cheat code for immediate fight against boss
def startGame():
    print("")
    print("\033[1;42;30m New Clan \033[0m")
    print("")

    global player
    global position
    global food
    global heal_potion
    global mana_stone

    position = [1, 3]

    player = Player()

    (player.skills).append(light_heal())
    (player.skills).append(fire_ball())


    food = food()
    heal_potion = heal_potion()
    mana_stone = mana_stone()

    (player.itemList).append(food)
    (player.itemList).append(heal_potion)
    (player.itemList).append(mana_stone)

    # Cheat mode for immediate fight against boss Vanir
    if Cheat == True:
        position = [6, 3]
        player.atk = 13
        player.maxHp = 40
        player.maxMp = 30
        player.hp = player.maxHp
        player.mp = player.maxMp
        player.weapon = 15
        player.armor = 5
        EventVanir()

    print(">> You are a beginner adventurer living in the town of Axel known for its trading activities as well as its guild bringing together people looking for adventures.")
    time.sleep(2)
    print(">> You get out of bed and decide to walk around the city, you think at first to go to a café, but you prefer to go to the adventurers' guild.")
    time.sleep(2)
    print(">> You enter the guild, to take an easy quest to get a can of money, give you your quest to the charming receptionist of the luna guild to validate your quest")
    time.sleep(2)
    print('')
    print('\033[33m')
    print('')
    print("Luna: It's been a long time since you switched to the guild")
    time.sleep(1.5)
    player.name = input(">> Could you remind me your name again?: ")
    print("Luna: Give me your quest,", player.name, "I'll validate it right away.")
    time.sleep(1.5)
    print('\033[39m')
    print('')
    print(">> While Luna validates your quest you decide to look on your adventurer map your stats:")
    time.sleep(1.5)
    print('')
    print('\033[34m')
    print(">> You're in level 1")
    print(player.hp,"/",player.hp,"PV")
    print(player.mp,"/",player.mp,"PM")
    print("> Spells: ")
    print("> Fast care")
    print("> Fireball")
    print("> You have",player.coins,"Coins")
    time.sleep(3)
    print('\033[39m')
    print(">> Before Luna validates your quest, a large group of wounded and terrorized adventurers arrives explaining that the group of heroes has failed and that the demon general Vanir has planned to send a plague on the city of Axel and has decided to hide in a castle.")
    print('\033[33m')
    time.sleep(1.5)
    print(">> Luna: This is a big problem because all the adventurers are either buried or have left the city and the only adventurer available is you.")
    time.sleep(1.5)
    print("")
    print(">> Your adventrue begins now...")

    Grille()
    Event()


# Generate a grid of size "largeurGrille" * "hauteurGrille"
# and assign a state depending of the heigt (or x value).
def Grille():
    for x in range(hauteurGrille):
        for y in range(largeurGrille):
            state = "undefined"

            if x <= 2 and y == 3:
                state = "city"
            elif x <= 4 and x > 2:
                state = "plains"
            elif x <= 6 and x > 4:
                state = "forest"
            elif x <= 8 and x > 6:
                state = "castle"

            grille.append([x, y, state])


# Ask the player were he wants to go, and if the case chosen is defined and in the boundaries of the grid.
# If so, update position, send a message and launch event function. If not, ask again for a direction.
def Movement():
    MovementPos = str(input("\033[1;36m Which path do you want to take? (N/E/S/W) \033[0m"))

    if MovementPos == "N":
        if position[0] * hauteurGrille >= 0 and position[0] * hauteurGrille <= hauteurGrille * (hauteurGrille - 2) and \
                grille[((position[0] + 1) * largeurGrille + position[1])][2] != "undefined":
            position[0] += 1
            print("\033[36m >> You chose North \033[0m")
        else:
            print("\033[31m >> This Path is blocked! Please choose another direction.\033[0m")
            Movement()

    elif MovementPos == "W":
        if position[1] * largeurGrille >= 1 and position[1] <= largeurGrille and \
                grille[(position[0] * largeurGrille + (position[1] - 1))][2] != "undefined":
            position[1] -= 1
            print("\033[36m >> You chose West. \033[0m")
        else:
            print("\033[31m Oh no! This path is blocked! Please choose another one... \033[0m")
            Movement()

    elif MovementPos == "E":
        if position[1] >= 0 and position[1] <= largeurGrille - 2 and \
                grille[(position[0] * largeurGrille + (position[1] + 1))][2] != "undefined":
            position[1] += 1
            print("\033[36m You want to go East? \033[0m")
        else:
            print("\033[31m This one is also blocked! Please choose another path... \033[0m")
            Movement()

    elif MovementPos == "S":
        if position[0] * hauteurGrille >= 1 and position[0] * hauteurGrille <= hauteurGrille * (hauteurGrille - 1) and \
                grille[((position[0] - 1) * largeurGrille + position[1])][2] != "undefined":
            position[0] -= 1
            print("\033[36m You picked South")
        else:
            print("\033[31m Please choose another direction please ;-;... \033[0m")
            Movement()

    else:
        print("\033[31m What are you talking about? Please choose: \033[0m")
        print("North (N)")
        print("East (E)")
        print("South (S)")
        print("West (W)")
        Movement()

    Event()


# Define what happens when you go on a new tile : send message corresponding of the zone,
#  and launch the shop or a fight
def Event():
    if position == [6, 3]:
        
        global vanir
        
        EventVanir()
    elif position == [0, 3]:
        print(
            "\033[1;34m>> You have arrived in a small bazaar full of objects, run by a merchant named Satou Kazuma\033[0m")
        Shop()
    elif grille[((position[0]) * largeurGrille + position[1])][2] == "plains":
        print("\033[1;36m You find yourself in the plains, populated by low level enemies. \033[0m")
    elif grille[((position[0]) * largeurGrille + position[1])][2] == "forest":
        print("\033[1;36m You find yourself in the forest, populated by medium level enemies. \033[0m")
    elif grille[((position[0]) * largeurGrille + position[1])][2] == "castle":
        print("\033[1;36m You find yourself in the castle, populated by high level enemies. \033[0m")
    elif grille[((position[0]) * largeurGrille + position[1])][2] == "city":
        print("\033[1;36m You find yourself in the town of Axel, where novice adventurers in search of adventure congregate. \033[0m")
        print("\033[1;36m You soon find a store in the far South \033[0m")

    if grille[((position[0]) * largeurGrille + position[1])][2] != "city":
        spawnEnemies()

    Movement()


# Create a list of random enemies in random number, according to the tile on the grid the player is on,
# And launch fight against the enemies list with a message
def spawnEnemies():
    Enemies = []
    print("\033[1;31m>> Monsters come out of no where and attack you! \033[0m")

    if grille[((position[0]) * largeurGrille + position[1])][2] == "plains":
        enemyType = random.randint(0, 1)
        if enemyType == 0:
            enemyType = "Cabbage"
            enemyNumber = random.randint(2, 4)
            for i in range(enemyNumber):
                Enemies.append(flying_cabbage())
        elif enemyType == 1:
            enemyType = "Giant Frogs"
            enemyNumber = random.randint(1, 2)
            for i in range(enemyNumber):
                Enemies.append(giant_frog())

    elif grille[((position[0]) * largeurGrille + position[1])][2] == "forest":
        enemyType = random.randint(2, 3)
        if enemyType == 2:
            enemyType = "Wolf"
            enemyNumber = random.randint(2, 4)
            for i in range(enemyNumber):
                Enemies.append(wolf())
        elif enemyType == 3:
            enemyType = "Bandits"
            enemyNumber = random.randint(1, 4)
            for i in range(enemyNumber):
                Enemies.append(bandit())
        elif enemyType == 4:
             enemyType = "Explosive Rocks"
             enemyNumber = random.randint(1,2)
             for i in range (enemyNumber) :
                 Enemies.append(explosive_rock())

    elif grille[((position[0]) * largeurGrille + position[1])][2] == "castle":
        enemyType = random.randint(4, 5)
        if enemyType == 4:
            enemyType = "Zombies"
            enemyNumber = random.randint(2, 3)
            for i in range(enemyNumber):
                Enemies.append(undead())
        elif enemyType == 5:
            enemyType = "Skeleton"
            enemyNumber = random.randint(2, 3)
            for i in range(enemyNumber):
                Enemies.append(skeleton())

    print("\033[33m You face", enemyNumber, enemyType, "! \033[0m")
    Fight(Enemies)


# Main fight function. Display hp and mp, and ask the player what action he wants to do.

# "1" for normal attack, with a 20% chance of critical hit with double damage.
# if there is more than one enemy, ask for wich one target.
# After attck, launch EndPlayerTurn function.

# "2" for skills and spell, launch skill function
# "3" for items, launch item function

# "4" for escape, with a 30% chance of failure. If fail, launch EndPlayerTurn function.
# if success, send message and launch movement fonction

# For all fight function, enemies list is in parameter,
# and entering an incorrect integer when choosing option send you back to the precedent menu.
def Fight(enemies):
    print("\033[1;34m Vous have ", player.hp, " / ", player.maxHp, "pv")
    print(" You have ", player.mp, " / ", player.maxMp, "pm \033[0m")

    print("\033[34m1 - Attack")
    print("2 - Skills and spells")
    print("3 - Inventory")
    print("4 - Leak")

    ChoixCombat = int(input("> What do you choose ? (1/2/3/4) : \033[0m"))

    # Normal attack with 1/5 chance of critical with double damage.
    # Let you choose your target if there is more than one.
    # Also add weapon damages to the total damage dealed, and end the player turn
    if ChoixCombat == 1:

        if len(enemies) > 1:
            ChoixEnemy = int(input("\033[34m Which one do you want to attck ? \033[0m")) - 1
            while ChoixEnemy < 0 or ChoixEnemy > len(enemies) - 1:
                ChoixEnemy = int(input("\033[31m Wrong, which one do you want to attack? \033[0m")) - 1
        else:
            ChoixEnemy = 0

        critical = random.randint(0, 9)

        if critical >= 8:
            damage = player.atk * 2 + player.weapon
            print("\033[1;32m You inflict a ton of damage! CRITICAL ATTACK ", damage,
                  "damage!\033[0m")
        else:
            damage = player.atk + player.weapon
            print("\033[32m You attack the monster with your weapon and inflict", damage, " damage \033[0m")
        enemies[ChoixEnemy].hp -= damage
        EndPlayerTurn(enemies)

    # Launch skills and spell function
    elif ChoixCombat == 2:
        Skill(enemies)

    # Launch item function
    elif ChoixCombat == 3:
        Item(enemies)

    # Attemp to flee with a 30% failure rate. Return to movement function if success,
    # end player turn if failure.
    elif ChoixCombat == 4:
        fuite = random.randint(0, 9)
        if fuite <= 7:
            print("\033[32m You gather all your courage and run away like a bitch... \033[0m")
            print("")
            Movement()
        else:
            print("\033[31m You ran with your eyes closed and bumped into another monster... \033[0m")
            EnemiesTurn(enemies)

    # If the player sends an incorrect value on the menu, restart fight function
    else:
        print("\033[31m What? Please choose an actual option next time.\033[0m")
        Fight(enemies)


# After the player action, check if some enemies have 0 or less hp.
# If so, remove them from the enemies list, and add xp, gold and loot to the player inventory.
# Next, detect if the enemies list is empty (meaning all enemies are dead).
# If so, end the fight and launch level function.
# If not, launch the enemies turn.
def EndPlayerTurn(enemies):
    scanEnemy = 0

    while scanEnemy < len(enemies):
        if enemies[scanEnemy].hp <= 0:
            print("\033[1;32m", enemies[scanEnemy].name, scanEnemy + 1, " fainted !\033[0m")
            player.xp += enemies[scanEnemy].xp
            player.coins += enemies[scanEnemy].gold

            drop = random.randint(0,3)
            if drop == 0:
                enemies[scanEnemy].item.count += 1
 
            enemies.pop(scanEnemy)
        scanEnemy += 1

    if not enemies:
        print("\033[1;32m You win! !\033[0m")
        print("\033[32m You have ", player.coins, " coins in total \033[0m")
        Level()
        Movement()
    else:
        for u in range(len(enemies)):
            print("\033[32m He stays", enemies[u].hp, "Pv at", enemies[u].name, u + 1, "\033[0m")
        EnemiesTurn(enemies)


# Let every enemy in enemies list perform an attack, with a 20% chance of messing.
# The player armor stat reduce incomming damage by its value
# Next, check if the player still have some hp.
# If so, launch again fight function.
# If not, launch game over function.
def EnemiesTurn(enemies):
    for i in range(len(enemies)):
        dodge = random.randint(0, 9)
        if dodge >= 8:
            print("\033[32m You dodge", enemies[i].name, i + 1, "! \033[0m")
        else:
            print("\033[33m ", enemies[i].name, i + 1, "Attack ! \033[0m")
            print("\033[31m You lost", enemies[i].atk - player.armor, "PV \033[0m")
            player.hp -= enemies[i].atk - player.armor

    print("\033[33m You still have", player.hp, "PV \033[0m")

    if player.hp <= 0:
        gameOver()
    else:
        Fight(enemies)


# Send Game Over message, and ask for a replay.
def gameOver():
    print("")
    print(
        "\033[1;31m Your adventure ends here. With a little luck, a kind goddess will want to reincarnate you (Ephc!))")
    print(" But while waiting your remains will feed the monsters ... \033[0m")
    print("")
    retry = str(input("\033[1;32m Will you retry? y/n \033[0m"))
    if retry == "yes" or retry == "Yes":
        mainMenu()
    elif retry == "no" or retry == "No": 
        sys.exit()
    else :
        print("... Even that, is it too hard for you? ...")
        sys.exit()
    


# After the fight, calculate if the xp have reached the amount needed to gain a level.
# If so, send message,add stats, retrieve hp and mp, and increases the amount of xp needed for next level.
# If not, tell what amount of xp is still needed to reach next level, and return to movement function
def Level():
    while player.xp >= player.xpSup:
        player.lvl += 1
        print("\033[1;32m Congrats, you have leveled up!", player.lvl, "! \033[0m")
        player.xpSup = int(player.xpSup * 2.2)
        player.atk += 1
        player.maxHp += 3
        player.hp = player.maxHp
        player.maxMp += 2
        player.mp = player.maxMp
        print("\033[32m atk: ", player.atk, ", hp: ", player.maxHp, ", mp: ", player.maxMp, "\033[0m")
        print("\033[1;32m Your PVs and PMs have restored\033[0m")
    print("\033[32m You still have ", (player.xpSup - player.xp),
          " xp before you can level up to the next level.\033[0m")


# If skill option is choosen in fight menu, display the amount of mp
# and the skills unlocked by the player, and ask him to choose one.

# If it's an healing spell, check if the player don't already have all his hp, and if he have enouth mp.
# Then, heal de player and remove some mp according to the values of the spell.
# If the number of hp exeeds maxHp set hp to maxHp value.

# If it's an offensive spell, let the player choose the target if there is more than one,
# verify if there is enouth mp and deal the amount of damage fixed by the spell.

# Not all spells are implemented yet.

# Next, launch EndplayerTurn function.
def Skill(enemies):
    print("\033[1;34m You have ", player.mp, " / ", player.maxMp, "pm \033[0m")
    for j in range(len(player.skills)):
        print(j + 1, " - ", (player.skills[j]).name, "(", (player.skills[j]).cost, "mp )")

    ChoixSorts = int(input("\033[1;34m > Choose a Spell \033[0m")) - 1

    if ChoixSorts < len(player.skills):
        ChoixSorts = player.skills[ChoixSorts]

        # Healing spells :

        if ChoixSorts.name == "Light care" or ChoixSorts.name == "Medium Care" or ChoixSorts.name == "Heavy Care" :

            if player.mp >= ChoixSorts.cost :
                if player.hp < player.maxHp:
                    player.mp -= ChoixSorts.cost
                    player.hp += ChoixSorts.heal
                    print("\033[1;32m You have been treated for ", ChoixSorts.heals, " PV ! \033[0m")
                    if player.hp > player.maxHp:
                        player.hp = player.maxHp
                        print("\033[32m You have ", player.hp, " PV \033[0m")
                        EndPlayerTurn(enemies)
                    else :
                        print("\033[32m Your health is already full. \033[0m")
                        Skill(enemies)
                else :
                    print("You already have all you lives !")
                    Skill(enemies)
            else:
                print("\033[31m You don't have enough mana \033[0m")
                print("\033[33m You missed! ", ChoixSorts.cost - player.mp, " MP \033[0m")
            Skill(enemies)

        # Other spells

        elif ChoixSorts.name == "Sacred Shrine" :
            if player.mp >= ChoixSorts.cost :
                if len(enemies) > 1:
                    ChoixEnemy = int(input("\033[34m Which enemy do you want to attack? \033[0m")) - 1
                    while ChoixEnemy < 0 or ChoixEnemy > len(enemies) - 1:
                        ChoixEnemy = int(input("\033[31m Incorrect! Which enemy would you like to attack? \033[0m")) - 1
                else:
                    ChoixEnemy = 0

                enemies[ChoixEnemy].hp -= ChoixSorts.dmg
                print("\033[32m You have inflicted", ChoixSorts.dmg, "Mmagic damadge to",enemies[ChoixEnemy].name, ChoixEnemy + 1,"\033[33m")
                player.hp += ChoixSorts.heal
                player.mp -= ChoixSorts.cost
                print("\033[1;32m You recovered", ChoixSorts.heal, " PV \033[0m")
                if player.hp > player.maxHp:
                    player.hp = player.maxHp
                    print("\033[32m You still have ", player.hp, " PV \033[0m")
                EndPlayerTurn(enemies)
            else:
                print("\033[31m You lack the mana to continue \033[31m")
                print("\033[33m You missed ", ChoixSorts.cost - player.mp, " MP \033[0m")
                Skill(enemies)
                
        # Offensive spells :
        
        elif ChoixSorts.name == "Life Drain ":
            if player.mp >= ChoixSorts.cost:
                enemies[ChoixEnemy].hp -= ChoixSorts.dmg
                player.hp += ChoixSorts.heal
                player.mp -= ChoixSorts.cost
                print("You inflicted ", ChoixSorts.dmg, "magic damadge to ",enemies[ChoixEnemy].name, ChoixEnemy + 1)
                print("You won", ChoixSorts.heal, " PV")
                if player.hp > player.maxHp:
                    player.hp = player.maxHp
                    print("\033[32m You still have ", player.hp, " PV left.\033[0m")
                EndPlayerTurn(enemies)
            else:
                print("\033[31m You don't have andy mana left \033[0m")
                print("\033[33m You missed ", player.skills[ChoixSorts].cost - player.mp, " MP \033[0m")
                Skill(enemies)

        if player.mp >= ChoixSorts.cost:

            if len(enemies) > 1:
                ChoixEnemy = int(input("\033[34m Which one would you like to attack? ? \033[0m")) - 1
                while ChoixEnemy < 0 or ChoixEnemy > len(enemies) - 1:
                    ChoixEnemy = int(input("\033[31m Wrong! Which enemy would you like to attack? ? \033[0m")) - 1   
            else:
                ChoixEnemy = 0

            player.mp -= ChoixSorts.cost
            enemies[ChoixEnemy].hp -= ChoixSorts.dmg
            print("\033[1;32m You inflicted", ChoixSorts.dmg, "magic damage to",enemies[ChoixEnemy].name, ChoixEnemy + 1, "\033[0m")
            EndPlayerTurn(enemies)    
        else :
            print("\033[31m You don't have enough mana! \0331m")
            print("\033[33m You missed! ", ChoixSorts.cost - player.mp, " MP \033[0m")
            Skill(enemies)

    else:
        print("\033[31m No correspondandt,  \033[0m")
        Fight(enemies)


# If item option is choosen in fight menu, display the items unlocked by the player, and ask him to choose one.

# If it's an healing item, check if the player don't already have all his hp, and if he have one in stock.
# Then, heal de player and remove one item from the stock.
# If the number of hp exeeds maxHp set hp to maxHp value.

# Not all items are implemented yet.

# Next, launch EndplayerTurn function.
def Item(enemies):
    for j in range(len(player.itemList)):
        print("\033[34m",j + 1, " - ", (player.itemList[j].name),"( ",player.itemList[j].count,"in stock ) \033[0m")
    ChoixItem = int(input("\033[1;34m > What will you use ? (Choose a number) : \033[0m")) - 1
    if ChoixItem < len(player.itemList):
        if (player.itemList[ChoixItem]).name == "Provisions":
            if food.count > 0 :
                if player.hp < player.maxHp:
                    player.hp += food.heal
                    food.count -= 1
                    print(food.count)
                    print("\033[1;32m You treated for ", food.heal, " PV ! \033[0m")
                    if player.hp > player.maxHp:
                        player.hp = player.maxHp
                        print("\033[32m You have ", player.hp, "PV \033[0m")
                        EndPlayerTurn(enemies)
                else:
                    print("\033[33m Your hp is full \033[0m")
                    Item(enemies)
            else:
                print("\033[31m Your food inventory is empty! \033[0m")
                Item(enemies)

        elif (player.itemList[ChoixItem]).name == "Care Potion":
            if heal_potion.count > 0:
                if player.hp < player.maxHp:
                    player.hp += heal_potion.heal
                    heal_potion.count -= 1
                    print("\033[1;32m You treated for ", heal_potion.heal, " PV !\033[0m")
                    if player.hp > player.maxHp:
                        player.hp = player.maxHp
                        print("\033[32m You have ", player.hp, "PV \033[0m")
                        EndPlayerTurn(enemies)
                else:
                    print("\033[33m Your health bar is full \033[0m")
                    Item(enemies)
            else:
                print("\033[31m You don't have any potions left! \033[0m")
                Item(enemies)

        elif (player.itemList[ChoixItem]).name == "Mana Stone":
            if heal_potion.count > 0:
                if player.mp < player.maxMp:
                    player.mp += mana_stone.heal
                    mana_stone.count -= 1
                    print("\033[1;32m You gained ", mana_stone.heal, " PM! \033[0m")
                    if player.mp > player.maxMp:
                        player.mp = player.maxMp
                        print("\033[34m You have ", player.mp, "MP \033[0m")
                        EndPlayerTurn(enemies)
                else:
                    print("\033[33m Your mana is full ")
                    Item(enemies)
            else:
                print("\033[31m You don't have any potions left \033[0m")
                Item(enemies)
        else:
            print("\033[31m Error :( \033[0m")
            Fight(enemies)
    else:
        print("\033[31m Error :( \033[0m")
        Fight(enemies)


# When the player enters the shop, display how many coins(Eris) he has,
# and ask him wich category he want to see

# "1" let him see the weapons, wich add some damages independently of the atk value.

# "2" let him see the armors, wich add some damage reduction from the enmies attacks.

# "3" let him see the spell books, wich allows him to acquire new skills, usables during a fight with the skill menu.

# "4" let him see the items usables in fight.

# "5" let him go to the inn, wich allows him to recovers all his hp and mp in exchange of a little bit of money.

# For each purchase, verify if the player has enouth money before completion.
# For each shop menu, an incorrect value returns the player to the precedent menu.
def Shop():
    if player.coins > 0:
        print("\033[32m You have", player.coins, "Eris 033[0m")
        print("\033[34m> 1 - See weapons")
        print("> 2 - See armor")
        print("> 3 - See spell books")
        print("> 4 - See consumables")
        print("> 5 - See Hostel")
        print("> 6 - Going Out033[0m")
        ChoixMagasin = int(input("\033[1;34m> What are you intrested in ? (1/2/3/4/5/6) : \033[0m"))
        if ChoixMagasin == 1:
            print("\033[32m You have", player.coins, "Eris 033[0m")
            print("\033[34m1 - rusty sword - 20 Eris/ 3ATK")
            print("2 - iron sword - 56 Eris/ 6ATK")
            print("3 - steel sword - 120 ris/ 8ATK")
            print("4 - sword in mythril - 250 Eris/ 15ATK")
            print("5 - back 033[0m")
            ChoixArmes = int(input("\033[1;34m Que Voulez vous acheter ? (1/2/3/4/5) : \033[0m"))
            if ChoixArmes == 1:
                if player.coins >= 20:
                    print("\033[32m You bought a red sowrd \033[0m")
                    player.weapon = 3
                    player.coins -= 20
                    Shop()
                else:
                    print("\033[31m You don't have enough \033[0m")
                    Shop()
            elif ChoixArmes == 2:
                if player.coins >= 56:
                    print("\033[34m You bought a Iron sword !\033[0m")
                    player.weapon = 6
                    player.coins -= 56
                    Shop()
                else:
                    print("\033[31m You don't have enough! \033[0m")
                    Shop()
            elif ChoixArmes == 3:
                if player.coins >= 120:
                    print("\033[32m You bought a steel sword! !\033[0m")
                    player.weapon = 8
                    player.coins -= 120
                    Shop()
                else:
                    print("\033[31m You don't have enough for this \033[0m")
                    Shop()
            elif ChoixArmes == 4:
                if player.coins >= 250:
                    print("\033[32m You bought a mythic sword!\033[0m")
                    player.weapon = 15
                    player.coins -= 250
                    Shop()
                else:
                    print("\033[ You donèt have enough \033[0m")
                    Shop()
            else:
                print("\033[33m You go back into the store \033[0m")
                Shop()

        elif ChoixMagasin == 2:
            print("\033[32m You have", player.coins, "Eris \033[0m")
            print("\033[34m 1 - Traveller's clothing - 15 Eris/ 2DEF")
            print("2 - fur armour - 68 Eris / 4DEF")
            print("3-  Steel armour - 145 Eris / 7DEF")
            print("4 - Metal armour 300 Eris / 9DEF")
            print("5 - retern \033[0m")
            ChoixArmures = int(input("\033[1;34m What do you choose ? (1/2/3/4/5) : \033[0m"))
            if ChoixArmures == 1:
                if player.coins >= 15:
                    print("\033[32mv You bought Traveller's clothing !\033[0m")
                    player.armor = 1
                    player.coins -= 15
                    Shop()
                else:
                    print("\033[31m You don't have enough \033[0m")
                    Shop()

            elif ChoixArmures == 2:
                if player.coins >= 68:
                    print("\033[32m You bought fur armour ! \033[0m")
                    player.armor = 3
                    player.coins -= 68
                    Shop()
                else:
                    print("\033[31m You don't have enough \033[0m")
                    Shop()
            elif ChoixArmures == 3:
                if player.coins >= 145:
                    print("\033[32m You bought steel armour \033[0m")
                    player.armor = 5
                    player.coins -= 145
                    Shop()
                else:
                    print("\033[31m You don't have enough \033[0m")
                    Shop()
            elif ChoixArmures == 4:
                if player.coins >= 300:
                    print("\033[32m You bought a metal armour! \033[0m")
                    player.armor = 7
                    player.coins -= 300
                    Shop()
                else:
                    print("\033[31m You don't have enough \033[0m")
                    Shop()
            elif ChoixArmures == 5:
                print("\033[33m You returned all the articles to the store. \033[0m")
                Shop()

        elif ChoixMagasin == 3:
            print("\033[32m You have", player.coins, "Eris \033[0m")
            print("\033[34m1 - Intermediate care - 70 Eris")
            print("2 - Advanced care - 140 Eris")
            print("3-  Lightning - 76 Eris")
            print("4 - Explosion - 150 Eris")
            print("5 - Sacrade sanctuary- 180 Eris")
            print("6 - Life drain -  170 Eris")
            # print("7 - Explosion - 1000 Eris")
            print("7 - Return \033[0m")
            ChoixSort = int(input("\033[1;34m what do you choose ? (1/2/3/4/5/6/7) : \033[0m"))
            if ChoixSort == 1 :
                if player.coins >= 70:
                    print("\033[1;32m You bought Intermediate care !\033[0m")
                    print("\033[32m You now have that skill\033[0m")
                    (player.skills).append(intermediate_heal())
                    player.coins -= 70
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort\033[0m")
                    Shop()                       

            elif ChoixSort == 2:
                if player.coins >= 140:
                    print("\033[1;32m You bought advanced care !\033[0m")
                    print("\033[32m You now have that skill \033[0m")
                    (player.skills).append(advanced_heal())
                    player.coins -= 140
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort\033[0m")
                    Shop()

            elif ChoixSort == 3:
                if player.coins >= 76:
                    print("\033[1;32m You bought lightning\033[0m")
                    print("\033[32m You now have that skill\033[0m")
                    (player.skills).append(lightning())
                    player.coins -= 76
                    Shop()
                else:
                    print("\033[31m You don't have enough\033[0m")
                    Shop()

            elif ChoixSort == 4:
                if player.coins >= 150:
                    print("\033[1;32m You bought explosion \033[0m")
                    print("\033[32m You now have that skill \033[0m")
                    (player.skills).append(explosive_shoot())
                    player.coins -= 150
                    Shop()
                else:
                    print("\033[31m You don't have enough\033[0m")
                    Shop()

            elif ChoixSort == 5:
                if player.coins >= 180:
                    print("\033[1;32m Vous avez acheté le sort sanctuaire sacré \033[0m")
                    print("\033[32m You now have that skill \033[0m")
                    (player.skills).append(sacred_sanctuary())
                    player.coins -= 180
                    Shop()
                else:
                    print("\033[31m You don't have enough \033[0m")
                    Shop()

            elif ChoixSort == 6:
                if player.coins >= 170:
                    print("\033[1;32m Vous avez acheté le sort de drain de vie \033[0m")
                    print(" \033[32m You now have that skill \033[0m")
                    (player.skills).append(drain_touch())
                    player.coins -= 170
                    Shop()
                else:
                    print("\033[31m You don't have enough \033[0m")
                    Shop()
                
                elif ChoixSort == 7:
                 if player.coin >= 1000 :
                     print("Kazuma looks confused...")
                     print("A strange girl dressed in red accompanied by a black cat shows up suddenly.")
                     print("Strange Girl: You want to learn about the most powerful magic in the world ?")
                     print("Megumin: I'm Megumin! The greatest archmage and possessor of the sublime magic of explosion ! ")
                     print("You now have access to this skill")
                     (player.skills).append(explosion())
                     player.coins -= 1000
                     Shop()
                 else :
                     print("\033[31m You don't have enough money to buy this spell book \033[0m")
                     Shop()

            elif ChoixSort == 8:
                print("\033[33m You return all the articles to the store \033[0m")
                Shop()


        elif ChoixMagasin == 4:
            print("\033[32m You have", player.coins, "Eris \033[0m")
            print("\033[34m1 - Provisions - 10 Eris")
            print("2 - Potion of life- 100 Eris ")
            print("3 - Potion of mana- 60 Eris ")
            print("4 - Return \033[0m")
            ChoixObjet = int(input("\033[1;34m What do you choose ? (1/2/3/4) : \033[0m"))
            if ChoixObjet == 1:
                print("\033[32m You bought groceries !\033[0m")
                player.item.append("provision")
                player.coins -= 10
                Shop()
            elif ChoixObjet == 2:
                print("\033[32m You bought the postion of life !\033[0m")
                player.item.append("potion de vie")
                player.coins -= 100
                Shop()
            elif ChoixObjet == 3:
                print("\033[32m You bot the postion of mana !\033[0m")
                player.item.append("Potion of mana")
                player.coins -= 60
                Shop()
             elif ChoixObjet == 4:
                 print("\033[32m You have explotion potion !\033[0m")
                 player.item.append("Exploive Fragment")
                 player.coins -= 5
                 Shop()
            else:
                print("\033[33m You return all the atricles back to the store. \033[0m")
                Shop()
        elif ChoixMagasin == 5:
            print("\033[34m You enter a small inn that serves as a resting place")
            print(
                "Hostels or resting places are places that allow you to control your health and magic 033[0m")
            print("033[32m You have",player.hp," / ",player.maxHp,"PV and ",player.mp," / ",player.maxMp," MP 033[0M" )
            print("\033[32m You have", player.coins, "Eris,", player.hp, "/", player.maxHp, "PV et ", player.mp, "/",
                  player.maxMp, " MP \033[0m")
            repos = (input("\033[33m Do you want to rest for 20 Eris ? (Yes/No): \033[0m"))
            if repos == "Oui":
                player.hp = player.maxHp
                player.mp = player.maxMp
                player.coins -= 20
                print("\033[1;32m Vous étes reposez dans l'auberge, vous avez maintenant", player.hp, "PV/", player.mp,
                      "PM \033[0m")
                print("\033[32m You rest for", player.coins, "Eris \033[0m")
                Shop()
            elif repos == "No":
                print("\033[33m You leave and return to the store \033[0m")
                Shop()
        elif ChoixMagasin == 7:
            print("\033[31m You decide to leave the store\033[0m")
            Movement()
    else:
        print("\033[31m You have been kicked from the store.\033[0m")
    Movement()


# When the player enters the boss zone, start the fight against Vanir with a message.
def EventVanir():
    print("\033[0m- You are in front of a large metal door.")
    time.sleep(1.5)
    print("- You decide to open and face your enemy.")
    time.sleep(1.5)
    print("- You see a man wearing a black and white theatrical mask with blue hair and wearing a purple suit.")
    time.sleep(1.5)
    print('\033[35m')
    print("- Vanir: I've been waiting for you, adventurer.")
    time.sleep(1.5)
    print("- Vanir: You have faced many hardships so far like fighting many monsters and defeating most traps.")
    print('\033[39m')
    print("- You see little dolls in his image closing the door, preventing you from running away.")
    time.sleep(1.5)
    print('\033[35m')
    print("- Vanir: Now is the time for you and me to face off and find out which of evil or good will triumph, beware!")
    print('\033[39m')
    FightVanir()
    print("")
    print("\033[1;31m Coming soon to your game! \033[0m")


def FightVanir():
    print("\033[1;34m You have ", player.hp," / ",player.maxHp,"pv")
    print(" You have ", player.mp," / ",player.maxMp,"pm \033[0m")
    print("\033[34m1 - Attack")
    critical = random.randint(0,9)
    if critical >= 8:
            damage = (player.atk*2) + player.weapon
            print("\033[1;32m You use your sword and slice Vanir inflicting him", damage, "de dégats !\033[0m")
            vanir.hp -= damage
            EndVanir()
    else:
        damage = player.atk + player.weapon
        print("\033[32m You attack Vanir with a powerful heavy attack ", damage, "de dégats \033[0m")
        vanir.hp -= damage
        EndVanir()


def EndVanir():
         if vanir.hp <= 0:
             print("Vanir collapses dramatically, mortally wounded, Vanir begins to speak his last words.")
             time.sleep(1.5)
             print('\033[35m')
             print("Vanir: You got me...I've always dreamed of such a spectacular ending.")
             time.sleep(1.5)
             print("Vanir: My riches...I offer them to you.")
             time.sleep(1.5)
             print("Vanir: Thank you, adventurer, for this legendary ending.")
             time.sleep(1.5)
             print('\033[39m')
             print("With a final sigh, Vanir points to a chest.")
             time.sleep(1.5)
             print("You climb the stairs, passing over Vanir's remains and into the sealed chest.")
             time.sleep(1.5)
             print("")
            #THE TWO DIFFERENT ENDS 

            OpenChest = input("Do you want to open the chest (Yes/No): ")
            #BADENDING
            if OpenChest == "Yes" or OpenChest == "Yes" or OpenChest == "yes":
                print("You open the chest inside...nothing...except an old piece of paper. On it is written “YOU HAVE LOST”)
                time.sleep(1.5)
                print("You hear laughter coming from behind you")
                time.sleep(1.5)
                print("When you read the word, you hear Vanir's last laugh before he dies. You turn to hit him, but he's already gone, gone in peace.")
                time.sleep(1.5)
                print("You hear a sudden click, the door has been locked and hundreds of explosive dolls are heading your way")
                time.sleep(1.5)
                print("In a last burst of courage, you scream like a little girl and the explosions destroying the roof crush you under several rubble of stones killing you instantly.")
                print("")
                gameOver()

            #GOOD ENDING
            elif OpenChest == "No" or OpenChest == "No" or OpenChest == "no":
                 print("You smell the trap coming miles away and just walk away.")
                 time.sleep(1.5)
                 print("Vanir looks at you stunned.")
                 time.sleep(1.5)
                 print('\033[35m')
                 print("Vanir: But...my perfect ending!")
                 time.sleep(1.5)
                 print('\033[39m')
                 print("He disintegrates with one last tear.")
                 time.sleep(1.5)
                 print("Happy with your adventure, you return to the guild and spend all your bounty money on alcohol, food and coffee with your friends.")
                 time.sleep(1.5)
                 print("Today was a good day.")
                 sys.exit()
        else :
            print("\033[32m There is ",vanir.hp,"PV to Vanir\033[0m")
            VanirTurn()
            FightVanir()


def VanirTurn():
        dodge = random. randint(0, 9)
         if dodge >= 8:
             print("\033[32m You are dodging the Vanir dolls" "!\033[0m")
             FightVanir()
         else:
             print("\033[33m ""Vanir sends you explosive dolls\033[0m")
             print("\033[31m the explosion causes you", vanir.atk - player.armor,"damage \033[0m")
             player.hp -= vanir.atk - player.armor
             print("\033[33m you have left", player.hp, "PV \033[0m")
             FightVanir()
         if player.hp <= 0:
             print("you lost")
             gameOver()
         else:
             FightVanir()

largeurGrille = 7
hauteurGrille = 10
grille = []

light_heal()
fire_ball()
intermediate_heal()
advanced_heal()
lightning()
drain_touch()
sacred_sanctuary()
explosive_fragment()

vanir = Vanir()

# Set to True to access direct fight with equilibrated stats against boss Vanir
Cheat = False

mainMenu()
