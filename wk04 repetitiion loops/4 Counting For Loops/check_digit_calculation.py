# Input digits of IMO number
imo_digits = input("Enter the digits of the IMO number: ")

# Calculate the check digit
total = 0
# For each digit excluding the final one
for i in range(len(imo_digits)-1):
    # multiply by (7 - its index) and add to total
    total += int(imo_digits[i]) * (7 - i)
print(f"{total=}")

# compare right most digit of total (modulo 10) with right-most IMO digit
if total % 10 == int(imo_digits[-1]):
    print("Valid IMO number")
else:
    print("Not a valid IMO number")