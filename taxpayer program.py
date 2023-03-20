#All taxpayers are charged a flat tax rate of 20%
#All taxpayers are allowed a $10,000 standard deduction
#For each dependent, a taxpayer is allowed an additional $3,000 deduction
#Gross income must be entered to the nearest penny
#The income tax is expressed as a decimal number

TAX_FLAT_RATE = 0.20
STANDARD_DEDUCT = 10000.00
CHILD_DEDUCT = 3000.00

print("\t ++++++++++++ Welcome to the taxpayer program +++++++++++++++")
grossIncome = float(input("Enter the gross income: "))
childTax = int(input("Enter the number of dependents: "))

taxCharge = (grossIncome * TAX_FLAT_RATE) - STANDARD_DEDUCT
finalTax = taxCharge - (childTax * CHILD_DEDUCT)

print("The income tax is $" + str(round(finalTax, 1)))



