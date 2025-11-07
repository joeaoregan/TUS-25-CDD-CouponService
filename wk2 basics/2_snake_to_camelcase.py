# Program to convert snake_case to camelCase
snake_name = input("Enter a name in snake_case: ")

# 1. Replace the underscore with a space
camelName = snake_name.replace("_", " ")

# 2. Capitalise the individual "words"
# camelName.capitalize() # Only changes first letter of first word
camelName = camelName.title()

# 3. Remove the space
camelName = camelName.replace(" ", "")

# 4. Change the first letter to lowercase
# camelName[0] = camelName[0].lower() # cannot reassign using an index
camelName = camelName[0].lower() + camelName[1:]
print(f"The equivalent name in camelCase is: {camelName}")


