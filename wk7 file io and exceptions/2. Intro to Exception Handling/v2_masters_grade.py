# Version 2: Look Before You Leap
# Input a mark as a string, check that the string contains digits

# Input mark (as a string)
mark = input("Enter your overall mark: ")

# check if the input value consists only of digits
# this implies that the mark is a non-negative integer
if mark.isdigit():
    mark = int(mark) # convert input to int
    # Check if mark is valid
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
else:
    print("Invalid input: please enter a whole number")
