# Purpose: To calculate the period (time) of a pendulum
# Example of: Calculations using the math module
from math import pi, sqrt

# Input length (of the pendulum)
length = float(input("Input the length of the pendulum in metres: "))

# Calculate the period (time)
time = 2 * pi * sqrt(length / 9.81)

# Display the time
print(f"The time is {time:.2f} seconds")


