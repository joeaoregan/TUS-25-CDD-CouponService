mark = 100

# If mark is invalid
if not 0 <= mark <= 100: # pythonic
    print("Invalid Mark")
elif mark >= 70:
    print("First Class Honours")
elif mark >= 50:
    print("Second Class Honours")
elif mark >= 40:
    print("Pass")
else:
    print("No Award")