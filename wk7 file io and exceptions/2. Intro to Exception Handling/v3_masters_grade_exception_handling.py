# Version 2: Use Exception Handling
# Try to convert the input to an int, deal with the exceptions

try:    
    # Input mark
    mark = input("Enter your overall mark: ")

    # check if the mark is within the valid range
    if 0 <= mark <= 100:
        # determine the grade
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

except ValueError:
    # Handle non-integer input
    print("Invalid input: please enter a whole number")
