import decimal

unit_price = decimal.Decimal(input("Price: "))
q = decimal.Decimal(input("Quantity: "))

price = unit_price * q

cents = decimal.Decimal("0.0001")

print(price)

money_value = price.quantize(cents, decimal.ROUND_HALF_UP)
print(money_value)