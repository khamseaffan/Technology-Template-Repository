"""Module for calculator functionality."""

class Calculator:
    """Calculator class for arithmetic operations."""

    def __init__(self) -> None:
        """Initialize instance."""
        self.logger = None
        self.notifier = None

    def add(self, a: int, b: int) -> int:
        """Return the sum of a and b."""
        result = a + b
        if self.logger:
            self.logger.log(f"Addition: {a} + {b} = {result}")
        if self.notifier:
            self.notifier.notify(result)
        return result

    def subtract(self, a: int, b: int) -> int:
        """Return the difference of a and b."""
        result = a - b
        if self.logger:
            self.logger.log(f"Subtraction: {a} - {b} = {result}")
        return result

    def multiply(self, a: int, b: int) -> int:
        """Return the product of a and b."""
        result = a * b
        if self.logger:
            self.logger.log(f"Multiplication: {a} * {b} = {result}")
        return result

    def divide(self, a: int, b: int) -> int:
        """Return the division of a by b."""
        result = a // b
        if self.logger:
            self.logger.log(f"Division: {a} / {b} = {result}")
        return result
