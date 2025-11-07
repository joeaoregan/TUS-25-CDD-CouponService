# removes item (key-value pair), doesn't return anything:

contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }
del contacts['Conor']
print(contacts) # {'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}

# KeyError raised if the dictionary key does not exit
# del contacts['Deirdre'] # KeyError: 'Deirdre'
