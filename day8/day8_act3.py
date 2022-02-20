# DAY 8 - ACTIVITY 3
# Program Description: This is a program that utilizes a class named Student.

# This is the class that creates the student objects.
class Student():
    def __init__( self, name, mathGrade, scienceGrade, englishGrade ): 
        self.name = name
        self.mathGrade = mathGrade
        self.scienceGrade = scienceGrade
        self.englishGrade = englishGrade

    def computeAverage( self ): # For computing average
        self.averageGrade = ( self.mathGrade + self.scienceGrade + self.englishGrade ) / 3
        return self.averageGrade

    def studentStatus( self ): # For determining the student's status, the passing grade is >= 75
        if self.averageGrade >= float( 75 ):
            return "Passed"
        else:
            return "Failed"

    def displayStudentInfo( self ): # For displaying the student's info.
        print ( " Name: " , self.name )
        print ( " Math Grade: " , self.mathGrade ) 
        print ( " Science Grade: " , self.scienceGrade ) 
        print ( " English Grade: " , self.englishGrade ) 
        self.averageGrade = self.computeAverage()
        self.studentStatus = self.studentStatus()
        print ( "\n Average: {} ( {} )".format( self.averageGrade, self.studentStatus ) )
        print ( "\n=========================================================\n" )


# Once the user choose to close the program, the continueRunning will turn to False and the program will terminate.
continueRunning = True
while continueRunning == True:
    try:
        # This is the list that stores the student objects.
        studentObjectList = []
        
        # For taking in the user's input and creating the three student objects.
        print ( "\n================= Enter Student Details =================\n" )
        i = 1
        while i <= 3:
            try:
                print ( " ----- Student Number {} ----- ".format( i ) )
                studentName = str( input ( "    Enter Student Name: " ) )
                mathGrade = float ( input ( "    Enter Math Grade: " ) )
                scienceGrade = float ( input ( "    Enter Science Grade: " ) )
                englishGrade = float ( input ( "    Enter English Grade: " ) )
                tempObjectHolder = Student( studentName, mathGrade, scienceGrade, englishGrade )
                studentObjectList.append ( tempObjectHolder )
                i += 1
            except:
                print ( " Invalid Input " )
        print ( "\n=========================================================\n" )

        # This will display the content of the created student objects.
        # It will also ask the user if he/she would like to try again.
        hasChosen = False
        while hasChosen == False:
            # For printing/displaying the properties of the car objects.
            print ( "\n==================== Student Display ====================\n" )
            for i in range ( len ( studentObjectList ) ):
                print ( " ----- Student Number {} ----- ".format( i + 1 ) )
                studentObjectList[i].displayStudentInfo()

            # Asking the user what he/she would like to do.
            print ( "\n=============== What Would you like to do? ==============\n" )
            print ( " [1] Try Again. " )
            print ( " [2] Close Program " )
            print ( "\n=========================================================\n" )
            try:
                userChoice = int ( input ( " Enter your Choice : " ) )
                if userChoice == 1: # Going back to the beginning where the user will have to create 3 student objects.
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
                print ( " Invalid Input " )
    except:
        print ( " Error. " )
