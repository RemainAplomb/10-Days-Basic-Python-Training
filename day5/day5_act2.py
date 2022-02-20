# DAY 5 - ACTIVITY 2
# Program Description: This is a program that reverses the user's inputted string using a function.

# This is the function that takes in the inputted word/string.
# It first counts how many characters there are in the string.
# Based on the given sample output in the activity, it was known that spaces should be added in the character count.
# Then, the function uses a for loop to reverse arrangement of the string.
def reverseString ( word ):
    elementCount = len ( list (word ) )
    finalString = ""
    for x in word:
        finalString = x + finalString
    return [ finalString.upper(), elementCount ]

# Using a while loop so that the program can run indefinitely.
# It will take the user's input then sends it to the function name reverseString.
# It also prints out the input as well as the output.
while True:
    print ( "\n-------------------- ENTER DETAILS --------------------" )
    inputtedString = str ( input ( " Enter a string: " ) )
    result = reverseString ( inputtedString )
    print ( "-------------------------------------------------------\n" )
    print ( "\n Input: {} ".format ( inputtedString ) )
    print ( "\n Output: {} ( {} characters ) ".format ( result[0], result[1] ) )
    print ( "\n-------------------------------------------------------\n" )
