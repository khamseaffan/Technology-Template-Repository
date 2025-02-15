class Calculator:
    """A simple calculator for performing basic arithmetic operations."""

    def __init__(self) -> None:
        self.logger = None
        self.notifier = None

    def add(self, a: int, b: int) -> int:
        result = a + b
        if self.logger:
            self.logger.log(f"Addition: {a} + {b} = {result}")
        if self.notifier:
            self.notifier.notify(result)
        return result

    def subtract(self, a: int, b: int) -> int:
        result = a - b
        if self.logger:
            self.logger.log(f"Subtraction: {a} - {b} = {result}")
        return result

    def multiply(self, a: int, b: int) -> int:
        result = a * b
        if self.logger:
            self.logger.log(f"Multiplication: {a} * {b} = {result}")
        return result
    
    def divide(self, a: int, b: int) -> int:
        result = a / b
        if self.logger:
            self.logger.log(f"Division: {a} / {b} = {result}")
        return result