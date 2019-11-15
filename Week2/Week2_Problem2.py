def monthlyPayment(balance, annualInteresetRate):
    monthlyInterestRate = annualInterestRate / 12
    minimumFixedMonthlyPayment = 0
    updatedBalance = balance
    while updatedBalance >= 0:
        minimumFixedMonthlyPayment += 10
        updatedBalance = balance
        for month in range(1, 13):
            monthlyUnpaidBalance = updatedBalance - minimumFixedMonthlyPayment
            updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    return minimumFixedMonthlyPayment

balance = 3926
annualInterestRate = 0.2

minimumFixedMonthlyPayment = monthlyPayment(balance, annualInterestRate)
print("Lowest Payment:", minimumFixedMonthlyPayment)
