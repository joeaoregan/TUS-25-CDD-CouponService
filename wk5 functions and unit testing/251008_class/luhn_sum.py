# Function to calculate luhn sum
def calc_luhn_sum(digit_str):
    # create an empty string (the Luhn string) to store the 
    # multiplied digits, (e.g. this would be 0868582166)
    luhn_str = ""
    for i, digit in enumerate(digit_str[::-1]):
        if i % 2 == 0:
            luhn_str += digit
        else:
            luhn_str += str(int(digit) * 2)

    total = 0
    for digit in luhn_str:
        total += int(digit)
    # if the index is even
    # Add the corresponding digit to the Luh string
    # Otherwise
    # Multiply the digit by 2 and add to the Luhn string

    # return 0
    return total

# Pythonic way
def is_valid_sin(sin):
    return len(sin) == 9 and sin.isdigit() and calc_luhn_sum(sin) % 10 == 0

def is_valid_sin_old(sin):
    if len(sin) == 9 and sin.isdigit() and calc_luhn_sum(sin) % 10 == 0:
        return True
    else:
        return False
    
if __name__=="__main__":
    print(f"{calc_luhn_sum('046454286')=}")
    print(f"{is_valid_sin('046454286')=}")
