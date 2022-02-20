# Day2 - Activity1
# This is a program that adds Mr. or Ms. into the user's full name.

# If the user inputs 2 words as their full name, the program will split the string and take the element at index 0.
# Then, it will use that as the first name which will then used as an input in the replace method so that the Mr/Ms can be added.

# However, If the user inputs more than 2 words as their full name, the program will take split the string and take the element at the last index.
# The element at the last index will be used as the last name. Then, the Mr/Ms will be added.

# Apart from that, if the user inputs only a single word as their name. The program will directly add the Mr/Ms into the name.
# Furthermore, if the user's input are not within the parameters, the program will issue an invalid input warning.

mx = [ "Mr." , "Ms." ]

while True:
    print ( "-------------------- Enter Details --------------------" )
    sex = int ( input ( " Are you a [1] male or [2] female? " ) )
    fullName = str ( input ( " Enter your full name: " ) )
    print ( "-------------------------------------------------------" )

    if fullName == "" or sex < 1 or sex > 2 or sex == "":
        print ( " Invalid Input " )
    else:
        nameList = fullName.split(" ")
        firstName = nameList[0]
        lastName = nameList[ len(nameList) - 1 ]
        if len ( nameList ) == 1:
            resultName = mx[ sex-1 ] + firstName
        elif len ( nameList ) == 2:
            resultName = fullName.replace ( firstName, mx[sex -1] )
        elif len ( nameList ) > 2:
            resultName = mx[ sex-1 ] + lastName
        print ( " Good Day, {}! ".format( resultName ) )
    print ( "-------------------------------------------------------" )

    
    
