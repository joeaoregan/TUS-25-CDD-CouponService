# Dictionary Comprehensions: Multiple Modes
# Identify the keys that match the maximum frequency

# max_freq = max(frequencies.values())
# modes = {num: count for num, count in frequencies.items() if count == max_freq } # dictionary with keys and their frequencies for any that have the same as the max frequency

# data_dict.values() provides the values in the dictionary

# List with 2 modes

numbers = [6,3,9,6,6,5,9,3,9]
frequencies = {num: numbers.count(num) for num in set(numbers)}
print(frequencies) # {9: 3, 3: 2, 5: 1, 6: 3}

max_freq = max(frequencies.values())
modes = {num: freq for num, freq in frequencies.items() if freq == max_freq} # add any frequency that matches the max frequency to a dictionary
print(modes) # {9: 3, 6: 3}