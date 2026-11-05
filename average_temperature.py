# Client Project: Calculate average temperature

number_of_readings = int(input("Enter number of temperature readings: "))

if number_of_readings <= 0:
    print("Please enter at least one reading.")
else:
    total = 0.0

    for day in range(1, number_of_readings + 1):
        temperature = float(input(f"Enter temperature {day}: "))
        total = total + temperature

    average = total / number_of_readings
    print(f"Average temperature is {average:.2f}°C")
