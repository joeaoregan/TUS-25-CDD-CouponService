from string import ascii_lowercase # abc...xyz

# Input a message
plaintext = input("Enter the message to be enciphered: ")

ciphertext = "" # start with an empty string

# for each character in the plaintext, converted to lowercase
for character in plaintext.lower():
    # if the character is not a letter, skip it
    if not character.isalpha():
        continue # skips this character - goes to for statement

    else:
        # get position of the letter in the alphabet
        index = ascii_lowercase.index(character)

        # add the index and a space onto the ciphertext
        ciphertext += str(index) + " "

print("The ciphertext is:", ciphertext)