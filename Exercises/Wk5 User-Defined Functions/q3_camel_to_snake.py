# A00258304
# Write a Python function camel_to_snake(identifier) that converts a string from camelCase to snake_case.
# You may only use string methods and control structures: no lists, lambdas, or other features not yet covered in the Applied Scripting module. 
# You may assume there are no consecutive uppercase characters, e.g. HTTPRequest.
#
# One approach is as follows:
# Set snake_name to an empty string
# For each character in the identifier
#    If character is uppercase
#        If snake_name is not empty
#            Add an underscore to snake_name
#        Otherwise
#            Add lowercase version of character to snake_name
#    Otherwise
#        Add character to snake_name
# Return snake_name

def camel_to_snake(identifier):
    snake_name = ""
    for character in identifier:
        if character.isupper():
            print(character)
            if snake_name:
                 snake_name += '_'            
            snake_name += character.lower()
        else:
            snake_name += character

    return snake_name

print(camel_to_snake("testCase"))

        
