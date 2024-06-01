def is_command(value: str) -> int:
    """Checks the value between 0 and 6. """
    while True:
        try:
            value = int(value)
            if 0 < value <= 6:
                return value
            value = input("Value should be between 0 and 7, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid input: ")