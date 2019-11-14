def monthlyBalance(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate/12
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return updatedBalanceEachMonth

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
numberOfMonths = 12

while numberOfMonths > 0:
    balance = monthlyBalance(balance, annualInterestRate, monthlyPaymentRate)
    numberOfMonths -= 1
    print ("Month " + str(numberOfMonths) + " Remaining balance: " + str(round(balance, 2)))
