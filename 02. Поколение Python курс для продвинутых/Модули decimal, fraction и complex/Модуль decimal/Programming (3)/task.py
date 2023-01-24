from decimal import Decimal


num = Decimal(input())

result = num.exp() + num.ln() + num.log10() + num.sqrt()

print(result)