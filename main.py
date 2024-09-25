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
        """Базовый метод для вывода данных

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

    def show(self, output_object: BaseOuput = ConsoleOutput()) -> None:
        self.__history_manager.show_history(self.__data, output_object)

    def update(self, new_data: str) -> None:
        self.__history_manager.update(self.__data, new_data)

    def clear(self) -> None:
        self.__history_manager.clear(self.__data)

    def set_data(self, filename: str) -> None:
        self.__data = self.__history_manager.get_from_file(filename)

    def save(self) -> None:
        self.__history_manager.save(self.__data)


class Calculator:
    """Класс-исполнитель, черех него вызываются методы объектов, определенных в полях класса."""

    def __init__(
            self,
            history: History = History(TxtFileHistoryManager()),
            calculations: BaseCalculations = BaseDeceminalCalculation()
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
    
    def show_hisotry(self, output_object: BaseOuput = ConsoleOutput()) -> None:
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


class BaseProccessing(abc.ABC):
    "Базовый класс для запуска программы"

    def __init__(
            self, main_object: Calculator,
            input_object: BaseInput,
            output_oject: BaseOuput) -> None:
        """Инициализация для работы с прогрммой

        :param main_object: рабочее тело (калькулятор)
        :param input_object: объект вывода
        :param output_oject: объект вывода
        """
        self._calculator: Calculator = main_object
        self._input: BaseInput = input_object
        self._output: BaseOuput = output_oject

        self._calculator.load_history(res.default_history_filename)

    def __del__(self):
        self._calculator.save_history()
        self._output.print_text("Хорошего дня :)")

    @abc.abstractmethod
    def run(self) -> None:
        "Базовый метод для работы программы"
        pass


class CodeProccesing(BaseProccessing):
    "Класс для работы программы через консоль"

    def __init__(
                self, main_object: Calculator,
                input_object: BaseInput = ConsoleInput(),
                output_oject: BaseOuput = ConsoleOutput()) -> None:
        super().__init__(main_object, input_object, output_oject)

    def run(self) -> None:
        main_command: str = self._input.get_command(res.main_command_hint)

        while main_command != "0":
            if main_command == "1":
                self.__run_local()

            elif main_command == "2":
                filename: str = self._input.get_command(res.filename_input_hint)
                self._calculator.load_history(filename)

                self._output.print_text(res.loaded_successfully) if len(self._calculator.get_history()) \
                    else self._output.print_text(res.something_went_wrong) 

            main_command = self._input.get_command(res.main_command_hint)

    def __run_local(self) -> None:
        local_command: str = self._input.get_command(res.local_command_hint)

        while local_command != "0":
            if local_command == "1":
                self.__calculator_run()

            elif local_command == "2":
                self._output.print_text(res.no_notes_in_history) if not len(self._calculator.get_history()) else \
                    self._calculator.show_hisotry()
                
            elif local_command == "3":
                self._calculator.clear_history()
                self._output.print_text(res.cleared_successfully)

            local_command = self._input.get_command(res.local_command_hint)

    def __calculator_run(self) -> None:
        calculator_command: str = self._input.get_command(res.calculator_instructions)
        
        while calculator_command != "0":
            if calculator_command == "1":
                self._calculator.set_values(*self._input.get_numbers())
                self._output.print_answer(*self._calculator.get_values(), self._calculator.sum_two_numbers(), "+")

            elif calculator_command == "2":
                self._calculator.set_values(*self._input.get_numbers())
                self._output.print_answer(*self._calculator.get_values(), self._calculator.sub_two_numbers(), "-")

            elif calculator_command == "3":
                self._calculator.set_values(*self._input.get_numbers())
                self._output.print_answer(*self._calculator.get_values(), self._calculator.mul_two_numbers(), "*")

            elif calculator_command == "4":
                self._calculator.set_values(*self._input.get_numbers())
                self._output.print_answer(*self._calculator.get_values(), self._calculator.div_two_numbers(), "/")

            elif calculator_command == "5":
                self._calculator.set_values(*self._input.get_numbers())
                self._output.print_answer(*self._calculator.get_values(), self._calculator.percent_from_number(), "%")

            calculator_command = self._input.get_command(res.calculator_instructions)


def main() -> None:
    CodeProccesing(Calculator(), ConsoleInput(), ConsoleOutput()).run()


if __name__ == "__main__":
    main()
