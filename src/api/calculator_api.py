from typing import NoReturn
from src.calculator.calculator import SimpleCalculator
from src.logger.logger import SimpleLogger
from src.notifier.notifier import SimpleNotifier


class CalculatorAPI:
    def __init__(self) -> None:
        self.calculator = SimpleCalculator()
        self.logger = SimpleLogger()
        self.notifier = SimpleNotifier()

    def calculate(
        self, operation: str, num1: float, num2: float
    ) -> dict[str, str | float]:
        if not isinstance(num1, int | float) or not isinstance(num2, int | float):
            msg = "Inputs must be numbers"
            raise TypeError(msg)

        def _raise(ex: type[Exception], message: str) -> NoReturn:
            raise ex(message)

        result = None
        try:
            if operation == "add":
                result = self.calculator.add(num1, num2)
            elif operation == "subtract":
                result = self.calculator.subtract(num1, num2)
            elif operation == "multiply":
                result = self.calculator.multiply(num1, num2)
            elif operation == "divide":
                if num2 == 0:
                    _raise(ValueError, "Division by zero is not allowed.")
                result = self.calculator.divide(num1, num2)
            else:
                _raise(ValueError, "Unsupported operation.")
        except (ValueError, TypeError) as e:
            self.logger.log(f"Error: {e}")
            return {"error": str(e)}
        else:
            self.logger.log(
                f"Performed {operation}: {num1} {operation} {num2} = {result}"
            )
            return {
                "operation": operation,
                "num1": num1,
                "num2": num2,
                "result": result,
            }
