# main: Calculating the value of a function using a power series expansion of the function
# Version: 1.0
# Author: Volodin I.
# Date: 01.05.2024

import math
from prettytable import PrettyTable

table = PrettyTable()

def input_value(prompt, validation_func):
    """
    General function for input with validation
    """
    while True:
        try:
            value = validation_func(input(prompt))
            return value
        except ValueError:
            print("Invalid input, please enter a valid value.")

def is_size(value):
    """
    Checks the value to make sure it is greater than 0
    """
    value = int(value)
    if value > 0:
        return value
    else:
        raise ValueError

def is_eps(value):
    """
    Checks the value to be between 0 and 1
    """
    value = float(value)
    if 0 < value < 1:
        return value
    else:
        raise ValueError

def is_value(value):
    """
    Checks the value to make sure it is a valid float
    """
    return float(value)

def is_correct_command(value):
    """
    Checks the value to be between 0 and 4
    """
    value = int(value)
    if 0 <= value <= 3:
        return value
    else:
        raise ValueError

def get_size_tuple():
    """
    Returns a number that will be the size of the list
    """
    return input_value("Enter size of list: ", is_size)

def generator(size: int):
    """
    Returns a sequence of numbers
    """
    for _ in range(size):
        yield input_value("Enter values: ", is_value)

def get_list():
    """
    Returns eps and generator
    """
    size = get_size_tuple()
    return input_value("Enter eps: ", is_eps), tuple(generator(size))

def get_values():
    """
    Returns eps and value
    """
    return input_value("Enter eps: ", is_eps), input_value("Enter value: ", is_value)

def get_taylor_series_math(value: int):
    """
    Returns the value of a function using a module math
    """
    return math.exp(value)

def get_taylor_series(eps: float, value: int):
    """
    Returns the value of a function using eps
    """
    s = a = 1
    n = 1
    while abs(a) > eps and n < 501:
        a *= value / n
        s += a
        n += 1
    return n, s

def add_value(eps: float, value):
    """
    Adds values to the table
    """
    n, s = get_taylor_series(eps, value)
    smath = get_taylor_series_math(value)

    table.field_names = ["x", "n", "F(x)", "Math F(x)", "eps"]
    table.add_row([value, n, s, smath, eps])

def add_tuple(eps: float, *args):
    """
    Unpacks the tuple and calls the method 'add_value'
    """
    for value in args:
        add_value(eps, value)

def output_table():
    """
    Returns and clear the table
    """
    print(table)
    table.clear()

def menu():
    """
    Returns menu
    """
    print("\n1: Counting a series for one number")
    print("2: Counting a series for several numbers")
    print("3: Exit")

def main():
    """
    Executes the main.
    """
    actions = {1: get_values, 2: get_list}

    while True:
        menu()
        command = input_value("\nEnter a value: ", is_correct_command)
        if command in actions:
            eps, values = actions[command]()
            add_tuple(eps, *([values] if command == 1 else values))
            output_table()
        elif command == 3:
            break