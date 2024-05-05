from errors import is_correct_command
import Task1
import Task2
import Task3
import Task4
import Task5

def commands_list():
    """
    Returns menu
    """
    print("\n1 - run Task1")
    print("2 - run Task2")
    print("3 - run Task3")
    print("4 - run Task4")
    print("5 - run Task5")
    print("6: Exit")

def main():
    tasks = {
        1: Task1.main,
        2: Task2.main,
        3: Task3.main,
        4: Task4.main,
        5: Task5.main,
    }

    while True:
        commands_list()
        command = is_correct_command(input("\nEnter value: "))
        if command in tasks:
            tasks[command]()
        elif command == 6:
            break

if __name__ == '__main__':
    main()