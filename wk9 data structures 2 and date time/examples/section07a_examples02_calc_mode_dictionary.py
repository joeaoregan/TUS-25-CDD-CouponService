def calc_mode(numbers):
    """
    Calculate the mode (most frequent element) of a list using a dictionary.
    """
    if not numbers:
        return None  # empty list has no mode

    # Count frequencies
    frequencies = {}
    for number in numbers:
        frequencies[number] = frequencies.get(number, 0) + 1

    # return the key with maximum frequency
    return max(frequencies, key=frequencies.get)

if __name__ == "__main__":
    print(f"{calc_mode([6,3,9,6,6,5,9])=}")
    





