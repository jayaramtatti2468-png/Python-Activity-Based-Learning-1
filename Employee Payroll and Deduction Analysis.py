name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime = float(input("Enter overtime payment: "))
incentives = float(input("Enter incentives: "))

gross = basic + allowances + overtime + incentives

if gross <= 20000:
    deduction_rate = 0.05
elif gross <= 50000:
    deduction_rate = 0.10
else:
    deduction_rate = 0.15

deduction = gross * deduction_rate
net_salary = gross - deduction

print("\nEmployee Salary Statement")
print("Employee Name:", name)
print("Gross Salary:", gross)
print("Deduction:", deduction)
print("Net Salary:", net_salary)