
contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }

# initialised over multiple lines for clarity
contacts = {
    'Ailbhe': '0861234567', # Key, Value
    'Bláthnaid': '0879876543',
    'Conor': '0855554321'
}

print(contacts)
print(type(contacts))

data_dict= {} # Empty dictionary
data_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

# Dictionaries preserve the insertion order of the key-value pair
# Previously they had been unordered like a set

contacts = {}
print(bool(contacts)) # False (empty dictionary)

if data_dict: # True if the dictionary is not empty
    print("Dictionary has items")
else:
    print("Dictionary has no items")