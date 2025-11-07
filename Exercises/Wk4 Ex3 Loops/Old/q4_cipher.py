# A00258304

from string import ascii_lowercase

plaintext = input("Enter a message to encipher: ")
ciphertext = ""

for char in plaintext.lower():
    index = ascii_lowercase.find(char)
    if char.isalpha():
        new_index = (index+3) % 26
        ciphertext += ascii_lowercase[new_index]
    else:
        ciphertext += char
print(f"The enciphered message is: {ciphertext}")