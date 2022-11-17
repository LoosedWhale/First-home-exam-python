#Takes the days the car is being rentend and checks if its greater than 3 or less then 3
#If the days renting is greater then 3 then print the input times 1200. Adds the Swedish currency "Kr"
#If the days renting is less then 3 ask for how many Swedish miles the user is going to drive then multiply it by 20 and add 700. Adds the Swedish currency "Kr"
#Else prints a nice msg for those whom have choosen to right a negative number

def costCarRenting():
    daysRenting = int(input("How many days do you want to rent the car? \n"))
    if daysRenting > 3:
        totalSum = 1200 * daysRenting
        print("Your sum is: ")
        print(str(totalSum) + "Kr")
    elif daysRenting <= 3:
        mil = int(input("How many mil are you going? \n"))
        totalSum = 700 + (20*mil)
        if totalSum > 0:
            print(str(totalSum) + "Kr")
        else:
            print("Why have you inserted negative numbers. dude wtf man")
costCarRenting()
