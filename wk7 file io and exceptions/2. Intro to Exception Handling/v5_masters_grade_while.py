# Initialise a flag to track valid input
valid_input = False

# Keep going until the user enters valid input
while not valid_input:
    try:
        # Ask the user to enter a mark
        mark = int(input("Enter your overall mark: "))
    except ValueError:
        print("Invalid input: please enter a whole number")
    else:
        # Only run if conversion succeeded
        if 0 <= mark <= 100:
            valid_input = True  # Input is valid, exit loop
        else:
            print("Invalid Mark: must be between 0 and 100")

# Determine the grade after successful input
if mark >= 70:
    print("First Class Honours")
elif mark >= 50:
    print("Second Class Honours")
elif mark >= 40:
    print("Pass")
else:
    print("No Award")