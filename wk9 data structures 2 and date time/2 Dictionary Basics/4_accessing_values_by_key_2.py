# Another way: get() method

contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }
print(contacts.get('Ailbhe')) # 0861234567

print(contacts.get('Deirdre')) # None

print(contacts.get('Deirdre', "Not in contacts")) # Provide a default value for when none returned