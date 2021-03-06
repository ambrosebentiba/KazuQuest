import random
import sys
import time

# Define the starting stats of the player
class Player:
    def __init__(self):
        self.name = "Kazutrash"
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
        self.name = "choux volant"
        self.item = food


class giant_frog:
    def __init__(self):
        self.hp = 4
        self.atk = 3
        self.xp = 4
        self.gold = 3
        self.name = "grenouille géante"
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
        self.name = "mort-vivant"
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
        self.name = "Potion de soin"
        self.heal = 10
        self.count = 1


class mana_stone:
    def __init__(self):
        self.name = "Pierre de mana"
        self.heal = 10
        self.count = 1


# class explosive_fragment:
#     def __init__(self):
#         self.name = "Fragment explosif"
#         self.dmg = 5
#         self.count = 1


# Define stats of skills and spells
class light_heal:
    def __init__(self):
        self.name = "Soins légers"
        self.heal = 5
        self.cost = 5

class intermediate_heal:
    def __init__(self):
        self.name = "Soins intermédiaires"
        self.hp = 10
        self.cost = 10

class advanced_heal:
    def __init__(self):
        self.name = "Soins avancés"
        self.heal = 20
        self.cost = 18

class fire_ball:
    def __init__(self):
        self.name = "Boule de feu"
        self.cost = 6
        self.dmg = 4

class lightning:
    def __init__(self):
        self.name = "Eclair"
        self.cost = 9
        self.dmg = 9

class sacred_sanctuary:
    def __init__(self):
        self.name = "Sanctuaire Sacré"
        self.cost = 11
        self.heal = 9
        self.dmg = 4

class drain_touch:
    def __init__(self):
        self.name = "Drain de Vie"
        self.cost = 11
        self.heal = 4
        self.dmg = 9

# class explosive_shoot:
#     def init(self):
#         self.name = "Tir explosif"
#         self.cost = 15
#         self.dmg = 11



# Display the menu at the start of the game, wich allows the player to start a new game or see the credits.
def mainMenu():
    print("1.Nouvelle partie")
    print("2.Histoire & Régles")
    print("3.Crédits")
    print("4.Quitter")
    #ASKING THE USER WHAT THEY WHANT 
    selecMenu = int(input("Que voulez-vous faire? 1/2/3/4 : "))
    if selecMenu == 1:
        startGame()
    elif selecMenu == 2:
        print("- Il était une fois un groupe de puissants aventuriers, composé d’une Archimage ,d’une croisée , d’une Archiprêtre et d’un vaillant et charismatique héros provenant d’un autre monde ont décidé de faire face au général du roi démon Vanir et sont devenus des légendes...")
        time.sleep(2.5)
        print("- Sauf que non. ")
        time.sleep(2.5)
        print("- La croisée avait pour mission de tuer des choux dans les plaines mais étant une masochiste incapable de manier une épée, elle ne réussit pas en tuer un seul et les conséquences ont été désatreuses car la moitié des champs de la ville furent détruits.")
        time.sleep(2.5)
        print("- Dû à ses dettes immenses provenant de l’achat d’une grande quantité d’alcool dans la ville d’Axel, l’archiprêtre à décidé de fuir ses dettes et de se réfugier dans la forêt réveillant de nombreuses bêtes.")
        time.sleep(2.5)
        print("- Pour exprimer son amour pour la magie d’explosion, la jeune archimage déchaîna sa magie sur un château abandonné rempli de mort vivant ou de squelette qui dormait paisiblement. Vous êtes le seul espoir face au démoniaque et puissant Vanir pour rétablir l’ordre et la paix dans la ville d’Axel.")
        time.sleep(2.5)
        print("- Quant au héros, on raconte qu'il a disparu et est devenu marchand dans le but de vivre une vie de paresse sans avoir à combattre.")
        time.sleep(2.5)
        print("")
        print("--------------------------------------------")
        print("")
        print("Vous êtes un aventurier débutant dont le rôle est d'éliminer un puissant afin de rétablir la paix dans la vile!")
        print("Vous devrez : ")
        print("- Affronter des monstre pour gagner de l’argent/item/xp et gloire,")
        print("- Utiliser cet argent pour acheter des puissantes armes/armures/sorts,")
        print("- Atteindre le chateau du puissant démon Vanir et le vaincre !")
        #confirm = str(input("Sortir? Ecrire oui quand vous êtes prêts. "))
        #if confirm == "oui" or confirm == "Oui" or confirm == "o" or confirm == "1" :
        print("")
        mainMenu()
    elif selecMenu == 3:
        print("____________________________________________________")
        print("|                                                   |")
        print("|        Contributors to the Kazuquest project :    |")
        print("|                                                   |")
        print("|     ",'\033[36m',"          Ambrose Ben Tiba      ",'\033[39m',"          |")
        print("|     ",'\033[35m',"            Cyril Chuzel        ",'\033[39m',"          |")
        print("|     ",'\033[31m',"           Merwan Mahiout       ",'\033[39m',"          |")
        print("|                                                   |")
        print("|          And thanks also to our professor         |")
        print("|     ",'\033[32m',"    Loic Janin",'\033[39m',"from",'\033[32m',"HETIC",'\033[39m',"who            |")
        print("|              taught us about Python               |")
        print("|                                                   |")
        print("|___________________________________________________|")
        mainMenu()
    elif selecMenu == 4:
        print("Alors comme ça on fuit? Adieu sale couard!")
        sys.exit()


