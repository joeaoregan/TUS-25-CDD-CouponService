with open("comedy2.txt") as users_file:
    print(f"{'Name':20} {'Username'}")
    for line in users_file:
        # split the name into first name and last name
        fullname = line.strip() # strip the newline character
        try:
            firstname, lastname = fullname.split()
        except ValueError:
            print(f"Skipping line (unexpected format): {line.strip()}")
            continue # skip to the next line of the file

        # generate the username
        username = (firstname[0] + lastname).lower()
        # print with aligned columns
        print(f"{fullname:20} {username}")