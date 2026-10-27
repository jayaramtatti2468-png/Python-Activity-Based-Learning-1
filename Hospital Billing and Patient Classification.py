consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))
age = int(input("Enter patient age: "))

total = consultation + diagnostic + treatment

if age >= 60:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

if final_bill >= 10000:
    category = "High-cost patient"
elif final_bill >= 5000:
    category = "Medium-cost patient"
else:
    category = "Low-cost patient"

print("Total Bill:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
print("Patient Category:", category)