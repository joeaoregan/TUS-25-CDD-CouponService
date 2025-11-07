# Input mark
mark = int(input("Enter your overall mark: "))
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
    print("Invalid Mark")

# doesn't handle decimal input