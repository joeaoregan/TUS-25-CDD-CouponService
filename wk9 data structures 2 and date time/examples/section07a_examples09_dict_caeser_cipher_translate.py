# Program to encipher using the Caesar Cipher
# Enciphers lowercase plaintext to uppercase ciphertext
# Example using str.maketrans() and str.translate()
from string import ascii_lowercase, ascii_uppercase

# create the cipher alphabet by shifting uppercase letters 3 places to the right
cipher_alphabet = ascii_uppercase[3:] + ascii_uppercase[:3]

# create a translation table: lowercase → shifted uppercase
cipher_table = str.maketrans(ascii_lowercase, cipher_alphabet)

# encipher a plaintext message
plaintext = input("Enter the message to be enciphered: ")
ciphertext = plaintext.lower().translate(cipher_table)
print(f"The enciphered message is {ciphertext}")

