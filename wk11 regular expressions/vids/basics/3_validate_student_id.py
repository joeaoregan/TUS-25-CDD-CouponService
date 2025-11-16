# Program to validate an AIT Student ID
# Regular Expressio: A[0-9]{8}
import re

# Input the student ID
student_id = input("Enter the Student ID: ")

# compare the regex to the string
match = re.fullmatch("A\d{8}", student_id, re.I) # [0-9]

# check if there was a match
if match:
    print("Valid AIT Student ID")
else:
    print("Not a valid AIT Student ID")