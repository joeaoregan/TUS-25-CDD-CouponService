# Program to convert snake_case to camelCase using a list
snake_name = input("Enter a variable name in snake_case: ")

# splitting a string creates a list of "words"
words = snake_name.split("_")

# capitalise all the other words apart from the first
# for i in range(1, len(words)):
#     words[i] = words[i].capitalize()

# Works because we are building a new list
new_words = [words[0]]
for word in words[1:]:
    new_words.append(word.capitalize())

# joining a list creates a string
# camel_name = "".join(words)
camel_name = "".join(new_words)

print(f"Equivalent variable name in camelCase: {camel_name}")

# Enter a variable name in snake_case: my_long_variable_name
# Equivalent variable name in camelCase: myLongVariableName