password = input("Enter password: ")

# initialisse flag variables
lowercase = uppercase = digit = special = False

# check each character in the password
for character in password:
    if character.islower():
        lowercase = True
    elif character.isupper():
        uppercase = True
    elif character.isdigit():
        digit = True
    elif not character.isalnum():
        special = True

# check if all flags are True
if all((lowercase, uppercase, digit, special)):
    print("Valid password")
else:
    print("Invalid password.")
    print("Include upper and lowercase letters, digits and special characters.")
    