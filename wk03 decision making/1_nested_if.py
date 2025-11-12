mark = 100

# If mark is valid
if 0 <= mark <= 100:
    if mark >= 70:
        print("First Class Honours")
    elif mark >= 50:
        print("Second Class Honours")
    elif mark >= 40:
        print("Pass")
    else:
        print("No Award")
else:
    print("Invalid Mark")