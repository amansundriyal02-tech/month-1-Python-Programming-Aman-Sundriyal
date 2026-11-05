"""
Week 1: Introduction to Python Programming
A beginner-friendly menu program demonstrating input/output, variables,
data types, operators, if-else, for loops, and while loops.
"""

def temperature_converter():
    print("\n--- Temperature Converter ---")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:.2f}°C = {fahrenheit:.2f}°F")


def calculator():
    print("\n--- Simple Calculator ---")
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        return

    print("Result:", result)


def average_temperature():
    print("\n--- Average Temperature Calculator ---")
    count = int(input("How many temperature readings do you want to enter? "))

    if count <= 0:
        print("Please enter a number greater than zero.")
        return

    total = 0.0
    for day in range(1, count + 1):
        temperature = float(input(f"Enter temperature for reading {day}: "))
        total += temperature

    average = total / count
    print(f"Average temperature: {average:.2f}°C")


def show_loop_demo():
    print("\n--- Loop Demonstration ---")
    print("Using for loop:")
    for number in range(1, 6):
        print(number)

    print("Using while loop:")
    count = 1
    while count <= 5:
        print(count)
        count += 1


def main():
    while True:
        print("\n========== WEEK 1 PYTHON PROJECT ==========")
        print("1. Temperature Converter")
        print("2. Simple Calculator")
        print("3. Average Temperature (Client Project)")
        print("4. For and While Loop Demo")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            calculator()
        elif choice == "3":
            average_temperature()
        elif choice == "4":
            show_loop_demo()
        elif choice == "5":
            print("Thank you for using the Week 1 Python Project!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
