# DAY 8 - ACTIVITY 4
# Program Description: This is a program that uses two classes. The parent class named House and the child class named TownHouse.
# The program creates a town house object which stores the users input. Furthermore, it also has other functions like turning the oven and lights.

# The parent class 
class House():
    def __init__( self, floorSize, noOfFloors, noOfDoors ): # Initializing the needed fields
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors

        self.lightStatus = False
        self.ovenStatus = False

    def lightClose( self ): # For turning off the lights
        self.lightStatus = False
        print ( "\n=========================================================\n" )
        print ( " The light has been turned off. " )
        print ( "\n=========================================================\n" )
        return
    
    def lightOpen( self ): # for turning on the lights
        self.lightStatus = True
        print ( "\n=========================================================\n" )
        print ( " The light has been turned on. " )
        print ( "\n=========================================================\n" )
        return

    def ovenOpen( self ): # for turning on the oven
        self.ovenStatus = True
        print ( "\n=========================================================\n" )
        print ( " The oven has been turned on. " )
        print ( "\n=========================================================\n" )
        return

    def ovenClose( self ): # turning off the oven
        self.ovenStatus = False
        print ( "\n=========================================================\n" )
        print ( " The oven has been turned off. " )
        print ( "\n=========================================================\n" )
        return


class TownHouse( House ):
    def __init__( self, floorSize, noOfFloors, noOfDoors, noOfWindows ): # Compared to the parent class, the TownHouse class has an added field named noOfWindows
        super().__init__( floorSize, noOfFloors, noOfDoors ) # for the inheritance
        
        self.noOfWindows = noOfWindows

    def switchOn( self ): # For turning on both the lights and oven
        self.lightOpen()
        self.ovenOpen()
        return

    def switchOff( self ): # for turning on the lights and oven
        self.lightClose()
        self.ovenClose()
        return

    def townHouseDetails( self ):
        print ( "\n=================== Town House Details ==================\n" )
        print ( " Floor Size: " , self.floorSize )
        print ( " Number of Floors: " , self.noOfFloors )
        print ( " Number of Doors: " , self.noOfDoors )
        print ( " Number of Windows: " , self.noOfWindows )
        print ( "\n Is the lights on? " , self.lightStatus )
        print ( " Is the oven on? " , self.ovenStatus )
        print ( "\n=========================================================\n" )
        return


# If the user chooses to end the program, this will turn to False and the while loop will stop which will terminate the program.
continueRunning = True
while continueRunning == True:
    try:
        # For taking in the user's input and creating the town house object
        print ( "\n================ Enter Town House Details ===============\n" )
        floorSize = float( input ( " How many square meters is the floor size (int/float)? " ) )
        noOfFloors = int( input ( " How many Floors are there (int)? " ) )
        noOfDoors = int( input ( " How many Doors are there (int)? " ) )
        noOfWindows = int( input ( " How many Windows are there (int)? " ) )
        print ( "\n=========================================================\n" )
        townHouseObject = TownHouse( floorSize, noOfFloors, noOfDoors, noOfWindows )

        # For asking and executing the user's desired command.
        hasChosen = False
        while hasChosen == False:
            townHouseObject.townHouseDetails()
            print ( "\n=============== What Would you like to do? ==============\n" )
            print ( " [1] Modify floor size " )
            print ( " [2] Change number of floors " )
            print ( " [3] Change number of doors " )
            print ( " [4] Change number of windows " )
            print ( " [5] Open Lights " )
            print ( " [6] Close Lights " )
            print ( " [7] Open Oven " )
            print ( " [8] Close Oven " )
            print ( " [9] Switch ON " )
            print ( " [10] Switch OFF " )
            print ( " [11] Try Again " )
            print ( " [12] Close Program " )
            print ( "\n=========================================================\n" )
            try:
                userChoice = int ( input ( " Enter your Choice : " ) )
                if userChoice == 1: # Changing floor size
                    try:
                        floorSize = float( input ( " How many square meters is the floor size (int/float)? " ) )
                        townHouseObject.floorSize = floorSize
                    except:
                        print ( " Invalid Input. " )
                elif userChoice == 2: # changing number of floors
                    try:
                        noOfFloors = int( input ( " How many Floors are there (int)? " ) )
                        townHouseObject.noOfFloors = noOfFloors
                    except:
                        print ( " Invalid Input. " )
                elif userChoice == 3: # changing number of doors
                    try:
                        noOfDoors = int( input ( " How many Doors are there (int)? " ) )
                        townHouseObject.noOfDoors = noOfDoors
                    except:
                        print ( " Invalid Input. " )
                elif userChoice == 4: # changing number of windows
                    try:
                        noOfWindows = int( input ( " How many Windows are there (int)? " ) )
                        townHouseObject.noOfWindows = noOfWindows
                    except:
                        print ( " Invalid Input. " )
                elif userChoice == 5: # turning on the light
                    townHouseObject.lightOpen()
                elif userChoice == 6: # turning off the light
                    townHouseObject.lightClose()
                elif userChoice == 7: # turning on the oven
                    townHouseObject.ovenOpen()
                elif userChoice == 8: # turning off the oven
                    townHouseObject.ovenClose()
                elif userChoice == 9: # switching on the lights and oven
                    townHouseObject.switchOn()
                elif userChoice == 10: # switching on the light and oven
                    townHouseObject.switchOff()
                elif userChoice == 11: # Going back to the beginning
                    print ( "\n=========================================================\n" )
                    print ( "                  Going Back to the start. " )
                    print ( "\n=========================================================\n" )
                    hasChosen = True
                elif userChoice == 12: # Ending the program.
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
        print ( " Invalid Input " )


