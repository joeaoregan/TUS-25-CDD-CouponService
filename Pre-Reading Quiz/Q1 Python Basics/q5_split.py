# A00258304

# The variable fullname contains a person’s firstname and lastname, e.g. "Joe Bloggs"
# What does the variable lastname contain after the following statement is executed:
# firstname, lastname = fullname.split()

# a. An empty string
# b. "Bloggs" # Correct
# c. "Joe Bloggs"
# d. "Joe"

fullname = "Joe Bloggs"
firstname, lastname = fullname.split()
print(lastname)
print(type(lastname))