from calculations import BaseCalculations
from history import History
from output_input import BaseOuput


class Calculator:
    """Класс-исполнитель, черех него вызываются методы объектов, определенных в полях класса."""

    def __init__(
            self,
            history: History,
            calculations: BaseCalculations
    ) -> None:
        """Конструктор базового класа

        :param history: параметр истории вычислений, по умолчанию создает пустую историю
        :param calculations: методы вычисления математических операций, по умолчанию для десятичных чисел
        """
        self.__a: int | float
        self.__b: int | float
        self.__answer: int | float
        self.__calculations: BaseCalculations = calculations
        self.__history: History = history

    def set_values(self, a: int | float, b: int | float) -> None:
        """Метод, задающий значения полям чисел

        :param a: число a
        :param b: число b
        """
        self.__a, self.__b = a, b

    def get_values(self) -> tuple[int | float, int | float]:
        """Метод, возвращающий значения чисел

        :return: кортеж с двумя числами
        """
        return (self.__a, self.__b)

    def sum_two_numbers(self) -> int | float:
        self.__answer = self.__calculations.sum_two_numbers(self.__a, self.__b)
        self.__update_history(f"{self.__a} + {self.__b} = {self.__answer}")
        return self.__answer

    def sub_two_numbers(self) -> int | float:
        self.__answer = self.__calculations.sub_two_numbers(self.__a, self.__b)
        self.__update_history(f"{self.__a} - {self.__b} = {self.__answer}")
        return self.__answer

    def div_two_numbers(self) -> int | float:
        self.__answer = self.__calculations.div_two_numbers(self.__a, self.__b)
        self.__update_history(f"{self.__a} / {self.__b} = {self.__answer}")
        return self.__answer

    def mul_two_numbers(self) -> int | float:
        self.__answer = self.__calculations.mul_two_numbers(self.__a, self.__b)
        self.__update_history(f"{self.__a} * {self.__b} = {self.__answer}")
        return self.__answer

    def percent_from_number(self) -> int | float:
        self.__answer = self.__calculations.percent_from_number(self.__a, self.__b)
        self.__update_history(f"{self.__a} % {self.__b} = {self.__answer}")
        return self.__answer
    
    def show_hisotry(self, output_object: BaseOuput) -> None:
        self.__history.show(output_object)

    def get_history(self):
        return self.__history.get()

    def __update_history(self, new_data: str):
        self.__history.update(new_data)

    def load_history(self, filename: str):
        self.__history.set_data(filename)

    def save_history(self):
        self.__history.save()

    def clear_history(self):
        self.__history.clear()