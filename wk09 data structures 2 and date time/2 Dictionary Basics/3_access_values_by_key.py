contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }
print(contacts['Ailbhe']) # 0861234567

# print(contacts['Deirdre']) # KeyError: 'Deirdre'

# Exception Handling

name = input("Enter the person's name: ")
try:
    print(f"{name}'s number is {contacts[name]}")
except KeyError:
    print(f"{name} is not in contacts")

# or check if key in dictionary
name = input("Enter the person's name: ")
if name in contacts:
    print(f"{name}'s number is {contacts[name]}")
else:
    print(f"{name} is not in contacts")

