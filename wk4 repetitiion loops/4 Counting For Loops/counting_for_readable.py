# keep going until 6 valid numbers have been picked
for i in range(6): # SEQUENCE IS 0, 1, 2, 3, 4, 5
    # Input the number
    print("\nNumber", i+1)
    number = int(input("Enter a number between 1 and 47: "))

    # While the number is not valid
    while not 1 <= number <= 47:
        print("Invalid number")

        # Input the number again
        number = int(input("Enter a number between 1 and 47: "))

    print("Number is valid")

print("6 Valid Numbers")