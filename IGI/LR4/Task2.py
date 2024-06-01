import re
from zipfile import ZipFile


class TextAnalyzer:
    def __init__(self, filename: str) -> None:
        self.__text = None
        self.__filename = filename

    @property
    def text(self) -> str:
        return self.__text

    @property
    def filename(self) -> str:
        return self.__filename

    def read_file(self, filename: str) -> str:
        """Read text from a file. """
        with open(filename, 'r') as file:
            self.__text = file.read()
        return self.__text

    def write_result_file(self, filename: str) -> None:
        """Write text to a file. """
        t = self.read_file("text.txt")
        with open(filename, 'w') as file:
            file.write(f"Count sentences in text: {self.get_count_sentences(t)}")
            file.write(f"\nCount sentences in text of each type: ")
            for keys, values in self.get_type_sentences(t).items():
                file.write(f"\n{keys}: {values}")
            file.write(f"\nAverage sentence length in characters: ")
            for keys, values in self.avg_sentence_length(t).items():
                file.write(f"\n{keys}: {values}")
            file.write(f"\nAverage word length in text in characters: {self.avg_word_length(t)}")
            file.write(f"\nCount of emoticons in a text: {self.search_smile(t)}")
            file.write(f"\nAll words starting with a lowercase consonant: {self.search_word(t)}")
            file.write(f"\nCar numbers: {self.search_car_number(t)}")
            file.write(f"\nWords that have a minimum length: {self.search_min_word(t)}")
            file.write(f"\nAll words followed by a comma: {self.search_comma(t)}")
            file.write(f"\nLongest word that ends with 'y': {self.search_y(t)}")
            file.write(f"\nIs valid MAC address: {self.is_valid_mac(t)}")
            file.write(f"\nNumber of words in the text: {self.word_count(t)}")
            file.write(f"\nLongest word and its position: {self.longest_word_info(t)}")
            file.write(f"\nEvery odd word: {self.odd_words(t)}")

    def output(self) -> None:
        """Print text to console. """
        t = self.read_file("text.txt")
        print(f"\nCount sentences in text: {self.get_count_sentences(t)}")
        print(f"\nCount sentences in text of each type:")
        for keys, values in self.get_type_sentences(t).items():
            print(f"\t{keys}: {values}")
        print(f"\nAverage sentence length in characters: ")
        for keys, values in self.avg_sentence_length(t).items():
            print(f"\t{keys}: {values}")
        print(f"\nAverage word length in text in characters: {self.avg_word_length(t)}")
        print(f"\nCount of emoticons in a text: {self.search_smile(t)}")
        print(f"\nAll words starting with a lowercase consonant: {self.search_word(t)}")
        print(f"\nCar numbers: {self.search_car_number(t)}")
        print(f"\nWords that have a minimum length: {self.search_min_word(t)}")
        print(f"\nAll words followed by a comma: {self.search_comma(t)}")
        print(f"\nLongest word that ends with 'y': {self.search_y(t)}")
        print(f"\nIs valid MAC address: {self.is_valid_mac(t)}")
        print(f"\nNumber of words in the text: {self.word_count(t)}")
        print(f"\nLongest word and its position: {self.longest_word_info(t)}")
        print(f"\nEvery odd word: {self.odd_words(t)}")

    @staticmethod
    def write_zip(filename: str) -> None:
        """Write zip file. """
        with ZipFile("results.zip", 'w') as myzip:
            myzip.write(filename)

    @staticmethod
    def info_zip(filename: str) -> None:
        """Print info about zip file. """
        with ZipFile(filename, 'r') as myzip:
            for item in myzip.infolist():
                print(f"\nFile Name: {item.filename} Date: {item.date_time} Size: {item.file_size}")

    @staticmethod
    def read_zip() -> None:
        """Read zip file. """
        with ZipFile("results.zip", 'r') as myzip:
            print(myzip.read("results.txt"))

    @staticmethod
    def get_count_sentences(text: str) -> int:
        """Count the sentences number of text. """
        return len(re.findall(r'\w+[.!?]', text))

    @staticmethod
    def get_type_sentences(text: str) -> dict:
        """Count the type of sentences number of text. """
        patterns = dict()
        narrative_pattern = len(re.findall(r'\w+\.', text))#регулярные выражения
        question_pattern = len(re.findall(r'\w+\?', text))
        exclamation_pattern = len(re.findall(r'\w+!', text))
        patterns["narrative"] = narrative_pattern
        patterns["question"] = question_pattern
        patterns["exclamation"] = exclamation_pattern
        return patterns

    @staticmethod
    def avg_sentence_length(text: str) -> dict:
        """Average sentence length of text. """
        text_pattern = [sentence.strip() for sentence in re.split(r'[.!?]', text) if sentence.strip()]
        avg_sentence_length = dict()
        for sentence in text_pattern:
            words_pattern = re.findall(r'\w+', sentence)
            total_characters = sum(len(word) for word in words_pattern if re.findall(r'[A-Za-z]+', word))
            total_words = sum(1 for word in words_pattern if re.findall(r'[A-Za-z]+', word))
            if total_words > 0:
                avg = total_characters / total_words
                avg_sentence_length[sentence] = avg
        return avg_sentence_length

    @staticmethod
    def avg_word_length(text: str) -> float:
        """Average word length of text. """
        word_pattern = [word for word in re.findall(r'\w+', text)]
        total_characters = sum(len(word) for word in word_pattern)
        if len(word_pattern) > 0:
            avg = total_characters / len(word_pattern)
            return avg
        return 0

    @staticmethod
    def search_smile(text: str) -> int:
        """Search for SMILES in text. """
        return len([word for word in re.findall(r'[:;]-*\(+|[:;]-*\)+|[:;]-*\[+|[:;]-*]+', text)])

    @staticmethod
    def search_word(text: str) -> list:
        """Search for words in text. """
        return [word for word in re.findall(r'\b[bcdfghjklmnpqrstvwxyz]\w*', text)]

    @staticmethod
    def search_car_number(text: str):
        """Search for car numbers in text. """
        number_pattern = re.findall(r'[0-9]{4}\s[ABEIKMHOPCTX]{2}-[1-7]', text)
        if number_pattern:
            return number_pattern[:]
        return None

    @staticmethod
    def search_min_word(text: str) -> int:
        """Search for min word in text. """
        word_pattern = [word for word in re.findall(r'\w+', text)]
        return sum(1 for word in word_pattern if len(word) == min(len(word) for word in word_pattern))

    @staticmethod
    def search_comma(text: str) -> list:
        """Search for comma in text. """
        return [word.replace(',', '').strip() for word in re.findall(r'\w+,\s*', text)]

    @staticmethod
    def search_y(text: str) -> str:
        """Search for y value in text. """
        return ''.join(max([word for word in re.findall(r'\w+y\s', text)], key=lambda x: len(x)))

    @staticmethod
    def is_valid_mac(text: str) -> bool:
        """Check if the given text contains a valid MAC address. """
        mac_pattern = re.compile(r'([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}')
        return bool(mac_pattern.search(text))

    @staticmethod
    def word_count(text: str) -> int:
        """Count the number of words in the text. """
        words = re.findall(r'\w+', text)
        return len(words)

    @staticmethod
    def longest_word_info(text: str) -> tuple:
        """Find the longest word and its position in the text. """
        words = re.findall(r'\w+', text)
        if words:
            longest_word = max(words, key=len)
            position = words.index(longest_word) + 1
            return longest_word, position
        return '', -1

    @staticmethod
    def odd_words(text: str) -> list:
        """Return every odd word from the text. """
        words = re.findall(r'\w+', text)
        return words[::2]


def is_command(value: str) -> int:
    """Checks the value to be between 0 and 5. """
    while True:
        try:
            value = int(value)
            if 0 < value < 5:
                return value
            value = input("Value should be between 0 and 5, input value: ")
        except ValueError:
            value = input("Invalid input, please enter a valid value: ")


def menu() -> None:
    """Menu for user input. """
    print("\n1: Read text from file")
    print("2: Start the task")
    print("3: Get the info about zip")
    print("4: Exit\n")


def main() -> None:
    txt = None
    while True:
        menu()
        command = is_command(input("Enter value: "))
        if command == 1:
            txt = TextAnalyzer("text.txt")
        if command == 2:
            if txt is None:
                print("\nText not found, please try again")
                continue
            txt.output()
            txt.write_result_file("results.txt")
            txt.write_zip("results.txt")
        if command == 3:
            if txt is None:
                print("\nText not found, please try again")
                continue
            txt.info_zip("results.zip")
        if command == 4:
            break

