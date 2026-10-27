event = input("Enter event name: ")
participants = int(input("Enter number of participants: "))
fee = float(input("Enter registration fee per participant: "))

venue = float(input("Enter venue expenses: "))
food = float(input("Enter food expenses: "))
decoration = float(input("Enter decoration expenses: "))
other = float(input("Enter other expenses: "))

income = participants * fee
expenses = venue + food + decoration + other
balance = income - expenses

print("\nCampus Event Financial Report")
print("Event Name:", event)
print("Total Income:", income)
print("Total Expenses:", expenses)
print("Surplus/Deficit:", balance)

if balance > 0:
    print("Status: Surplus")
elif balance < 0:
    print("Status: Deficit")
else:
    print("Status: Break-even")