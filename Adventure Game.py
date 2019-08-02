from AG_Coordinates import tunnels
from Player impo


def DisplayMenu():
    print("Welcome to Unique Adventure Game Name! \n"
          "You are adventurer that got lost in a \n"
          "cave system in the Greek wilderness while \n"
          "exploring ancient ruins\n\n")

    print("You have a backpack that can carry up to 10 items, a torch, \n"
          "an unfinished map, and a strong will to find the way out\n")

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

    while userAlive:
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



# names = ["nate", "al", "bob"]
# names.contains("nate") = True  names.contains("yoseph") = False


main()




