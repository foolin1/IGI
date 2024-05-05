# main: Counting the number of non-negative numbers in a sequence
# Version: 1.0
# Author: Volodin I.
# Date: 01.05.2024

from sequence_initialization import initialize_sequence_user_input, initialize_sequence_generator

def initialize_sequence_user_input2():
    sequence = []
    while True:
        try:
            number = input("Enter a number: ")
            if float(number) < -100:
                break
            sequence.append(float(number))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return sequence

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
            return initialize_sequence_user_input2()
        elif choice == '2':
            n = int(input("Enter the number of elements to generate: "))
            return initialize_sequence_generator(n)
        else:
            print("Invalid choice. Please enter 1 or 2.")

def count_non_negative_numbers(numbers):
    """
    Returns the count of non-negative numbers
    """
    return len([num for num in numbers if num >= 0])

def main():
    """
    Executes the main.
    """
    numbers = choose_initialization_method()
    print("Final list: ", numbers)
    count = count_non_negative_numbers(numbers)
    print(f"Count of non-negative numbers: {count}")