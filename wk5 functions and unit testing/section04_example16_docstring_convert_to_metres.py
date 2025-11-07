# Purpose: To convert a distance in metres to feet and inches
# Example of: Function with multiple return values

def metres_to_imperial(metres):
    """
    Convert a distance from metres to feet and inches.

    Parameters
    ----------
    metres : float
        The distance in metres.

    Returns
    -------
    whole_feet : int
        The feet part of the distance.
    inches : float
        The inches part of the distance (may include decimals).

    Examples
    --------
    >>> f"{metres_to_imperial(1.8288)}"
    '(6, 0.0)'
    >>> f"{metres_to_imperial(0.3048)}"
    '(1, 0.0)'
    >>> f"{metres_to_imperial(2.0)[0]} ft {metres_to_imperial(2.0)[1]:.2f} in"
    '6 ft 6.74 in'
    >>> f"{metres_to_imperial(0)}"
    '(0, 0.0)'
    >>> f"{metres_to_imperial(0.0254)}"
    '(0, 1.0)'
    """
    # Calculate feet as metres x 3.28084
    feet = metres * 3.28084

    # Calculate whole_feet as integer part of feet
    whole_feet = int(feet)

    # Calculate inches as (feet - whole_feet) * 12
    inches = (feet - whole_feet) * 12

    # return the results as a tuple
    return whole_feet, inches

# Call the function
# The code inside the if statement only runs if this script is executed, not imported
if __name__ == "__main__":
    # Input metres
    metres = float(input("Enter the distance in metres: "))

    # convert to feet and inches
    feet, inches = metres_to_imperial(metres)

    # Print whole_feet, inches
    print(f"Equivalent distance is {feet} feet, {inches:.1f} inches")

