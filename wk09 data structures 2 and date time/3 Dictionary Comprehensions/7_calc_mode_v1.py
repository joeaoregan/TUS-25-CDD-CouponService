# Example: calc_mode() - version 1

def calc_mode(numbers):
    if not numbers:
        return None # empty list has no mode
    
    # Count frequencies using a set (inefficient for long lists)
    frequencies = {num: numbers.count(num) for num in set(numbers)}

    # Fin the maximum frequency
    max_freq = max(frequencies.values())

    # Find all numbers with the maximum frequency
    modes = [number for number, count in frequencies.items() if count == max_freq]

    # Return a single value if only one mode, otherwise return list of modes
    return modes[0] if len(modes) == 1 else modes


if __name__ == "__main__":
    data = [6,3,9,6,6,5,9,3]
    print(f"{calc_mode(data)=}") # calc_mode(data)=6

    data2 = [6,3,9,6,6,5,9,3,9]
    print(f"{calc_mode(data2)=}") # calc_mode(data2)=[9, 6]