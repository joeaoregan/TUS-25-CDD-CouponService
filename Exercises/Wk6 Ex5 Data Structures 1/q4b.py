# A00258304

from string import ascii_lowercase

frequencies = []

text = input("Enter the text: ").lower()

# Version 1: Count each letter of the Alphabet
# for letter in ascii_lowercase:
#     frequencies.append(text.count(letter))

# Version 2: Process each letter of the text

# frequencies = [0] * 26
# # print(frequencies)
# # for i, letter in enumerate(text):
# for letter in text:
#     if letter.isalpha():
#         frequencies[ascii_lowercase.find(letter)] += 1
#     else:
#         continue

# Version 3: Process each unique letter of the text
unique_characters = set(text)
for character in set:
    if character.isalpha():
        index = ascii_lowercase.index(character)
        count = text.count(character)
        frequencies[index] = count

print("\nLetter Frequency")
for letter,frequency in zip(ascii_lowercase,frequencies):
    print(f"{letter:^5}{frequency:^9}")
    
print(f"\nMost frequent letter: {ascii_lowercase[frequencies.index(max(frequencies))]}")
