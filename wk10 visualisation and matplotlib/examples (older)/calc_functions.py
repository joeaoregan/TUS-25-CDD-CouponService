# Program Name: calc_functions.py
# Purpose: Functions for calculating meean, mode, standard vediation and correlation
# Example of: Functions with list

from math import sqrt

def calc_mean(values):
    """
    Calculate the mean (average) of a list of numbers

    Parameters
    ----------
    values : list
        A list of numbers.

    Returns
    -------
    float
        The mean value.

    """
    # try to calculate the mean
    try:
        # mean is the sum of the values divided by the number of values
        return sum(values)/len(values)
    # what can go wrong?
    # ZeroDivisionError - if the list is empty
    # TypeError - is the list is not all 
    except (ZeroDivisionError, TypeError):
        return None

def check_list_all_numbers(values):
    """
    To check if the values in a list are all numbers

    Parameters
    ----------
    values : list
        A list of values.

    Returns
    -------
    bool
        True if the values in the list are all numbers.
        False if the list is empty, or if there is at least 1 non-numeric value.
    """
    # empty list returns False
    if len(values) == 0:
        return False
    else:
        # go through the list and look for a non-numeric value
        for value in values:
            if not isinstance(value,(int,float)):
                return False
        # otherwise the whole list has been processed and the values are all numbers
        else:
            return True

def calc_median(values):
    """
    Calculate the median (middle value) of a list of numbers

    Parameters
    ----------
    values : list
        A list of numbers.

    Returns
    -------
    float
        The median (middle value), or None if it cannot be calculated.
    """
    # empty list returns False
    if not check_list_all_numbers(values):
        return None
    else:
        # sort the list in order
        values.sort()

        # determine the mid-index
        mid_index = int(len(values)/2)

        # if there's an odd number of values
        if len(values) % 2:
            # median is the value at the mid index
            return values[mid_index]
        else: # otherwise there's an even number of values
            return (values[mid_index-1] + values[mid_index])/2
        
def calc_mode(values):
    """
    Calculate the mode of a list of numbers / most common value in a list

    Parameters
    ----------
    values : list
        A list of values.

    Returns
    -------
        The mode (most common number), or None if it cannot be calculated.
    """
    # empty list returns False
    if not len(values): # same as if len(values) == 0
        return None
    else:
        # create a dictionary:
        # the keys will be the elements in the original list,
        # the value will be the frequency count for the element
        frequencies = {}

        # go through the list elements one at a time
        for value in values:
            # if it's not in the dictionary
            if not value in frequencies:
                # insert it with a frequency of 1
                frequencies[value] = 1
            # otherwise, it's already in the list
            else:
                # increase its frequency by 1
                frequencies[value] += 1

        # return the item with the highest frequency
        return max(frequencies, key=frequencies.get)
    
def calc_standard_deviation(values):
    """
    Calculate the standard deviation of a list of numbers

    Parameters
    ----------
    values : list
        A list of values.

    Returns
    -------
    float    
        The standard deviation, or None if it cannot be calculated.
    """
    # if the standard deviation can't be calculated
    if not check_list_all_numbers(values):
        return None
    else:
        # calvculate the mean
        mean = calc_mean(values)

        # create a list of the deviations squared
        deviations = [ (x - mean) ** 2 for x in values ]

        # calculate and return the standard deviation
        return sqrt(sum(deviations)/(len(values)-1))

def calc_correlation(x_values, y_values):
    """
    Calculate the correlation of two list of numbers

    Parameters
    ----------
    x_values : list
        A list of values.

    y_values : list
        A list of related values

    Returns
    -------
    float    
        The correlation between the lists, or None if it cannot be calculated.
    """
    # if the correlation can't be calculated
    if not check_list_all_numbers(x_values) or not check_list_all_numbers(x_values) or len(x_values) != len(y_values):
        return None
    else:
        # calvculate the means
        x_mean = calc_mean(x_values)
        y_mean = calc_mean(y_values)

        # create a list of the deviations
        x_deviations = [ x - x_mean for x in x_values ]
        y_deviations = [ y - y_mean for y in y_values ]

        # create a list of the deviations multiplied
        xy_deviations = [ x*y for (x,y) in zip(x_deviations,y_deviations)]

        # create a list of the deviations squared
        x_sqd_deviations = [ (x - x_mean) ** 2 for x in x_values ]
        y_sqd_deviations = [ (y - y_mean) ** 2 for y in y_values ]

        # calculate and return the standard deviation
        return sum(xy_deviations)/(sqrt(sum(x_sqd_deviations))*sqrt(sum(y_sqd_deviations)))