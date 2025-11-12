# Program to encipher using the Caesar Cipher
# Example of using zip() and dict() to create a dictionary
from string import ascii_lowercase, ascii_uppercase

# create the cipher alphabet by shifting each letter 3 places to the right
cipher_alphabet = ascii_uppercase[3:] + ascii_uppercase[:3] # DEFGHIJKLMNOPQRSTUVWXYZABC
# print(cipher_alphabet)

# dictionary created using zip() and dict()
cipher_dict = dict(zip(ascii_lowercase, cipher_alphabet)) # {'a': 'D', 'b': 'E', 'c': 'F', 'd': 'G', 'e': 'H', 'f': 'I', 'g': 'J', 'h': 'K', 'i': 'L', 'j': 'M', 'k': 'N', 'l': 'O', 'm': 'P', 'n': 'Q', 'o': 'R', 'p': 'S', 'q': 'T', 'r': 'U', 's': 'V', 't': 'W', 'u': 'X', 'v': 'Y', 'w': 'Z', 'x': 'A', 'y': 'B', 'z': 'C'}
# print(cipher_dict)

# encipher a plaintext message
plaintext = input("Enter the message to be enciphered: ") # Hello World
ciphertext = ""
for char in plaintext.lower(): # convert to lowercase here, leave original message as it was
    if char.isalpha():
        ciphertext += cipher_dict[char]
    else:
        ciphertext += char
print(f"The enciphered message is {ciphertext}") # The enciphered message is KHOOR ZRUOG