import random


def playerNameGen():
    firstNames = ["Dequarius", "Lamar", "Lonzo", "Kunta", "Ezekial", "Charles", "Carmelon", "Kobus", "Elvin", "Julius", "Dolph"]
    lastNames =["Carter", "Smiff", "Johnson", "Porter", "Ali", "Byrd", "Wilkins", "Morris", "Paul", "Cole", "Miller"]

    ranFName=firstNames [random.randint(0,10)]
    ranLName=lastNames [random.randint(0,10)]

    playerName= ranFName + " " + ranLName

    return playerName

def setFoilStatus():
    fStatus="Non-Foil"
    if random.randint(0,10) == 10:
        fStatus="Foil"
    return fStatus

def setAutoStatus():
    aStatus="Non-Auto"
    if random.randint(0,100) == 100:
        aStatus="Auto"
    return aStatus

case_list=[]

for i in range (0,15):
    getName =playerNameGen()
    getFoil = setFoilStatus()
    getAuto = setAutoStatus()
    case ={getName: (getFoil,getAuto)}
    case_list.append(case)

for i, v in enumerate(case_list):
    print (i,v)
