# DAY 4- ACTIVITY 2
# Program Description: This is a program which takes in the user's input and gets the sum of the 2 numbers.
# Everytime a proper calculation is done, the program asks the user if he would like to try again.
# if the user answers y or yes, the program will continue running.
# however, if the user says n or no, the program will terminate.

# This condition will determine the state of the program. whether to continue running ( True ) or terminate ( False ).
continueRunning = True
while continueRunning:
    # will use try-except method just in case the user inputs a string as a number. 
    try:
        # the program will turn the number into a float so that it can get the sum of whole numbers as well as those
        # that have a decimal. It will also use the format method to properly print the result.
        print ( "\n-------------------- ENTER DETAILS --------------------" )
        firstNum = float ( input ( " Enter first number ( integer/float ) : " ) )
        secondNum = float ( input ( " Enter second number ( integer/float ) : " ) )
        print ( "-------------------------------------------------------\n" )
        print ( " The sum of {} and {} is {}. \n".format ( firstNum, secondNum, ( firstNum + secondNum ) ) )
        print ( "-------------------------------------------------------\n" )

        # Here, the program will ask the user if he would like to continue using the program. 
        hasChosen = False
        while hasChosen == False:
            try:
                userChoice = str ( input ( " Would you like to try again? Y/y if Yes and N/n if No. " ) )
                if userChoice.lower() == "y" or userChoice.lower() == "yes" :
                    hasChosen = True
                elif userChoice.lower() == "n" or userChoice.lower() == "no" :
                    print ( " Thank you! " )
                    continueRunning = False
                    hasChosen = True
                else:
                    print ( " Invalid Input. " )
            except:
                print ( " Invalid Input. " )
    except:
        print ( " Invalid Input. " )
        
