print("Pick 6 Numbers from 1-47")
print("------------------------")

count = 0 # number of valid numbers picked

# keep going until 6 valid numbers have been picked
while count < 6:
    # Input the number
    print("\nNumber", count + 1)
    number = int(input("Enter a number between 1 and 47: "))

    # While the number is not valid
    while not 1 <= number <= 47:
        print("Invalid number")

        # Input the number again
        number = int(input("Enter a number between 1 and 47: "))

    print("Number is valid")

    count = count + 1 # another valid number picked

print("6 valid numbers")