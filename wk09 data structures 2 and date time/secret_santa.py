# Secret Santa

names = ['Ashok', 'Bláthnaid', 'Carla', 'Dawid']

# version 1: inefficient

allocation = {'Ashok': 'Bláthnaid', 'Bláthnaid': 'Dawid', 'Carla': 'Ashok', 'Dawid': 'Carla'}

print(allocation)

# version 2: using a loop

from random import shuffle
 
givers = ['Ashok', 'Bláthnaid', 'Carla', 'Dawid']
shuffle(givers)

secret_santa = {}

# for i,name in givers[:-1]:
#     secret_santa[name] = name[i+1]

for i,name in enumerate(givers[:-1]):
    secret_santa[name] = name[i+1]

print(secret_santa)

for i,name in enumerate(givers[:-1]):
    secret_santa[name] = givers[i+1]

print(secret_santa)


# Version 3

print(givers)

receivers = givers.copy()
print(receivers)

receivers.remove('Bláthnaid')
print(receivers)

from random import choice

print(choice(receivers))

secret_santa = {'Bláthnaid':'Carla'}

# Ashok
receivers = givers.copy()
print(receivers)
receivers.remove('Ashok')
print(receivers) # Carla already assigned ...remvove Carla too
receivers.remove('Carla')
print(receivers)
print(choice(receivers))

secret_santa['Ashok'] = 'Dawid'

print(secret_santa)


def time_allocation_function(allocator, names, reps=1000):
    start = perf_counter()
    for _ in range(reps):
        allocator(names)
    end = perf_counter()
    return end - start