import abc
from io import TextIOWrapper


class BaseCalculations(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def sum_two_numbers(a: int | float, b: int | float) -> int | float:
        pass

    @staticmethod
    @abc.abstractmethod
    def sub_two_numbers(a: int | float, b: int | float) -> int | float:
        pass

    @staticmethod
    @abc.abstractmethod
    def div_two_numbers(a: int | float, b: int | float) -> int | float:
        pass

    @staticmethod
    @abc.abstractmethod
    def mul_two_numbers(a: int | float, b: int | float) -> int | float:
        pass

    @staticmethod
    @abc.abstractmethod
    def percent_from_number(a: int| float, b: int | float) -> int | float:
        pass


class BaseDeceminalCalculation(BaseCalculations):

    @staticmethod
    def sum_two_numbers(a: int | float, b: int | float) -> int | float:
        return a + b

    @staticmethod
    def sub_two_numbers(a: int | float, b: int | float) -> int | float:
        return a - b

    @staticmethod
    def div_two_numbers(a: int | float, b: int | float) -> int | float:
        return a / b

    @staticmethod
    def mul_two_numbers(a: int | float, b: int | float) -> int | float:
        return a * b

    @staticmethod
    def percent_from_number(a: int | float, b: int | float) -> int | float:
        return a / 100 * b


class HistoryManager(abc.ABC):
    @staticmethod
    def update(old_data: list[str], new_data: str) -> None:
        old_data.insert(0, new_data)

    @staticmethod
    def clear(data: list[str]) -> None:
        data.clear()

    @staticmethod
    @abc.abstractmethod
    def get_from_file(filename: str) -> list[str]:
        pass

    @staticmethod
    @abc.abstractmethod
    def save(data: list[str]) -> None:
        pass


class TxtFileHistoryManager(HistoryManager):
    @staticmethod
    def save(data: list[str]) -> None:
        with open("history.txt", "w") as history_file:
            note: str
            for note in data:
                history_file.write(f"{note}\n")

    @staticmethod
    def get_from_file(filename: str) -> list[str]:
        with open(filename) as history_file:
            return list(history_file)


class History:
    def __init__(self, historyManager: HistoryManager = TxtFileHistoryManager()):
        self.__data: list[str] = list()
        self.__history_manager: HistoryManager = historyManager

    def update(self, new_data: str) -> None:
        self.__history_manager.update(self.__data, new_data)

    def clear(self) -> None:
        self.__history_manager.clear(self.__data)

    def set_data(self, filename: str) -> None:
        self.__data = self.__history_manager.get_from_file(filename)

    def save(self) -> None:
        self.__history_manager.save(self.__data)


class Calculator:
    """
    Creates an object calculator, taking a history of calculations as a parameter
    """
    def __init__(
            self,
            history: History = History(TxtFileHistoryManager()),
            calculations: BaseCalculations = BaseDeceminalCalculation()
    ) -> None:
        self.__a: int | float
        self.__b: int | float
        self.__calculations: BaseCalculations = calculations
        self.__history: History = history

    def set_values(self, a: int | float, b: int | float) -> None:
        self.__a,self.__b = a, b

    def sum_two_numbers(self) -> int | float:
        return self.__calculations.sum_two_numbers(self.__a, self.__b)

    def sub_two_numbers(self) -> int | float:
        return self.__calculations.sub_two_numbers(self.__a, self.__b)

    def div_two_numbers(self) -> int | float:
        return self.__calculations.div_two_numbers(self.__a, self.__b)

    def mul_two_numbers(self) -> int | float:
        return self.__calculations.mul_two_numbers(self.__a, self.__b)

    def percent_from_number(self) -> int | float:
        return self.__calculations.percent_from_number(self.__a, self.__b)

    def update_history(self, new_data: str):
        self.__history.update(new_data)

    def load_history(self, filename: str):
        self.__history.set_data(filename)

    def save_history(self):
        self.__history.save()

    def clear_history(self):
        self.__history.clear()


class BaseInput(abc.ABC):
    pass
