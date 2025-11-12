# Swap the keys and values

contacts = {'Emergency': '999', 'Bláthnaid': '0859988775', 'Deepak': '0831122334'}
# reverse_contacts = { v,k for k,v in contacts.items()} # Syntax error
reverse_contacts = {v:k for k,v in contacts.items()} # not so obvious

print(contacts)
print(reverse_contacts)

reverse_contacts = {number:name for name,number in contacts.items()} # more readable