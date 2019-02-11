from AG_coordinates_dic import tunnels
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
    

def left(userCoordinates, movement):
    myTunnels = [] 
    tunnel = tunnels() #calls tunnels
    validMove = False
    l00p == True

    movementC = []

    originalCoordinates = userCoordinates
    
# loops through dictionary to find which tunnel we're in
    for i in tunnel:
       if userCoordinates in tunnel[i]:
            myTunnels.append(i)
            
#New method of movent that allows me to append each coordinate moved into a list so i can check if any coordinate the user passes is an intersection point
    for i in range(1, movement + 1):
        userCoordinates[0] -= 1
        movementC.append(userCoordinates)
   
    #checks for coordinate in tunnels
    for j in myTunnels:
        if userCoordinates in tunnel[j]:
            validMove = True
            for i in movementC: #checks to see if any of the coordinates in movementC are in the Intersections key of the tunnels dictionary
                if i in tunnels[Intersections]:
                    print("You are at an intersection:",tunnels[Intersections][tunnels[Intersections].indexOf(i)],"You can go through this tunnel")
                    #notifies the user of the intersection point
            
    #Takes back the movement if coordinate is not found in tunnels
    if validMove == False:
        print("That is not a valid to move make here. Make a different move.")
        userCoordinates[0] += movement

        


def right(userCoordinates, movement):
    myTunnels = []
    tunnel = tunnels()
    validMove = False

    movementC = []

    for i in tunnel:
       if userCoordinates in tunnel[i]:
            myTunnels.append(i)
    
    for i in range(1, movement + 1):
        userCoordinates[0] += 1
        movementC.append(userCoordinates)
    

    for j in myTunnels:
        if userCoordinates in tunnel[j]:
            validMove = True
            for i in movementC:
                if i in tunnels[Intersections]:
                    print("You are at an intersection:",tunnels[Intersections][tunnels[Intersections].indexOf(i)],"You can go through this tunnel")

    if validMove == False:
        print("That is not a valid move to make here. Make a different move.")
        userCoordinates[0] -= movement



def forwards(userCoordinates, movement):
    myTunnels = []
    tunnel = tunnels()
    validMove = False

    movementC = []

    for i in tunnel:
        if userCoordinates in tunnel[i]:
            myTunnels.append(i)
    
    for i in range(1, movement = 1):
        userCoordinates[2] += 1
        movementC.append(userCoordinates)
    

    for j in myTunnels:
        if userCoordinates in tunnel[j]:
            validMove = True
            for i in movementC:
                if i in tunnels[Intersections]:
                    print("You are at an intersection:",tunnels[Intersections][tunnels[Intersections].indexOf(i),"You can go throught this tunnel")

    if validMove == False:
        print("That is not a valid move to make here. Make a different move.")
        userCoordinates[2] -= movement

    print(userCoordinates)
        

def backwards(userCoordinates, movement):
    myTunnels = []
    tunnel = tunnels()
    validMove = False

    for i in tunnel:
        if userCoordinates in tunnel[i]:
            myTunnels.append(i)
    
    userCoordinates[2] -= movement

    for j in myTunnels:
        if userCoordinates in tunnel[j]:
            validMove = True

    if validMove == False:
        print("That is not a valid move to make here. Make a different move.")
        userCoordinates[2] += movement


def up(userCoordinates, movement):
    myTunnels = []
    tunnel = tunnels()
    validMove = False

    for i in tunnel:
        if userCoordinates in tunnel[i]:
            myTunnels.append(i)
    
    userCoordinates[0] += movement

    for j in myTunnels:
        if userCoordinates in tunnel[j]:
            validMove = True

    if validMove == False:
        print("That is not a valid move to make here. Make a different move.")
        userCoordinates[0] -= movement


def down(userCoordinates, movement):
    myTunnels = []
    tunnel = tunnels()
    validMove = False

    for i in tunnel:
        if userCoordinates in tunnel[i]:
            myTunnels.append(i)
    
    userCoordinates[0] -= movement

    for j in myTunnels:
        if userCoordinates in tunnel[j]:
            validMove = True

    if validMove == False:
        print("That is not a valid move to make here. Make a different move.")  
        userCoordinates[0] += movement
        
    

def notifyIntersections(userCoordinates, movement, direction):
    movementC = []

    
    


def main():
    userCoordinates =[0,0,0]
    movement = 0
    #tunnels = tunnels()
    DisplayMenu()
    userAlive = True

    while userAlive:
        direction = getMoveDirection()
        movement = getMoveAmount()

        if direction.lower() == "left":
            left(userCoordinates, movement)
            notifyIntersection()

        elif direction.lower() == "right":
            right(userCoordinates, movement)

        elif direction.lower() == "forwards":
            forwards(userCoordinates, movement)

        elif direction.lower() == "backwards":
            backwards(userCoordinates, movement)

        print(userCoordinates)

#names = ["nate", "al", "bob"]
# names.contains("nate") = True  names.contains("yoseph") = False


main()


