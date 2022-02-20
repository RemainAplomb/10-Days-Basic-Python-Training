# DAT 9 - ACTIVITY 1
# Program Description: This is a python program that uses txt files to record the user's inputs.
# It can create a record, view records, and clear records.

# Importing the os
# This will help the program manage directories.
# It will be helpful in locaating where the records.txt will be placed.
# The location will be currentDirectory/records/records.txt
import os

# getting current directory where the program is currently located.
try:
    currentDirectory = os.getcwd()
    ###print(currentDirectory)
except:
    print ( " Error : Cannot find the Current Directory. " )



# This is a function that checks if the email that the user has inputted is following the proper format.
# The program only accepts in this format: whatever@whatever.whatever
def isEmailFormat ( email ):
    try:
        if "@" in email:
            test1 = email.split( "@" )
            if "." in test1[1]:
                test2 = test1[1].split( "." )
                return True
            else:
                return False
        else:
            return False
    except:
        return False


# Once the user chooses [d], the while loop will stop and the program will terminate
continueRunning = True
while continueRunning == True:
    try:
        # Printing possible choices.
        print ( "\n=============== What would you like to do? ==============\n" )
        print ( " [a] Add Record " )
        print ( " [b] View Records " )
        print ( " [c] Clear All Records " )
        print ( " [d] Exit " )
        print ( "\n=========================================================\n" )

        hasChosen = False
        while hasChosen == False:
            try:
                # Asking for user's choice of action
                userChoice = str ( input ( " Your Choice: " ) )
                if userChoice.lower() == "a": # For adding Records. This is selection [a]
                    if not os.path.exists( currentDirectory + "\\records\\"  ): # For creating the records folder which will house the records.txt
                        os.makedirs( currentDirectory + "\\records\\")
                    try:
                        print ( "\n======================= ADD RECORD ======================\n" )
                        name = str ( input ( " Enter name: " ) )
                        email = str ( input ( " Enter email: " ) )
                        address = str ( input ( " Enter address " ) )
                        print ( "\n=========================================================\n" )
                        
                        # The user's input will only be recorded if the following are met:
                        # [1] The name must be in alpha form. Only letters will be accepted.
                        # [2] The email must be in proper format ( e.g. : whatever@whatever.whatever )
                        if ( all( x.isalpha() or x.isspace() for x in name ) or name.isalpha() ) and isEmailFormat( email ): 
                            recordsTXT = open( currentDirectory + "\\records\\records.txt" , "a+" )
                            recordsTXT.write( "Name: " + name + "\n" )
                            recordsTXT.write( "Email: " + email + "\n" )
                            recordsTXT.write( "Address: " + address + "\n\n" )
                            recordsTXT.close()
                            hasChosen = True
                        else:
                            print ( " Invalid Input. " )
                            print ( " Please Note: " )
                            print ( "    The name must be in alpha form. " )
                            print ( "       Don't put ( ./@/x/8/ etc. ) " )
                            print ( "    The email must be in proper format. " )
                            print ( "       Example: thisisemail@whatever.whatever " )
                        print ( "\n=========================================================\n" )
                        hasChosen = True
                    except:
                        print ( "\n Invalid Input " )
                elif userChoice.lower() == "b": # For displaying records. This is selection [b]
                    if not os.path.exists( currentDirectory + "\\records\\"  ): # For creating the records folder which will house the records.txt
                        os.makedirs( currentDirectory + "\\records\\")
                    try:
                        # The program will try to fetch the txt file that contains the records.
                        # If it fails to do so, the program will print out that the records is empty.
                        # Furthermore, if the fetched txt file doesn't have any records, the program will also print records is empty.
                        recordsList = [ line.strip() for line in open ( currentDirectory + "\\records\\records.txt" ) ]
                        print ( recordsList )
                        print ( "\n===================== DISPLAY RECORD ====================\n" )
                        if ( len( recordsList ) == 0 ):
                            print ( " The records is empty. " )
                        else: # If there are records found, the program will display it.
                            recordNum = 0
                            for i in range ( len ( recordsList ) ):
                                try:
                                    temp = recordsList[i].split()
                                    if temp[0] == "Name:":
                                        recordNum += 1
                                        print ( " ----- Record number {} ----- ".format ( recordNum ) )
                                        print ( "    " + recordsList[i] )
                                    else:
                                        print ( "    " + recordsList[i] )
                                except:
                                    pass
                        print ( "\n=========================================================\n" )
                        hasChosen = True
                    except:
                        print ( "\n===================== DISPLAY RECORD ====================\n" )
                        print ( " The records is empty. " )
                        print ( "\n=========================================================\n" )
                elif userChoice.lower() == "c": # For clearing records. This is selection [c]
                    if not os.path.exists( currentDirectory + "\\records\\"  ): # For creating the records folder which will house the records.txt
                        os.makedirs( currentDirectory + "\\records\\")
                    try:
                        # Here, rewrite the records.txt into a blank text file
                        open( currentDirectory + "\\records\\records.txt" , 'w').close()
                        print ( "\n=========================================================\n" )
                        print ( "               The Records has been cleared. " )
                        print ( "                        No Records found. " )
                        print ( "\n=========================================================\n" )
                        hasChosen = True
                    except:
                        print ( " Error " )
                elif userChoice.lower() == "d": # For ending/terminating the program. This is selection [d]
                    if not os.path.exists( currentDirectory + "\\records\\"  ): # For creating the records folder which will house the records.txt
                        os.makedirs( currentDirectory + "\\records\\")
                    print ( "\n=========================================================\n" )
                    print ( "                         THANK YOU " )
                    print ( "\n=========================================================\n" )
                    hasChosen = True
                    continueRunning = False
                else: # If the user's input is not within the given choices, the program will print and invalid input error.
                    print ( " Invalid Input " )
            except:
                print ( " Invalid Input. " )
    except:
        print( " Error. " )
