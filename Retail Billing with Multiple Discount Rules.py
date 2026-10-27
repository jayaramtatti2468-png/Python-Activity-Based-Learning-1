amount = float(input("Enter purchase amount: "))

if amount < 0:
    print("Invalid amount")
else:
    if amount >= 5000:
        discount = amount * 0.20
    elif amount >= 2000:
        discount = amount * 0.10
    elif amount >= 1000:
        discount = amount * 0.05
    else:
        discount = 0

    after_discount = amount - discount
    tax = after_discount * 0.05
    total = after_discount + tax

    print("Purchase Amount:", amount)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final Bill:", total)