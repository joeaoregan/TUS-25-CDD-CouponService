# Deep Copy
# data_dict2 = copy.deepcopy(data_dict1)

# copy.deepcopy() recursively copies everything, including nested
# objects, so the original and the copy are completely independent.

import copy
contacts1 = {'Ailbhe': ['0861234567']}
contacts2 = copy.deepcopy(contacts1)

# Changes to a nested object in one dictionary doesn't affect the other:
contacts2['Ailbhe'].append('0870001111')

print(contacts1) # {'Ailbhe': ['0861234567']}
print(contacts2) # {'Ailbhe': ['0861234567', '0870001111']}