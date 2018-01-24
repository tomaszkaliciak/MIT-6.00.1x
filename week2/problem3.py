
balance = 320000
annualInterestRate = 0.2
lowerBound = balance/12
monthlyInterstRate = annualInterestRate / 12.0
upperBound = (balance*(1 + monthlyInterstRate)**12) / 12.0
result = upperBound

while True:
    mid = (lowerBound + upperBound) / 2
    tempBalance = balance
    for i in range(0, 12):
        monthlyUnpaidBalance = tempBalance - mid
        tempBalance = monthlyUnpaidBalance + monthlyInterstRate * monthlyUnpaidBalance
    if tempBalance > 0:
        lowerBound = mid
    else:
        upperBound = mid

    if abs(tempBalance) < 0.01:
        print("Lowest Payment:", round(mid, 2))
        break
