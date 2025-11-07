# Write a program which inputs a text string and uses one of the following algorithms to calculate and display the frequencies of each letter, 
# and the most frequent letter. You'll find it useful to import ascii_lowercase from the string module.

# Important: You must use either a list or a set to implement the algorithm. You may not use a dictionary or any other data structure 
# (apart from a list or set). If you use a dictionary or any other data structure (apart from a list or set) in your solution, 
# your program will be manually awarded zero marks.

# Version 1: Count each letter of the Alphabet
# Input the text and convert to lowercase
# Create an empty list for the frequencies
# For each letter of the alphabet
#     Count the frequency of the letter in the text and add it to the frequencies
# Display the letters and their frequencies
# Determine and display the most frequent letter

# Version 2: Process each letter of the text
# Input the text and convert to lowercase
# Create a list of the frequencies of the 26 letters, initialised to zero
# For each character in the text
#     If the character is a letter
#         Find the index of the letter in the alphabet (use ascii_lowercase.index(character))
#         Increase by 1 the value of the corresponding element in the frequencies list
# Display the letters and their frequencies
# Determine and display the most frequent letter

# Version 3: Process each unique letter of the text
# Input the text and convert to lowercase
# Create a list of the frequencies of the 26 letters
# Use a set to get the unique characters in the text (use set(text))
# For each character in the set
#     If the character is a letter
#         Find the index of the letter in the alphabet (use ascii_lowercase.index(character))         
#         Count the number of times this letter appears in the text (use text.count(character))         
#         Store the count in the corresponding element of the frequencies list
# Display the letters and their frequencies
# Determine and display the most frequent letter

# Note: The following code was used to tabulate the results:

# print("\nLetter Frequency")
# for letter,frequency in zip(ascii_lowercase,frequencies):
#     print(f"{letter:^5}{frequency:^9}")

# For example:

# Test               | Input                          | Result
# ------------------ | ------------------------------ | --------------------------------------------------------------------------
# Groucho Marx       | I refuse to join any club that | Enter the text: I refuse to join any club that would have me as a member.
#                    | would have me as a member.     |
#                    |                                | Letter Frequency
#                    |                                |   a       5
#                    |                                |   b       2
#                    |                                |   c       1
#                    |                                |   d       1
#                    |                                |   e       6
#                    |                                |   f       1
#                    |                                |   g       0
#                    |                                |   h       2
#                    |                                |   i       2
#                    |                                |   j       1
#                    |                                |   k       0
#                    |                                |   l       2
#                    |                                |   m       3
#                    |                                |   n       2
#                    |                                |   o       3
#                    |                                |   p       0
#                    |                                |   q       0
#                    |                                |   r       2
#                    |                                |   s       2
#                    |                                |   t       3
#                    |                                |   u       3
#                    |                                |   v       1
#                    |                                |   w       1
#                    |                                |   x       0
#                    |                                |   y       1
#                    |                                |   z       0
#                    |                                |
#                    |                                | Most frequent letter: e
# ------------------ | ------------------------------ | --------------------------------------------------------------------------
# Pangram 1:         | The quick brown fox jumps      | Enter the text: The quick brown fox jumps over the lazy dog.
# Quick brown fox    | over the lazy dog.             |
#                    |                                | Letter Frequency
#                    |                                |   a       1
#                    |                                |   b       1
#                    |                                |   c       1
#                    |                                |   d       1
#                    |                                |   e       3
#                    |                                |   f       1
#                    |                                |   g       1
#                    |                                |   h       2
#                    |                                |   i       1
#                    |                                |   j       1
#                    |                                |   k       1
#                    |                                |   l       1
#                    |                                |   m       1
#                    |                                |   n       1
#                    |                                |   o       4
#                    |                                |   p       1
#                    |                                |   q       1
#                    |                                |   r       2
#                    |                                |   s       1
#                    |                                |   t       2
#                    |                                |   u       2
#                    |                                |   v       1
#                    |                                |   w       1
#                    |                                |   x       1
#                    |                                |   y       1
#                    |                                |   z       1
#                    |                                |
#                    |                                | Most frequent letter: o
# ------------------ | ------------------------------ | --------------------------------------------------------------------------
# Pangram 2:         | Five hexing wizard             | Enter the text: Five hexing wizard bots jump quickly.
# Hexing wizard bots | bots jump quickly.             |
#                    |                                | Letter Frequency
#                    |                                |    a       1
#                    |                                |    b       1
#                    |                                |    c       1
#                    |                                |    d       1
#                    |                                |    e       2
#                    |                                |    f       1
#                    |                                |    g       1
#                    |                                |    h       1
#                    |                                |    i       4
#                    |                                |    j       1
#                    |                                |    k       1
#                    |                                |    l       1
#                    |                                |    m       1
#                    |                                |    n       1
#                    |                                |    o       1
#                    |                                |    p       1
#                    |                                |    q       1
#                    |                                |    r       1
#                    |                                |    s       1
#                    |                                |    t       1
#                    |                                |    u       2
#                    |                                |    v       1
#                    |                                |    w       1
#                    |                                |    x       1
#                    |                                |    y       1
#                    |                                |    z       1
#                    |                                |
#                    |                                | Most frequent letter: i


# A00258304

# from string import ascii_lowercase

# frequencies = []

# # text = input("Enter the text: ")
# text = "I refuse to join any club that would have me as a member."

# for letter in ascii_lowercase:    
#     # frequencies.append([letter, text.count(letter)])
#     frequencies.append(text.count(letter))

# # text = "abababa"

# # counter = text.count("a")
# # print(counter)

# print("Letter Frequency")
# # for i in frequencies:
#     # print(f"   {i[0]}       {i[1]}")
# for i, letter in enumerate(ascii_lowercase):
#     print(f"   {letter}       {frequencies[i]}")

# print()
# print(f"Most frequent letter: {ascii_lowercase[frequencies.index(max(frequencies))]}")




# A00258304

from string import ascii_lowercase

frequencies = []

text = input("Enter the text: ").lower()

# Version 1: Count each letter of the Alphabet
# for letter in ascii_lowercase:
#     frequencies.append(text.count(letter))
    
# print("\nLetter Frequency")
# for i, letter in enumerate(ascii_lowercase):
#     print(f"   {letter}       {frequencies[i]}")

# Version 2: Process each letter of the text
frequencies = [0] * 26
# print(frequencies)
# for i, letter in enumerate(text):
# for letter in text:
#     if letter.isalpha():
#         frequencies[ascii_lowercase.find(letter)] += 1
#     else:
#         continue
    
# Version 3: Process each unique letter of the text
# unique_characters = set(text)
# for character in unique_characters:
for character in set(text):
    if character.isalpha():
        index = ascii_lowercase.index(character)
        count = text.count(character)
        frequencies[index] = count

print("\nLetter Frequency")
for letter,frequency in zip(ascii_lowercase,frequencies):
    print(f"{letter:^5}{frequency:^9}")
    
print(f"\nMost frequent letter: {ascii_lowercase[frequencies.index(max(frequencies))]}")
