# Check for an invalid IP address octet
octet = int(input("Enter the octet: "))

# while the value is not valid
while not 0 <= octet <= 255:
    print("Invalid, try again")
    octet = int(input("Enter the octet: "))

# value is valid
print("Valid octet entered")