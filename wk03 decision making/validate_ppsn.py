# Program to validate a (simplified) PPSN

# Input ppsn
# ppsn = input("Enter your PPSN: ")
ppsn = "1234567A"

# chick if its valid
# If ppsn has length 8 and the first 7 characters are digits and the last character is a letter
if len(ppsn) == 8 and ppsn[:7].isdigit() and ppsn[-1].isalpha():
    print("Valid PPSN")
else:
    print("Invalid PPSN")