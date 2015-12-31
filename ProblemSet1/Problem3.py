"""Problem 1:
problem 2 is to show what is the minimum to pay each month to pay off in 12 months time
"""

def getNumberInput(prompt):
    while(True):
        user_input = raw_input(prompt)
        try:
            return float(user_input)
        except:
            pass


"""Problem 1:
problem 3 using bisection to find minimum payment in a year
"""


def getNumberInput(prompt):
    while(True):
        user_input = raw_input(prompt)
        try:
            return float(user_input)
        except:
            pass

def getMonthlyPaymentUpperBound(balance,apr):
    return (balance*(1+(apr/12.0))**12.0)/12.0



original_outstanding = getNumberInput("Enter the outstanding balance on your credit card: ")
apr = getNumberInput("Enter the annual credit card interest rate as a decimal: ")

lowerbound = original_outstanding / 12.0
upperbound = getMonthlyPaymentUpperBound(original_outstanding,apr)
outstanding = original_outstanding
month_needed = None
monthly_minimum_payment = None

while(True):
    outstanding = original_outstanding
    monthly_minimum_payment = ((upperbound + lowerbound) / 2.0)
    month_needed = 0
    for i in range(12):
        interest = (apr * outstanding ) / 12.0
        outstanding = outstanding + interest - monthly_minimum_payment
        month_needed = month_needed + 1
        if(outstanding <= 0):
            break
    if outstanding > 0:
        lowerbound = monthly_minimum_payment
    elif outstanding <= 0 and abs(outstanding) < 0.12:
        break
    else:
        upperbound = monthly_minimum_payment


print("")
print("RESULT")
print("Monthly payment to pay off debt in 1 year: $")+format(monthly_minimum_payment,".2f")
print("Number of months needed: ")+str(month_needed)
print("Balance: ")+format(outstanding,".2f")