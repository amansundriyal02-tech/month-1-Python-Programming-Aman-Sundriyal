"""Convert temperatures between Celsius and Fahrenheit."""


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose conversion (1/2): ").strip()
    try:
        value = float(input("Enter temperature: "))
        if choice == "1":
            print(f"{value:.2f}°C = {celsius_to_fahrenheit(value):.2f}°F")
        elif choice == "2":
            print(f"{value:.2f}°F = {fahrenheit_to_celsius(value):.2f}°C")
        else:
            print("Invalid choice. Select 1 or 2.")
    except ValueError:
        print("Please enter a valid numeric temperature.")


if __name__ == "__main__":
    main()
