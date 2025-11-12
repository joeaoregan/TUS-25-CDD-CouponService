# Dictionary Comprehensions: Frequencies
# Count frequencies of unique list items
numbers = [1, 2, 3, 1, 2, 1, 4, 3, 1, 2, 5]
frequencies = {num: numbers.count(num) for num in set(numbers)}
print(frequencies)

# set(numbers) returns unique numbers in the list:
numbers = [6,3,9,6,6,5,9,3]
print(set(numbers)) # {9, 3, 5, 6}

# frequencies
# keys are the numbers
# values are the frequencies

numbers = [6,3,9,6,6,5,9,3]
frequencies = {num: numbers.count(num) for num in set(numbers)}
print(frequencies)