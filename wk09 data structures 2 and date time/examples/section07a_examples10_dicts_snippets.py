# contacts1 = {'Ailbhe': '0861234567'}
# contacts2 = contacts1


#print(f"{contacts2=}")
# contacts2['Bláthnaid'] = '0879876543'
# print(f"{contacts1=}")
# print(f"{contacts2=}")


# {'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}

# contacts1 = {'Ailbhe': '0861234567'}
# contacts2 = contacts1.copy()

# contacts2['Bláthnaid'] = '0879876543'
# print(f"{contacts1=}")
# print(f"{contacts2=}")


# contacts1 = {'Ailbhe': ['0861234567']}
# contacts2 = contacts1.copy()
# contacts2['Ailbhe'].append('0870001111')
# print(f"{contacts1=}")
# print(f"{contacts2=}")

# import copy
# contacts1 = {'Ailbhe': ['0861234567']}
# contacts2 = copy.deepcopy(contacts1)
# contacts2['Ailbhe'].append('0882223333')
#print(f"{contacts1=}")
#print(f"{contacts2=}")

# contacts1 = {'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
# contacts2 = {'Conor': '0855554321', 'Bláthnaid': '0871112222'}
# # combine the two dictionaries into a single one
# merged = contacts1 | contacts2
# print(f"{merged=}")

# contacts = {'Ailbhe': '0861234567', 'Bláthnaid': '0879876543'}
# contacts2 = {'Conor': '0855554321', 'Bláthnaid': '0871112222'}
# # update the first dictionary with the contents of the second
# contacts |= contacts2
# print(f"{contacts=}")




# # {'Ailbhe': ['0861234567', '0870001111']}  <- nested list still shared


