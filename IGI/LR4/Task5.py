import numpy as np


class Matrix:
    def __init__(self, n: int, m: int) -> None:
        self._matrix = np.random.randint(0, 100, (n, m))
        self._dimensions = (n, m)

    def __str__(self) -> str:
        return str(self._matrix)

    @property
    def dimensions(self) -> tuple:
        return self._dimensions

    @property
    def matrix(self) -> np.ndarray:
        return self._matrix

    @staticmethod
    def from_array(array: list) -> 'Matrix':
        """Converting an Array to a Matrix. """
        m = Matrix(0, 0)
        m._matrix = np.array(array)
        m._dimensions = m.matrix.shape
        return m

    def operation(self, func) -> np.ndarray:
        """Returns the result of the function. """
        return func(self._matrix)


class UpdateMatrix(Matrix):
    def __init__(self, n: int, m: int) -> None:
        super().__init__(n, m)
        self._last_row = self.matrix[-1]

    def sort_last_row(self) -> np.ndarray:
        """Sorts the elements of the last row. """
        self._last_row = np.sort(self._last_row)
        return self._last_row

    def median_of_last_row(self) -> tuple:
        """Finds the median of the last row. """
        return np.median(self._last_row), self.calculate_median_manually()

    def calculate_median_manually(self):
        """Calculates the median of the last row. """
        sorted_row = np.sort(self._last_row)
        mid = len(sorted_row) // 2
        if len(sorted_row) % 2 == 0:
            return (sorted_row[mid - 1] + sorted_row[mid]) / 2
        return sorted_row[mid]


def is_command(value: str) -> int:
    """Checks the value to be between 0 and 3. """
    while True:
        try:
            value = int(value)
            if 0 < value < 3:
                return value
            value = input("Value should be between 0 and 3, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_size(value: str) -> int:
    """ Checks the value to make sure it is greater than 0. """
    while True:
        try:
            value = int(value)
            if value > 0:
                return value
            value = input("Value should be greater than 1, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_value(value: str) -> float:
    """ Checks the value to make sure it is greater than 0. """
    while True:
        try:
            value = float(value)
            if value > 0:
                return value
            value = input("Value should be greater than 0, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def menu() -> None:
    """Menu for user input. """
    print("\n1: Start program")
    print("2: Exit\n")


def main():
    while True:
        menu()
        command = is_command(input("Enter value: "))
        if command == 1:
            n, m = is_size(input("Enter n: ")), is_size(input("Enter m: "))
            mat = UpdateMatrix(n, m)
            print('Matrix: \n', mat)
            print(f"\nLast row sorted: {mat.sort_last_row()}")
            print(f"\nMedians of last row: {mat.median_of_last_row()}")
        if command == 2:
            break