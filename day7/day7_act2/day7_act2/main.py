#  DAY 7 - ACTIVITY 2
# Program Description: This is a basic calculator program that takes in 2 numbers from the user and performs the specified math operation.


# This is a module that has the basic math operations. It contains add, subtract, multiply, and divide.
# Please note that this is a separate .py file,
# It can be found in the same folder as this main.py
import MathOperations


# As usual, this is will be responsible for terminating the program.
# Once the user chose not to continue, the continueRunning will be set to False
continueRunning = True
while continueRunning == True:
    try:
        # Printing the possible math operations for the user to choose from.
        print ( "\n==================== MATH OPERATIONS ====================\n" )
        print ( " [1] Add " )
        print ( " [2] Subtract " )
        print ( " [3] Multiply " )
        print ( " [4] Divide " )
        print ( "\n=========================================================\n" )

        # For taking in the user's choice as well as conducting the selected math operation.
        hasChosen = False
        while hasChosen == False:
            try:
                userChoice = int ( input ( " Enter your choice: " ) )
                if userChoice == 1:
                    # Taking two numbers from the user to conduct addition.
                    hasChosen = True
                    print ( "\n=========================================================\n" )
                    num1 = float ( input ( " Enter first number to add: " ) )
                    num2 = float ( input ( " Enter second number to add: " ) )
                    print ( "\n=========================================================\n" )
                    if num1 <= 0 or num2 <= 0:
                        print ( "Invalid input. The program doesn't accept numbers less than or equal to zero. \n" )
                    else:
                        result = MathOperations.add( num1, num2 ) # referencing the function add that can be found in the imported module.
                        #result = 0.0
                        if result == False and result != 0.0:
                            print ( " Error in adding. Please check your inputs. \n" )
                        else:
                            print ( " {} added with {} is equals to {} \n".format( num1, num2, result ) )
                elif userChoice == 2:
                    # Taking two numbers from the user to conduct subtraction.
                    hasChosen = True
                    print ( "\n=========================================================\n" )
                    num1 = float ( input ( " Enter first number to subtract: " ) )
                    num2 = float ( input ( " Enter second number to subtract: " ) )
                    print ( "\n=========================================================\n" )
                    if num1 <= 0 or num2 <= 0:
                        print ( "Invalid input. The program doesn't accept numbers less than or equal to zero. \n" )
                    else:
                        result = MathOperations.subtract( num1, num2 ) # referencing the function subtract that can be found in the imported module.
                        #print ( result )
                        if result == False and result != 0.0:
                            print ( " Error in subtracting. Please check your inputs. \n" )
                        else:
                            print ( " {} subtracted with {} is equals to {} \n".format( num1, num2, result ) )
                elif userChoice == 3:
                    # Taking two number inputs from the user to conduct multiplication.
                    hasChosen = True
                    print ( "\n=========================================================\n" )
                    num1 = float ( input ( " Enter first number to multiply: " ) )
                    num2 = float ( input ( " Enter second number to multiply: " ) )
                    print ( "\n=========================================================\n" )
                    if num1 <= 0 or num2 <= 0:
                        print ( "Invalid input. The program doesn't accept numbers less than or equal to zero. \n" )
                    else:
                        result = MathOperations.multiply( num1, num2 ) # referencing the function multiply that can be found in the imported module.
                        if result == False and result != 0.0:
                            print ( " Error in multiplication. Please check your inputs. \n" )
                        else:
                            print ( " {} multiplied by {} is equals to {} \n".format( num1, num2, result ) )
                elif userChoice == 4:
                    # Taking two numbers from the user to conduct division.
                    hasChosen = True
                    print ( "\n=========================================================\n" )
                    num1 = float ( input ( " Enter first number to divide: " ) )
                    num2 = float ( input ( " Enter second number to divide: " ) )
                    print ( "\n=========================================================\n" )
                    if num1 <= 0 or num2 <= 0:
                        print ( "Invalid input. The program doesn't accept numbers less than or equal to zero. \n" )
                    else:
                        result = MathOperations.divide( num1, num2 ) # referencing the function divide that can be found in the imported module.
                        if result == False and result != 0.0:
                            print ( " Error in division. Please check your inputs. \n" )
                        else:
                            print ( " {} divided by {} is equals to {} \n".format( num1, num2, result ) )
                else:
                    print ( " Invalid Input. \n" )
            except:
                print ( " Invalid Input. \n" )

        # This block of code will ask the user if he/she would like to continue using the program.
        # If not, the program will print a thank you message. Then, it will terminate.
        print ( "=========================================================\n" )
        hasChosen = False
        while hasChosen == False:
            try:
                userChoice = str ( input ( " Would you like to try again? Y/y if Yes and N/n if No. " ) )
                if userChoice.lower() == "y" or userChoice.lower() == "yes" :
                    hasChosen = True
                elif userChoice.lower() == "n" or userChoice.lower() == "no" :
                    print ( "\n=========================================================\n" )
                    print ( "                       THANK YOU!            \n" )
                    print ( "=========================================================\n" )
                    continueRunning = False
                    hasChosen = True
                else:
                    print ( " Invalid Input. " )
            except:
                print ( " Invalid Input. " )
    except:
        print ( " Invalid Input. \n" )
