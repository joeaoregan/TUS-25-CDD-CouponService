# Program to calculate gravity using a pendulum
from math import pi
length = float(input("Enter the length of the pendulum: ")) # assume decimal number input
period = float(input("Enter the period of the pendulum: ")) # assume decimal number input
# g = 4*pi*pi*length / T * T
gravity = 4 * pi**2 * length / period ** 2
print(f"Gravity is {gravity:.2f}") # f-strign displays output to decimal places