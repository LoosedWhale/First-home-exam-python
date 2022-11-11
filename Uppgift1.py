"""Uppgift ett 1 a) skapar en function där en if sats testar om 1 = 1.
Om detta uppfylls så skrivs True ut annars skrivs False ut"""

def selectionExp():
    if 1 == 1:
        print("True")
    else:
        print("False")
selectionExp()

"""Uppgift ett 1 b) skapar en function. I funktionen skappas en list.
Denna lista testar om index plats 2 har värdet 3.
Om det uppfylls så skriver den ut Detta kommer att skrivas ut. 
Annars skrivs Detta kommer inte att skrivas ut"""

def selectionExpnrtwo():
    selectionExptwo_list = [1, 2 ,3]
    if selectionExptwo_list[2] == 3:
        print("Detta kommer att skrivas ut")
    else:
        print("Detta kommer inte att skrivas ut")

selectionExpnrtwo()


"""Uppgift ett 2 a) Skapar en function. Denna funktion innehåller en lista som har värdet Sofia i sig.
Listan är nu lika mid sig själv gånger tre.
För att värden i Listan skriv ut värdena, i detta fall Sofia Sofia Sofia. 
"""

def iterationExpOne():
    SofiaList = ["Sofia "]
    SofiaList = SofiaList*3
    for x in SofiaList:
        print(x)
iterationExpOne()

"""Uppgift ett 2 b) Skapar en funktion.
En variable med ett string värde skapas.
För värdena i stringen skriv ut dem.
Skriver ut all bokstäver även mellan slag på en ny rad i terminalen.
"""
def interationExpTwo():
    interationExpTwoString = "Moyai är nice "
    for x in interationExpTwoString:
        print(x)
interationExpTwo()