# Initialize the game grid and the stats of the player, and launch the game.
# Also activate cheat code for immediate fight against boss
def startGame():
    print("")
    print("\033[1;42;30m NOUVELLE PARTIE \033[0m")
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

    print("- Vous êtes un aventurier débutant vivant dans la ville d’Axel réputée ""pour ses activités de commerce ainsi que pour sa guilde réunissant les personnes en quête d’aventures.")
    time.sleep(1.5)
    print("- Vous levez de votre lit et décidez de vous balader dans la ville, vous pensez au début aller dans un “café”,mais vous préférez aller à la guilde des aventuriers.")
    time.sleep(1.5)
    print("- Vous entrez dans la guilde, pour prendre une quête facile pour obtenir un peux d’argent, vous donner votre quête à la charmante réceptionniste de la guilde Luna pour qu’elle valide votre quête")
    time.sleep(1.5)
    print('\033[33m')
    print("- Luna : Ca fait longtemps que vous n'êtes pas passé à la guilde")
    time.sleep(1.5)
    player.name = input("- Luna : Tu pourrais me rappeler ton prénom ?: ")
    print("- Luna : Donne moi ta quête ",player.name,"je vais te la valider tout de suite.")
    time.sleep(1.5)
    print('\033[39m')
    print("- Pendant que Luna valide votre quête vous décidez de regarder sur votre carte d’aventurier vos statistiques:")
    time.sleep(1.5)
    print('\033[34m')
    print("- Vous êtes au niveau 1.")
    print(player.hp,"/",player.hp,"PV")
    print(player.mp,"/",player.mp,"PM")
    print("- Sorts:")
    print("- Soin rapide")
    print("- Boule de feu")
    print("- Vous avez",player.coins,"Eris")
    time.sleep(3)
    print('\033[39m')
    print("- Avant que Luna valide votre quête, un grand groupe d'aventuriers blessés et terrorisés arrive expliquant que le groupe de héros a échoué et que le général démon Vanir à prévu d'envoyer un fléau sur la ville d’Axel et a décidé de se cacher dans un château.")
    print('\033[33m')
    time.sleep(1.5)
    print("- Luna: C’est un grand problème car tous les aventuriers sont soit enfouis ou ont quitté la ville et le seul aventurier disponible c'est toi.")
    time.sleep(1.5)
    print("- Vous quittez la guilde et votre aventure commence maintenant: ")
    print("")

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
    MovementPos = str(input("\033[1;36m > Dans quelle direction voulez-vous aller ? (N/O/S/E) \033[0m"))

    if MovementPos == "N":
        if position[0] * hauteurGrille >= 0 and position[0] * hauteurGrille <= hauteurGrille * (hauteurGrille - 2) and \
                grille[((position[0] + 1) * largeurGrille + position[1])][2] != "undefined":
            position[0] += 1
            print("\033[36m Vous partez vers le nord \033[0m")
        else:
            print("\033[31m La zone est bloquée, essayez une autre direction \033[0m")
            Movement()

    elif MovementPos == "O":
        if position[1] * largeurGrille >= 1 and position[1] <= largeurGrille and \
                grille[(position[0] * largeurGrille + (position[1] - 1))][2] != "undefined":
            position[1] -= 1
            print("\033[36m Vous partez vers l'ouest \033[0m")
        else:
            print("\033[31m La zone est bloquée, essayez une autre direction \033[0m")
            Movement()

    elif MovementPos == "E":
        if position[1] >= 0 and position[1] <= largeurGrille - 2 and \
                grille[(position[0] * largeurGrille + (position[1] + 1))][2] != "undefined":
            position[1] += 1
            print("\033[36m Vous partez vers l'est \033[0m")
        else:
            print("\033[31m La zone est bloquée, essayez une autre direction \033[0m")
            Movement()

    elif MovementPos == "S":
        if position[0] * hauteurGrille >= 1 and position[0] * hauteurGrille <= hauteurGrille * (hauteurGrille - 1) and \
                grille[((position[0] - 1) * largeurGrille + position[1])][2] != "undefined":
            position[0] -= 1
            print("\033[36m Vous partez vers le sud")
        else:
            print("\033[31m La zone est bloquée, essayez une autre direction \033[0m")
            Movement()

    else:
        print("\033[31m Direction non reconnue, veuillez rééssayer \033[0m")
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
            "\033[1;34m Vous êtes arrivé dans un petit bazar remplis d'objets, tenu par un marchand nommé Satou Kazuma\033[0m")
        Shop()
    elif grille[((position[0]) * largeurGrille + position[1])][2] == "plains":
        print("\033[1;36m Vous vous trouvez dans les plaines, peuplées d'enemis de bas niveau. \033[0m")
    elif grille[((position[0]) * largeurGrille + position[1])][2] == "forest":
        print("\033[1;36m Vous vous trouvez dans la foret, habitée par des enemis de rang intermediaire. \033[0m")
    elif grille[((position[0]) * largeurGrille + position[1])][2] == "castle":
        print("\033[1;36m Vous vous trouvez dans le chateau, hanté par de nombreux enemis de rang supérieur \033[0m")
    elif grille[((position[0]) * largeurGrille + position[1])][2] == "city":
        print("\033[1;36m Vous vous trouvez dans la ville d'Axel, où se rassemblent les aventuriers débutants en quête d'aventure. \033[0m")
        print("\033[1;36m Vous trouverez un magasin à l'extrème sud. \033[0m")

    if grille[((position[0]) * largeurGrille + position[1])][2] != "city":
        spawnEnemies()

    Movement()


