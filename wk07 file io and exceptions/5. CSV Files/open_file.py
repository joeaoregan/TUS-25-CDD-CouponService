with open("comedy.txt") as users_file:
    print(f"{'Name':20} {'Username'}")
    for line in users_file:
        # split the name into first name and last name
        fullname = line.strip() # strip the newline character
        firstname, lastname = fullname.split()

        # generate the username
        username = (firstname[0] + lastname).lower()
        # print with aligned columns
        print(f"{fullname:20} {username}")