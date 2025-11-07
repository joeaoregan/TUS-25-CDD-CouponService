# A00258304
# Question 1: Secret Santa

def is_valid_allocation(allocation):
    for key in allocation:
        print(f"key: {key + ",":<7} value: {allocation[key]}")
        if key == allocation[key]:
            return False
    return True

def allocate_secret_santa(names):
    from random import shuffle
    givers = names.copy()    
    # shuffle the list of givers
    shuffle(givers)
    
    # create an ampty dicionary
    allocation = {}

    # for each index, name in the list except the last
    # insert the current name with the next name as a key-value pair in the dictionary
    for i, name in enumerate(givers[:-1]):
        allocation[name] = givers[i+1]
        
    # insert the last name with the first name a sa a key-value pair in the dictionary
    allocation[givers[-1]] = givers[0]

    return allocation









# Valid allocation dictionary, 3 names
allocation = {'Curly': 'Mo', 'Larry': 'Curly', 'Mo': 'Larry'}
print(f"{is_valid_allocation(allocation)=}")

# Invalid allocation dictionary, 3 names
allocation = {'Curly': 'Curly', 'Larry': 'Mo', 'Mo': 'Larry'}
print(f"{is_valid_allocation(allocation)=}")

# Valid allocation dictionary, 4 names
allocation = {'Ashok': 'Carla', 'Bláthnaid': 'Dawid', 'Carla': 'Bláthnaid', 'Dawid': 'Ashok'}
print(f"{is_valid_allocation(allocation)=}")

# Invalid allocation dictionary, 4 names
allocation = {'Ashok': 'Dawid', 'Bláthnaid': 'Bláthnaid', 'Carla': 'Ashok', 'Dawid': 'Carla'}
print(f"{is_valid_allocation(allocation)=}")

# Valid allocation dictionary, 5 names
allocation = {'Chico': 'Harpo', 'Groucho': 'Zeppo', 'Gummo': 'Groucho', 'Harpo': 'Gummo', 'Zeppo': 'Chico'}
print(f"{is_valid_allocation(allocation)=}")

# Invalid allocation dictionary, 5 names
allocation = {'Chico': 'Chico', 'Groucho': 'Gummo', 'Gummo': 'Harpo', 'Harpo': 'Groucho', 'Zeppo': 'Zeppo'}
print(f"{is_valid_allocation(allocation)=}")

# 3 names, Allocation 1
from random import seed;
seed(1)
names = ['Curly', 'Larry', 'Moe']
my_allocation =  {'Larry': 'Moe', 'Moe': 'Curly', 'Curly': 'Larry'}
print("Correct" if my_allocation == allocate_secret_santa(names) else f"Incorrect")