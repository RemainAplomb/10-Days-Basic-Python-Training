# Activity 1

# Program Description: This is a program that takes in the user's grade to determine whether the student passed or failed the semester.
# Furthermore, it also tells the user which subjects he would need to retake.

# These are the pre-determined possible outputs.
possibleOutputs = [ "Congratulations! You passed the semester. " ,
                    "You will not need to re-enroll any subject. " ,
                    "But you need to re-enroll {} subject. ",
                    "Sorry, You failed the semester. " ]

# The program will run continously.
while True:
    # In this block of code, the program will take in the user's input. It only accepts float and strings.
    print ( "==================== ENTER DETAILS ====================" )
    name = str ( input ( "Name: " ) )
    mathGrade = float ( input ( "Math: " ) )
    scienceGrade = float ( input ( "Science: " ) )
    englishGrade = float ( input ( "English: " ) )
    print ( "=======================================================\n" )

    # The Average grade is calculated and printed.
    averageGrade = ( mathGrade + scienceGrade + englishGrade ) / 3
    print ( "Average: " + str( round (averageGrade, 2 )) + "\n" )

    # In this block of code, the program will use the for loop to check if there are any grades that is less than 75.
    # If there are, it will be included in the failed subjects that will be printed later.
    grades = { "Math" : mathGrade, "Science" : scienceGrade, "English" : englishGrade }
    failedSubjects = ""
    for x in list(grades):
        if grades[x] < 75:
            if failedSubjects == "":
                failedSubjects = x
            else:
                failedSubjects = failedSubjects + " and " + x

    # These are the possible outputs that the program can print.
    # If all of the grades is above 75, it will print passed as well as tell the user that there is no need to re-enroll any subject.
    # If the average grade is less than 75, it will tell the user that he had failed the semester.
    # However, if the average grade is above 75 but the user has a failing grade, the program will alert the user to re-enroll the failed subject.
    if averageGrade >= 75 and failedSubjects == "":
        print ( possibleOutputs[0] + possibleOutputs[1] )
    elif averageGrade < 75:
        print ( possibleOutputs[3] )
    elif averageGrade >= 75 and failedSubjects != "" :
        print ( (possibleOutputs[0] + possibleOutputs[2] ).format( failedSubjects ) )
    print ( "=======================================================\n" )
    
