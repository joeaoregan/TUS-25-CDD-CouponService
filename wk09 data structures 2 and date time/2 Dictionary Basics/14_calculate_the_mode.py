# Example: Calculate the Mode
# Get the key with the highest frequency

def calc_mode(numbers):
    """ Calculate the mode (most frequent element) of a list using a dictionary."""
    if not numbers:
        return None # empty list has no mode
    
    # Count frequencies
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1 # if we don't have it set 0, otherwise increment by 1

    # return the key with maximm frequency
    return max(frequencies, key=frequencies.get) # get the key corresponding to the maximum value


if __name__=="__main__":
    print(f"{calc_mode([6,3,9,6,6,5,9,3])=}") # calc_mode([6,3,9,6,6,5,9,3])=6