# A00258304
# Define a function is_valid_username(name) that returns True only if all these are true:
# * It is at least 5 characters long
# * It contains only letters and digits (no spaces or punctuation)
# * It does not start with a digit

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
        
print(f"{is_valid_username(name)=}")
