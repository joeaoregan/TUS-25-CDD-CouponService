# Write a program which uses a list to analyse a student's marks.

# The program should:
#   Create an empty list for the marks
#   Repeat while the length of the list is less than 6:
#     Input the mark as an integer
#     If the mark is between 0 and 100, inclusive:
#         Add the mark to the list
#     Otherwise:
#         Display the message "Invalid mark"
#   Display the number of valid marks (the number of values in the list)
#   Display the average mark to the nearest integer
#   Display the highest mark
#   Display the lowest mark

# For example:

# Test	                    | Input | Result
# ------------------------- | ----- | --------------------
# All valid marks           | 67    | Enter the mark: 67
#                           | 80    | Enter the mark: 80
#                           | 59    | Enter the mark: 59
#                           | 75    | Enter the mark: 75
#                           | 78    | Enter the mark: 78
#                           | 90    | Enter the mark: 90
#                           |       | Number of marks: 6
#                           |       | Average mark: 75
#                           |       | Highest mark: 90
#                           |       | Lowest mark: 59
# ------------------------- | ----- | --------------------
# Includes invalid marks    | 87    | Enter the mark: 87
# which will be pointed out | 110   | Enter the mark: 110
#                           | 100   | Invalid mark: 110
#                           | 98    | Enter the mark: 100
#                           | 89    | Enter the mark: 98
#                           | -50   | Enter the mark: 89
#                           | 75    | Enter the mark: -50
#                           | 0     | Invalid mark: -50
#                           |       | Enter the mark: 75
#                           |       | Enter the mark: 0
#                           |       | Number of marks: 6
#                           |       | Average mark: 75
#                           |       | Highest mark: 100
#                           |       | Lowest mark: 0


# A00258304
marks = []
while len(marks) < 6:
    mark = int(input("Enter the mark: "))
    if 0 <= mark <= 100:
        marks.append(mark)
    else:
        print(f"Invalid mark: {mark}")

print(f"Number of marks: {len(marks)}")
print(f"Average mark: {(sum(marks) / len(marks)):.0f}")
print(f"Highest mark: {max(marks)}")
print(f"Lowest mark: {min(marks)}")