units = int(input("Enter number of units produced: "))
material = float(input("Enter material cost: "))
labour = float(input("Enter labour cost: "))
overhead = float(input("Enter overhead cost: "))
price = float(input("Enter selling price per unit: "))

if units <= 0:
    print("Invalid number of units")
else:
    total_cost = material + labour + overhead
    revenue = units * price
    profit = revenue - total_cost

    print("Total Manufacturing Cost:", total_cost)
    print("Cost Per Unit:", total_cost / units)
    print("Total Revenue:", revenue)
    print("Profit/Loss:", profit)

    if profit > 0:
        print("Result: Profit")
    elif profit < 0:
        print("Result: Loss")
    else:
        print("Result: No Profit, No Loss")