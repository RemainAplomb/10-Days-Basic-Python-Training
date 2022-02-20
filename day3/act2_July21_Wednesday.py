# Activity 2

# Program Description: This is a program that takes in the user's input to determine how much bonus the employee will receive.
# There are three departments, and in each one there are two category of bonus.
# Those who had been in the company for less than a decade will receive a lower bonus.
# On the otherhand, if the employee has been in the company for a decade or more, he/she will receive more.

officeBonuses = { "it" : [ 10000, 5000 ] ,
                  "acct" : [ 12000, 6000 ] ,
                  "hr" : [ 15000, 7500 ] }

# The program will run continously.
while True:
    # I used the try method so that if the user has inputted wrongly, the program will not terminate immediately.
    # Instead, it will alert the user that there's an error detected.
    try:
        # In this block of code, the program will take in the user's input. It only accepts float and strings.
        print ( "==================== ENTER DETAILS ====================" )
        name = str ( input ( " Enter employee name: " ) )
        yearsInService = float (input ( " Enter years-in-service( integer or float ): " ))
        office = str ( input ( " Enter office ( IT/ACCT/HR ): " ) )
        print ( "=======================================================\n" )

        # This block of code will determine if the years of service is less than a decade.
        isLessThanDecade = 0 # 1 for True, 0 for False
        if yearsInService >= 10:
            isLessThanDecade = 0
        elif yearsInService < 10:
            isLessThanDecade = 1

        # Printing using the format method.
        print ( " Hi {}, your bonus is {}. \n".format( name, officeBonuses[ office.lower() ][ isLessThanDecade ] ) )
        print ( "=======================================================\n" )
    except:
        print ( "=======================================================\n" )
        print ( " Error Detected. \n" )
        print ( "=======================================================\n" )
