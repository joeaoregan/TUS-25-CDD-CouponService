# A00258304

# The variable period stores a decimal number.
# Which of the following lines of code will display the value of period formatted to three decimal places?

# a. print("The period is {period:.3f} seconds")
# b. print("The period is {period:.3} seconds")
# c. print(f"The period is {period:.3} seconds")
# d. print(f"The period is {period:.3f} seconds") # Correct

period = 30.123456

print("The period is {period:.3f} seconds") # The period is {period:.3f} seconds

print("The period is {period:.3} seconds") # The period is {period:.3} seconds

print(f"The period is {period:.3} seconds") # The period is 30.1 seconds

print(f"The period is {period:.3f} seconds") # The period is 30.123 seconds