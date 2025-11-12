# Using Dictionaries for Counting Frequencies

# keys: things being counted
# values: the frequencies (counts)

# Create and empty dictionary for the frequencies
# For each item in the dataset
#   if this is a new item, Set the frequency to 1
#   Otherwise increase the frequency by 1

# Basic Version

numbers = [1, 2, 3, 1, 3, 4, 5, 1, 1, 3, 3, 8, 7, 2, 5]
frequencies = {}

for number in numbers:
    if number not in frequencies: # new number
        frequencies[number] = 1 # insert it with frequency of 1 for new items
    else:
        frequencies[number] += 1 # increase frequency by 1 if it exists already

print(numbers)
print(frequencies)