
balance = 3926
annualInterestRate = 0.2

result = 0


monthyInterstRate = annualInterestRate/12.0

for nPayment in range(0, balance, 1):
    tempBalance = balance
    for i in range(0, 12):
        monthlyUnpaidBalance = tempBalance - nPayment
        tempBalance = monthlyUnpaidBalance + monthyInterstRate * monthlyUnpaidBalance
    if tempBalance <= 0:
        result = nPayment
        break
print("Lowest Payment:", result)
