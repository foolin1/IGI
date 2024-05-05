import random

def initialize_sequence_user_input():
    sequence = []
    while True:
        try:
            number = input("Enter a number (or 'q' to quit): ")
            if number.lower() == 'q':
                break
            sequence.append(float(number))
        except ValueError:
            print("Invalid input. Please enter a number.")
    return sequence

def initialize_sequence_generator(n, start=-100, end=100):
    return [random.uniform(start, end) for _ in range(n)]