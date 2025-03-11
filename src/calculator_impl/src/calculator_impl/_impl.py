"""Implementation for Calculator Module."""

import calculator  
import notifier


class CalculatorImpl(calculator.Calculator):
    """Concrete implementation of the Calculator."""

    def __init__(self) -> None:
        """Initialize instance."""
        self._notifier = None  # Default is no notifier

    @property
    def notifier_instance(self) -> notifier.Notifier | None:
        """Get the notifier instance."""
        return self._notifier

    @notifier_instance.setter
    def notifier_instance(self, value: notifier.Notifier | None) -> None:
        """Set the notifier instance."""
        self._notifier = value

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        result = a + b
        if self._notifier:
            self._notifier.notify(result)
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a and b."""
        result = a - b
        if self._notifier:
            self._notifier.notify(result)
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        result = a * b
        if self._notifier:
            self._notifier.notify(result)
        return result

    def divide(self, a: float, b: float) -> float:
        """Return the division of a by b."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        if self._notifier:
            self._notifier.notify(result)
        return result


def get_calculator() -> calculator.Calculator:
    """Return an instance of a CalculatorImpl."""
    return CalculatorImpl()  # Use the actual implementation
