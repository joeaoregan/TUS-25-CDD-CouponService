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