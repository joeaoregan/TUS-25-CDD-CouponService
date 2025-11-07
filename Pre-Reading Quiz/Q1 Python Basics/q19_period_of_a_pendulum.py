# A00258304

# The period of a pendulum, which is the time taken to swing over and back, is given by the formula
# Which of the following lines of code is the correct implementation of this formula?

# a. period = 2 * pi * sqrt(length / gravity) # correct
# b. period = 2 * pi * sqrt(length * gravity)
# c. period = 2pi * sqrt(length / gravity)
# d. period = 2 * pi * sqrt(length) / gravity

from math import pi, sqrt

length = 5
gravity = 4

period = 2 * pi * sqrt(length / gravity)
print(period)