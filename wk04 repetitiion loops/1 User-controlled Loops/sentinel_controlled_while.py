# keep going until the user is finished
while True:
    # Input fahrenheit temperature
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))

    # check if they are finished
    if fahrenheit == 9999:
        break

    # Convert to Celsius
    celsius = 5/9 * (fahrenheit - 32)

    # Print Celsius temperature
    print(f"The temperature in Celsius is: {celsius:.1f}")

print()
print("All temperatures processed")