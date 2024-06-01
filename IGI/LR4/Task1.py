import csv
import pickle


class TeacherLoad:
    def __init__(self, last_name: str, class_name: str, hours: int) -> None:
        self._last_name = last_name
        self._class_name = class_name
        self._hours = hours

    @property #свойство геттер
    def last_name(self):
        return self._last_name

    @property
    def class_name(self):
        return self._class_name

    @property
    def hours(self):
        return self._hours

    @hours.setter #свойство сеттер
    def hours(self, value: int):
        if value < 0:
            raise ValueError("Hours cannot be negative")
        self._hours = value

    def __str__(self) -> str:
        return f"{self.last_name} teaches {self.class_name} for {self.hours} hours."


class SchoolLoad:
    def __init__(self, loads: list = None):
        self._loads = loads if loads else []

    @property
    def loads(self):
        return self._loads

    def add_load(self, load: TeacherLoad):
        self._loads.append(load)

    def total_load_per_teacher(self) -> dict:
        load_dict = {}
        for load in self._loads:
            if load.last_name in load_dict:
                load_dict[load.last_name] += load.hours
            else:
                load_dict[load.last_name] = load.hours
        return load_dict

    def max_load_teacher(self) -> str:
        load_dict = self.total_load_per_teacher()
        max_teacher = max(load_dict, key=load_dict.get)
        return f"{max_teacher} has the maximum load of {load_dict[max_teacher]} hours."

    def min_load_teacher(self) -> str:
        load_dict = self.total_load_per_teacher()
        min_teacher = min(load_dict, key=load_dict.get)
        return f"{min_teacher} has the minimum load of {load_dict[min_teacher]} hours."

    def get_teacher_load(self, last_name: str) -> str:
        load_dict = self.total_load_per_teacher()
        if last_name in load_dict:
            return f"{last_name} has a total load of {load_dict[last_name]} hours."
        return f"No teacher found with the last name '{last_name}'."


class FileMixin:
    def write_to_file(self, data: list, file_name: str) -> None:
        raise NotImplementedError

    def read_from_file(self, file_name: str) -> 'SchoolLoad':
        raise NotImplementedError


class CSVSerializer(FileMixin):
    def write_to_file(self, data: list, file_name: str) -> None:
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['last_name', 'class_name', 'hours'])
            for load in data:
                writer.writerow([load.last_name, load.class_name, load.hours])

    def read_from_file(self, file_name: str) -> 'SchoolLoad':
        loads = []
        try:
            with open(file_name, "r", newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    loads.append(TeacherLoad(row['last_name'], row['class_name'], int(row['hours'])))
        except FileNotFoundError:
            raise FileNotFoundError("File not found")
        return SchoolLoad(loads)


class PickleSerializer(FileMixin):
    def write_to_file(self, data: list, file_name: str) -> None:
        with open(file_name, "wb") as file:
            pickle.dump(data, file)

    def read_from_file(self, file_name: str) -> 'SchoolLoad':
        try:
            with open(file_name, "rb") as file:
                loads = pickle.load(file)
                print(loads)
                return SchoolLoad(loads)
        except FileNotFoundError:
            raise FileNotFoundError("File not found")


def menu() -> None:
    print("\n1: Writing to a file using CSV")
    print("2: Reading from a file using CSV")
    print("3: Writing to a file using pickle")
    print("4: Reading from a file using pickle")
    print("5: Display total load per teacher")
    print("6: Display teacher with maximum load")
    print("7: Display teacher with minimum load")
    print("8: Display load of a specific teacher")
    print("9: Exit\n")


def main() -> None:
    data_csv = [
        TeacherLoad("Smith", "Math", 10),
        TeacherLoad("Johnson", "Science", 15),
        TeacherLoad("Williams", "History", 5),
        TeacherLoad("Smith", "Physics", 8),
        TeacherLoad("Johnson", "Chemistry", 7)
    ]
    data_pickle = [
        TeacherLoad("Brown", "English", 12),
        TeacherLoad("Taylor", "Biology", 14),
        TeacherLoad("Miller", "Geography", 9),
        TeacherLoad("Wilson", "Physics", 11),
        TeacherLoad("Moore", "Chemistry", 13)
    ]
  
    school_load = SchoolLoad()
    csv_serializer = CSVSerializer()
    pickle_serializer = PickleSerializer()

    while True:
        menu()
        command = input("Enter value: ")
        if command == '1':
            csv_serializer.write_to_file(data_csv, "school_load.csv")
            print("Data written to school_load.csv")
        elif command == '2':
            school_load = csv_serializer.read_from_file("school_load.csv")
            print("Data read from school_load.csv")
        elif command == '3':
            pickle_serializer.write_to_file(data_pickle, "school_load.pkl")
            print("Data written to school_load.pkl")
        elif command == '4':
            school_load = pickle_serializer.read_from_file("school_load.pkl")
            print("Data read from school_load.pkl")
        elif command == '5':
            for teacher, load in school_load.total_load_per_teacher().items():
                print(f"{teacher}: {load} hours")
        elif command == '6':
            print(school_load.max_load_teacher())
        elif command == '7':
            print(school_load.min_load_teacher())
        elif command == '8':
            last_name = input("Enter the last name of the teacher: ")
            print(school_load.get_teacher_load(last_name))
        elif command == '9':
            break
        else:
            print("Invalid command, please try again.")
