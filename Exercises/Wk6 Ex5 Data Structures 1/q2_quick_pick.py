# “Lotto” is the main national lottery game, where you pick six numbers from 1–47 and try to match the numbers drawn. A Quick Pick is when the lottery system chooses your numbers for you at random, instead of you selecting them yourself.

# Write a program which inputs a single string representing the numbers of a lotto quick pick, separated by spaces, and verifies that it is a valid quick pick, based on the following:

# 1. There are 6 numbers. 
# 2. The minimum number is ≥ 1. 
# 3. The maximum number is ≤ 47. 
# 4. The numbers are unique. Hint: Use len(set(numbers)) == 6
# 5. The numbers are sorted in order. Hint: Use numbers == sorted(numbers)
# To create a list from the string input, you can use a list comprehension, for example:
# numbers_list = [ int(i) for i in values_string.split() ]

# Your program should use decision making (if-else) to determine whether or not the quickpick is valid and then display an appropriate message. You may use nested-ifs or the and conditional operator or a combination.

# For example:
# Test                   | Input                     | Result
# ---------------------- | ------------------------- | -----------------------------------------------------------------
# Valid quickpick        | 4  12  14  16  19  34     | Enter the numbers separated by spaces: 4  12  14  16  19  34
#                        |                           | Valid Quickpick
# ---------------------- | ------------------------- | -----------------------------------------------------------------
# Too few numbers        | 7  25  28  31  33         | Enter the numbers separated by spaces: 7  25  28  31  33
#                        |                           | Not a valid Quickpick
# ---------------------- | ------------------------- | -----------------------------------------------------------------
# Too many numbers       | 1  16  24  28  31  36  38 | Enter the numbers separated by spaces: 1  16  24  28  31  36  38
#                        |                           | Not a valid Quickpick
# ---------------------- | ------------------------- | -----------------------------------------------------------------
# Invalid number 0       | 0  16  17  20  28  45     | Enter the numbers separated by spaces: 0  16  17  20  28  45
#                        |                           | Not a valid Quickpick
# ---------------------- | ------------------------- | -----------------------------------------------------------------
# Invalid number 48      | 8  16  17  20  28  48     | Enter the numbers separated by spaces: 8  16  17  20  28  48
#                        |                           | Not a valid Quickpick
# ---------------------- | ------------------------- | -----------------------------------------------------------------
# Contains a duplicate   | 8  16  17  20  20  47     | Enter the numbers separated by spaces: 8  16  17  20  20  47
#                        |                           | Not a valid Quickpick
# ---------------------- | ------------------------- | -----------------------------------------------------------------
# Contains a duplicate,  | 8  16  17  20  20  32 47  | Enter the numbers separated by spaces: 8  16  17  20  20  32 47
# but 6 distinct numbers |                           | Not a valid Quickpick
# ---------------------- | ------------------------- | -----------------------------------------------------------------
# Not sorted             | 9  27  26  12  11  18     | Enter the numbers separated by spaces: 9  27  26  12  11  18
#                        |                           | Not a valid Quickpick

# A00258304
valid = True

numbers_string = input("Enter the numbers separated by spaces: ")
numbers = [ int(number) for number in numbers_string.split()]

# print(numbers)

# Too few numbers and too many numbers
# if len(set(numbers)) != 6:
#     valid = False

# Invalid numbers
if valid:
    for number in numbers:
        if number < 1 or number > 47:
            valid = False
            break

# Contains a duplicate, but 6 distinct numbers
# if valid:
#     if len(numbers) != len(set(numbers)):
#         valid = False

# Not sorted
# if valid:
# if numbers != sorted(numbers):
#     valid = False

# correct amount of numbers + no duplicates + sorted
if valid and len(set(numbers)) == 6 and len(numbers) == len(set(numbers)) and numbers == sorted(numbers):
    print("Valid Quickpick")
else:
    print("Not a valid Quickpick")