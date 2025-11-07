# A00258304

from string import ascii_lowercase

def get_percent_letter_frequencies(filename):
    with open(filename) as file:       
        book = file.read()
        # print(len(book))
        frequencies = {}

        for char in ascii_lowercase:
            # print(char)
            # for letter in book:
            #     if char == letter:
            #         frequencies[char] += 1
            #     else:
            #          frequencies[char] = 1
            frequencies[char] = book.lower().count(char)

        total = sum(frequencies.values())

        percentages = {}

        for char in frequencies:
            percentages[char] = frequencies[char] / total * 100
            # print(f"{char}, {frequencies[char]}, {total}, {(frequencies[char]/total*100)}")

        file.close()

        return percentages

        
percent_frequencies = get_percent_letter_frequencies("Carmilla.txt")
print("Letter Frequency")
for letter in sorted(percent_frequencies):
    print(f"{letter:^5}{percent_frequencies.get(letter):^9.1f}")