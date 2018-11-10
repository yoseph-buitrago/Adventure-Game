
def DisplayMenu():
    print("Welcome to Unique Adventure Game Name! \n",
         "You are adventurer that got lost in a \n",
         "cave system in the Greek wilderness while \n",
         "exploring ancient ruins")

    print("You have a backpack that can carry up to 10 items, a torch, \n",
          "an unfinished map, and a strong will to find the way out")

    print("You have to light your torch every 30 seconds or you can't move. \n",
          "Your map tells you there rooms in throughout the tunnle. Rooms have \n",
          "chests to get coins, matches, and weapons Some rooms have special \n",
          "materials, shrines, and collectables. The goal is to find the way out.")
    

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
    

def left(userCoordinates, movement):
    userCoordinates[0] -= movement


def right(userCoordinates, movement):
    userCoordinates[0] += movement


def forwards(userCoordinates, movement):
    userCoordinates[2] += movement


def backwards(userCoordinates, movement):
    userCoordinates[2] -= movement


def up(userCoordinates, movement):
    userCoordinates[1] += movement


def down(userCoordinates, movement):
    userCoordinates[1] -= movement
    

def main():
    userCoordinates =[0,0,0]
    movement = 0

    userAlive = True

    while userAlive:
        direction = getMoveDirection()
        movement = getMoveAmount()

        if direction.lower() == "left":
            left(userCoordinates, movement)

        elif direction.lower() == "right":
            right(userCoordinates, movement)

        elif direction.lower() == "forwards":
            forwards(userCoordinates, movement)

        elif direction.lower() == "backwards":
            backwards(userCoordinates, movement)

        print(userCoordinates)



main()


