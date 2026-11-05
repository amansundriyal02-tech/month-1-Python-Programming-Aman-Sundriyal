"""Basic command-line calculator with input validation."""


def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    raise ValueError("Unsupported operator. Use +, -, *, or /.")


def main():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        print("Result:", calculate(num1, operator, num2))
    except ValueError as error:
        print("Input error:", error)
    except ZeroDivisionError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
