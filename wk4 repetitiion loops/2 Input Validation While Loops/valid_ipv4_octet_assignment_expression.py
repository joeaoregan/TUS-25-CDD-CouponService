# while the value is not valid
while not 0 <= (octet := int(input("Enter the octet: "))) <= 255:
    print("Invalid, try again")

# value is valid
print("Valid octet entered")