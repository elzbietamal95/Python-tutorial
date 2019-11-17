def monthlyBalance(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate/12
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalanceEachMonth = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return updatedBalanceEachMonth

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(1, 13):
    balance = monthlyBalance(balance, annualInterestRate, monthlyPaymentRate)
    print ("Month " + str(month) + " Remaining balance: " + str(round(balance, 2)))
