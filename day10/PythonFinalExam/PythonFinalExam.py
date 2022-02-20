# RESTAURANT DINING RESERVATION SYSTEM
# Program Description: This program utilizes the class RestaurantReservation to execute the user's desired choices.
# This program stores the restaurant reservation into the txt file named reservations.txt
# The txt file can be located at currentDirectory/reservartions/reservations.txt

# Importing os so that the program will be able to create the folder which will house the reservations.txt
import os

# getting current directory where the program is currently located.
try:
    currentDirectory = os.getcwd()
    ###print(currentDirectory)
except:
    print ( " Error : Cannot find the Current Directory. " )


# This will facilitate the user's choices.
class RestaurantReservation():
    def __init__( self ):
        # If there are no reservations folder, the program will create one.
        try:
            self.reservationsList = [ line.strip() for line in open ( currentDirectory + "\\reservations\\reservations.txt" ) ]
        except:
            if not os.path.exists( currentDirectory + "\\reservations\\"  ): # For creating the records folder which will house the records.txt
                os.makedirs( currentDirectory + "\\reservations\\" )

    def viewReservations( self ): # This is for displaying the current reservations stored in the txt file.
        try:
            if not os.path.exists( currentDirectory + "\\reservations\\"  ): # For creating the records folder which will house the records.txt
                os.makedirs( currentDirectory + "\\reservations\\" )
            print ( "\n======================== VIEW RESERVATIONS =========================\n" )
            self.reservationsList = [ line.strip() for line in open ( currentDirectory + "\\reservations\\reservations.txt" ) ]
            self.fields = [ "#", "Date", "Time", "Name", "Adults", "Children" ]
            self.splitToSix = lambda lst, sz: [ lst[i:i+sz] for i in range( 0, len(lst), sz)]
            self.data = self.splitToSix( self.reservationsList , 5)
            if len( self.reservationsList ) == 0:
                print ( " There are no reservations. " )
                print ( "\n====================================================================\n" )
                return
            else:
                self.format_row = "{:<17}" * (len( self.fields ))
                print( self.format_row.format( *self.fields ))
                for i in range( len( self.data ) ):
                    print( self.format_row.format( i + 1, *self.data[i] ) )  
                print ( "\n====================================================================\n" )
                return
        except:
            print ( " There are no reservations. " )
            print ( "\n====================================================================\n" )
            return

    def deleteReservations( self ): # This is for deleting a reservation. The user will only have to choose the reservation number.
        try:
            if not os.path.exists( currentDirectory + "\\reservations\\"  ): # For creating the records folder which will house the records.txt
                os.makedirs( currentDirectory + "\\reservations\\" )
            print ( "\n======================= DELETE RESERVATIONS ========================\n" )
            self.fields = [ "#", "Date", "Time", "Name", "Adults", "Children" ]
            self.splitToSix = lambda lst, sz: [ lst[i:i+sz] for i in range( 0, len(lst), sz)]
            try:
                self.reservationsList = [ line.strip() for line in open ( currentDirectory + "\\reservations\\reservations.txt" ) ]
                self.data = self.splitToSix( self.reservationsList , 5)
            except:
                self.reservationsList = []
            if len( self.reservationsList ) == 0:
                print ( " There are no reservations. " )
                print ( "\n====================================================================\n" )
                return
            else:
                self.format_row = "{:<17}" * (len( self.fields ))
                print( self.format_row.format( *self.fields ))
                for i in range( len( self.data ) ):
                    print( self.format_row.format( i + 1, *self.data[i] ) )  
                print ( "\n====================================================================\n" )
                self.toDelete = int( input( " Enter reservation number: " ) )

                if ( self.toDelete - 1 ) < ( len( self.data ) ) and self.toDelete > 0:
                    open( currentDirectory + "\\reservations\\reservations.txt" , 'w').close()
                    for i in range( len( self.data ) ):
                        if i == ( self.toDelete - 1 ):
                            pass
                        else:
                            reservationsTXT = open( currentDirectory + "\\reservations\\reservations.txt" , "a+" )
                            reservationsTXT.write( self.data[i][0] + "\n" )
                            reservationsTXT.write( self.data[i][1] + "\n" )
                            reservationsTXT.write( self.data[i][2] + "\n" )
                            reservationsTXT.write( str(self.data[i][3]) + "\n" )
                            reservationsTXT.write( str(self.data[i][4]) + "\n" )
                            reservationsTXT.close()
                    print ( "\n====================================================================\n" )
                    print ( " The reservation has been deleted. " )
                    print ( "\n====================================================================\n" )
                else:
                    print ( " Invalid Input " )
                    print ( "\n====================================================================\n" )
        except:
            print ( " Invalid Input " )
            print ( "\n====================================================================\n" )
            return
        
    def generateReport( self ): # This is for displaying a report. This function will calculate the total adults, children, subtotal, and grand total.
        try:
            if not os.path.exists( currentDirectory + "\\reservations\\"  ): # For creating the records folder which will house the records.txt
                os.makedirs( currentDirectory + "\\reservations\\" )
            print ( "\n============================= REPORTS ==============================\n" )
            self.reservationsList = [ line.strip() for line in open ( currentDirectory + "\\reservations\\reservations.txt" ) ]
            self.fields = [ "#", "Date", "Time", "Name", "Adults", "Children", "Subtotal" ]
            self.splitToSix = lambda lst, sz: [ lst[i:i+sz] for i in range( 0, len(lst), sz)]
            self.data = self.splitToSix( self.reservationsList , 5)
            self.grandTotal = 0
            self.totalAdults = 0
            self.totalKids = 0
            if len( self.reservationsList ) == 0:
                print ( " There are no reservations. " )
                print ( "\n====================================================================\n" )
                return
            else:
                self.format_row = "{:<17}" * (len( self.fields ))
                print( self.format_row.format( *self.fields ))
                for i in range( len( self.data ) ):
                    self.subTotal = ( 500 * float( self.data[i][3] ) ) + ( 300 * float( self.data[i][4] ) )
                    self.grandTotal = self.grandTotal + self.subTotal
                    self.totalAdults = self.totalAdults + int( self.data[i][3] )
                    self.totalKids = self.totalKids + int( self.data[i][4] )
                    print( self.format_row.format( i + 1, *self.data[i] , self.subTotal ) )
                print ( "\n Total number of Adults: ", self.totalAdults )
                print ( " Total number of Kids: " , self.totalKids )
                print ( " Grand Total: PHP" , self.grandTotal )
                print ( "\n...........................nothing follows.........................." )
        except:
            print ( " There are no reservations. " )
            print ( "\n====================================================================\n" )
            return

        
    def makeReservations ( self ): # This is for creating a reservation.
        try:
            if not os.path.exists( currentDirectory + "\\reservations\\"  ): # For creating the records folder which will house the records.txt
                os.makedirs( currentDirectory + "\\reservations\\" )
            print ( "\n========================= MAKE RESERVATION =========================\n" )
            self.name = str( input ( " Enter name: " ) )
            self.date = str( input ( " Enter date: " ) )
            self.time = str( input ( " Enter time: " ) )
            self.nAdults = int( input ( " Enter number of Adults: " ) )
            self.nChildren = int( input ( " Enter number of Children: " ) )
            print ( "\n====================================================================\n" )
            if self.name == "" or self.date == "" or self.time == "":
                print ( " Empty inputted string detected. " )
            elif ( all( x.isalpha() or x.isspace() for x in self.name ) or self.name.isalpha() ):
                self.testDate = self.isDateFormat( self.date )
                self.testTime = self.isTimeFormat( self.time )
                if self.testDate == True and self.testTime == True :
                    reservationsTXT = open( currentDirectory + "\\reservations\\reservations.txt" , "a+" )
                    reservationsTXT.write( self.date + "\n" )
                    reservationsTXT.write( self.time + "\n" )
                    reservationsTXT.write( self.name + "\n" )
                    reservationsTXT.write( str(self.nAdults) + "\n" )
                    reservationsTXT.write( str(self.nChildren) + "\n" )
                    reservationsTXT.close()
                    print ( "               {} has successfully made a reservation. ".format( self.name ) )
                    print ( "\n====================================================================\n" )
                else:
                    pass
            else:
                print ( " Invalid Input in name. " )
                print ( " Name must be in alpha form. " )
            return
        except:
            print ( " Invalid Input. " )
            return


    def isDateFormat( self, checkDate ): # This is for checking if the user's inputted date follows the format. Example: November 8, 2000
        # The months_day contains the months and day inputs that are recognized by the program
        self.months_day = { "January" : 31, "February" : 28, "March" : 31, "April" : 30,
                            "May" : 31, "June" : 30, "July" : 31, "August" : 31, "September" : 30,
                            "October" : 31, "November" : 30, "December" : 31 ,
                            "Jan" : 31, "Feb" : 28, "Mar" : 31, "Apr" : 30,
                            "May" : 31, "Jun" : 30, "Jul" : 31, "Aug" : 31, "Sep" : 30,
                            "Oct" : 31, "Nov" : 30, "Dec" : 31} 
        self.checkDate = checkDate
        try:
            # The program will use .split to get determine which are the inputtedDay, inputtedMonth, and inputtedYear
            self.splitDate = self.checkDate.split( ", " )
            self.splitDate2 = self.splitDate[0].split( " " )
            self.inputtedMonth = self.splitDate2[0]
            self.inputtedDay = int(self.splitDate2[1])
            self.inputtedYear = int(self.splitDate[1])
            if ( self.inputtedMonth.capitalize() in self.months_day ): # Check if the user's inputted month is recognized by the program.
                if ( self.inputtedDay <= self.months_day[self.inputtedMonth.capitalize()] ) and self.inputtedDay > 0: # check if the inputted month is within parameters
                    if ( len( str( self.inputtedYear)) == 4 ): # Check if the year is composed of 4 digits. Example: 2000, 2010, 1990, 2100, ... , etc.
                         return True
                    else:
                        print ( " Invalid Input in Date. The year must be a 4 digit string. " )
                        print ( " Please input date like this: " )
                        print ( " Nov 10, 2020 or November 10, 2020 " )
                        print ( " The format is: {Month}(space){day}(comma)(space){year} " )
                        return False
                else:
                    print ( " Invalid Input in Date. Inputted day isn't within the days of the inputted month. " )
                    print ( " Please input date like this: " )
                    print ( " Nov 10, 2020 or November 10, 2020 " )
                    print ( " The format is: {Month}(space){day}(comma)(space){year} " )
                    return False
            else:
                print ( " Invalid Input in Date. Inputted month cannot be recognized. " )
                print ( " Please input date like this: " )
                print ( " Nov 10, 2020 or November 10, 2020 " )
                print ( " The format is: {Month}(space){day}(comma)(space){year} " )
                return False
        except:
            print ( " Invalid Input in Date. " )
            print ( " Please input date like this: " )
            print ( " Nov 10, 2020 or November 10, 2020 " )
            print ( " The format is: {Month}(space){day}(comma)(space){year} " )
            return False

    def isTimeFormat( self, checkTime ): # This will check if the inputted time follows the time format.
        self.checkTime = str(checkTime)
        try:
            # Using split to determine which input is Hour, Min, and Type.
            self.splitTime = self.checkTime.split( " " )
            self.splitTime2 = self.splitTime[0].split( ":" )
            self.inputtedHour = int( self.splitTime2[0] )
            self.inputtedMin = int( self.splitTime2[1] )
            self.inputtedType = self.splitTime[1]

            if self.inputtedType.lower() == "am" or self.inputtedType.lower() == "pm" : # The time type must be either "am" or "pm"
                if self.inputtedHour <= 12 and self.inputtedHour >= 1: # The inputted hour must be within 1-12
                    if self.inputtedMin <= 59 and self.inputtedMin >= 0: # The inputted minutes must be within 0-59
                        return True
                    else:
                        print ( "\n Invalid Input in Time. " )
                        print ( " The inputted minutes must be 0-59 " )
                        print ( " Time format: {Hour}(colon){minutes}(space){am or pm}" )
                        print ( " Example: 10:10 am or 12:00 pm " )
                        return False
                else:
                    print ( "\n Invalid Input in Time. " )
                    print ( " The inputted hour must be 1-12 " )
                    print ( " Time format: {Hour}(colon){minutes}(space){am or pm}" )
                    print ( " Example: 10:10 am or 12:00 pm " )
                    return False
            else:
                print ( "\n Invalid Input in Time" )
                print ( " Time should either be 'am' or 'pm'. " )
                print ( " Time format: {Hour}(colon){minutes}(space){am or pm}" )
                print ( " Example: 10:10 am or 12:00 pm " )
                return False
                
        except:
            print ( "\n Invalid Input in Time " )
            print ( " Time format: {Hour}(colon){minutes}(space){am or pm}" )
            print ( " Example: 10:10 am or 12:00 pm " )
            return False


