import abc

import res


class BaseInput(abc.ABC):
    "Базовый класс для ввода данных"

    @staticmethod
    @abc.abstractmethod
    def get_command(promt: str = "") -> str:
        """Метод для получения ввода

        :param promt: подсказка для ввода
        :return: полученный ввод
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def get_numbers(promt: str = res.numbers_input_command) -> tuple[int | float, int | float]:
        """Метод для получения чисел из ввода и их преобразования в кортеж

        :param promt: подсказка для ввода чисел
        :return: кортеж с введенными числами
        """
        pass


class ConsoleInput(BaseInput):
    "Класс для ввода данных с консоли"

    @staticmethod
    def get_command(promt: str = "") -> str:
        return input(promt).strip()
    
    @staticmethod
    def get_numbers(promt: str = res.numbers_input_command) -> tuple[int | float, int | float]:
        first_number: int | float
        second_number: int | float

        str_numbers: tuple[str, ...] = tuple(ConsoleInput.get_command(promt).split())

        first_number = float(str_numbers[0]) if "." in str_numbers[0] else int(str_numbers[0])
        second_number = float(str_numbers[1]) if "." in str_numbers[0] else int(str_numbers[1])
        return (first_number, second_number)


class BaseOuput(abc.ABC):
    "Базовый класс для вывода данных"

    @staticmethod
    @abc.abstractmethod
    def print_text(text: str) -> None:
        """Базовый метод для вывода данных>

        :param text: выходные данные (в формате строки)
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def print_answer(a: int | float, b: int | float, answer: int | float, operation: str) -> None:
        """Базовый метод для вывода результате вычислений в формате: a + b = c

        :param a: число a
        :param b: число b
        :param answer: результат вычислений
        :param operation: производимая математическая операция
        """
        pass


class ConsoleOutput(BaseOuput):
    "Класс для вывода данных в консоль"

    @staticmethod
    def print_text(text: str) -> None:
        print(text)

    @staticmethod
    def print_answer(a: int | float, b: int | float, answer: int | float, operation: str) -> None:
        print(f"{a} {operation} {b} = {round(answer, 3)}")