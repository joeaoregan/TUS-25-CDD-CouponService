# keep going until the user is finished
while True:
    # Input fahrenheit temperature
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))

    # Convert to Celsius
    celsius = 5/9 * (fahrenheit - 32)

    # Print Celsius temperature
    print(f"The temperature in Celsius is: {celsius:.1f}")

    # ask the user if they are finished
    response = input("Are you finished (y/n)? ")
    if response.lower() == "y":
        break

print()
print("All temperatures processed")