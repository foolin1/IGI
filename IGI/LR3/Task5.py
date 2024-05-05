# main: Finding the element with the maximum absolute value and the sum of elements between the first and second positive elements in a list
# Version: 1.0
# Author: Volodin
# Date: 01.05.2024
from sequence_initialization import initialize_sequence_user_input, initialize_sequence_generator

def choose_initialization_method():
    """
    Prompts the user to choose a method for initializing a sequence.
    The user can either manually input the sequence or generate a random sequence.
    Returns the initialized sequence.
    """
    while True:
        print("Choose the method to initialize the sequence:")
        print("1. User input")
        print("2. Generator")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            return initialize_sequence_user_input()
        elif choice == '2':
            n = int(input("Enter the number of elements to generate: "))
            return initialize_sequence_generator(n)
        else:
            print("Invalid choice. Please enter 1 or 2.")

def max_abs_element(lst):
    """
    Returns the element with the maximum absolute value from the given list.
    """
    return max(lst, key=abs)

def sum_between_positive(lst):
    """
    Returns the sum of elements between the first and second positive elements in the given list.
    If there are less than two positive elements, returns None.
    """
    positive_indices = [i for i, x in enumerate(lst) if x > 0]
    if len(positive_indices) < 2:
        return None
    return sum(lst[positive_indices[0]+1:positive_indices[1]])

def print_list(lst):
    """
    Prints the given list.
    """
    print("Your list: ", lst)

def main():
    """
    Executes the main
    """
    lst = choose_initialization_method()
    print_list(lst)
    print("Element with maximum absolute value: ", max_abs_element(lst))
    sum_between = sum_between_positive(lst)
    if sum_between is not None:
        print("Sum of elements between the first and second positive elements: ", sum_between)
    else:
        print("The list has less than two positive elements.")