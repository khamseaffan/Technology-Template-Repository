from src.calculator.calculator import Calculator
from src.logger.logger import Logger
from src.notifier.notifier import Notifier

class CalculatorAPI:
    def __init__(self):
        self.calculator = Calculator()
        self.logger = Logger()
        self.notifier = Notifier()

    def calculate(self, operation: str, num1: float, num2: float) -> dict:
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Inputs must be numbers")

        try:
            if operation == "add":
                result = self.calculator.add(num1, num2)
            elif operation == "subtract":
                result = self.calculator.subtract(num1, num2)
            elif operation == "multiply":
                result = self.calculator.multiply(num1, num2)
            elif operation == "divide":
                if num2 == 0:
                    raise ValueError("Division by zero is not allowed.")
                result = self.calculator.divide(num1, num2)
            else:
                raise ValueError("Unsupported operation")

            self.logger.log(f"Performed {operation} on {num1} and {num2}: Result = {result}")
            self.notifier.notify(f"Calculation performed: {operation}({num1}, {num2}) = {result}")

            return {"operation": operation, "num1": num1, "num2": num2, "result": result}

        except Exception as e:
            self.logger.log(f"Error performing {operation}: {str(e)}")
            return {"error": str(e)}
