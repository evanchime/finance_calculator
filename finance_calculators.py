# A program that allows the user to access two different financial calculators: an investment calculator 
# and a home loan repayment calculator.
#
# Print out the menu and user prompt. 
# 
# Handle case insensitivity of user input
# 
# If the user entered "investment" ask the user the amount of money they are depositing, 
# the interest rate, the number of years they plan on investing and whether they want simple or compound interest
# Depending on what interest it is, calculate the amount they will get back after the given period
#
# Else if they selected 'bond', ask the user to enter the present value of their home,
# the interest rate and the number of months they plan to take to repay the bond
# Calculate the monthly repayment amount and print it out

import math

print("\ninvestment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan\n\n")

calculator = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if calculator == "investment":
    deposit = float(input("Enter the amount of money you are depositing. Only the amount should be \
entered e.g. enter 1000 not R1000 : "))
    interest_rate = float(input("Enter the interest rate. Only the number of the interest \
rate should be entered e.g. enter 8 and not 8%: "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Enter the interest, 'simple' or 'compound': ").lower()
    
    if interest == "simple":
        # Simple interest formula. Divide interest_rate by 100 to convert percentage to decimal
        total = deposit * (1 + ((interest_rate / 100) * years))
    elif interest == "compound":
        # Compound interest formula. Divide interest_rate by 100 to convert percentage to decimal
        total = deposit * math.pow((1 + (interest_rate / 100)), years) 
    else:
        print("Invalid interest type entered. Please enter either 'simple' or 'compound'.")
    
    print(f"Total amount after {years} years: R{total:.2f}")

elif calculator == "bond":
    present_value = float(input("Enter the present value of the house. Only the amount should be \
entered e.g. enter 1000000 not R1,000,000: "))
    interest_rate = float(input("Enter the interest rate. Only the number of the interest rate \
should be entered e.g. enter 8 and not 8%: "))
    months = int(input("Enter the number of months you plan on taking to repay the bond: "))
     
     # Monthly repayment amount formula. Divide interest_rate by 100 to convert percentage to decimal
     # Divide by 12 to convert annual interest rate to monthly interest rate
    repayment = ((interest_rate / 100 / 12) * present_value) / (1 - math.pow((1 + (interest_rate / 100 / 12)), -months)) 
    
    print(f"Monthly repayment amount: R{repayment:.2f}")
