import abc


class BaseCalculations(abc.ABC):
    "Класс с базовыми математическими операциями"

    @staticmethod
    @abc.abstractmethod
    def sum_two_numbers(a: int | float, b: int | float) -> int | float:
        """Базовый метод для сложения чисел

        :param a: число a
        :param b: число b
        :return: сумма
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def sub_two_numbers(a: int | float, b: int | float) -> int | float:
        """Базовый метод для разности двух чисел

        :param a: число a
        :param b: число b
        :return: разность
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def div_two_numbers(a: int | float, b: int | float) -> int | float:
        """Базовый метод для чатсного двух чисел

        :param a: число a
        :param b: число b
        :return: частное
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def mul_two_numbers(a: int | float, b: int | float) -> int | float:
        """Базовый метод для произведения двух чисел

        :param a: число a
        :param b: число b
        :return: произведение
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def percent_from_number(a: int| float, b: int | float) -> int | float:
        """Базовый метод для нахожлдения процента от числа

        :param a: процент
        :param b: число
        :return: результат
        """
        pass


class BaseDeceminalCalculation(BaseCalculations):
    "Класс с методами математических опреаций для десятичных чисел"

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
        return b / 100 * a