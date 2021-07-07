import random

def playerNameGen():
    firstNames = ["Dequarius", "Lamar", "Lonzo", "Kunta", "Ezekial", "Charles", "Carmelon", "Kobus", "Elvin", "Julius", "Dolph"]
    lastNames =["Carter", "Smiff", "Johnson", "Porter", "Ali", "Byrd", "Wilkins", "Morris", "Paul", "Cole", "Miller"]

    ranFName=firstNames [random.randint(0,10)]
    ranLName=lastNames [random.randint(0,10)]

    playerName= ranFName + " " + ranLName

    return playerName

numCards = 5

cardsInPack = []

for i in range(0,numCards):
    getName = playerNameGen()
    cardsInPack.insert(i, getName)

print (cardsInPack)

