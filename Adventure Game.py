from Enemy import Enemy
from Player import Player
import random

def DisplayMenu():
    print("Welcome to Unique Adventure Game Name! \n"
          "You are adventurer that got lost in a \n"
          "cave system in the Greek wilderness while \n"
          "exploring ancient ruins\n\n")

    print("You have a backpack that can carry up to 15 items, a torch, 10 \n"
          "matches, an unfinished map, and a strong will to find the way out\n")

    print("You have to light your torch every 30 seconds or you can't move. \n"
          "Your map tells you there rooms in throughout the tunnle.\n\n"
          "Rooms have chests to get coins, matches, and weapons. Some rooms have special \n"
          "materials, shrines, and collectables. The goal is to find the way out.\n\n")


def getMoveDirection():
    direction = str(input("do you want to move left, right, forwards, or backwards: "))

    while direction.lower() != "left" and \
            direction.lower() != "right" and \
            direction.lower() != "forwards" and \
            direction.lower() != "backwards":
        direction = str(input("Not a valid answer. Please enter an answer: "))

    return direction


def getMoveAmount():
    movement = int(input("how many paces do you want to move(max 5): "))

    while movement < 0 or movement > 5:
        movement = int(input("Invalid number. Please enter a new number: "))

    return movement

def main():
    movement = 0
    DisplayMenu()
    userAlive = True
    user = Player()
    run = False

    while userAlive:
        chance = random.randint(1, 15)
        print(chance)

        direction = getMoveDirection()
        movement = getMoveAmount()

        if direction.lower() == "left":
            user.left(movement)

        elif direction.lower() == "right":
            user.right(movement)

        elif direction.lower() == "forwards":
            user.forwards(movement)

        elif direction.lower() == "backwards":
            user.backwards(movement)

        print("Current coordinates:", user.userCoordinates)


        if user.userCoordinates == [-5,0,-14]:
            print("Congratulations, you found your way out the cave system!")
            userAlive = False

        if movement >= 1:
            while chance == 13:
                enemy = Enemy()
                print("An enemy has appeared! And he hurt you fam!")
                while user.playerHealth >= 0 and enemy.enemyHealth >= 0 and run is False:
                    user.playerHealth -= enemy.attackDamage
                    print("It attacked, your health is now",user.playerHealth)
                    print("the bad dude's health is",enemy.enemyHealth)
                    attackChoice = str(input("Do you want to Attack or Run : "))
                    if attackChoice.lower() == "attack":
                        enemy.enemyHealth -= user.attackDamage
                        print("The bad dudes health is",enemy.enemyHealth)
                    chance = random.randint(1, 15)

                    if attackChoice.lower() == "run":
                        run = True
                        chance = random.randint(1, 15)

main()


# occurance chance = 13



