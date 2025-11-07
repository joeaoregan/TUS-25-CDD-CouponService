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