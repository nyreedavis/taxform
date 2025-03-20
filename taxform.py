"""
chapter 2 case study project 
pages 30-31
program: taxform.py
2/24/2025
applicaton to calculate a person's income tax.
"""

# initialize the constants
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0

# Input phase
grossIncome = float(input("Please enter the gross income: "))
numDependents = int(input("Next, enter the number of dependents: "))

# compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * numDependents) 
incomeTax = taxableIncome * TAX_RATE
incomeTax = round(incomeTax, 2)
# Output phase
print("For a gross income of $" + str(grossIncome) + " When claiming " + str(numDependents) + "dependent(s):")
print("The income tax is $" + str(incomeTax))
input("Press ENTER to exit the program")