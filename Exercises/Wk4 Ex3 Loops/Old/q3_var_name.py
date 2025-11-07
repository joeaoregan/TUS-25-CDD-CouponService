# A00258304

variable_name = input("Enter the variable name: ")

for char in variable_name:
    if (char.isalnum() or char == "_"):
        continue
    else:   
        print(f"Invalid character {char}")
        break
else:
    print("Valid variable name")