# Password-check using a wordlist (dictionary) file
# Demonstrate file input using for loop
filename = input("Enter the wordlist filename: ")
password = input("Enter the password: ")

# open and read the file
with open(filename) as wordsfile:
    # Search the file line by line for the password
    for word in wordsfile:
        if password == word.strip():
            print("Password is in the wordlist")
            break
    else:
        # Executed if the for-loop completes without a break
        print("Password is not in the wordlist")