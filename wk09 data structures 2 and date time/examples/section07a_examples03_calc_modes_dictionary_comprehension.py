def calc_mode(numbers):
    """
    Calculate the mode (most frequent element) of a list using a dictionary.
    Returns a single value if there is one mode, or a list of modes if there are more than 1.
    """
    if not numbers:
        return None  # empty list has no mode

    # Count frequencies using a set (inefficient for long lists)
    frequencies = {num: numbers.count(num) for num in set(numbers)}

    # Find the maximum frequency
    max_freq = max(frequencies.values())

    # Find all numbers with the maximum frequency
    modes = [number for number, count in frequencies.items() if count == max_freq]

    # Return a single value if only one mode, otherwise return list of modes
    return modes[0] if len(modes) == 1 else modes


if __name__ == "__main__":
    data = [6,3,9,6,6,5,9,3]
    print(f"{data=} {calc_mode(data)=}")  # Output: 6
    
    data2 = [6,3,9,6,6,5,9,3,9]
    print(f"{data2=} {calc_mode(data2)=}")  # Output: [9, 6]  (multiple modes)