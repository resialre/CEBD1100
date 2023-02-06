import decimal
# Tip Calculator

# Input: The number of diners
while True:
    try:
        diners = int(input("Please input number of diners: "))
        if diners < 0:
            print("Invalid input. Please input a whole, positive number")
            continue
        break
    except ValueError:
        print("Invalid input. Please input whole number.")
        continue
    else:
        break

# Input: The price of the meal, before tax
while True:
    try:
        price_square = float(input("Please input price of meal: "))
        if price_square < 0:
            print("Invalid input. Please input a positive number")
            continue
    except ValueError:
        print("Invalid input. Please input valid number.")
        continue
    else:
        price_square = decimal.Decimal(price_square)
        price_round = price_square.quantize(decimal.Decimal("0.01"), decimal.ROUND_HALF_UP)
        break


# Input: Tip percentage
exceptional = str("1) Exceptional 20%")
good = str("2) Good 15%")
basic = str("3) Basic 10%")
horrible = str("4) Horrible 0%")
while True:
    service_quality = str(input("Please select tip percentage: 1) Exceptional 20%, 2) Good 15%, 3) Basic 10%, 4) Horrible 0%: "))
    if service_quality in exceptional or service_quality == "20" or service_quality == "1" or service_quality == "exceptional":
        service_quality = 1
        break
    if service_quality in good or service_quality == "15" or service_quality == "2" or service_quality == "good":
        service_quality = 2
        break
    if service_quality in basic or service_quality == "10" or service_quality == "3" or service_quality == "basic":
        service_quality = 3
        break
    if service_quality in horrible or service_quality == "0" or service_quality == "4" or service_quality == "horrible":
        service_quality = 4
        break
    else:
        print("Please try again.")
        continue
def tip_percentage(service_quality):
    if service_quality == 1:
        return 20
    elif service_quality == 2:
        return 15
    elif service_quality == 3:
        return 10
    elif service_quality == 4:
        return 0

print (str(tip_percentage(service_quality)) + "%")

# Output: The number of diners
print(f"There are {diners} diners.")

# Output: The price of the meal before tax
def price_bt(price_round, diners):
    decimal.Decimal(diners)
    return price_round * diners

print(f"The price of the meal before tax is {price_bt(price_round, diners)}$.")

# Output: The Quebec tax added (Federal)


# Output: The Quebec tax added (Provincial)

# Output: The total including tax

# Output: The tip amount (based on the price before tax)

# Output: The grand total including tax

# Output: The amount owed per person





