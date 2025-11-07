# A00258304

# Based on the principles of Linear Motion, the velocity v of an object under constant acceleration is
# v = u + a * t
# where 
# u is the initial velocity in metres per second
# a is the acceleration in metres per second squared
# t is the time elapsed in seconds
# For example, a top sprinter in a 100m race would have values u = 0, a = 1.3 and t = 9.6 
# (assumes constant acceleration with is a simplification).

# Write and document a function calc_velocity() which takes parameters representing the acceleration, time elapsed 
# and initial velocity (with a default value of zero), and then calculates and returns the resulting velocity.

def calc_velocity(acceleration, time_elapsed, initial_velocity=0):
    return initial_velocity + acceleration * time_elapsed


calc_velocity()