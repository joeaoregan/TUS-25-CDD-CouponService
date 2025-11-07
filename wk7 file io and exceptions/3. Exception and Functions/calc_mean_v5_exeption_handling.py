def calc_mean(numbers):
    """ Calculate the average of a list of numbers"""
    if not numbers: # if guard
        raise ValueError("Cannot calculate the mean of an empty list")
    return sum(numbers)/len(numbers)

if __name__=="__main__":
    # Input a sequence of values as a string
    number_string = input("Enter a sequence of values separated by spaces: ")
    # Turn the input sequence into a list of numbers using list comprehension
    numbers = [ int(num) for num in number_string.split() ]

    try:
        # calculate and display the mean of the numbers
        print(f"The mean of the numbers is: {calc_mean(numbers):.1f}")
    except ValueError as e:
        print(e)