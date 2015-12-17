"""Problem 1:
problem 2 is to show what is the minimum to pay each month to pay off in 12 months time
"""


def getNumberInput(prompt):
    while(True):
        input = raw_input(prompt)
        try:
            return float(input)
        except:
            pass

def getTotalPayBack(balance, apr, time_in_month):
    return (1+apr)*balance/time_in_month

def updateBalace(balance, monthly_interest_rate, minimum_payment):
    return (balance * (1+monthly_interest_rate)) - minimum_payment

original_outstanding = getNumberInput("Enter the outstanding balance on your credit card: ");
apr = getNumberInput("Enter the annual credit card interest rate as a decimal: ");
monthly_interest_rate = apr / 12.0

estimate_payment = round(((1+apr)*original_outstanding)/12.0,-1)
month = 0
outstanding = original_outstanding

while(True):
    outstanding = original_outstanding
    for i in range(12):
        outstanding = updateBalace(outstanding,monthly_interest_rate,estimate_payment)
        month = i
        if(outstanding <= 0):
            break

    if(outstanding < 0 and abs(round(outstanding,-1))<120):
        break
    else:
        estimate_payment = estimate_payment - 10

print ""
print "RESULT"
print "Monthly payment to pay off debt in 1 year: $" + str(estimate_payment)
print "Number of months needed: " + str(month+1)
print "Balance: " + format(outstanding,".2f")