# Creating the restaurant reservation object.
rr = RestaurantReservation()

continueRunning = True
while continueRunning == True:
    try:
        # Printing the possible choices.
        print ( "\n=========================== SYSTEM MENU ============================\n" )
        print ( " [a] View All Reservations " )
        print ( " [b] Make Reservation " )
        print ( " [c] Delete Reservation " )
        print ( " [d] Generate Report " )
        print ( " [e] Exit " )
        print ( "\n====================================================================\n" )

        hasChosen = False
        while hasChosen == False:
            try:
                userChoice = str ( input ( " Enter your choice: " ) )
                if userChoice.lower() == "a": # If a, go to viewReservations function
                    hasChosen = True
                    rr.viewReservations()
                elif userChoice.lower() == "b": # if b, go to makeReservations function
                    hasChosen = True
                    rr.makeReservations()
                elif userChoice.lower() == "c": # If c, go to deleteReservations function
                    hasChosen = True
                    rr.deleteReservations() 
                elif userChoice.lower() == "d": # If d, go to generateReport function
                    hasChosen = True
                    rr.generateReport()
                elif userChoice.lower() == "e": # If e, terminate the program.
                    hasChosen = True
                    continueRunning = False
                    print ( "\n====================================================================\n" )
                    print ( "                             THANK YOU        " )
                    print ( "\n====================================================================\n" )
                else: # If the user's choice is not within the parameters, display invalid input.
                    print ( " Invalid Input \n" )
            except:
                print ( " Invalid Input \n" )
    except:
        print ( " Error " )
