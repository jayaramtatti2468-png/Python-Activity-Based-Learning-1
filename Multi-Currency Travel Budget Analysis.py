budget = float(input("Enter travel budget in INR: "))
currency = input("Enter currency (USD/EUR/GBP): ").upper()
amount = float(input("Enter foreign currency expenses: "))

if currency == "USD":
    rate = 83
elif currency == "EUR":
    rate = 90
elif currency == "GBP":
    rate = 105
else:
    rate = 0

if rate == 0:
    print("Unsupported currency")
else:
    expense = amount * rate
    balance = budget - expense

    print("Travel Expense in INR:", expense)

    if balance >= 0:
        print("Remaining Budget:", balance)
    else:
        print("Budget Exceeded By:", abs(balance))