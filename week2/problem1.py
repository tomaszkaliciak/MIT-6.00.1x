
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.0

for i in range(0, 12):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

print("Remaining balance:", round(balance, 2))
