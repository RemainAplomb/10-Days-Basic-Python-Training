# ACTIVITY 3: PYTHON NUMBERS
# Program Description: This is a program that takes the user's input to calculate for the employee's gross and net salary.
# The hourly rate is already pre-determined and has been set to 500.
# Additionally, the tax rate is set to 10 percent of the employee's gross income.


hourlyRate = 500
taxRate = 0.10

# A loop will be used to make sure that the user can use the program continously.
while True:
    # The program will mainly use float when working with the numbers.
    # This will help in the accuracy of the calculations.
    print ( "==================== ENTER DETAILS ====================" )
    employeeName = input ( " Employee Name: " )
    numberHours = float( input ( " Enter number of hours: " ) )
    grossSalary = float(numberHours) * float(hourlyRate)
    sssContribution = float( input ( " SSS contribution: " ) )
    philHealth = float ( input ( " Phil Health: " ) )
    housingLoan = float ( input ( " Housing loan: " ) )
    print ( "=======================================================\n" )

    # Generating payslip.
    print ( "======================  PAYSLIP  ======================" )
    print ( "================ EMPLOYEE INFORMATION =================" )
    print ( " Employee Name: " , employeeName )
    print ( " Rendered Hours: ", numberHours )
    print ( " Rate per Hour: ", hourlyRate )
    print ( " Gross Salary: ", grossSalary )
    print ( "====================== DEDUCTIONS =====================" )
    print ( " SSS: " , sssContribution )
    print ( " PhilHealth: " , philHealth )
    print ( " Other Loan: " , housingLoan )
    tax = float ( grossSalary ) * taxRate
    print ( " Tax : " , tax ) 
    deductions_total = sssContribution + philHealth + housingLoan + tax 
    print ( " Total Deductions: " , deductions_total )
    netSalary = grossSalary - deductions_total
    print ( "\n Net Salary: PHP " , netSalary )
    print ( "=======================================================\n" )

