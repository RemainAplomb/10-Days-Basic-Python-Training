# DAY 6 - ACTIVITY 2
# This is a module for getting the deductions.

# Please note that the tax is currently set at 12 percent of the gross salary.
# In addition, the function returns a list that has two elements.
# the first element is the tax.
# the second element is the totalDeduction.

def deductions ( grossSalary, loan, insurance ):
    tax = grossSalary * 0.12
    totalDeduction = tax + loan + insurance
    return [ tax, totalDeduction ]
