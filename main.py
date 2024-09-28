import abc

import res
from calculations import BaseDeceminalCalculation
from calculator import Calculator
from history import History, TxtFileHistoryManager
from output_input import BaseInput, BaseOuput, ConsoleInput, ConsoleOutput


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
                    self._calculator.show_hisotry(self._output)
                
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
    CodeProccesing(Calculator(History(TxtFileHistoryManager()), BaseDeceminalCalculation()), ConsoleInput(), ConsoleOutput()).run()


if __name__ == "__main__":
    main()
