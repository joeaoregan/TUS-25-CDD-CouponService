# Program to display each character in a string and its index
message = input("Enter a message: ")

for i in range(len(message)):
    print(f"{i=} {message[i]=}")
    