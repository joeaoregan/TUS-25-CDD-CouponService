# Program to convert snake_case to camelCase using a list
snake_name = input("Enter a variable name in snake_case: ")

# splitting a string creates a list of "words"
words = snake_name.split("_")

# List comprehension
camel_name = words[0] + "".join([word.capitalize() for word in words[1:]])

print(f"Equivalent variable name in camelCase: {camel_name}")

# Enter a variable name in snake_case: my_long_variable_name
# Equivalent variable name in camelCase: myLongVariableName