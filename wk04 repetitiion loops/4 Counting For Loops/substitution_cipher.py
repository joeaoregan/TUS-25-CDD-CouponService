from string import ascii_lowercase # abcdef...xyz

# Input a message
plaintext = input("Enter the message to be enciphered: ")

print(len(plaintext))

ciphertext = "" # start with an empty string

# for each character in the plaintext, converted to lowercase
for character in plaintext.lower():
    # if the character is not a letter, skip it
    if character.isalpha():
        # get position of the letter in the alphabet
        index = ascii_lowercase.index(character)

        # add the index and a space onto the ciphertext
        ciphertext += str(index) + " "

print("The ciphertext is:", ciphertext)