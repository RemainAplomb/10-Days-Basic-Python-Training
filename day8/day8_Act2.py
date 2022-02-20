# DAY 8 - ACTIVITY 2
# Program Description: This is a program that takes in two employee details and creates two objects using the Employee class.

# This is the class that creates the object for the employee's details
class Employee():
    def __init__ ( self, name, email, mobileNumber ):
        self.employeeName = name
        self.employeeEmail = email
        self.employeeMobileNumber = mobileNumber
    def displayProperties ( self ):
        print ( "    Employee Name: {} ".format( self.employeeName ) )
        print ( "    Employee Email: {} ".format( self.employeeEmail) )
        print ( "    Employee Mobile Number: {} ".format( self.employeeMobileNumber ) )


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

# If this turns to False, the program will terminate.
continueRunning = True
while continueRunning == True:
    try:
        # The list that will house the reference of the objects created.
        employeeObjectList = []

        # Asking for the user's input
        print ( "\n=================== Enter Employee Details ===================" )
        i = 1
        while i <= 2:
            try:
                print ( "\n ----- Employee Number {} ----- ".format( i ) )
                name = str( input ( "    Enter Employee's Name: " ) )
                email = str( input ( "    Enter Employee's Email: " ) )
                mobileNumber = str ( input ( "    Enter Employee's Mobile Number: " ) )
                if ( all( x.isalpha() or x.isspace() for x in name ) or name.isalpha() ) and mobileNumber.isdigit():
                    if i == 1 and ( len ( list (mobileNumber) ) == 11 ) and ( isEmailFormat( email ) ):
                        createEmployeeObject = Employee( name, email, mobileNumber )
                        employeeObjectList.append( createEmployeeObject )
                        i += 1
                    elif i == 2 and ( len ( list (mobileNumber) ) == 11 ) and ( isEmailFormat( email ) ):
                        temp = employeeObjectList[0]
                        if temp.employeeName == name:
                            print ( "\n    Invalid Input." )
                            print ( "    That exact same name string has already been used earlier. " )
                            print ( "    Please use other name string. " )
                        else:
                            createEmployeeObject = Employee( name, email, mobileNumber )
                            employeeObjectList.append( createEmployeeObject )
                            i += 1
                    else:
                        print ( "\n    Invalid Input. " )
                        print ( "    The mobile number must be 11 digits. " )
                        print ( "    The email must be in proper format. " )
                        print ( "    Example: thisisemail@whatever.whatever " )
                        
                else:
                    print ( "\n    Invalid Input. " )
                    print ( "    The program only accepts names that are alpha form. " )
                    print ( "    The program only accepts mobile numbers that are in digit form. " )
            except:
                print ( "\n    Invalid Input " )
        print ( "\n=========================================================\n" )


        # Printing the employee details contained in the 2 objects.
        hasChosen = False
        while hasChosen == False:
            # For printing/displaying the properties of the employee objects.
            print ( "\n================== Employee Details Display ==================\n" )
            for i in range ( len ( employeeObjectList ) ):
                print ( " ----- Employee Number {} ----- ".format( i + 1 ) )
                employeeObjectList[i].displayProperties()

            # Asking the user what he/she would like to do.
            print ( "\n=============== What Would you like to do? ==============\n" )
            print ( " [1] Try Again " )
            print ( " [2] Close Program " )
            print ( "\n=========================================================\n" )
            try:
                userChoice = int ( input ( " Enter your Choice: " ) )
                if userChoice == 1: # Going back to the beginning where the user will have to create 2 employee objects.
                    print ( "\n=========================================================\n" )
                    print ( "                  Going Back to the start. " )
                    print ( "\n=========================================================\n" )
                    hasChosen = True
                elif userChoice == 2: # Ending the program.
                    print ( "\n=========================================================\n" )
                    print ( "                         THANK YOU " )
                    print ( "\n=========================================================\n" )
                    hasChosen = True
                    continueRunning = False
                else:
                    print ( " Invalid Input " )
            except:
                print ( " Invalid Input. " )
    except:
        print ( " Error " )
