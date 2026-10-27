passengers = int(input("Enter number of passengers: "))
distance = float(input("Enter distance in km: "))
travel_class = input("Enter class (sleeper/AC): ").lower()
age = int(input("Enter passenger age: "))

if passengers <= 0 or distance < 0:
    print("Invalid input")
else:
    if travel_class == "sleeper":
        rate = 1
        reservation = 40
    elif travel_class == "ac":
        rate = 2
        reservation = 80
    else:
        rate = 0
        reservation = 0

    if rate == 0:
        print("Invalid travel class")
    else:
        fare = distance * rate

        if age >= 60:
            fare = fare - fare * 0.20

        total = (fare + reservation) * passengers

        print("Total Railway Fare:", total)