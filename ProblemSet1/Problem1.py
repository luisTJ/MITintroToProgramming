"""Problem 1:
problem one is to show total amount paid and remaining balance
when making minimum payment on credit card
"""


def getNumberInput(prompt):
    while(True):
        user_input = raw_input(prompt)
        try:
            return float(user_input)
        except:
            pass

def getMinimumMonthlyPayment(balance,rate):
    return balance * rate

def getInterestPaid(balance, apr):
    return apr/12.0 * balance

def getPrincipalPaid(balance, apr, paid):
    return paid - getInterestPaid(balance, apr)

outstanding = getNumberInput("Enter the outstanding balance on your credit card: ")
apr = getNumberInput("Enter the annual credit card interest rate as a decimal: ")
min_payment_rate = getNumberInput("Enter the minimum monthly payment rate as a decimal: ")
print "";

total_paid = 0.00
remain = 0.00

for i in range(12):
    print "Month: "+str(i+1)
    min = getMinimumMonthlyPayment(outstanding,min_payment_rate)
    principle_paid = getPrincipalPaid(outstanding,apr, min)
    remain = outstanding - principle_paid
    total_paid = total_paid + min
    print "Minimum monthly payment: $" + format(min,".2f")
    print "Principal paid: $"+ format(principle_paid,".2f")
    print "Remaining balance: $"+ format(remain,".2f")
    print ""
    outstanding = remain

print "RESULT"
print "Total amount paid: $" + format(total_paid,".2f")
print "Remaining balance: $" + format(remain, ".2f")