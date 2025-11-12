# Frequencies

numbers = [6,3,9,6,6,5,9,9]

frequencies = { num: numbers.count(num) for num in set(numbers)}
print(frequencies) # {9: 3, 3: 1, 5: 1, 6: 3}

print(max(frequencies)) # 9

print(frequencies.values()) # dict_values([3, 1, 1, 3])
print(max(frequencies.values())) # 3
max_frequency = max(frequencies.values()) # 3
