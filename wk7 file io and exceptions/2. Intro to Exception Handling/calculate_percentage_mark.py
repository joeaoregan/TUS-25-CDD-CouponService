# Initialise a flag to track valid input
valid_input = False

# keep going until the user enters valid input
while not valid_input:
    try:
        # Input total marks and marks obtained
        total_marks = int(input("Enter the total marks: "))
        obtained_marks = int(input("Enter the marks obtained: "))
        percentage = (obtained_marks / total_marks) * 100
    except ValueError: # int() conversion failed
        print("Invalid input: please enter whole numbers only. Try again.")
    except ZeroDivisionError: # total_marks is zero
        print("Invalid input: total marks cannot be zero. Try again.")
    except Exception as e:
        print(f"An unexpected error occured: {e}. Try again.")
    else:
        # Only proceeds if input is valid
        valid_input = True

# Calculate and display percentage
# percentage = (obtained_marks / total_marks) * 100 # Moved to try block to check for ZeroDivisionError
print(f"You percentage mark is: {percentage:.2f}%")