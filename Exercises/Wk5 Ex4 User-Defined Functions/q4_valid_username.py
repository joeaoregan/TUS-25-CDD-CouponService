# Define a function is_valid_username(name) that returns True only if all these are true:
# * It is at least 5 characters long
# * It contains only letters and digits (no spaces or punctuation)
# * It does not start with a digit

# Then write a program which uses a while loop to repeatedly prompt the user for a username until they provide a valid one.

# Important: For this question you need to include your function definition and your program code.

# For example:

# Test	                                              | Input      | Result
# --------------------------------------------------- | ---------- | --------------------------------------
# Test function: valid, all lowercase, exactly length | aoife      | Enter a username: aoife
# print(f"{is_valid_username('aoife')=}")             |            | Username accepted
#                                                     |            | is_valid_username('aoife')=True
# --------------------------------------------------- | ---------- | --------------------------------------
# Test function: valid, mixed case                    | FearghaL   | Enter a username: FearghaL
# print(f"{is_valid_username('FearghaL')=}")          |            | Username accepted
#                                                     |            | is_valid_username('FearghaL')=True
# --------------------------------------------------- | ---------- | --------------------------------------
# Test function: valid, mixed case, and digits        | LAo1se     | Enter a username: LAo1se
# print(f"{is_valid_username('LAo1se')=}")            |            | Username accepted
#                                                     |            | is_valid_username('LAo1se')=True
# --------------------------------------------------- | ---------- | --------------------------------------
# Test function: invalid, too short                   | conn       | Enter a username: conn
# print(f"{is_valid_username('conn')=}")              | root1      | Invalid username, try again
#                                                     |            | Enter a username: root1
#                                                     |            | Username accepted
#                                                     |            | is_valid_username('conn')=False
# --------------------------------------------------- | ---------- | --------------------------------------
# Test function: invalid, starts with digit           | 8conn      | Enter a username: 8conn
# print(f"{is_valid_username('8conn')=}")             | root1      | Invalid username, try again
#                                                     |            | Enter a username: root1
#                                                     |            | Username accepted
#                                                     |            | is_valid_username('8conn')=False
# --------------------------------------------------- | ---------- | --------------------------------------
# Right first time, mix of letters and digits         | deepak123  | Enter a username: deepak123
#                                                     |            | Username accepted
# --------------------------------------------------- | ---------- | --------------------------------------
# Test function: invalid, contains non-alphanumeric   | jo_bloggs  | Enter a username: jo_bloggs
# print(f"{is_valid_username('jo_bloggs')=}")         | root1      | Invalid username, try again
#                                                     |            | Enter a username: root1
#                                                     |            | Username accepted
#                                                     |            | is_valid_username('jo_bloggs')=False
# --------------------------------------------------- | ---------- | --------------------------------------
# Test function: invalid, contains non-alphanumeric   | jo.bloggs  | Enter a username: jo.bloggs
# print(f"{is_valid_username('jo.bloggs')=}")         | root1      | Invalid username, try again
#                                                     |            | Enter a username: root1
#                                                     |            | Username accepted
#                                                     |            | is_valid_username('jo.bloggs')=False
# --------------------------------------------------- | ---------- | --------------------------------------
# Right first time, exact min length, all lowercase   | aoife      | Enter a username: aoife
#                                                     |            | Username accepted
# --------------------------------------------------- | ---------- | --------------------------------------
# Test function: invalid, contains non-alphanumeric   | $jo_bloggs | Enter a username: $jo_bloggs
# print(f"{is_valid_username('$jo_bloggs')=}")        | root1      | Invalid username, try again
#                                                     |            | Enter a username: root1
#                                                     |            | Username accepted
#                                                     |            | is_valid_username('$jo_bloggs')=False
# --------------------------------------------------- | ---------- | --------------------------------------
# Repeatedly incorrect, then correct                  | 12bob      | Enter a username: 12bob 
#                                                     | b@b!       | Invalid username, try again
#                                                     | bob        | Enter a username: b@b!
#                                                     | bobby2     | Invalid username, try again
#                                                     |            | Enter a username: bob
#                                                     |            | Invalid username, try again
#                                                     |            | Enter a username: bobby2
#                                                     |            | Username accepted


# A00258304

def is_valid_username(name):
    return len(name) >= 5 and name.isalnum() and name[0].isalpha()


# print(is_valid_username("Joe")) # False - length
# print(is_valid_username("JoeOR")) # True
# print(is_valid_username("1oeOR")) # False - first character is a digit
# print(is_valid_username("Joe OR")) # False - space
# print(is_valid_username("Joe,OR")) # False - ,

name = ""
while True:
    name = input("Enter a username: ")
    if is_valid_username(name):
        print("Username accepted")
        break
    else:
        print("Invalid username, try again")
        
# print(f"{is_valid_username(name)=}")
