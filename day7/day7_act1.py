# DAY 7 - ACTIVITY 1
# Program Description: This is a program that generates a new name for the user. It uses a random generated number to pick
# among the list of possible names.

# To generate a random number, we will use the random module that is provided by python itself.
import random

# These lists contains the possible names that the user can get. This is a selection pool.
firstNameList = [ "Emelia" , "Violet" , "Betty" , "Kara" , "Nia" ,
                  "Robert" , "Carlton" , "Fabian" , "Wesley" , "Josiah" ]
middleNameList = [ "Consuelo" , "Rosario" , "Sancho" , "Savo" , "Sahyko" ,
                   "Socorro" , "Delight" , "Delphine" , "Marhsall" , "Mateus" ,
                   "Merton" ]
lastNameList = [ "Lewis" , "Leontes" , "Latos" , "Lysimachus" , "Lucius" ,
                 "Mercia" , "Morgan" , "Moore" , "Murphy" , "Agrawal" ,
                 "Adams" , "Alvarez" ]


# This is the function for generating a new name. It first generates a list of three random numbers that are within the
# specified parameters. For the first name, the number generated will be 0-9, for middle name 0-10 , and for last name 0-11.
def generateName():
    randomNumList = [ (random.randint(0, 9)) , (random.randint(0, 10)) ,
                      (random.randint(0, 11)) ]
    #print ( randomNumList )
    firstName = firstNameList[ randomNumList[0] ]
    middleName = middleNameList[ randomNumList[1] ]
    lastName = lastNameList [ randomNumList[2] ]
    return [ firstName , middleName , lastName ]
    

# As usual, to determine if the program should continue running.
# If the program should stop running, the variable will turn to False.
continueRunning = True
while continueRunning == True:
    try:
        # The program will only ask if the user wants to generate a new name.
        # Yes, yEs, ... , yeS, , Y , and y are all acceptable as yes.
        # No, no , nO , N , and n are all acceptable as no.
        print ( "==================== GENERATE NEW NAME ====================\n" )
        hasChosen = False
        while hasChosen == False:
            try:
                userChoice = str ( input ( " Would you like to generate a new name? Y/y if Yes and N/n if No. " ) )
                if userChoice.lower() == "y" or userChoice.lower() == "yes" :
                    hasChosen = True
                    newName = generateName ()
                    print ( "\n===========================================================\n" )
                    print ( " Congratulations! Your new name is {} {} {}. \n".format( newName[0] , newName[1] , newName[2] ) )
                    print ( "===========================================================\n" )
                elif userChoice.lower() == "n" or userChoice.lower() == "no" :
                    print ( "\n===========================================================\n" )
                    print ( "                       THANK YOU!            \n" )
                    print ( "===========================================================\n" )
                    continueRunning = False
                    hasChosen = True
                else:
                    print ( " Invalid Input. " )
            except:
                print ( " Invalid Input. " )
    except:
        print ( "Invalid Input. " )
