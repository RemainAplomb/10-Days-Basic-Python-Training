#  DAY 6 - ACTIVITY 1
# Program Description: This is a Record Keeping App that uses dictionary to store the user's inputted
# key and value. 

# The dictionary that will be used to store the records.
recordKeepingDict = {}

# This is the function for adding data into the dictionary. It takes in two arguments, the key and value.
# If the function successfully adds the data, it will return True.
# if not, it will return False.
def addData ( key, value ):
    try:
        tempList = list ( recordKeepingDict )
        if key in tempList:
            print ( " The key already exist in the dictionary. " )
            return False
        else:
            recordKeepingDict[ key ] = value
            return True
    except:
        return False

# This is the function for removing data from the dictionary. It takes in a single argument, the key.
# If the key is found, it will remove it along with its respective value from the dictionary.
# Then, it will return True.
# If the key is not in the dictionary, the function will return False along with printing an error.
def deleteData ( key) :
    try:
        tempList = list ( recordKeepingDict )
        if key in tempList:
            recordKeepingDict.pop( key )
            return True
        else:
            print ( " The key cannot be found in the dictionary. " )
            return False
    except:
        return False

# This is self explanatory. The function displays the keys and values present in the dictionary.
def displayDictionary ():
    print ( " The dictionary currently stores... " )
    for x in ( list ( recordKeepingDict ) ):
        print ( " Key : {} , Value = {} ".format( x, recordKeepingDict[x] ) )
    return

# If the program should continue running, it will be True. If not, then False.
continueRunning = True

while continueRunning:
    # will use try-except method just in case something is wrong with the inputs that the user had entered.
    try:
        # Printing the possible choices that the user could pick.
        print ( "\n-------------------- Choose --------------------" )
        print ( "\n   [A] Add Data " )
        print ( "   [B] Delete Data " )
        print ( "   [C] End " )
        print ( "\n------------------------------------------------\n" )

        # The program will take the user's choice.
        hasChosen = False
        while hasChosen == False:
            userChoice = str( input ( " Pick between the three( A/B/C ): " ) )
            if userChoice.lower() == "a" :
                hasChosen = True
                print ( "\n------------------------------------------------\n" )
                key = input ( " Enter Key to add: " ) 
                value = input ( " Enter Value to add: " )
                print ( "\n------------------------------------------------\n" )
                isAdded = addData ( key, value )
                if isAdded == True:
                    print ( " Key = {} and  Value = {} has been successfully stored.\n".format( key, value ) )
                else:
                    print ( " Error in adding data in the dictionary. " )
                print ( "\n------------------------------------------------\n" )
                displayDictionary()
            elif userChoice.lower() == "b" :
                hasChosen = True
                print ( "\n------------------------------------------------\n" )
                key = input ( " Enter Key to remove: " ) 
                print ( "\n------------------------------------------------\n" )
                isRemoved = deleteData ( key )
                if isRemoved == True:
                    print ( " Key = {} has been deleted.\n".format ( key ) )
                else:
                    print ( " Failed removing {}.\n".format ( key ) )
                print ( "\n------------------------------------------------\n" )
                displayDictionary()
            elif userChoice.lower() == "c" :
                hasChosen = True
                continueRunning = False
                print ( "\n------------------------------------------------\n" )
                print ( "                   THANK YOU " )
                print ( "\n------------------------------------------------\n" )
            else:
                print ( " INVALID INPUT " )
    except:
        print ( " Error Detected. " )
