def calc_mean(numbers):
    """ Calculate the average of a list of numbers"""
    if numbers:
        return sum(numbers)/len(numbers)
    else:
        return None

if __name__=="__main__":
    # Input a sequence of values as a string
    number_string = input("Enter a sequence of values separated by spaces: ")
    # Turn the input sequence into a list of numbers using list comprehension
    numbers = [ int(num) for num in number_string.split() ]

    # calculate the mean of the numbers
    mean = calc_mean(numbers)
    
    if mean: # check the mean is not None
        print(f"The mean of the numbers is: {calc_mean(numbers):.1f}")
    else:
        print("Cannot calculate the mean of an empty list")