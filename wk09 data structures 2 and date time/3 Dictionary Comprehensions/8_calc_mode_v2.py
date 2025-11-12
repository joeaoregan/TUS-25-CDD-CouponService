# Example: calc_mode() - Version 2 (More Efficient)

def calc_mode(numbers):
    if not numbers:
        return None # empty list has no mode
    
    # Count frequenceis (more efficient for long lists)
    frequencies = {}
    for num in numbers:
        frequencies[num] = frequencies.get(num,0) + 1 # more efficient

    # Find the maximum frequency
    max_freq = max(frequencies.values())

    # Find all numbers with the maximum frequency
    modes = [number for number, count in frequencies.items() if count == max_freq]

    # Return a single value if one mode, otherwise return list of modes
    return modes[0] if len(modes) == 1 else modes



if __name__ == "__main__":
    data = [6,3,9,6,6,5,9,3]
    print(f"{calc_mode(data)=}") # calc_mode(data)=6

    data2 = [6,3,9,6,6,5,9,3,9]
    print(f"{calc_mode(data2)=}") # calc_mode(data2)=[6, 9]