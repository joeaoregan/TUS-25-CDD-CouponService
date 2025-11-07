# A00258304

# winning_numbers = input("Enter the winning lotto numbers: ")
winning_list = [ int(number) for number in input("Enter the winning lotto numbers: ").split()]
# numbers = input("Enter your numbers: ")1
numbers = [ int(number) for number in input("Enter your numbers: ").split()]

# if(winning_numbers == numbers):
#     print("win")

count = 0

# print(winning_list)
# print(numbers)

for i in numbers:
    if i in winning_list:
        count += 1

print(f"You matched {count} numbers")