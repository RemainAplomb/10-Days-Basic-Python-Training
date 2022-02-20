#  DAY 7 - ACTIVITY 2

# This is a module for the basic calculator program.
# The main.py which can be found along with this module contains framework of the program.

# Please keep in mind that the functions in this module only takes in two arguments.
# Furthermore, if the function fails to conduct the said operation, it will return a False value.

# Function for addition
def add ( num1, num2 ):
    try:
        result = num1 + num2
        return result
    except:
        return False

# Function for subtraction
def subtract ( num1, num2 ):
    try:
        result = num1 - num2
        return result
    except:
        return False

# Function for multiplication
def multiply ( num1, num2 ):
    try:
        result = num1 * num2
        return result
    except:
        return False

# Function for division.
def divide ( num1, num2 ):
    try:
        result = num1 / num2
        return result
    except:
        return False
