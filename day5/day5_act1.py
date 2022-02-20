# DAY 5 - ACTIVITY 1
# Program Description: This is a program that uses a function ( studentAverage ) to process the student's grade.

# This is the function that will take in the user's inputted information.
# Then it will calculate the student's average.
# lastly, it will add the information into the studentGrades dictionary.
def studentAverage ( name, mathGrade, englishGrade, scienceGrade ):
    averageGrade = ( mathGrade + englishGrade + scienceGrade ) / 3
    studentGrades[ name ] = [ averageGrade, mathGrade, englishGrade, scienceGrade ]
    return
    
continueRunning = True
while continueRunning:
    studentGrades = {}
    # will use try-except method just in case something is wrong with the inputs that the user had entered.
    try:
        # For taking in the user's input as well as referencing the function.
        # The program will ask the user for the grades of 3 students.
        print ( "\n-------------------- ENTER DETAILS --------------------" )
        for i in range ( 3 ):
            name = str ( input ( " Enter student name: " ) )
            mathGrade = float ( input ( " Enter math grade: " ) )
            englishGrade = float ( input ( " Enter english grade: " ) )
            scienceGrade = float ( input ( " Enter science grade: " ) )
            studentAverage ( name, mathGrade, englishGrade, scienceGrade )
            print ( "-------------------------------------------------------\n" )
            print ( " Student number {}'s ( {} ) grade has been added. \n".format ( i + 1, name.capitalize() ) )
            print ( "-------------------------------------------------------\n" )

        # for printing out the result.
        print ( " Output: \n" )
        for x in ( list( studentGrades ) ):
            print ( " {}'s grade ( Math = {}, Science = {}, Engllish = {} ) and the average is {}. ".format ( x.capitalize(), studentGrades[x][1], studentGrades[x][3], studentGrades[x][2], studentGrades[x][0]))
        print ( "\n-------------------------------------------------------\n" )
    except:
        print ( " Invalid input. " )
