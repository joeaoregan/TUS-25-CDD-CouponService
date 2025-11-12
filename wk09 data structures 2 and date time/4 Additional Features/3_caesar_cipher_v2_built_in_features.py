from string import ascii_lowercase, ascii_uppercase

# create the cipher alphabet by shifting each letter 3 places to the right
cipher_alphabet = ascii_uppercase[3:] + ascii_uppercase[:3]

# create a translation table: lowercase - shifted uppercase
cipher_table = str.maketrans(ascii_lowercase, cipher_alphabet) # Makes a translation table, represents letters as pairs of unicode values
# str.maketrans() creates a translation tables (Unicode values)
# cipher_table dict 26 {97:68, 98:69, 99:0,...}

# encipher a plaintext message
plaintext = input("Enter the message to be enciphered: ") # Hello World
ciphertext = plaintext.lower().translate(cipher_table)
# str.translate() replaces characters in input text with corresponding value
print(f"The enciphered message is {ciphertext}")


