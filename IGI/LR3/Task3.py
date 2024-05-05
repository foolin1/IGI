# main: Counting the number of words starting with a lowercase letter in a string
# Version: 1.0
# Author: Volodin I.
# Date: 01.05.2024

from decorator import timer_decorator


def input_string():
    """
    Returns the input string
    """
    return input("Enter the string: ")

def count_words_starting_with_lowercase(string):
    """
    Returns the count of words starting with a lowercase letter
    """
    return sum(1 for word in string.split(" ") if word and word[0].islower())

@timer_decorator
def main():
    """
    Executes the main.
    """
    string = input_string()
    count = count_words_starting_with_lowercase(string)
    print(f"Count of words starting with a lowercase letter: {count}")
