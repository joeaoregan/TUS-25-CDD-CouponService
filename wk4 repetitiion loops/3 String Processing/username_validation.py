# Example of a for loop to process the characters of a string
username = input("Enter username: ")

# Check if the username conatins Admin
if "Admin" in username:
    print("Invalid: username must not contain Admin")
# Check if username is too long
elif len(username) > 15:
    print("Invalid: exceeds 15 characters")
# Check if it contains an invalid character
else:
    # process each character, one at a time
    for char in username:
        # if the character is invalid
        if not char.isalpha() and not char.isdigit() and char != "_":
            print("Invalid character: ", char)
            break # exit loop
    # reached end of username
    else:
        print(username, "is valid")