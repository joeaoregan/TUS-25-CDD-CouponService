# Writing Pythonic Code

# Program to display a greeting
print("Enter your name: ");
name = input();
print("Hello " + name);


# Q1. How many syntax Errors will this generate?
# A. 0 - No syntax errors, python igneores ;

# Q2. How many Pythonic style breaches does it contain?
# A. 


print("Hello",name) # better
print(f"Hello {name}") # Pythonic

# While programs may work they're not Pythonic
name = input("Enter your name: ")
print(f"Hello {name}")