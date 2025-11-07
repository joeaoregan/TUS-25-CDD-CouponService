# Use a for loop when iterating over a sequence (e.g. the characters of a string)

message = "Hello World"

# Pythonic
for char in message:
    print(char)

# Use a for loop when you need a counting loop

# Pythonic
for i in range(10):
    print(i, end=" ")

print()  # for newline

# Use enumerate() when you need each value of a sequence
# along with its index

# Pythonic
for i, char in enumerate(message):
    print(f"{i} {char}")