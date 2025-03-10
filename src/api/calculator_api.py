from src.calculator.calculator import Calculator
from src.logger.logger import Logger
from src.notifier.notifier import Notifier

class CalculatorAPI:
    def __init__(self) -> None:
        self.calculator = Calculator()
        self.logger = Logger()
        self.notifier = Notifier()

    def calculate(self, operation: str, num1: float, num2: float) -> dict:
        if not isinstance(num1, int | float) or not isinstance(num2, int | float):
            raise TypeError("Inputs must be numbers")

        try:
            if operation == "add":
                result = self.calculator.add(num1, num2)
            elif operation == "subtract":
                result = self.calculator.subtract(num1, num2)
            elif operation == "multiply":
                result = self.calculator.multiply(num1, num2)
            elif operation == "divide":
                if num2 == 0:
                    error_msg = "Division by zero is not allowed."
                    raise ValueError(error_msg)
                result = self.calculator.divide(num1, num2)
            else:
                error_msg = "Unsupported operation."
                raise ValueError(error_msg)

            self.logger.log(f"Performed {operation}: {num1} {operation} {num2} = {result}")
            return {"operation": operation, "num1": num1, "num2": num2, "result": result}

        except (ValueError, TypeError) as e:
            self.logger.log(f"Error performing {operation}: {e!s}")
            return {"error": str(e)}
