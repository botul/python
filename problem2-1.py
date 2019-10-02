balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    pay = balance * monthlyPaymentRate
    unpaidb = balance - pay
    balance = unpaidb + unpaidb * (annualInterestRate / 12)

print(round(balance, 2))
