"""Calculate the average of user-entered temperature readings."""


def main():
    try:
        count = int(input("Enter number of temperature readings: "))
        if count <= 0:
            print("Please enter at least one reading.")
            return

        readings = []
        for day in range(1, count + 1):
            while True:
                try:
                    readings.append(float(input(f"Enter temperature {day}: ")))
                    break
                except ValueError:
                    print("Please enter a valid number.")

        print(f"Average temperature is {sum(readings) / count:.2f}°C")
    except ValueError:
        print("Please enter a whole number for the number of readings.")


if __name__ == "__main__":
    main()
