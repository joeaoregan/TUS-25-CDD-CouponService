# Input and convert mark
try:
    mark = int(input("Enter your overall mark: "))
except ValueError:
    print("Invalid input: please enter a whole number")
else:
    # Only run if conversion succeeded
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
        print("Invalid Mark: must be between 0 and 100")