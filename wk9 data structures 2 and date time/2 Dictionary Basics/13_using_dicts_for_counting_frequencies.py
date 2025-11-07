# Using Dictionaries for Counting Frequencies


# Using .setdefault(key, default)

numbers = [1, 2, 3, 1, 3, 4, 5, 1, 1, 3, 3, 8, 7, 2, 5]
frequencies = {}

for number in numbers:
    # if the number is not already in the dictionary
    # insert it iwth a value of 0
    frequencies.setdefault(number, 0)
    # and then increase the frequency by 1
    frequencies[number] += 1

print(frequencies)

# Using .get(key, default)

numbers = [1, 2, 3, 1, 3, 4, 5, 1, 1, 3, 3, 8, 7, 2, 5]
frequencies = {}

for number in numbers:
    # get current frequency, or 0 if it's not in the dictionary
    # and then increase the frequency by 1 and update the item
    frequencies[number] = frequencies.get(number, 0) + 1

print(frequencies)