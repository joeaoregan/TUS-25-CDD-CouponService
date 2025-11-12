# Program to calculate gravity using a pendulum
from math import pi
length = float(input("Enter the length of the pendulum: ")) # assume decimal number input
period = float(input("Enter the period of the pendulum: ")) # assume decimal number input
gravity = 4*pi**2*length/(period**2) # gravity formula; a ** b is a to the power of b. Also math.pow(a,b)
print(f"Gravity is {gravity:.2f}") # f-string displays output to 2 decimal places
