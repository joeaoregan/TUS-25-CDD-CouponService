# Shallow Copy
# data_dict2 = data_dict1.copy()

# A shallow copy of a dictionary creates a new dictioanry object,
#     keys and values are references to the same bojects in the original.

# This is fine for dictionaries with immutable objects as values.
contacts1 = {'Ailbhe': '0861234567'}
contacts2 = contacts1.copy()

# Changes to one dictionary doesn't affect the other
contacts2['Blárhnaid'] = "0879876543"
print(f"{contacts1=}") # contacts1={'Ailbhe': '0861234567'}
print(f"{contacts2=}") # contacts2={'Ailbhe': '0861234567', 'Blárhnaid': '0879876543'}
