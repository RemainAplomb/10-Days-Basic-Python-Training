# DAY 6 - ACTIVITY 2
# Program Description: This is a program that uses modules to calculate the gross salary, total deductions, and net salary of the employee.

# These are the modules that was made for this activity. They should be in the same folder as this main.py
import GrossSalary
import SalaryDeductions
import NetSalary


continueRunning = True
while continueRunning == True:
    try:
        # The program will mainly use float when working with the numbers.
        # This will help in the accuracy of the calculations.
        print ( "==================== ENTER DETAILS ====================" )
        employeeName = input ( " Employee Name: " )
        numberHours = float( input ( " Enter number of hours: " ) )
        loan = float ( input ( " Enter loan amount: " ) )
        healthInsurance = float ( input ( " Enter health insurance amount: " ) )

        # Using the three modules, grossSalary, deductions, and net salary will be computed.
        # Please keep in mind that the function deduction in SalaryDeductions returns [ tax, totalDeduction ]
        grossSalary = GrossSalary.gross_salary ( numberHours )
        deductions = SalaryDeductions.deductions( grossSalary, loan, healthInsurance )
        netSalary = NetSalary.net( grossSalary, deductions[1] )

        # For printing out the output.
        print ( "======================= OUTPUT ========================\n" )
        print ( " Name: {} ".format ( employeeName ) )
        print ( " Hour: {} hour(s) \n".format( numberHours ) )
        print ( " Gross Salary: PHP {} \n".format ( grossSalary ) )
        print ( " Tax: PHP {} ".format( deductions[0] ) )
        print ( " Loan: PHP {} ".format( loan ) )
        print ( " Insurance: PHP {} \n".format( insurance ) )
        print ( " Total Deductions: PHP {} \n".format ( deductions[1] ) )
        print ( " Net Salary: PHP {} \n".format( netSalary ) )
        print ( "=======================================================\n" )

        # Asking the user if he/she would like to continue using the program.
        hasChosen = False
        while hasChosen == False:
            try:
                userChoice = str ( input ( " Would you like to try again? Y/y if Yes and N/n if No. " ) )
                if userChoice.lower() == "y" or userChoice.lower() == "yes" :
                    hasChosen = True
                elif userChoice.lower() == "n" or userChoice.lower() == "no" :
                    print ( "\n=======================================================\n" )
                    print ( "                       THANK YOU            \n" )
                    print ( "=======================================================\n" )
                    continueRunning = False
                    hasChosen = True
                else:
                    print ( " Invalid Input. " )
            except:
                print ( " Invalid Input. " )
    except:
        print ( " Invalid Input. " )
        
