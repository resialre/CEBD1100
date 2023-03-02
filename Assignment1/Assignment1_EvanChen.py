import decimal

# Tip Calculator

# Input: The number of diners

while True:
    try:
        diners = int(input("Please input number of diners: "))
        if diners <= 0:
            print("Invalid input. Please input a whole, positive number")  # The number of diners cannot be negative or 0
            continue
        break
    except ValueError:
        print("Invalid input. Please input whole number.")  # Prevents user from inputting anything other than integers
        continue

# Input: The price of the meal, before tax

while True:
    try:
        price_square = float(input("Please input price of meal: "))
        if price_square < 0:
            print("Invalid input. Please input a positive number")  # Price of meal cannot be a negative value
            continue
    except ValueError:
        print("Invalid input. Please input valid number.")  # Prevents user from inputting anything other than integers
        continue
    else:
        price_square = decimal.Decimal(price_square)
        price_round = price_square.quantize(decimal.Decimal("0.01"), decimal.ROUND_HALF_UP)  # Output is 2 decimal place
        break

# Input: Tip percentage

exceptional = str("1) Exceptional 20%")  # Service quality assigned values for condition checks in next function
good = str("2) Good 15%")
basic = str("3) Basic 10%")
horrible = str("4) Horrible 0%")

while True:
    service_quality = str(
        input("Please select tip percentage: 1) Exceptional 20%, 2) Good 15%, 3) Basic 10%, 4) Horrible 0%: "))
    if service_quality in horrible or service_quality == "0" or service_quality == "4" or service_quality == "horrible":   # Wide range of acceptable answers for better user experience
        service_quality = 4
        break
    elif service_quality in basic or service_quality == "10" or service_quality == "3" or service_quality == "basic":
        service_quality = 3
        break
    elif service_quality in good or service_quality == "15" or service_quality == "2" or service_quality == "good":
        service_quality = 2
        break
    elif service_quality in exceptional or service_quality == "20" or service_quality == "1" or service_quality == "exceptional":
        service_quality = 1
        break
    else:
        print("Please try again.")  # Allows user to try re-inputting if they entered anything unintended
        continue


def tip_percentage(service_quality):   # Assigns a tip percentage value to the service quality
    if service_quality == 1:
        return 20
    elif service_quality == 2:
        return 15
    elif service_quality == 3:
        return 10
    elif service_quality == 4:
        return 0


tip_percentage(service_quality)     # Calls the function

print("You have selected " + str(tip_percentage(service_quality)) + "% in tip.")


# Output: The number of diners

def number_of_diners():     # Not really needed, but I wanted to make sure that if there were only 1 diner, the conjugation is correct
    if diners == 1:
        print("There is 1 diner.")
    else:
        print(f"There are {diners} diners.")

number_of_diners()


# Output: The price of the meal before tax

def price_bt(price_round, diners):
    decimal.Decimal(diners)
    return price_round * diners


print(f"The price of the meal before tax is {price_bt(price_round, diners):.2f}$.")

# Output: The Quebec tax added (Federal); given GST = 5%

gst = float()


def gst_tax(price_bt, gst):     # To account for future changes in GST, allows the function to be modified accordingly
    gst = 0.05
    return float(price_bt(price_round, diners)) * float(gst)


print(f"The Quebec federal tax added is {gst_tax(price_bt, gst):.2f}$.")

# Output: The Quebec tax added (Provincial); given QST = 9.975%

qst = float()


def qst_tax(price_bt, qst):     # To account for future changes in QST, allows the function to be modified accordingly
    qst = 0.09975
    return float(price_bt(price_round, diners)) * float(qst)


print(f"The Quebec provincial tax added is {qst_tax(price_bt, qst):.2f}$.")

# Output: The total including tax

total_notip = float(price_bt(price_round, diners)) + float(gst_tax(price_bt, gst)) + float(qst_tax(price_bt, qst))
print(f"The grand total for the meal is {total_notip:.2f}$.")

# Output: The tip amount (based on the price before tax)

tip_amount = (tip_percentage(service_quality) / 100) * float(price_bt(price_round, diners))
print(f"The tip amount is {tip_amount:.2f}$.")

# Output: The grand total including tax

grand_total = total_notip + tip_amount
print(f"The grand total for the meal is {grand_total:.2f}$.")

# Output: The amount owed per person if everyone is paying equally

amount_pp = grand_total / diners
print(f"The amount owed per person is {amount_pp:.2f}$.")
