# Write a program which checks how many of the 6 winning Lotto numbers a player has matched.

# The program should:
# Input the winning numbers as a single string, separated by spaces
# Create a list containing the individual winning numbers, using winning_list = winning_numbers.split()
# Input the player's numbers as a single string, separated by spaces
# Create a list containing the player's numbers (in the same way as the second step, above)
# Initialise a variable count to zero; this will count how many numbers have been matched
# For each of the player's numbers
#     If the player's number is in the winning numbers list:
#         Increase count by 1
# Display how many numbers the player matched

# For example:

# Test              | Input            | Result
# ----------------- | ---------------- | --------------------------------------------------
# Jackpot winner    | 6 12 22 27 42 46 | Enter the winning lotto numbers: 6 12 22 27 42 46
# - matched all 6   | 6 12 22 27 42 46 | Enter your numbers: 6 12 22 27 42 46
#                   |                  | You matched 6 numbers
# ----------------- | ---------------- | --------------------------------------------------
# Matched none      | 6 12 22 27 42 46 | Enter the winning lotto numbers: 6 12 22 27 42 46
#                   | 1 4 17 8 9 23    | Enter your numbers: 1 4 17 8 9 23
#                   |                  | You matched 0 numbers
# ----------------- | ---------------- | --------------------------------------------------
# Matched 2 numbers | 6 12 22 27 42 46 | Enter the winning lotto numbers: 6 12 22 27 42 46
#                   | 5 13 17 6 18 42  | Enter your numbers: 5 13 17 6 18 42
#                   |                  | You matched 2 numbers


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