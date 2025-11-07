# keep going until the loop has been repeated 6 times
for i in range(6):
    # Input fahrenheit temperature
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))

    # Convert to Celsius
    celsius = 5/9 * (fahrenheit - 32)

    # Print Celsius temperature
    print(f"The temperature in Celsius is: {celsius:.1f}")  
