"""
program_name : debt
aurthor : muthelo phindulo
student_number : 225004680

input:  principal_amount
        numner_of_years
        interest

output:A -> annual fixed repayment amount
"""

#program to calcuulate the debt amount user will pay at a given time period
#the formula : A = (P * (1 + r)**N) *  r / ((1 + r)**N - 1)

#get the inputs from the user
number_of_years = int(input("Enter the number of years: "))

principal_amount = float(input("Enter the principal amount: "))

interest = float(input("Enter the interest: "))

#convert the interest
r = interest/100

#to calculate the value of A using given inputs
A = (principal_amount * (1 + r)**number_of_years *  r) / ((1 + r)**number_of_years - 1)

#round the value of A to 2 decimal places
A = round(A,2)

#display the value of A
print(f"the value of A is R{A:,.2f}")