# Create a list of random enemies in random number, according to the tile on the grid the player is on,
# And launch fight against the enemies list with a message
def spawnEnemies():
    Enemies = []
    print("\033[1;31m Des monstres vous attaquent par surprise !\033[0m")

    if grille[((position[0]) * largeurGrille + position[1])][2] == "plains":
        enemyType = random.randint(0, 1)
        if enemyType == 0:
            enemyType = "choux"
            enemyNumber = random.randint(2, 4)
            for i in range(enemyNumber):
                Enemies.append(flying_cabbage())
        elif enemyType == 1:
            enemyType = "grenouille(s) géante(s)"
            enemyNumber = random.randint(1, 2)
            for i in range(enemyNumber):
                Enemies.append(giant_frog())

    elif grille[((position[0]) * largeurGrille + position[1])][2] == "forest":
        enemyType = random.randint(2, 3)
        if enemyType == 2:
            enemyType = "loup(s)"
            enemyNumber = random.randint(2, 4)
            for i in range(enemyNumber):
                Enemies.append(wolf())
        elif enemyType == 3:
            enemyType = "bandit(s)"
            enemyNumber = random.randint(1, 4)
            for i in range(enemyNumber):
                Enemies.append(bandit())
        # elif enemyType == 4:
        #     enemyType = "rocher(s) explosif(s)"
        #     enemyNumber = random.randint(1,2)
        #     for i in range (enemyNumber) :
        #         Enemies.append(explosive_rock())

    elif grille[((position[0]) * largeurGrille + position[1])][2] == "castle":
        enemyType = random.randint(4, 5)
        if enemyType == 4:
            enemyType = "mort-vivant(s)"
            enemyNumber = random.randint(2, 3)
            for i in range(enemyNumber):
                Enemies.append(undead())
        elif enemyType == 5:
            enemyType = "squelette(s)"
            enemyNumber = random.randint(2, 3)
            for i in range(enemyNumber):
                Enemies.append(skeleton())

    print("\033[33m Vous affrontez", enemyNumber, enemyType, "! \033[0m")
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
    print("\033[1;34m Vous avez ", player.hp, " / ", player.maxHp, "pv")
    print(" Vous avez ", player.mp, " / ", player.maxMp, "pm \033[0m")

    print("\033[34m1 - Attaquer")
    print("2 - Compétences et Sorts")
    print("3 - Inventaire")
    print("4 - Fuite")

    ChoixCombat = int(input("> Que voulez-vous faire ? (1/2/3/4) : \033[0m"))

    # Normal attack with 1/5 chance of critical with double damage.
    # Let you choose your target if there is more than one.
    # Also add weapon damages to the total damage dealed, and end the player turn
    if ChoixCombat == 1:

        if len(enemies) > 1:
            ChoixEnemy = int(input("\033[34m Lequel voulez-vous attaquer ? \033[0m")) - 1
            while ChoixEnemy < 0 or ChoixEnemy > len(enemies) - 1:
                ChoixEnemy = int(input("\033[31m Incorrect. Lequel voulez-vous attaquer ? \033[0m")) - 1
        else:
            ChoixEnemy = 0

        critical = random.randint(0, 9)

        if critical >= 8:
            damage = player.atk * 2 + player.weapon
            print("\033[1;32m vous infligez des dégats sévéres au monstre  et lui infligez", damage,
                  "de dégats !\033[0m")
        else:
            damage = player.atk + player.weapon
            print("\033[32m vous attaquez le monstre avec votre arme et lui infligez", damage, "de dégats \033[0m")
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
            print("\033[32m Vous rassemblez votre courage avant de fuir en hurlant \033[0m")
            print("")
            Movement()
        else:
            print("\033[31m Vous courez dans la mauvaise direction et rentrez dans un monstre \033[0m")
            EnemiesTurn(enemies)

    # If the player sends an incorrect value on the menu, restart fight function
    else:
        print("\033[31m Erreur, retour en arrière \033[0m")
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
            print("\033[1;32m", enemies[scanEnemy].name, scanEnemy + 1, " est vaincu !\033[0m")
            player.xp += enemies[scanEnemy].xp
            player.coins += enemies[scanEnemy].gold

            drop = random.randint(0,3)
            if drop == 0:
                enemies[scanEnemy].item.count += 1
 
            enemies.pop(scanEnemy)
        scanEnemy += 1

    if not enemies:
        print("\033[1;32m Vous remportez le combat !\033[0m")
        print("\033[32m Vous avez ", player.coins, " pieces d'or au total. \033[0m")
        Level()
        Movement()
    else:
        for u in range(len(enemies)):
            print("\033[32m Il reste", enemies[u].hp, "PV à", enemies[u].name, u + 1, "\033[0m")
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
            print("\033[32m Vous esquivez l'attaque de", enemies[i].name, i + 1, "! \033[0m")
        else:
            print("\033[33m ", enemies[i].name, i + 1, "Attaque ! \033[0m")
            print("\033[31m vous avez perdu", enemies[i].atk - player.armor, "PV \033[0m")
            player.hp -= enemies[i].atk - player.armor

    print("\033[33m il vous reste", player.hp, "PV \033[0m")

    if player.hp <= 0:
        gameOver()
    else:
        Fight(enemies)


