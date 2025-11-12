# Dictionary Comprehensions
# Create a dictionary in a single expression

# { key_expression: value_expression for itmem in iterable if condition }

# key_expression determines the dictionary key
# value_expression determines the corresponding value
# iterable is any iterable to loop over (e.g. string, list, tuple)
# if condition is an optional filter to include only certain items

squares_dict = { i:i**2 for i in range(1,6) }
print(squares_dict) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

