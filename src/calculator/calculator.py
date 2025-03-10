from typing import Optional
from .calculator_interface import Calculator
import logger
import notifier

"""Module for calculator functionality."""


class SimpleCalculator(Calculator):
    """Calculator class for arithmetic operations."""

    def __init__(self) -> None:
        """Initialize instance."""
        self._logger: Optional[logger.Logger] = None
        self._notifier: Optional[notifier.Notifier] = None

    @property
    def logger(self) -> Optional[logger.Logger]:
        return self._logger
    
    @logger.setter
    def logger(self, value: Optional[logger.Logger]) -> None:  # Match interface type
        self._logger = value

    @property
    def notifier(self) -> Optional[notifier.Notifier]:
        return self._notifier
    
    @notifier.setter
    def notifier(self, value: Optional[notifier.Notifier]) -> None:  # Match interface type
        self._notifier = value

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