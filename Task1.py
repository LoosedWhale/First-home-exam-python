# Task one a) create a function where an if statment checks if 1 = 1. 
# If that is true print "True" else print "False


def selectionExp():
    if 1 == 1:
        print("True")
    else:
        print("False")
selectionExp()


# Task one b) creats a funktion with a list. 
# If the list index number has the value 3 then print "This will be seen" else print "This will not be seen"

def selectionExpNrTwo():
    selectionExpTwoList = [1, 2 ,3]
    if selectionExpTwoList[2] == 3:
        print("This will be seen")
    else:
        print("This will not be seen")

selectionExpNrTwo()

# Task one 2 a) creats a function. 
# The functions contins a list and this list is equal to it self 3 times
# For the values in the updated list print the values

def iterationExpOne():
    SofiaList = ["Sofia "]
    SofiaList = SofiaList*3
    for x in SofiaList:
        print(x)
iterationExpOne()

#Task one 2 b) creats a funtion.
#Creats a varible with a value
#for the values in the varible print them (will print the letters and spaces seperated)

def interationExpTwo():
    interationExpTwoString = "Moyai is nice "
    for x in interationExpTwoString:
        print(x)
interationExpTwo()

