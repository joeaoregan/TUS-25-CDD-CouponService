

ppsn_alphabet = "WABCDEFGHIJKLMNOPQRSTUV"

weighting = [8, 7, 6, 5, 4, 3, 2]

# ppsn = input("Enter a PPSN: ").upper()
ppsn = "2546736P"

total = 0

for i, x in enumerate(ppsn[:7]):
    # print(f"{x} * {weighting[i]} = {int(x) * weighting[i]}")

    total += int(x) * weighting[i]

remainder = total % 23
check_character = ppsn_alphabet[remainder]
# print(f"Check character should be: {check_character}")
if check_character == ppsn[-1]:
    print(f"PPSN {ppsn} is valid")
else:
    print(f"PPSN {ppsn} is not valid")