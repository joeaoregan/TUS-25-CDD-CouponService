# A00258304

# The Polybius Square Cipher is a substitution cipher that replaces each letter of a plaintext 
# message with a pair of coordinates from a 5×5 grid; I and J are enciphered identically:

# a) Write a Python function create_polybius_square() which returns a dictionary representing the 
# Polybius Square where each key is a letter of the uppercase alphabet and the corresponding value 
# is a two-digit code string representing the row and column numbers corresponding to the letter, as follows:
# * Create a string representing the letters of the uppercase alphabet, without the letter J
# * Create an empty dictionary representing the Polybius Square
# * Initialise an integer index i to zero (this gives access to the letters of the alphabet, without J)
# * For each row from 1 to 6
#   - For each column from 1 to 6
#       * Insert into the dictionary the upper case letter at index i with a two-digit code string representing the 
#         row and column numbers as the corresponding value using polybius_square[alphabet[index]] = f"{row}{col}"
#       * Increase the index i by 1
# * Return the dictionary

# Excerpt of the dictionary:

# b) Write a Python function which takes two parameters, a string representing the plaintext message to be enciphered 
# and a dictionary representing the Polybius Square, and enciphers and returns the ciphertext created by replacing 
# each letter of the plaintext with the corresponding two-digit string from the Polybius Square, as follows:    
#   * Set the ciphertext to an empty string
#   * Convert the plaintext to uppercase
#   * For each character in the plaintext
#       - If the character is a key in the Polybius Square
#           * Get the corresponding 2-digit string from the Polybius Square and add it and a string to the ciphertext
#       - Otherwise if the character is "J" then get the 2-digit string for "I" from the Polybius Square and add it and a string to the ciphertext
#   * Return the ciphertext

# c) Write a Python function which takes two parameters, a string representing the ciphertext message to be deciphered 
# and a dictionary representing the Polybius Square, and deciphers and returns the plaintext created by replacing each 
# two-digit string of the ciphertext with the corresponding letter string from the Polybius Square. 
# One approach is as follows:

# * Use a dictionary comprehension to create a reverse Polybius Square, i.e.
#   reverse_polybius_square = {v: k for k, v in polybius_square.items()}
# * Set the plaintext to an empty string
# * For each 2-digit code in the ciphertext, separated by spaces
#   - If the code is in the reverse_polybius_square
#       * Get the corresponding letter from the reverse_polybius_square and add it to the plaintext
# * Return the plaintext


# a.
def create_polybius_square():
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    polybius_square = {}
    index = 0

    for row in range(1, 6):
        for col in range(1, 6):
            polybius_square[alphabet[index]] = f"{row}{col}"
            index += 1

    # print(polybius_square)
    return polybius_square

# print(create_polybius_square())

# b.
def encipher_message(plaintext, dict):
    ciphertext = ""
    plaintext = plaintext.upper()
    # print(plaintext)
    for char in plaintext:
        if char in dict.keys():
            ciphertext += dict[char] + " "
        elif char == "J":
            ciphertext += dict["I"] + " "
    return ciphertext.strip() # remove final space


# encipher_message("hello world", {})

# print(encipher_message("testing123", create_polybius_square())) # 44 15 43 44 24 33 22


# c.
def decipher_message(ciphertext, polybius_square):
    reverse_polybius_square = {v: k for k, v in polybius_square.items()}
    plaintext = ""
    for code in ciphertext.split():
        if code in reverse_polybius_square:
            plaintext += reverse_polybius_square[code]
    return plaintext