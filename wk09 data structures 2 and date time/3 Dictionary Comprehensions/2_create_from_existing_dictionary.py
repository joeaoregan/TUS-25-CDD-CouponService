
# Create a dictionary from an existing one

# {} key_expression: value_expression for k,v in dict.items() }

# Phone numbers in international format

contacts = {'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321'}
international_contacts = {name: f"+353 {number[1:]}" for name, number in contacts.items() }
print(international_contacts) # {'Ailbhe': '+353 861234567', 'Bláthnaid': '+353 879876543', 'Conor': '+353 855554321'}