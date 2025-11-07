# stat the count at zero
count = 0

# Input the required number of values (number of repititions)
num_values = int(input("How many temperature values? "))

# keep going until the count reaches num_values
while count < num_values:
    # Input fahrenheit temperature
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))

    # Convert to Celsius
    celsius = 5/9 * (fahrenheit - 32)

    # Print Celsius temperature
    print(f"The temperature in Celsius is: {celsius:.1f}")

    # increase the count
    count += 1

print()
print("All temperatures processed")