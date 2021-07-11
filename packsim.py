import random
import copy

def setPlayerName():
    firstNames = ["Dequarius", "Lamar", "Lonzo", "Kunta", "Ezekiel", "Charles", "Carmelon", "Kobus", "Elvin", "Julius", "Dolph"]
    lastNames =["Carter", "Smiff", "Johnson", "Porter", "Ali", "Byrd", "Wilkins", "Morris", "Paul", "Cole", "Miller"]

    ranFName=firstNames [random.randint(0,10)]
    ranLName=lastNames [random.randint(0,10)]

    playerName= ranFName + " " + ranLName

    return playerName

def setCardStatus():
    cStatus="Error! No Card Status Assigned!"
    ranNumGen=random.randint(0,100)
    if ranNumGen >50 and ranNumGen <91:
        cStatus="Insert"
    else:
        if ranNumGen>90 and ranNumGen<100:
            cStatus="Foil"
        else:
            if ranNumGen==100:
                cStatus="Auto"
            else:
                cStatus="Base"
    return cStatus

def collectionAdd(existingCollection, cardsToAdd):
    
    d=dict()

    for key in set(list(existingCollection.keys()) + list(cardsToAdd.keys())):
        try:
         d.setdefault(key,[]).append(existingCollection[key])        
        except KeyError:
         pass

        try:
         d.setdefault(key,[]).append(cardsToAdd[key])          
        except KeyError:
         pass
    return d

def newPackGen():


    #Generates the attributes of each card in the pack. The pack consists of 15 cards, and each card consists of the Player Name and its status or type (Base, Insert, Foil, Autograph)   
    player_list=[]
    status_list=[]

    for i in range (0,15):
        getName =setPlayerName()
        getStatus = setCardStatus()

        #This ensures that a player only ever shows up once in a pack, and guarantees 15 cards in every pack
        while getName in player_list:
            getName = setPlayerName()

        player_list.insert(i, getName)
        status_list.insert(i, getStatus)

    #This creates the card as a dictionary, with the player name as the key and the card status as its value
    getPack = dict(zip(player_list, status_list))
    return getPack

#Sets the user's current card collection to an empty dictionary
currentCollection=dict()

print("Welcome to Sports Ball Trading Card Pack Opening Simulator!")
print("Would you like to (O)pen a new pack, (V)iew your collection, or (Q)uit?")

userInput=input()
userInput=userInput.lower()

while userInput !="q":
    #Pressing "O" opens a new pack of 15 cards and adds them to the user's collection
    if userInput=="o":
        openPack=newPackGen()
        print ("Here are the cards you pulled: " )
    
        for i, (k, v) in enumerate(openPack.items()):
             print (i,k,":",v)
        #This is the process for adding the opened cards to the dictionary
        currentCollection=copy.deepcopy(collectionAdd(currentCollection,openPack))
    #Pressing "V" views the cards the player has currently collected along with their card types    
    elif userInput=="v":
        print ("Here are the players you have collected, along with their variants:")
        for i, (k, v) in enumerate(currentCollection.items()):
            print (i,k,":",v)
    

    print("Would you like to (O)pen a new pack, (V)iew your collection, or (Q)uit?")
    userInput=input()
    userInput=userInput.lower()

##TODO: the deepcopy() function seems to add dictionaries as values. For example, if the user collects 3 base cards of the same player, the output will look like this: [[[BASE]]].
##There may be another way to add the cards to the user's collection each time a pack is opened.

