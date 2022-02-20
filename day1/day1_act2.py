# Day1 - Activity2
# Program Description: This is a basic program that calculates for the user's average based on the inputs.
# The program operates using float and the average is rounded to the 2nd decimal place.

while True:
    print ( "-------------------- Enter Details -------------------- " )
    name = input ( " Name: " )
    mathGrade = float ( input ( " Math Grade: " ) )
    scienceGrade = float ( input ( " Science Grade: " ) )
    englishGrade = float ( input ( " English Grade: " ) )

    averageGrade =  ( mathGrade + scienceGrade + englishGrade ) / 3

    print ( "\n Average: {}".format( round( averageGrade, 2 ) ) )
    print ( " ------------------------------------------------------ \n" )
