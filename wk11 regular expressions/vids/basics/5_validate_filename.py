# Program to validate a filename
# Regular Expression: \w+\.\w+     \w means [0-9a-zA-z-]
# \w+\.\w{3} - 3 character extension, \w+\.\w{1,3}
# + means 1 or more
import re

# input the username
filename = input("Enter the filename: ")

# match = re.fullmatch("\w+\.\w+", filename) # <any number of characters>.<any number of characters>
match = re.fullmatch("\w+\.\w{1,3}", filename) # <any number of characters>.<between 1 and 3 characters>
# match = re.fullmatch("\w+.\w+", filename) # Not correct: <one or more characters><any character><one or more characters>


# check if they match
if match:
    print("Valid filename")
else:
    print("Not a valid filename")

# test
# test&trace.py # invalid
# test_trace.py # valid
# test-trace.py # valid
# MySpecialFile101.txt