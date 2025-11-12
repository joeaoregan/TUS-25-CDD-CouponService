# Iterate over the key-value pairs

# data_dict = {}
# for key, value in data_dict.items():
#     print(key, value)

contacts = {'Emergancy': '112', 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}

print(f"{'Name':<12} {'Number'}")
for name, number in contacts.items():
    print(f"{name:<12} {number}")

# Insertion order
# Name         Number
# Emergancy    112
# Ailbhe       0861234567
# Bláthnaid    0879876543

# Sort the items in order of the keys

print(f"{'Name':<12} {'Number'}")
for name, number in sorted(contacts.items()):
    print(f"{name:<12} {number}")

# Key order
# Name         Number
# Ailbhe       0861234567
# Bláthnaid    0879876543
# Emergancy    112