# A00258304

# If firstname contains "Colin", what does the slice firstname[:3]  contain?

# a. "lin"
# b. "Co"
# c. "Col" # Correct. String slice str[:end] starts at index 0 and includes the characters up to, but not including, index end. Think of it as the first 3 characters of the string.
# d. "Coli"

firstname = "Colin"
print(firstname[:3])