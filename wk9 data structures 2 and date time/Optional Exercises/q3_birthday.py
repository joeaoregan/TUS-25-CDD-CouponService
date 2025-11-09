# A00258304

# Write a program which uses a dictionary and the datetime module to store people’s birthdays.

# The program should allow the user to:
# * Input a person’s date of birth and name
# * Determine their next birthday
# * Insert birthday and name into dictionary
# * Display the birthdays, in date order

# The dictionary keys should be a date object, the dictionary values should be a list of names.

# For example:

# Input	       | Result
# ------------ | -------------------------------------
# a            | [S]how [A]dd [Q]uit: a
# Bart         | Enter the person's name: Bart
# 1/1/1980     | Enter their date of birth: 1/1/1980
# a            |
# Homer        | [S]how [A]dd [Q]uit: a
# 12/5/1951    | Enter the person's name: Homer
# a            | Enter their date of birth: 12/5/1951
# Bruce Lee    |
# 27/11/1940   | [S]how [A]dd [Q]uit: a
# a            | Enter the person's name: Bruce Lee
# Jimi Hendrix | Enter their date of birth: 27/11/1940
# 27/11/1942   |
# a            | [S]how [A]dd [Q]uit: a
# Lisa         | Enter the person's name: Jimi Hendrix
# 9/5/1982     | Enter their date of birth: 27/11/1942
# a            |
# Marge        | [S]how [A]dd [Q]uit: a
# 19/3/1953    | Enter the person's name: Lisa
# q            | Enter their date of birth: 9/5/1982
#              |
#              | [S]how [A]dd [Q]uit: a
#              | Enter the person's name: Marge
#              | Enter their date of birth: 19/3/1953
#              |
#              | [S]how [A]dd [Q]uit: q


import datetime

birthdays = {}

while True:
    choice = input("[S]how [A]dd [Q]uit: ")

    if choice.lower() == "q":
        break

    if choice.lower() == "a":
        name = input("Enter the person's name: ")
        # dob = datetime.date.fromisoformat(input("Enter their date of birth: "))
        # dob = datetime.datetime.strptime(input("Enter their date of birth: "), "%d/%m/%Y").date()
        dob = input("Enter their date of birth: ")
        # print(dob)
        # print(dob.strftime("%d/%m/%Y"))
        birthdays[dob] = name
        # break

print(birthdays)
