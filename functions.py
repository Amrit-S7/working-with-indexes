"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Amrit Sandhu
ID:      190957080
Email:   sand7080@mylaurier.ca
__updated__ = "2022-11-21"
-------------------------------------------------------
"""
# Imports

# Constants


def list_factors(num):
    """
    -------------------------------------------------------
    Takes an integer greater than 0 as a parameter (num) and 
    returns a list of the factors that make up that 
    number excepting the number itself.
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - number greater than 0 (int > 0)
    Returns:
        factors - list of factors that make up num, excluding num (int)
    -------------------------------------------------------
    """
    factors = []
    i = 1
    for i in range(1, num, 1):
        if (num % i) == 0:
            factors.append(i)
        else:
            continue
    return factors


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: numbers = list_positives()
    -------------------------------------------------------
    Returns:
        numbers - A list of positive integers (list of int)
    -------------------------------------------------------
    """
    user = 1
    numbers = []
    while (user != 0):
        user = int(input("Enter a positive number: "))
        if user > 0:
            numbers.append(user)
        else:
            continue
    return numbers


def list_indexes(values, target):
    """
    -------------------------------------------------------
    Finds the indexes of target in values.
    Use: locations = list_indexes(values, target)
    -------------------------------------------------------
    Parameters:
        values - list of value (list of int)
        target - value to look for in num_list (int)
    Returns:
        locations - list of indexes of target (list of int)
    -------------------------------------------------------
    """
    locations = []
    i = 1
    length = len(values)
    if (target in values):
        for i in range(length):
            number = values[i]
            if number == target:
                locations.append(i)
    return locations


def subtract_lists(minuend, subtrahend):
    """
    -------------------------------------------------------
    Updates the list minuend removing from it the values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are not included in the updated list.
    subtrahend is unchanged
    Use: subtract_lists(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to remove from minuend (list)
    Returns:
        None
    -------------------------------------------------------
    """
    for i in subtrahend:
        while i in minuend:
            minuend.remove(i)
    return


def is_sorted(values):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = is_sorted(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list)
    Returns:
        in_order - True if values is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    in_order = True
    index = -1
    for i in range(1, len(values)):
        if (values[i - 1]) > (values[i]):
            in_order = False
            index = i - 1
    return in_order, index
