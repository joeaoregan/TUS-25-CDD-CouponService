# Example: Regex for a filename
# Write a program to validate a filename in the form name.extension, e.g. test.txt
# which contains only letters, numbers, the hyphen – and the underscore _
# The regex is: ^\w+\.\w+$

# The quantifier + means 1 or more (at least 1).  
# The character class \w # represents a “word” character, 
# that is, one of a-zA-Z0-9–_

# Program 5: Validate a filename

# Program to validate a filename
# Example of regular expressions with an escaped meta-character \.
import re

# keep going until the user wants to stop
while True:
    filename = input("Enter a filename or q to quit: ")

    if filename == "q":
        break # break from the loop

    # apply the regular expression
    match = re.fullmatch(r"\w+.\w+", filename) # raw string regex

    # check if it matches
    if match:
        print("Valid filename")
    else:
        print("Not a valid filename")