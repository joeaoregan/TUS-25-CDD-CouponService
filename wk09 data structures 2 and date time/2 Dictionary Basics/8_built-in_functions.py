# len() - returns the number of items (key-value pairs)

contacts = { 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543', 'Conor': '0855554321' }
print(len(contacts)) # 3


# sorted() - returns a sorted list of keys
contacts = {'Emergancy': '112', 'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
print(sorted(contacts)) # ['Ailbhe', 'Bláthnaid', 'Emergancy']


# min() / max() - return the "smallest" / "largest" key
print(min(contacts)) # Ailbhe
print(max(contacts)) # Emergancy

ports = {80: 'HTTP', 22: 'SSH', 443: 'HTTPS'}
print(min(ports)) # 22
print(max(ports)) # 443