# iterate over the keys

# data_dict = {}
# for key in data_dict:
#     print(key, data_dict[key])


contacts = {'Emergancy': '112', 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
print(f"{'Name':<12} {'Number'}")
for name in contacts:
    print(f"{name:<12} {contacts[name]}")

# Insertion order:
# Name         Number
# Emergancy    112
# Ailbhe       0861234567
# Bláthnaid    0879876543


contacts = {'Emergancy': '112', 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
print(f"{'Name':<12} {'Number'}")
for name in sorted(contacts):
    print(f"{name:<12} {contacts[name]}")

# Alphabetical order by keys
# Name         Number
# Ailbhe       0861234567
# Bláthnaid    0879876543
# Emergancy    112
