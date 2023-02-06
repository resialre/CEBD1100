customer_type = input("Customer type: R/W")
customer_type = customer_type.lower()
invoice_type = float(input("Invoice: 1-1000"))
receipt = "Discount: "

def discount_percent(customer_type, invoice_type):
    if customer_type == "W":
        if invoice_type >= float(500.00):
            return 0.05
        if invoice_type < float(500.00):
            return 0.04
    elif customer_type == "R":
        if invoice_type >= float(250.00):
            return 0.02
        if invoice_type >= 100 and invoice_type < 250:
            return 0.01
    elif customer_type == "R":
        if invoice_type < 100:
            return 0.00
    else:
        print("Invalid")

print(receipt + str(discount_percent(customer_type, invoice_type)))