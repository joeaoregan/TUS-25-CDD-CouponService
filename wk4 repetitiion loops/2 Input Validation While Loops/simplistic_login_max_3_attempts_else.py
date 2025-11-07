import sys

count = 0 # number of login attempts

while count < 3: # maximum of 3 attempts
    # Input username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check if they match the correct username and password
    if username == "jbloggs" and password == "Secret123":
        print("Login successful")
        break # exit the loop
    else:
        print("Login failed")
        count += 1
else:
    print("Too many login attempts")
    sys.exit() # terminate the program

print("\nWelcome")