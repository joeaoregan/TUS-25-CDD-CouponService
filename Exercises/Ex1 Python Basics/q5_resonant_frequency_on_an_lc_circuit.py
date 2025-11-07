# A00258304

# An LC circuit, also called a resonant circuit, consists of an inductor, 
# represented by the letter L, and a capacitor, represented by the letter C. 

# The resonant frequency is given by the formula
# f = 1 / (2PI(LC^0.5)
# where L is the inductance in henries, and C is the capacitance in farads.

# Write a program which inputs the values of the inductance and the capacitance and then 
# calculates and displays the resonant frequency on an LC circuit correct to 3 decimal places.

# Example:

# Input         | Result
# --------------|--------------------------------------
# 1.5           | Enter the inductance: 1.5
# 0.000000039   | Enter the capacitance? 0.000000039
# 658.025       | Resonant Frequency: 658.025
# --------------|--------------------------------------
# 0.3           | Enter the inductance: 0.3
# 0.00000008434 | Enter the capacitance? 0.00000008434
#               | Resonant Frequency: 1000.559
# --------------|--------------------------------------
# 0.02          | Enter the inductance: 0.02
# 0.000008      | Enter the capacitance? 0.000008
#               | Resonant Frequency: 397.887

from math import pi, sqrt

inductance = float(input("Enter the inductance: "))
capacitance = float(input("Enter the capacitance? "))

# resonant_frequency = 1 / (2 * pi * (inductance * capacitance) ** (1/2))
resonant_frequency = 1 / (2 * pi * sqrt(inductance * capacitance))

print(f"Resonant Frequency: {resonant_frequency:.3f}")