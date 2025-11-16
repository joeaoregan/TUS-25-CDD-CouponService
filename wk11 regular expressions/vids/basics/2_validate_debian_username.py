# Program to validate a Debian Username
# Regular Expression: ^[a-x][-a-z0-9_]*$
import re

#input the username
username = input("Enter the username: ")

# apply the regex to the username string
# match = re.fullmatch("[a-z][-a-z0-9_]*", username)
# match = re.fullmatch("[a-z][-a-z0-9_]{3}", username) # must start with lowercase letter, minimum of 4 characters
# match = re.fullmatch("[a-z][-a-z0-9_]{3,7}", username) # must start with lowercase letter, between 4 and 8 characters ({3,7} + start letter)
match = re.fullmatch("[a-z][-a-z0-9_]{3,}", username) # must start with lowercase letter, 4 or more characters

# check if they match
if match:
    print("Valid username")
else:
    print("Not a valid username")
