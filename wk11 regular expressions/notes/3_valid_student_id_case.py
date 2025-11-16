# Ignore Case: re.I
# In some siturations, you may want to specify that uppercase and lowercase don't matter.
# e.g., you could consider that both the following are valid as AIT Student IDs:
# A00123456 and a00123456

# Use the "flag" (boolean variable) re.I as a parameter for match and fullmatch to specify that the
# regex should ignore case (so the letter A could also match the lowercase letter a):
# re.fullmatch("A[0-9]{8}", student_id, re.I)

# An alternative approach would be to use brackets to specify the set of characters [aA]:
# re.fullmatch("[aA][0-9]{8}", student_id) 
# This means that the first character can be a lowercase or uppercase letter "a", followed by 8 digits.

# Program 3: Validate AIT Student ID (ignore case)
# Program to check if an AIT Student ID is valid
# Example of Regular Expressions 
import re

# input the username
student_id = input("Enter Student ID: ")

# compare the regex to the string
match = re.fullmatch("A[0-9]{8}", student_id, re.I)
# match = re.fullmatch("[aA][0-9]{8}", student_id) # Alternative

# check if there's a match
if match: # match object not None -> the regex and string match
    print("Valid AIT Student ID")
else:
    print("Not a valid AIT Student ID")

