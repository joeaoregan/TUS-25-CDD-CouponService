# Alaising 
# data_dict2 = data_dict1 # different reference to the same dictionary
# Assigning a dictionary to a new variable
# creates another reference to the same dictionary object

contacts1 = {'Ailbhe': '0861234567'}
contacts2 = contacts1

# Any change made through one variable will be reflected in the other
contacts2['Bláthnaid'] = "0879876543"
print(f"{contacts1=}") # contacts1={'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
print(f"{contacts2=}") # contacts2={'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
