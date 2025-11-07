# A00258304

# Based on the principles of Linear Motion, the velocity v of an object under constant acceleration is
# v = u + a * t
# where 
#     u is the initial velocity in metres per second
#     a is the acceleration in metres per second squared
#     t is the time elapsed in seconds
# For example, a top sprinter in a 100m race would have values u = 0, a = 1.3 and t = 9.6 
# (assumes constant acceleration with is a simplification).

# u = 0m/s
# a = 1.3 m/s²
# t = 9.6s
# v = ?

# Write and document a function calc_velocity() which takes parameters representing the acceleration, time elapsed 
# and initial velocity (with a default value of zero), and then calculates and returns the resulting velocity.

# Important: CodeRunner will test your function by running it using the test cases below. 
# Just include your function definition, don't include any program code.

# For Example:

# Test                                                                                                       | Result
# ---------------------------------------------------------------------------------------------------------- | ------------------------------------
# 100m sprinter's velocity at end of race                                                                    | Velocity is 12.48 metres per second
# print(f"Velocity is {calc_velocity(1.3, 9.6):.2f} metres per second")
# ---------------------------------------------------------------------------------------------------------- | ------------------------------------
# Velocity of an object in free fall                                                                         | Velocity is 49.0 metres per second
# print(f"Velocity is {calc_velocity(9.8, 5):.1f} metres per second")
# ---------------------------------------------------------------------------------------------------------- | ------------------------------------
# An airplane landing with initial velocity of 70.0 m/s and then decelerates at 1.50 m/s2 for 37.625 seconds | Velocity is 13.562 metres per second
# print(f"Velocity is {calc_velocity(-1.5, 37.625, 70):.3f} metres per second")                              |


def calc_velocity(acceleration, time_elapsed, initial_velocity=0):
    return initial_velocity + acceleration * time_elapsed


calc_velocity()