# Send Game Over message, and ask for a replay.
def gameOver():
    print("")
    print(
        "\033[1;31m Votre aventure s'achève ici. Avec un peu de chance, une gentille déesse voudra bien vous réincarner (Ephc !)")
    print(" Mais en attendant votre dépouille nourirra les monstres... \033[0m")
    print("")
    retry = str(input("\033[1;32m Voulez-vous recommencer ? (Oui/Non) \033[0m"))
    if retry == "Oui" or retry == "oui":
        mainMenu()
    elif retry == "Non" or retry == "non": 
        sys.exit()
    else :
        print("...Même ça, c'est trop dur pour toi ?...")
        sys.exit()
    


# After the fight, calculate if the xp have reached the amount needed to gain a level.
# If so, send message,add stats, retrieve hp and mp, and increases the amount of xp needed for next level.
# If not, tell what amount of xp is still needed to reach next level, and return to movement function
def Level():
    while player.xp >= player.xpSup:
        player.lvl += 1
        print("\033[1;32m Félicitation, vous êtes passé au niveau", player.lvl, "! \033[0m")
        player.xpSup = int(player.xpSup * 2.2)
        player.atk += 1
        player.maxHp += 3
        player.hp = player.maxHp
        player.maxMp += 2
        player.mp = player.maxMp
        print("\033[32m atk: ", player.atk, ", hp: ", player.maxHp, ", mp: ", player.maxMp, "\033[0m")
        print("\033[1;32m Vos PV et vos PM ont étés restaurés ! \033[0m")
    print("\033[32m Il vous reste ", (player.xpSup - player.xp),
          " points d'xp avant de passer au niveau supérieur \033[0m")


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
    print("\033[1;34m Vous avez ", player.mp, " / ", player.maxMp, "pm \033[0m")
    for j in range(len(player.skills)):
        print(j + 1, " - ", (player.skills[j]).name, "(", (player.skills[j]).cost, "mp )")

    ChoixSorts = int(input("\033[1;34m > Choisissez un sort (donner numero) : \033[0m")) - 1

    if ChoixSorts < len(player.skills):
        ChoixSorts = player.skills[ChoixSorts]

        # Healing spells :

        if ChoixSorts.name == "Soins légers" or ChoixSorts.name == "Soins intermédiaires" or ChoixSorts.name == "Soins avancés" :

            if player.mp >= ChoixSorts.cost :
                if player.hp < player.maxHp:
                    player.mp -= ChoixSorts.cost
                    player.hp += ChoixSorts.heal
                    print("\033[1;32m Vous avez été soigné de ", ChoixSorts.heals, " PV ! \033[0m")
                    if player.hp > player.maxHp:
                        player.hp = player.maxHp
                        print("\033[32m Il vous reste ", player.hp, " PV \033[0m")
                        EndPlayerTurn(enemies)
                    else :
                        print("\033[32m Votre santée est déjà pleine \033[0m")
                        Skill(enemies)
                else :
                    print("Vous avez déjà toute votre vie !")
                    Skill(enemies)
            else:
                print("\033[31m Vous n'avez pas assez de mana \033[0m")
                print("\033[33m Il vous manque ", ChoixSorts.cost - player.mp, " MP \033[0m")
            Skill(enemies)

        # Other spells

        elif ChoixSorts.name == "Sanctuaire Sacré" :
            if player.mp >= ChoixSorts.cost :
                if len(enemies) > 1:
                    ChoixEnemy = int(input("\033[34m Lequel voulez-vous attaquer ? \033[0m")) - 1
                    while ChoixEnemy < 0 or ChoixEnemy > len(enemies) - 1:
                        ChoixEnemy = int(input("\033[31m Incorrect. Lequel voulez-vous attaquer ? \033[0m")) - 1
                else:
                    ChoixEnemy = 0

                enemies[ChoixEnemy].hp -= ChoixSorts.dmg
                print("\033[32m Vous avez infligé", ChoixSorts.dmg, "dégats magiques à",enemies[ChoixEnemy].name, ChoixEnemy + 1,"\033[33m")
                player.hp += ChoixSorts.heal
                player.mp -= ChoixSorts.cost
                print("\033[1;32m Vous avez récupéré", ChoixSorts.heal, " PV \033[0m")
                if player.hp > player.maxHp:
                    player.hp = player.maxHp
                    print("\033[32m Il vous reste ", player.hp, " PV \033[0m")
                EndPlayerTurn(enemies)
            else:
                print("\033[31m Vous n'avez pas assez de mana \033[31m")
                print("\033[33m Il vous manque ", ChoixSorts.cost - player.mp, " MP \033[0m")
                Skill(enemies)
                
        # Offensive spells :
        
        elif ChoixSorts.name == "Drain de vie":
            if player.mp >= ChoixSorts.cost:
                enemies[ChoixEnemy].hp -= ChoixSorts.dmg
                player.hp += ChoixSorts.heal
                player.mp -= ChoixSorts.cost
                print("vous avez infligé", ChoixSorts.dmg, "dégats magiques à",enemies[ChoixEnemy].name, ChoixEnemy + 1)
                print("vous avez gagné", ChoixSorts.heal, " PV")
                if player.hp > player.maxHp:
                    player.hp = player.maxHp
                    print("\033[32m Il vous reste ", player.hp, " PV \033[0m")
                EndPlayerTurn(enemies)
            else:
                print("\033[31m Vous n'avez pas assez de mana \033[0m")
                print("\033[33m Il vous manque ", player.skills[ChoixSorts].cost - player.mp, " MP \033[0m")
                Skill(enemies)

        if player.mp >= ChoixSorts.cost:

            if len(enemies) > 1:
                ChoixEnemy = int(input("\033[34m Lequel voulez-vous attaquer ? \033[0m")) - 1
                while ChoixEnemy < 0 or ChoixEnemy > len(enemies) - 1:
                    ChoixEnemy = int(input("\033[31m Incorrect. Lequel voulez-vous attaquer ? \033[0m")) - 1   
            else:
                ChoixEnemy = 0

            player.mp -= ChoixSorts.cost
            enemies[ChoixEnemy].hp -= ChoixSorts.dmg
            print("\033[1;32m Vous infligez", ChoixSorts.dmg, "dégats magiques à",enemies[ChoixEnemy].name, ChoixEnemy + 1, "\033[0m")
            EndPlayerTurn(enemies)    
        else :
            print("\033[31m Vous n'avez pas assez de mana \033[31m")
            print("\033[33m Il vous manque ", ChoixSorts.cost - player.mp, " MP \033[0m")
            Skill(enemies)

    else:
        print("\033[31m Pas de sort correspondant, retour en arrière \033[0m")
        Fight(enemies)


