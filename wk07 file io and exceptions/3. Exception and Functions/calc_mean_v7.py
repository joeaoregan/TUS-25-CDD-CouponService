import traceback

def calc_mean(numbers):
    """ Calculate the average of a list of numbers.
    
    Parameters
    ----------
    numbers : list of numeric values
        A list containing numeric values (integers or floats) for which the mean
        is to be calculated. The list must not be empty.

    Raises
    ------
    ValueError
        If the list is empty a ValueError is raised to indicate that the mean
        cannot be calculated.
    TypeError
        If any element in the list is not numeric (e.g., a string), a TypeError
        is raised

    Returns
    -------
    float
        The arithmetic mean of the numbers in the list.
    """
    try:
        return sum(numbers) / len(numbers)
    except ZeroDivisionError as e:
        raise ValueError("Cannot calculate the mean of an empty list") from e
    except TypeError:
        raise TypeError("All elements in the list must be numeric.")

if __name__=="__main__":
    valid_input = False
    ## keep going until a valid input has been provided
    while not valid_input:
        # Input a sequence of values as a string
        number_string = input("Enter a sequence of values separated by spaces: ")
        
        try:
            # Turn the input sequence into a list of numbers using list comprehension
            numbers = [ int(num) for num in number_string.split() ]
        except ValueError:
            print("Please ensure only numeric values are provided")
        else:
            valid_input = True

    try:
        # calculate and display the mean of the numbers
        print(f"The mean of the numbers is: {calc_mean(numbers):.1f}")
    except ZeroDivisionError as e:
        print(e)
