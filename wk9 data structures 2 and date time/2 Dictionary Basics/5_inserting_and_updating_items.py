# Insert a new item (key-value pair):
contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }
contacts['Deepak'] = '0831122334'
print(contacts['Deepak']) # 0831122334


# Assigning a value to an existing key updates the value
contacts['Deepak'] = "0879988776"
print(contacts['Deepak']) # 0879988776

# Keys have to be unique
# A set will ignore adding a new value
# Dictionary will update existing value