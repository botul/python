balance = 320000
annualInterestRate = 0.2
b0 = balance
air = annualInterestRate
mRate = air / 12.0
fixed = b0 / 12.0
fixed_lower = b0 / 12.0
fixed_upper = (b0 * (1 + air) ** 12) / 12.0
unpaidb = balance

while True:
    for i in range(12):
        unpaidb = balance - fixed
        balance = unpaidb + mRate * unpaidb
    if abs(balance) < 0.1:
        print("Lowest Payment: ", round(fixed, 2))
        break
    else:
        if balance < 0:
            fixed_upper = fixed
        elif balance > 0:
            fixed_lower = fixed

        fixed = (fixed_lower + fixed_upper) / 2
        balance = b0