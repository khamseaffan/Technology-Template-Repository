from .calculator_interface import Calculator

"""Module for calculator functionality."""


class SimpleCalculator(Calculator):
    """Calculator class for arithmetic operations."""

    def __init__(self) -> None:
        """Initialize instance."""
        self.logger = None
        self.notifier = None

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        result = a + b
        if self.logger:
            self.logger.log(f"Addition: {a} + {b} = {result}")
        if self.notifier:
            self.notifier.notify(str(result))
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a and b."""
        result = a - b
        if self.logger:
            self.logger.log(f"Subtraction: {a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        result = a * b
        if self.logger:
            self.logger.log(f"Multiplication: {a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Return the division of a by b."""
        result = a // b
        if self.logger:
            self.logger.log(f"Division: {a} / {b} = {result}")
        return result


__all__ = ["SimpleCalculator"]