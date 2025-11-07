# The Luhn Algorithm is a check digit formula to validate ID numbers, such as the Canadian Social Insurance Number (SIN).

# 1. Write a function calc_luhn_sum() which take a single string parameter representing a series of digits and then calculates 
#    and returns the Luhn sum (the result of the Luhn Algorithm, as explained here, page 16) 
# 2. The Canadian Social Insurance Number (SIN) is a 9-digit number for which the Luhn sum is evenly divisible by 10. Write a function is_valid_sin()
#     which takes a single string parameter representing a Canadian Social Insurance Number and returns a boolean value indicating whether or not it is a valid SIN.
# Important: CodeRunner will test your functions by running them using the test cases below. Just include your function definitions, don't include any program code.

# For example:

# Test	                                    | Result
# ----------------------------------------- | --------------------------------
# Example from Wikipedia, Valid SIN         | calc_luhn_sum('046454286')=50
# print(f"{calc_luhn_sum('046454286')=}")   | is_valid_sin('046454286')=True
# print(f"{is_valid_sin('046454286')=}")    |
# ----------------------------------------- | --------------------------------
# Another Valid SIN                         | calc_luhn_sum('502347735')=40
# print(f"{calc_luhn_sum('502347735')=}")   | is_valid_sin('502347735')=True
# print(f"{is_valid_sin('502347735')=}")    |
# ----------------------------------------- | --------------------------------
# Invalid SIN (wrong Luhn Sum)              | calc_luhn_sum('046454287')=51
# print(f"{calc_luhn_sum('046454287')=}")   | is_valid_sin('046454287')=False
# print(f"{is_valid_sin('046454287')=}")    |
# ----------------------------------------- | --------------------------------
# Invalid SIN (too many digits)             | calc_luhn_sum('8464542861')=39
# print(f"{calc_luhn_sum('8464542861')=}")  | is_valid_sin('8464542861')=False
# print(f"{is_valid_sin('8464542861')=}")   |
# ----------------------------------------- | --------------------------------
# Invalid SIN (too few digits)              | calc_luhn_sum('996454286')=60
# print(f"{calc_luhn_sum('996454286')=}")   | is_valid_sin('996454286')=True
# print(f"{is_valid_sin('996454286')=}")    |
# ----------------------------------------- | --------------------------------
# Invalid SIN, contains a letter            | is_valid_sin('X46454286')=False
# print(f"{is_valid_sin('X46454286')=}")    |
# ----------------------------------------- | --------------------------------
# Invalid SIN, contains a special character | is_valid_sin('5%2347735')=False
# print(f"{is_valid_sin('5%2347735')=}")    |


# A00258304
def calc_luhn_sum(digits):
    luhn = ""
    total = 0
    for i, digit in enumerate(digits[::-1]):
        if i % 2 == 0:
            luhn += digit # odd digits unchanged
        else:
            luhn += str(int(digit) * 2) # even digits doubled

    for digit in luhn:
        total += int(digit)
        # print("total:",total)
    return total
    

def is_valid_sin(canadian_sin):
    return len(canadian_sin) == 9 and canadian_sin.isdigit() and calc_luhn_sum(canadian_sin) % 10 == 0

# calc_luhn_sum()

if __name__=="__main__":
    print(f"{calc_luhn_sum('046454286')=}")
    print(f"{is_valid_sin('046454286')=}")

    print(f"{calc_luhn_sum('502347735')=}")
    print(f"{is_valid_sin('502347735')=}")

    print(f"{calc_luhn_sum('046454287')=}")
    print(f"{is_valid_sin('046454287')=}")

    print(f"{calc_luhn_sum('8464542861')=}")
    print(f"{is_valid_sin('8464542861')=}")

    print(f"{calc_luhn_sum('996454286')=}")
    print(f"{is_valid_sin('996454286')=}")
    
    print(f"{is_valid_sin('X46454286')=}")
    
    print(f"{is_valid_sin('5%2347735')=}")