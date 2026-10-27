minutes = int(input("Enter monthly call minutes: "))
data = float(input("Enter monthly data usage in GB: "))

basic = 199 + max(0, minutes - 300) * 0.50
basic += max(0, data - 2) * 50

standard = 399 + max(0, minutes - 1000) * 0.30
standard += max(0, data - 10) * 30

premium = 599 + max(0, minutes - 2000) * 0.20
premium += max(0, data - 25) * 20

print("Basic Plan:", basic)
print("Standard Plan:", standard)
print("Premium Plan:", premium)

if basic <= standard and basic <= premium:
    print("Best Plan: Basic")
elif standard <= premium:
    print("Best Plan: Standard")
else:
    print("Best Plan: Premium")