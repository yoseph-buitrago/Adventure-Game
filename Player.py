from AG_Coordinates import tunnels
class Player:
    def __init__(self):
        self.userCoordinates = [0,0,0]
        self.walkingSpeed = 2
        self.playerHealth = 30
        self.inventory = []


    def left(self, movement):
        myTunnels = []
        tunnel = tunnels()  # calls tunnels
        validMove = False
        intersectionPoints = []

        # loops through dictionary to find which tunnel we're in
        for i in tunnel:
            if self.userCoordinates in tunnel[i]:
                myTunnels.append(i)

        # New method of movement that allows me to append each coordinate moved into a list so i can check if any coordinate the user passes is an intersection point
        for i in range(1, movement + 1):
            self.userCoordinates[0] -= 1

        # checks for coordinate in tunnels
        for j in myTunnels:
            if self.userCoordinates in tunnel[j]:
                validMove = True
                # notifies the user of the intersection point

        # Takes back the movement if coordinate is not found in tunnels
        if not validMove:
            print("That is not a valid to move make here. Make a different move.")
            self.userCoordinates[0] += movement

        else:
            checkIntersection = self.userCoordinates.copy()
            for i in range(0, movement):
                j = 0
                if i == 0:
                    j = 0
                else:
                    j = 1

                checkIntersection[0] -= j
                if checkIntersection in tunnel["Intersections"]:
                    intersectionPoints.append(checkIntersection.copy())

            if len(intersectionPoints) != 0:
                print("You passed some intersection points:", intersectionPoints)
                tayK = str(input("Do you want to go through those points? (yes or no): "))

                while tayK.lower() != "yes" and tayK.lower() != "no":
                    tayK = str(input("Enter a valid answer. (yes or no):"))

                if tayK.lower() == "yes":
                    soulja = int(input(
                        "What intersection point do you want to go to (Enter 1 - {})".format(len(intersectionPoints))))

                    while soulja < 1 or soulja > len(intersectionPoints):
                        soulja = int(input("Please enter a valid option:"))

                    userCoordinates = intersectionPoints[soulja - 1].copy()
                    print("Current Coordinates:", self.userCoordinates)

    def right(self, movement):
        myTunnels = []
        tunnel = tunnels()  # calls tunnels
        validMove = False
        intersectionPoints = []

        # loops through dictionary to find which tunnel we're in
        for i in tunnel:
            if self.userCoordinates in tunnel[i]:
                myTunnels.append(i)

        # New method of movement that allows me to append each coordinate moved into a list so i can check if any coordinate the user passes is an intersection point
        for i in range(1, movement + 1):
            self.userCoordinates[0] += 1

        # checks for coordinate in tunnels
        for j in myTunnels:
            if self.userCoordinates in tunnel[j]:
                validMove = True
                # notifies the user of the intersection point

        # Takes back the movement if coordinate is not found in tunnels
        if not validMove:
            print("That is not a valid to move make here. Make a different move.")
            self.userCoordinates[0] -= movement

        else:
            checkIntersection = self.userCoordinates.copy()
            for i in range(0, movement):
                j = 0
                if i == 0:
                    j = 0
                else:
                    j = 1

                checkIntersection[0] -= j
                if checkIntersection in tunnel["Intersections"]:
                    intersectionPoints.append(checkIntersection.copy())

            if len(intersectionPoints) != 0:
                print("You passed some intersection points:", intersectionPoints)
                tayK = str(input("Do you want to go through those points? (yes or no): "))

                while tayK.lower() != "yes" and tayK.lower() != "no":
                    tayK = str(input("Enter a valid answer. (yes or no):"))

                if tayK.lower() == "yes":
                    soulja = int(input(
                        "What intersection point do you want to go to (Enter 1 - {})".format(
                            len(intersectionPoints)), ))

                    while soulja < 1 or soulja > len(intersectionPoints):
                        soulja = int(input("Please enter a valid option:"))

                    userCoordinates = intersectionPoints[soulja - 1].copy()
                    print("Current Coordinates:", self.userCoordinates)

    def forwards(self, movement):
        myTunnels = []
        tunnel = tunnels()  # calls tunnels
        validMove = False
        intersectionPoints = []

        # loops through dictionary to find which tunnel we're in
        for i in tunnel:
            if self.userCoordinates in tunnel[i]:
                myTunnels.append(i)

        # New method of movement that allows me to append each coordinate moved into a list so i can check if any coordinate the user passes is an intersection point
        for i in range(1, movement + 1):
           self.userCoordinates[2] += 1

        # checks for coordinate in tunnels
        for j in myTunnels:
            if self.userCoordinates in tunnel[j]:
                validMove = True
                # notifies the user of the intersection point

        # Takes back the movement if coordinate is not found in tunnels
        if not validMove:
            print("That is not a valid to move make here. Make a different move.")
            self.userCoordinates[2] -= movement

        else:
            checkIntersection = self.userCoordinates.copy()
            for i in range(0, movement):
                j = 0
                if i == 0:
                    j = 0
                else:
                    j = 1

                checkIntersection[2] -= j
                if checkIntersection in tunnel["Intersections"]:
                    intersectionPoints.append(checkIntersection.copy())

            if len(intersectionPoints) != 0:
                print("You passed some intersection points:", intersectionPoints)
                tayK = str(input("Do you want to go through those points? (yes or no): "))

                while tayK.lower() != "yes" and tayK.lower() != "no":
                    tayK = str(input("Enter a valid answer. (yes or no):"))

                if tayK.lower() == "yes":
                    soulja = int(input(
                        "What intersection point do you want to go to (Enter 1 - {})".format(len(intersectionPoints))))

                    while soulja < 1 or soulja > len(intersectionPoints):
                        soulja = int(input("Please enter a valid option:"))

                    userCoordinates = intersectionPoints[soulja - 1].copy()
                    print("Current Coordinates:", self.userCoordinates)

        return self.userCoordinates

    def backwards(self, movement):
        myTunnels = []
        tunnel = tunnels()  # calls tunnels
        validMove = False
        intersectionPoints = []

        # loops through dictionary to find which tunnel we're in
        for i in tunnel:
            if self.userCoordinates in tunnel[i]:
                myTunnels.append(i)

        # New method of movement that allows me to append each coordinate moved into a list so i can check if any coordinate the user passes is an intersection point
        for i in range(1, movement + 1):
            self.userCoordinates[2] -= 1

        # checks for coordinate in tunnels
        for j in myTunnels:
            if self.userCoordinates in tunnel[j]:
                validMove = True
                # notifies the user of the intersection point

        # Takes back the movement if coordinate is not found in tunnels
        if not validMove:
            print("That is not a valid to move make here. Make a different move.")
            self.userCoordinates[2] += movement

        else:
            checkIntersection = self.userCoordinates.copy()
            for i in range(0, movement):
                j = 0
                if i == 0:
                    j = 0
                else:
                    j = 1

                checkIntersection[2] -= j
                if checkIntersection in tunnel["Intersections"]:
                    intersectionPoints.append(checkIntersection.copy())

            if len(intersectionPoints) != 0:
                print("You passed some intersection points:", intersectionPoints)
                tayK = str(input("Do you want to go through those points? (yes or no): "))

                while tayK.lower() != "yes" and tayK.lower() != "no":
                    tayK = str(input("Enter a valid answer. (yes or no):"))

                if tayK.lower() == "yes":
                    soulja = int(input(
                        "What intersection point do you want to go to (Enter 1 - {})".format(
                            len(intersectionPoints)), ))

                    while soulja < 1 or soulja > len(intersectionPoints):
                        soulja = int(input("Please enter a valid option:"))

                    userCoordinates = intersectionPoints[soulja - 1].copy()
                    print("Current Coordinates:", self.userCoordinates)