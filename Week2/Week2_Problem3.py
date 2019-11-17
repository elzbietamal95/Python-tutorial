def monthlyPayment(balance, annualInteresetRate):
    monthlyInterestRate = annualInterestRate / 12
    monthlyPaymentLowerBound = balance / 12
    monthlyPaymentUpperBound = balance * ((1 + monthlyInterestRate) ** 12) / 12
    averageMonthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2
    while abs(monthlyPaymentUpperBound - monthlyPaymentLowerBound) >= 0.01:
        updatedBalance = balance
        for month in range(1, 13):
            monthlyUnpaidBalance = updatedBalance - averageMonthlyPayment
            updatedBalance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
        if updatedBalance > 0:
            monthlyPaymentLowerBound = averageMonthlyPayment
        else:
            monthlyPaymentUpperBound = averageMonthlyPayment
        averageMonthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2
    return averageMonthlyPayment


balance = 320000
annualInterestRate = 0.2
fixedMonthlyPayment = monthlyPayment(balance, annualInterestRate)
print("Lowest Payment:", round(fixedMonthlyPayment, 2))