# If item option is choosen in fight menu, display the items unlocked by the player, and ask him to choose one.

# If it's an healing item, check if the player don't already have all his hp, and if he have one in stock.
# Then, heal de player and remove one item from the stock.
# If the number of hp exeeds maxHp set hp to maxHp value.

# Not all items are implemented yet.

# Next, launch EndplayerTurn function.
def Item(enemies):
    for j in range(len(player.itemList)):
        print("\033[34m",j + 1, " - ", (player.itemList[j].name),"( ",player.itemList[j].count,"en stock ) \033[0m")
    ChoixItem = int(input("\033[1;34m > Que voulez-vous utiliser ? (Choisir nombre) : \033[0m")) - 1
    if ChoixItem < len(player.itemList):
        if (player.itemList[ChoixItem]).name == "Provisions":
            if food.count > 0 :
                if player.hp < player.maxHp:
                    player.hp += food.heal
                    food.count -= 1
                    print(food.count)
                    print("\033[1;32m Vous avez été soigné de ", food.heal, " PV ! \033[0m")
                    if player.hp > player.maxHp:
                        player.hp = player.maxHp
                        print("\033[32m Vous avez ", player.hp, "PV \033[0m")
                        EndPlayerTurn(enemies)
                else:
                    print("\033[33m Votre vie est déja au maximum \033[0m")
                    Item(enemies)
            else:
                print("\033[31m Vous n'avez plus de nourriture \033[0m")
                Item(enemies)

        elif (player.itemList[ChoixItem]).name == "Potion de soin":
            if heal_potion.count > 0:
                if player.hp < player.maxHp:
                    player.hp += heal_potion.heal
                    heal_potion.count -= 1
                    print("\033[1;32m Vous avez été soigné de ", heal_potion.heal, " PV !\033[0m")
                    if player.hp > player.maxHp:
                        player.hp = player.maxHp
                        print("\033[32m Vous avez ", player.hp, "PV \033[0m")
                        EndPlayerTurn(enemies)
                else:
                    print("\033[33m Votre vie est déja au maximum \033[0m")
                    Item(enemies)
            else:
                print("\033[31m Vous n'avez plus de potion de vie \033[0m")
                Item(enemies)

        elif (player.itemList[ChoixItem]).name == "Pierre de mana":
            if heal_potion.count > 0:
                if player.mp < player.maxMp:
                    player.mp += mana_stone.heal
                    mana_stone.count -= 1
                    print("\033[1;32m Vous avez été soigné de ", mana_stone.heal, " PM! \033[0m")
                    if player.mp > player.maxMp:
                        player.mp = player.maxMp
                        print("\033[34m Vous avez ", player.mp, "MP \033[0m")
                        EndPlayerTurn(enemies)
                else:
                    print("\033[33m Votre mana est déja au maximum ")
                    Item(enemies)
            else:
                print("\033[31m Vous n'avez plus de potions \033[0m")
                Item(enemies)
        else:
            print("\033[31m Erreur, retour en arrière \033[0m")
            Fight(enemies)
    else:
        print("\033[31m Erreur, retour en arrière \033[0m")
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
        print("\033[32m Vous avez", player.coins, "Eris \033[0m")
        print("\033[34m> 1 - Voir armes")
        print("> 2 - Voir armures")
        print("> 3 - Voir livres de sorts")
        print("> 4 - Voir consommables")
        print("> 5 - Voir Auberge")
        print("> 6 - Sortir\033[0m")
        ChoixMagasin = int(input("\033[1;34m> Qu'est ce qui vous interesse ? (1/2/3/4/5/6) : \033[0m"))
        if ChoixMagasin == 1:
            print("\033[32m Vous avez", player.coins, "Eris \033[0m")
            print("\033[34m1 - épée rouillée - 20 Eris/ 3ATK")
            print("2 - épée en fer - 56 Eris/ 6ATK")
            print("3- épée en acier - 120 ris/ 8ATK")
            print("4 - épée en mythril - 250 Eris/ 15ATK")
            print("5 - retour \033[0m")
            ChoixArmes = int(input("\033[1;34m Que Voulez vous acheter ? (1/2/3/4/5) : \033[0m"))
            if ChoixArmes == 1:
                if player.coins >= 20:
                    print("\033[32m Vous avez acheté une épée rouilée! \033[0m")
                    player.weapon = 3
                    player.coins -= 20
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter cet objet \033[0m")
                    Shop()
            elif ChoixArmes == 2:
                if player.coins >= 56:
                    print("\033[34m Vous avez acheté une épée en fer !\033[0m")
                    player.weapon = 6
                    player.coins -= 56
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter cet objet \033[0m")
                    Shop()
            elif ChoixArmes == 3:
                if player.coins >= 120:
                    print("\033[32m Vous avez acheté une épée en acier !\033[0m")
                    player.weapon = 8
                    player.coins -= 120
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter cet objet \033[0m")
                    Shop()
            elif ChoixArmes == 4:
                if player.coins >= 250:
                    print("\033[32m Vous avez acheté une épée en mythril !\033[0m")
                    player.weapon = 15
                    player.coins -= 250
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter cet objet \033[0m")
                    Shop()
            else:
                print("\033[33m Vous retournez voir les articles du magasin \033[0m")
                Shop()

        elif ChoixMagasin == 2:
            print("\033[32m Vous avez", player.coins, "Eris \033[0m")
            print("\033[34m 1 - vétements de voyageur - 15 Eris/ 2DEF")
            print("2 - armure en fer - 68 Eris / 4DEF")
            print("3-  armure en acier - 145 Eris / 7DEF")
            print("4 - armure en orchicalque 300 Eris / 9DEF")
            print("5 - retour \033[0m")
            ChoixArmures = int(input("\033[1;34m Que Voulez vous acheter ? (1/2/3/4/5) : \033[0m"))
            if ChoixArmures == 1:
                if player.coins >= 15:
                    print("\033[32m Vous avez acheté un vétement de voyageur !\033[0m")
                    player.armor = 1
                    player.coins -= 15
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter cet armure \033[0m")
                    Shop()

            elif ChoixArmures == 2:
                if player.coins >= 68:
                    print("\033[32m Vous avez acheté une armure en fer ! \033[0m")
                    player.armor = 3
                    player.coins -= 68
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter cet armure \033[0m")
                    Shop()
            elif ChoixArmures == 3:
                if player.coins >= 145:
                    print("\033[32m Vous avez acheté une armure en acier ! \033[0m")
                    player.armor = 5
                    player.coins -= 145
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter cet armure \033[0m")
                    Shop()
            elif ChoixArmures == 4:
                if player.coins >= 300:
                    print("\033[32m Vous avez acheté une armure en orichalque ! \033[0m")
                    player.armor = 7
                    player.coins -= 300
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter cet armure \033[0m")
                    Shop()
            elif ChoixArmures == 5:
                print("\033[33m Vous retournez voir les articles du magasin \033[0m")
                Shop()

        elif ChoixMagasin == 3:
            print("\033[32m Vous avez", player.coins, "Eris \033[0m")
            print("\033[34m1 - Soin intermédiaire- 70 Eris")
            print("2 - Soins avancés - 140 Eris")
            print("3-  Eclair - 76 Eris")
            print("4 - Tir Explosif - 150 Eris")
            print("5 - Sanctuaire sacré- 180 Eris")
            print("6 - Drain de vie -  170 Eris")
            # print("7 - Explosion - 1000 Eris")
            print("7 - retour \033[0m")
            ChoixSort = int(input("\033[1;34m Que Voulez vous acheter ? (1/2/3/4/5/6/7) : \033[0m"))
            if ChoixSort == 1 :
                if player.coins >= 70:
                    print("\033[1;32m Vous avez acheté le sort soin intermédiaire !\033[0m")
                    print("\033[32m Vous avez désormais accès à cette compétence\033[0m")
                    (player.skills).append(intermediate_heal())
                    player.coins -= 70
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort\033[0m")
                    Shop()                       

            elif ChoixSort == 2:
                if player.coins >= 140:
                    print("\033[1;32m Vous avez acheté le sort soin avancé !\033[0m")
                    print("\033[32m Vous avez désormais accès à cette compétence\033[0m")
                    (player.skills).append(advanced_heal())
                    player.coins -= 140
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort\033[0m")
                    Shop()

            elif ChoixSort == 3:
                if player.coins >= 76:
                    print("\033[1;32m Vous avez acheté le sort d'éclair\033[0m")
                    print("\033[32m Vous avez désormais accès à cette compétence\033[0m")
                    (player.skills).append(lightning())
                    player.coins -= 76
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort\033[0m")
                    Shop()

            elif ChoixSort == 4:
                if player.coins >= 150:
                    print("\033[1;32m Vous avez acheté le sort tir explosif \033[0m")
                    print("\033[32m Vous avez désormais accès à cette compétence \033[0m")
                    (player.skills).append(explosive_shoot())
                    player.coins -= 150
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort \033[0m")
                    Shop()

            elif ChoixSort == 5:
                if player.coins >= 180:
                    print("\033[1;32m Vous avez acheté le sort sanctuaire sacré \033[0m")
                    print("\033[32m Vous avez désormais accès à cette compétence \033[0m")
                    (player.skills).append(sacred_sanctuary())
                    player.coins -= 180
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort \033[0m")
                    Shop()

            elif ChoixSort == 6:
                if player.coins >= 170:
                    print("\033[1;32m Vous avez acheté le sort de drain de vie \033[0m")
                    print(" \033[32mvous avez désormais accès à cette compétence \033[0m")
                    (player.skills).append(drain_touch())
                    player.coins -= 170
                    Shop()
                else:
                    print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort \033[0m")
                    Shop()

            # elif ChoixSort == 7:
                # if player.coin >= 1000 :
                #     print("Kazuma vous regarde bizzarement...")
                #     print("Une étrange fille vêtue de rouge accompagnée d'un chat noir se montre soudainement.")
                #     print("Fille étrange : Tu veux en apprendre sur la magie la plus puissante au monde ?")
                #     print("Megumin : Je suis Megumin ! La plus grande des archimage et possesseuse de la sublime magie d'explosion ! ")
                #     print("vous avez accès maintenant à cette compétences")
                #     (player.skills).append(explosion())
                #     player.coins -= 1000
                #     Shop()
                # else :
                #     print("\033[31m Vous n'avez pas assez d'argent pour acheter ce livre de sort \033[0m")
                #     Shop()

            elif ChoixSort == 8:
                print("\033[33m Vous retournez voir les articles du magasin \033[0m")
                Shop()


        elif ChoixMagasin == 4:
            print("\033[32m Vous avez", player.coins, "Eris \033[0m")
            print("\033[34m1 - Provisions - 10 Eris")
            print("2 - Potions de vie- 100 Eris ")
            print("3 - Pierres de mana- 60 Eris ")
            print("4 - retour \033[0m")
            ChoixObjet = int(input("\033[1;34m Que Voulez vous acheter ? (1/2/3/4) : \033[0m"))
            if ChoixObjet == 1:
                print("\033[32m Vous avez acheté des provisions !\033[0m")
                player.item.append("provision")
                player.coins -= 10
                Shop()
            elif ChoixObjet == 2:
                print("\033[32m Vous avez acheté une potion de vie !\033[0m")
                player.item.append("potion de vie")
                player.coins -= 100
                Shop()
            elif ChoixObjet == 3:
                print("\033[32m Vous avez acheté une pierre de mana !\033[0m")
                player.item.append("pierre de mana")
                player.coins -= 60
                Shop()
            # elif ChoixObjet == 4:
            #     print("\033[32m Vous avez acheté une pierre explosives !\033[0m")
            #     player.item.append("fragment explosif")
            #     player.coins -= 5
            #     Shop()
            else:
                print("\033[33m Vous retournez voir les articles du magasin \033[0m")
                Shop()
        elif ChoixMagasin == 5:
            print("\033[34m Vous entrez dans une petite auberge qui sert de lieu de repos")
            print(
                "Les Auberges ou les lieu de repos sont des endroits qui vous permettent de régnérer votre santé et votre magie \033[0m")
            # print("\033[32m Vous avez",player.hp," / ",player.maxHp,"PV et ",player.mp," / ",player.maxMp," MP \033[0M" )
            print("\033[32m Vous avez", player.coins, "Eris,", player.hp, "/", player.maxHp, "PV et ", player.mp, "/",
                  player.maxMp, " MP \033[0m")
            repos = (input("\033[33m Voulez-vous vous reposez dans l'auberge pour 20 Eris ? (Oui/Non): \033[0m"))
            if repos == "Oui":
                player.hp = player.maxHp
                player.mp = player.maxMp
                player.coins -= 20
                print("\033[1;32m Vous étes reposez dans l'auberge, vous avez maintenant", player.hp, "PV/", player.mp,
                      "PM \033[0m")
                print("\033[32m il vous reste", player.coins, "Eris \033[0m")
                Shop()
            elif repos == "Non":
                print("\033[33m Vous quittez l'auberge et retournez au magasin \033[0m")
                Shop()
        elif ChoixMagasin == 7:
            print("\033[31m Vous décidez de partir du magasin\033[0m")
            Movement()
    else:
        print("\033[31m Vous avez été kick du magasin\033[0m")
    Movement()


# When the player enters the boss zone, start the fight against Vanir with a message.
def EventVanir():
    print("\033[0m- Vous êtes devant une grande porte en métal.")
    time.sleep(1.5)
    print("- Vous décidez d'ouvrir et de faire face a votre ennemi.")
    time.sleep(1.5)
    print("- Vous voyez un homme portant un masque de théâtre de noir et de blanc ayant les cheveux bleu et portant un costume violet.")
    time.sleep(1.5)
    print('\033[35m')
    print("- Vanir : Je vous attendais, aventurier.")
    time.sleep(1.5)
    print("- Vanir : Vous avez fait face à bien des épreuves jusqu'ici comme combattre de nombreux monstres et vaincu la plupart des pièges.")
    print('\033[39m')
    print("- Vous voyez des petites poupées à son image fermant la porte, vous empêchant de vous enfuir.")
    time.sleep(1.5)
    print('\033[35m')
    print("- Vanir : Il est maintenant temps pour vous et moi de nous affronter et de savoir lequel du mal ou du bien triomphera, en garde !")
    print('\033[39m')
    FightVanir()
    # print("")
    # print("\033[1;31m Bientôt dans votre jeu ! \033[0m")


def FightVanir():
    print("\033[1;34m Vous avez ", player.hp," / ",player.maxHp,"pv")
    print(" Vous avez ", player.mp," / ",player.maxMp,"pm \033[0m")
    print("\033[34m1 - Attaquer")
    critical = random.randint(0,9)
    if critical >= 8:
            damage = (player.atk*2) + player.weapon
            print("\033[1;32m vous utiliser votre épée et tranché Vanir lui infligean", damage, "de dégats !\033[0m")
            vanir.hp -= damage
            EndVanir()
    else:
        damage = player.atk + player.weapon
        print("\033[32m vous attaquez Vanir avec une puissante attaque lourde ", damage, "de dégats \033[0m")
        vanir.hp -= damage
        EndVanir()


def EndVanir():
        if vanir.hp <= 0:
            print("Vanir s'effondre de manière dramatique, mortellement blessé, Vanir commence à prononcer ses derniers mots.")
            time.sleep(1.5)
            print('\033[35m')
            print("Vanir : Vous m’avez eu...j’ai toujours rêvé d’une fin aussi spectaculaire.")
            time.sleep(1.5)
            print("Vanir : Mes richesses...je vous les offre.")
            time.sleep(1.5)
            print("Vanir : Merci, aventurier, pour cette fin digne d’une légende.")
            time.sleep(1.5)
            print('\033[39m')
            print("Dans un dernier soupir, Vanir pointe un coffre du doigt.")
            time.sleep(1.5)
            print("Vous montez les escaliers, passant au-dessus de la dépouille de Vanir et vous dirigez vers le coffre scellé .")
            time.sleep(1.5)
            print("")
            #THE TWO DIFFERENT ENDS 

            OpenChest = input("Voulez vous ouvrir le coffre (Oui/Non) : ")
            #BAD ENDING
            if OpenChest == "Oui" or OpenChest  == "Yes" or OpenChest == "oui" :
                print("Vous ouvrez le coffre à l’intérieur...rien...à l’exception d’un vieux morceau de papier. Dessus est inscrit “VOUS AVEZ PERDU")
                time.sleep(1.5)
                print("Vous entendez un rire venant de derrière vous")
                time.sleep(1.5)
                print("Quand vous lisez le mot, vous entendez le dernier rire de Vanir avant de mourir. Vous vous retournez pour le frapper, mais il a déjà disparu, parti en paix.")
                time.sleep(1.5)
                print("Vous entendez un clic soudain, la porte à été verrouillée et des centaines de poupées explosives se dirigent vers vous")
                time.sleep(1.5)
                print("Dans un dernier élan de courage, vous hurlez comme une fillette et les explosions détruisant le toit vous écrasent sous plusieurs gravats de pierres vous tuant instantanément.")
                print("")
                gameOver()

            #GOOD ENDING
            elif OpenChest == "Non" or OpenChest  == "No" or OpenChest == "non" :
                print("Vous sentez le piège venir à des kilomètres et vous contentez de partir.")
                time.sleep(1.5)
                print("Vanir vous regarde stupéfait.")
                time.sleep(1.5)
                print('\033[35m')
                print("Vanir : Mais...ma fin  parfaite!")
                time.sleep(1.5)
                print('\033[39m')
                print("Il se désintègre en lâchant une dernière larme.")
                time.sleep(1.5)
                print("Content de votre aventure, vous retournez à la guilde et dépensez tout l’argent de votre prime en alcool, en nourriture et de passer au café avec vos amis.")
                time.sleep(1.5)
                print("Aujourd'hui fut une bonne journée.")
                sys.exit()
        else :
            print("\033[32m Il reste ",vanir.hp,"PV à Vanir\033[0m")
            VanirTurn()
            FightVanir()


def VanirTurn():
        dodge = random.randint(0, 9)
        if dodge >= 8:
            print("\033[32m Vous esquivez les poupées de Vanir" "! \033[0m")
            FightVanir()
        else:
            print("\033[33m ""Vanir vous envoie des poupées explosives\033[0m")
            print("\033[31m l'explosion vous cause ", vanir.atk - player.armor,"de domages \033[0m")
            player.hp -= vanir.atk - player.armor
            print("\033[33m il vous reste", player.hp, "PV \033[0m")
            FightVanir()
        if player.hp <= 0:
            print("vous avez perdu")
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

# explosive_fragment()

vanir = Vanir()

# Set to True to access direct fight with equilibrated stats against boss Vanir
Cheat = False

mainMenu()