from errors import is_command
from menu import menu
import Task1
import Task2
import Task3
import Task4
import Task5


def program():
    while True:
        menu()
        command = is_command(input("\nEnter value: "))
        if command == 1:
            Task1.main()
        if command == 2:
            Task2.main()
        if command == 3:
            Task3.main()
        if command == 4:
            Task4.main()
            pass
        if command == 5:
            Task5.main()
            pass
        if command == 6:
            break


if __name__ == "__main__":
    program()