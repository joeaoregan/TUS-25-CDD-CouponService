# Removes item (key-value pair), returns the value

contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }
print(contacts.pop('Conor')) # 0855554321


# KeyError raised if the dictionary key does not exist

# Specific default value to return, if key not in dictionary:
# data_dict.pop(key, default_value)

print(contacts.pop('Deirdre', 'Not in contacts')) # Not in contacts

