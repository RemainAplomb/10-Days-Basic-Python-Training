# DAY 8 - ACTIVITY 1
# Program Details: This is a program that uses a class called car to create 3 car objects. The properties of the objects are the user's inputted color,
# model, and manufacturer. Once the 3 car objects has been created, the user will still be able to change/modify his desired property of a certain car.


# This is the car class, it has 3 fields.
# It is also able to display its properties using THIS-IS-A-CAR-OBJECT.displayProperties()
class Car():
    def __init__( self, color, model, manufacturer ):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer
    def displayProperties( self ):
        print ( "    The Car's Color : {} ".format( self.color ) )
        print ( "    The Car's Model: {} ".format( self.model ) )
        print ( "    The Car's Manufacturer: {} ".format( self.manufacturer ) )


continueRunning = True
while continueRunning == True:
    try:
        # This is the list that stores the car objects that will be created.
        objectList = []
        
        # For taking in the user's input and creating the three car objects.
        # It also stores the object's reference into the objectList
        print ( "\n=================== Enter Car Details ===================\n" )
        i = 1
        while i < 4:
            try:
                print ( " ----- Car Number {} ----- ".format( i ) )
                carColor = str( input ( "    Enter Car's Color: " ) )
                carModel = str ( input ( "    Enter Car's Model: " ) )
                carManufacturer = str ( input ( "    Enter Car's Manufacturer: " ) )
                tempObjectHolder = Car( carColor, carModel, carManufacturer )
                objectList.append ( tempObjectHolder )
                i += 1
            except:
                print ( " Invalid Input " )
        print ( "\n=========================================================\n" )

        
        hasChosen = False
        while hasChosen == False:
            # For printing/displaying the properties of the car objects.
            print ( "\n================== Car Details Display ==================\n" )
            for i in range ( len ( objectList ) ):
                print ( " ----- Car Number {} ----- ".format( i + 1 ) )
                objectList[i].displayProperties()

            # Asking the user what he/she would like to do.
            print ( "\n=============== What Would you like to do? ==============\n" )
            print ( " [1] Modify car " )
            print ( " [2] Go back to the beginning " )
            print ( " [3] Close Program " )
            print ( "\n=========================================================\n" )
            try:
                userChoice = int ( input ( " Enter your Choice : " ) )
                if userChoice == 1:
                    carNumber = int ( input ( " What car number? " ) ) # Asking the user what car number to modify.
                    try:
                        if carNumber <= 0: # carNumber <= 0 are not taken as proper inputs.
                            print ( " Invalid Car Number. " )
                        else:
                            carChosen = objectList[ carNumber - 1 ] # Taking the chosen car's object reference
                            print ( "\n=========================================================\n" )
                            print ( " ----- Chosen Car Number {} ----- ".format( carNumber ) )
                            carChosen.displayProperties() # Displaying the chosen car's properties
                            print ( "\n=========================================================\n" )
                            
                            # Asking for details and conducting the property replacement.
                            whatProperty = str ( input ( " What property to modify [Color/Model/Manufacturer] ? " ) )
                            replaceWith = str ( input ( " What would you like to replace it with? " ) )
                            try:
                                if whatProperty.lower() == "color" :
                                    carChosen.color = replaceWith
                                    print ( "\n=========================================================\n" )
                                    print ( " Car's color has been replaced with {}. ".format( replaceWith ) )
                                elif whatProperty.lower() == "model" :
                                    carChosen.model = replaceWith
                                    print ( "\n=========================================================\n" )
                                    print ( " Car's model has been replaced with {}. ".format( replaceWith ) )
                                elif whatProperty.lower() == "manufacturer" :
                                    carChosen.manufacturer = replaceWith
                                    print ( "\n=========================================================\n" )
                                    print ( " Car's manufacturer has been replaced with {}. ".format( replaceWith ) )
                                else:
                                    print ( " Invalid Input. " )
                                print ( "\n=========================================================\n" )
                            except:
                                print ( " Invalid Input. " )
                    except:
                        print ( " Invalid Car Number. " )
                elif userChoice == 2: # Going back to the beginning where the user will have to create 3 car objects.
                    print ( "\n=========================================================\n" )
                    print ( "                  Going Back to the start. " )
                    print ( "\n=========================================================\n" )
                    hasChosen = True
                elif userChoice == 3: # Ending the program.
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
    
                        
