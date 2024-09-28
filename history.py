import abc

from output_input import BaseOuput


class HistoryManager(abc.ABC):
    "Класс, отвечающий за действия с историей вычислений калькулятора"

    @staticmethod
    def get_history(data: list[str]) -> list[str]:
        return data

    @staticmethod
    def show_history(data: list[str], output_object: BaseOuput) -> None:
        """Метод, выводящий историю вычислений

        :param data: данные истории вычислений
        :param output_object: объект класса для вывода
        """
        note: str
        for note in data:
            output_object.print_text(note)

    @staticmethod
    def update(old_data: list[str], new_data: str) -> None:
        """Метод, обновляющий историю вычислений калькулятора новой записью

        :param old_data: имеющаяся история вычислений
        :param new_data: новая запись
        """
        old_data.insert(0, new_data)

    @staticmethod
    def clear(data: list[str]) -> None:
        """Метод, очищаюйщий историю вычислений

        :param data: используемая история вычислений
        """
        data.clear()

    @staticmethod
    @abc.abstractmethod
    def get_from_file(filename: str) -> list[str]:
        """Метод, позволяющий получить историю вычислений из файла

        :param filename: имя файла
        :return: история вычислений в формате списка со строками
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def save(data: list[str]) -> None:
        """Метод, сохраняющий историю вычислений

        :param data: используемая история вычислений
        """
        pass


class TxtFileHistoryManager(HistoryManager):
    "Класс для работы с историей, представленной в виде документа формата .txt"
    @staticmethod
    def save(data: list[str]) -> None:
        with open("history.txt", "w") as history_file:
            note: str
            for note in data:
                history_file.write(note)

    @staticmethod
    def get_from_file(filename: str) -> list[str]:
        with open(filename) as history_file:
            return list(note.strip("\n") for note in history_file)


class History:
    "Класс, отвечающий за хранение и обработку данных"

    def __init__(self, historyManager: HistoryManager = TxtFileHistoryManager()):
        self.__data: list[str] = list()
        self.__history_manager: HistoryManager = historyManager

    def get(self):
        return self.__history_manager.get_history(self.__data)

    def show(self, output_object) -> None:
        self.__history_manager.show_history(self.__data, output_object)

    def update(self, new_data: str) -> None:
        self.__history_manager.update(self.__data, new_data)

    def clear(self) -> None:
        self.__history_manager.clear(self.__data)

    def set_data(self, filename: str) -> None:
        self.__data = self.__history_manager.get_from_file(filename)

    def save(self) -> None:
        self.__history_manager.save(self.__data)