# Program to encipher using the Caesar Cipher
# Example of using zip() and dict() to create a dictionary
from string import ascii_lowercase, ascii_uppercase

# create the cipher alphabet by shifting each letter 3 places to the right
cipher_alphabet = ascii_uppercase[3:] + ascii_uppercase[:3]

# dictionary created using zip() and dict()
cipher_dict = dict(zip(ascii_lowercase,cipher_alphabet))

# encipher a plaintext message
plaintext = input("Enter the message to be enciphered: ")
ciphertext = ""
for char in plaintext.lower():
    if char.isalpha():
        ciphertext += cipher_dict[char]
    else:
        ciphertext += char
print(f"The enciphered message is {ciphertext}")


