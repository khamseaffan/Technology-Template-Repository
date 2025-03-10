"""Implementation for Calculator Module."""

import calculator

class Calculator(calculator.Calculator):
    """Calculator class for arithmetic operations."""

    def __init__(self) -> None:
        """Initialize instance."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        result = a + b
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a and b."""
        result = a - b
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        result = a * b
        return result

    def divide(self, a: float, b: float) -> float:
        """Return the division of a by b."""
        result = a // b
        return result
    
def get_calculator() -> calculator.Calculator:
    return Calculator()