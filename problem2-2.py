balance = 4773
annualInterestRate = 0.2

b0 = balance
air = annualInterestRate
mRate = air / 12
fixed = 0
unpaidb = balance

while True:
    for i in range(12):
        unpaidb = balance - fixed
        balance = unpaidb + mRate * unpaidb
    if balance <= 0:
        print("Lowest Payment: ", round(fixed, 2))
        break
    else:
        fixed += 10
        balance = b0