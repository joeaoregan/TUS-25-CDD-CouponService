# Creating a Dictionary from two iterables

# zip() - pairs elements from teh two iterables in order
# dict() - converts pairs into key-value entries in a dictionary

# Example: Caesar Cipher

from string import ascii_lowercase, ascii_uppercase

cipher_alphabet = ascii_uppercase[3:] + ascii_uppercase[:3]

cipher_dict = dict(zip(ascii_lowercase, cipher_alphabet))

print(cipher_dict)