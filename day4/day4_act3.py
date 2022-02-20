# DAY 4- ACTIVITY 3
# Program Description: This is a simple word bank program. It takes in the user's input and turns it into a string
# which will then be stored into the word bank list. After the user is done inputting his desired words, the program
# will print out the elements inside the word bank list.

# The list that will act as the word bank.
bankList = []

continueRunning = True
while continueRunning:
    # will use try-except method just in case something is wrong with the inputs that the user had entered.
    try:
        # the program will convert the user's input into a string.
        # Then, it will append the word into the bankList.
        print ( "\n-------------------- ENTER DETAILS --------------------" )
        word = str ( input ( " Enter a word ( string ) : " ) )
        print ( "-------------------------------------------------------\n" )
        bankList.append( word )
        print ( " {} has been stored in the word bank. \n".format( word ) )
        print ( "-------------------------------------------------------\n" )

        # Here, the program will ask the user if he would like to continue using the program.
        # If yes, the user will be able to continue adding more words into the bank list.
        # If not, the program will print out the elements inside the bankList.
        hasChosen = False
        while hasChosen == False:
            try:
                userChoice = str ( input ( " Would you like to try again? Y/y if Yes and N/n if No. " ) )
                if userChoice.lower() == "y" or userChoice.lower() == "yes" :
                    hasChosen = True
                elif userChoice.lower() == "n" or userChoice.lower() == "no" :
                    print ( "\n-------------------------------------------------------\n" )
                    print ( " The word bank contains: " )
                    for x in bankList:
                        print ( "      - {}.".format( x ) )
                    print ( "\n-------------------------------------------------------\n" )
                    continueRunning = False
                    hasChosen = True
                else:
                    print ( " Invalid Input. " )
            except:
                print ( " Invalid Input. " )
    except:
        print ( " Invalid Input. " )
        
