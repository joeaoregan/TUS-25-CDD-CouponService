# Write a Python function camel_to_snake(identifier) that converts a string from camelCase to snake_case.
# You may only use string methods and control structures: no lists, lambdas, or other features not yet covered in the Applied Scripting module. 
# You may assume there are no consecutive uppercase characters, e.g. HTTPRequest.
#
# One approach is as follows:
#
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

# Important: CodeRunner will test your function by running it using the test cases below. Just include your function definition, don't include any program code.

# For example:

# Test                                                           | Input                | Result
# -------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------
# Typical camelCase example                                      | camelCaseIdentifier  | camel_to_snake('camelCaseIdentifier')='camel_case_identifier'
# print(f"{camel_to_snake('camelCaseIdentifier')=}")             |                      | 
# -------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------
# Single internal capital                                        | anotherExample       | camel_to_snake('anotherExample')='another_example'
# print(f"{camel_to_snake('anotherExample')=}")                  |                      |
# -------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------
# Already lowercase (no change)                                  | simple               | camel_to_snake('simple')='simple'
# print(f"{camel_to_snake('simple')=}")                          |                      |
# -------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------
# Ends with a capital letter                                     | testCaseX            | camel_to_snake('testCaseX')='test_case_x'
# print(f"{camel_to_snake('testCaseX')=}")                       |                      |
# -------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------
# Long variable name                                             | myVariableNameIsLong | camel_to_snake('myVariableNameIsLong')='my_variable_name_is_long'
# print(f"{camel_to_snake('myVariableNameIsLong')=}")            |                      |
# -------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------
# Single lowercase character                                     | x                    | camel_to_snake('x')='x'
# print(f"{camel_to_snake('x')=}")                               |                      |
# -------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------
# Single uppercase character                                     | X                    | camel_to_snake('X')='x'
# print(f"{camel_to_snake('X')=}")                               |                      |
# -------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------
# Already in snake_case                                          | already_snake_case   | camel_to_snake('already_snake_case')='already_snake_case'
# print(f"{camel_to_snake('already_snake_case')=}")              |                      |

# A00258304

def camel_to_snake(identifier):
    snake_name = ""
    for character in identifier:
        if character.isupper():
            # print(character)
            if snake_name:
                 snake_name += '_'            
            snake_name += character.lower()
        else:
            snake_name += character

    return snake_name

# Test cases:
print(f"{camel_to_snake("camelCaseIdentifier")=}")
print(f"{camel_to_snake("anotherExample")=}")
print(f"{camel_to_snake("simple")=}")
print(f"{camel_to_snake("testCaseX")=}")
print(f"{camel_to_snake("myVariableNameIsLong")=}")
print(f"{camel_to_snake("x")=}")
print(f"{camel_to_snake("X")=}")
print(f"{camel_to_snake("already_snake_case")=}")
