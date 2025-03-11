"""Implementation for Calculator Module."""

import calculator
import logger
import notifier


class CalculatorImpl(calculator.Calculator):
    """Concrete implementation of the Calculator."""

    def __init__(self) -> None:
        """Initialize instance."""
        self._notifier = None
        self._logger = None

    @property
    def notifier_instance(self) -> notifier.Notifier | None:
        """Get the notifier instance."""
        return self._notifier

    @notifier_instance.setter
    def notifier_instance(self, value: notifier.Notifier | None) -> None:
        """Set the notifier instance."""
        self._notifier = value

    @property
    def logger_instance(self) -> logger.Logger | None:
        """Get the logger instance."""
        return self._logger

    @logger_instance.setter
    def logger_instance(self, value: logger.Logger | None) -> None:
        """Set the logger instance."""
        self._logger = value

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        result = a + b
        if self._notifier:
            self._notifier.notify(result)
        if self._logger:
            self._logger.log(f"Addition: {a} + {b} = {result}")
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a and b."""
        result = a - b
        if self._notifier:
            self._notifier.notify(result)
        if self._logger:
            self._logger.log(f"Subtraction: {a} - {b} = {result}")
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        result = a * b
        if self._notifier:
            self._notifier.notify(result)
        if self._logger:
            self._logger.log(f"Multiplication: {a} * {b} = {result}")
        return result

    def divide(self, a: float, b: float) -> float:
        """Return the division of a by b."""
        if b == 0:
            error_message = "Cannot divide by zero"
            raise ValueError(error_message)
        result = a / b
        if self._notifier:
            self._notifier.notify(result)
        if self._logger:
            self._logger.log(f"Division: {a} / {b} = {result}")
        return result


def get_calculator() -> calculator.Calculator:
    """Return an instance of a CalculatorImpl."""
    return CalculatorImpl()  # Use the actual implementation
