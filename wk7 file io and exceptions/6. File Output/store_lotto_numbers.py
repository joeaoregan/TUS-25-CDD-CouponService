from random import randint
# Create an empty list
lotto_list = []

# Keep repeating unitl we get 6 numbers
while len(lotto_list) < 6:
    #Randomly generate a number between 1 and 47
    number = randint(1, 47)

    # if not in the list
    if number not in lotto_list:
        # Add the number to the list
        lotto_list.append(number)

    # Sort hte list and display it
lotto_list.sort()
print("Your lotto numbers are", lotto_list)
    
# open the file in append mode
with open("lotto.txt", "a") as lotto_file: # open in append mode
    # for each number in the list
    for number in lotto_list:
        # write the number to the file
        lotto_file.write(str(number)+" ")
    else: # after the list has been processed, the for loop terminates
        lotto_file.write("\n") # add a new line after the 6 numbers


    