units = int(input("Enter electricity units: "))

if units < 0:
    print("Invalid units")
else:
    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    else:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 8

    fixed_charge = 50
    surcharge = bill * 0.05
    total = bill + fixed_charge + surcharge

    print("Energy Charge:", bill)
    print("Fixed Charge:", fixed_charge)
    print("Surcharge:", surcharge)
    print("Total Electricity Bill:", total)