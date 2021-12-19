pool = 30

attributes = {"Strength":0, "Health":0, "Wisdom":0, "Dexterity":0 }

choice = None
while choice !="0":

    print(
    """
    Character Creator
    ------

    Your current Attribute Scores:

    Strength:"""
    + str(attributes["Strength"]) +
    """
    Health:"""
    + str(attributes["Health"]) +
    """
    Wisdom:"""
    + str(attributes["Wisdom"]) +
    """
    Dexterity:"""
    + str(attributes["Dexterity"]) +
    """
    
    Your remaining points:"""
    + str(pool) +
    """
    ------
    Options:
    0-Quit
    1-Add Attribute Points
    2-Remove Attribute Points
    """
    )

    choice = input("What is your choice?:")

    #exit
    if choice=="0":
     print("Goodbye.")

    elif choice == "1":
       selectAdd = input ("Which attribute would you like to increase?:")
       selectAddNum= int(input ("By how much?:"))
       if selectAddNum > pool:
           print ("Whoops! You only have " + str(pool) + " points left!")
       else:
           if selectAdd in attributes:
               attributes[selectAdd] += selectAddNum
               pool -= selectAddNum
           else:
                print("That's not an attribute! Attribute names are case-sensitive!")

    elif choice =="2":
        selectRemove = input ("Which attribute would you like to decrease?:")
        selectRemoveNum = int(input("By how much?:"))
        if selectRemoveNum > attributes[selectRemove]:
            print("Whoops you only have " + str(attributes[selectRemove]) + " points in " + selectRemove)
        else:
            if selectRemove in attributes:
                attributes[selectRemove] -= selectRemoveNum
                pool += selectRemoveNum
            else:
                print("That's not an attribute! Attribute names are case-sensitive!")
    else:
        print("\nSorry, but " + choice + "was not a valid choice")
        
input("\nPress the enter key to exit.")
