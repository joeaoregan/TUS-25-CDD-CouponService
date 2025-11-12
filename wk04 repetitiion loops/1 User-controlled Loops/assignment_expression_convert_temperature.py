# keep going until the user is finished
while (fahrenheit := float(input("Enter the Fahrenheit temperature or 9999 to finish: "))) != 9999:
    # Convert to Celsius
    celsius = 5/9 * (fahrenheit - 32)

    # Print Celsius temperature
    print(f"The temperature in Celsius is: {celsius:.1f}")