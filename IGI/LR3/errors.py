def is_correct_command(value):
    """
    Checks the value
    """
    while True:
        try:
            value = int(value)
            if 0 < value < 7:
                return value
            value = input("Value should be in range [1,6], input value: ")
        except ValueError:
            value = input("Invalid input, please try again: ")