# A00258304

from string import ascii_lowercase

frequencies = []

# text = input("Enter the text: ")
text = "I refuse to join any club that would have me as a member."

for letter in ascii_lowercase:    
    # frequencies.append([letter, text.count(letter)])
    frequencies.append(text.count(letter))

# text = "abababa"

# counter = text.count("a")
# print(counter)

print("Letter Frequency")
# for i in frequencies:
    # print(f"   {i[0]}       {i[1]}")
for i, letter in enumerate(ascii_lowercase):
    print(f"   {letter}       {frequencies[i]}")

print()
print(f"Most frequent letter: {ascii_lowercase[frequencies.index(max(frequencies))]}")