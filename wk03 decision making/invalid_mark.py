mark = 101

# Option 1
if mark <= 0 and mark >= 100:
    pass

# Option 2
if mark > 0 or mark > 100:
    pass

# Option 3
if not 0 <= mark <= 100:
    pass


mark = 101

print(0 <= mark <= 100)

print(mark < 0 or mark > 100)

print(mark < 0 and mark > 100) # False