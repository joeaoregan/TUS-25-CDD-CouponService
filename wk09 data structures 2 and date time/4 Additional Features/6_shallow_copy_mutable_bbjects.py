# Shallow Copy
# data_dict2 = data_dict1.copy()

# if the values in a dictionary are mutable (list of phone numbers),
# modifying the values affecgt both dictionaries,
# because the nested object is shared in a shallow copy

contacts1 = {'Ailbhe': '0861234567'}
contacts2 = contacts1.copy()

# Changes to the objecgt through one dictionary affects the other one too:

contacts2['Ailbhe'] = "0870001111"

print(f"{contacts1=}") # contacts1={'Ailbhe': '0861234567'}
print(f"{contacts2=}") # contacts2={'Ailbhe': '0870001111'}

contacts1 =  {'Ailbhe': ['0871234567']}
print(contacts1['Ailbhe'])
contacts1['Ailbhe'].append('09024400')

print(contacts1['Ailbhe'])

contacts2 = contacts1.copy()
print(contacts1)
print(contacts2)

contacts2['Bláthnaid'] = ['0851122334']
print(contacts2)
print(contacts1)

contacts1['Ailbhe'].append('0901234567')
print(contacts1)
print(contacts2)