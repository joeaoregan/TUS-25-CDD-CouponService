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