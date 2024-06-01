from abc import ABC, abstractmethod
import math
import numpy as np
from matplotlib import pyplot as plt


class GeometricFigure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color


class Triangle(GeometricFigure):
    figure = "Треугольник"

    def __init__(self, side, angle_b, angle_c, color):
        self.color = Color(color)
        self._side = side
        self._angle_b = angle_b
        self._angle_c = angle_c

    def calculate_area(self):
        """Calculate the area of triangle. """
        return 0.5 * self._side ** 2 * math.sin(math.radians(self._angle_b)) * math.sin(math.radians(self._angle_c)) / math.sin(math.radians(180 - self._angle_b - self._angle_c))

    def get_info(self):
        """Print info about the figure. """
        return "{type} {color} цвета со стороной {side} и углами {angle_b} и {angle_c} градусов".format(
            type=self.figure,
            color=self.color.color,
            side=self._side,
            angle_b=self._angle_b,
            angle_c=self._angle_c
        )

    def plot(self):
        """Plot the triangle. """
        b_rad = math.radians(self._angle_b)
        c_rad = math.radians(self._angle_c)

        x = [0, self._side * math.sin(b_rad) / (math.sin(b_rad) + math.sin(c_rad)), self._side]
        y = [0, self._side * math.sin(c_rad) / (math.sin(b_rad) + math.sin(c_rad)), 0]

        plt.plot(x + x[:1], y + y[:1], color=self.color.color)
        plt.fill(x, y, color=self.color.color, alpha=0.4)

        plt.axis('equal')
        plt.title(input("Подпись графика: "))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()

def is_command(value: str) -> int:
    """Checks the value to be between 0 and 4. """
    while True:
        try:
            value = int(value)
            if 0 < value < 4:
                return value
            value = input("Value should be between 0 and 4, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_angle(value: str) -> float:
    """Checks the value to be between 0 and 90. """
    while True:
        try:
            value = float(value)
            if 0 < value < 90:
                return value
            value = input("Angle should be acute, input angle: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_side(value: str) -> float:
    """Checks the value to be greater than 0. """
    while True:
        try:
            value = float(value)
            if value > 0:
                return value
            value = input("Side should be greater than 0, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def is_color(value: str) -> str:
    while True:
        if value in ['blue', 'black', 'pink', 'red', 'green', 'yellow', 'orange']:
            return value
        value = input("Color should be blue, black, pink, red, green, yellow, orange, input value: ")


def menu() -> None:
    """Menu for user input. """
    print("\n1: Input the values")
    print("2: Get info about a triangle")
    print("3: Exit\n")


def main():
    triangle = None
    while True:
        menu()
        command = is_command(input("Enter value: "))
        if command == 1:
            side = is_side(input("Enter the length of the side of the triangle: "))
            angle_b = is_angle(input("Enter the angle B of the triangle in degrees: "))
            angle_c = is_angle(input("Enter the angle C of the triangle in degrees: "))
            color = is_color(input("Enter triangle color: "))
            triangle = Triangle(side, angle_b, angle_c, color)
        if command == 2:
            if triangle is None:
                print("\nFigure not found, please try again")
                continue
            print("Area of a triangle:", triangle.calculate_area())
            print(triangle.get_info())
            triangle.plot()
            with open("info.txt", "w") as file:
                file.write("Area of a triangle: {}\n".format(triangle.calculate_area()))
                file.write("{}\n".format(triangle.get_info()))
        if command == 3:
            break