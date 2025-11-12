# Input username and password
username = input("Username: ")
password = input("Password: ")

# keep going until the username and password are both correct
while username != "jbloggs" or password != "Secret123":
    print("Invalid username or password, try again")

    # Input username and password again
    username = input("Username: ")
    password = input("Password: ")
    
print("Login successful")