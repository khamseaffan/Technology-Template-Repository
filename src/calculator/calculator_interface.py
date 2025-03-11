from abc import ABC, abstractmethod

class CalculatorInterface(ABC):
    """Abstract base class for a calculator."""

    @abstractmethod
    def add(self, a: float | int, b: float | int) -> float | int:
        """Perform addition operation."""
        pass

    @abstractmethod
    def subtract(self, a: float | int, b: float | int) -> float | int:
        """Perform subtraction operation."""
        pass

    @abstractmethod
    def multiply(self, a: float | int, b: float | int) -> float | int:
        """Perform multiplication operation."""
        pass

    @abstractmethod
    def divide(self, a: float | int, b: float | int) -> float | int:
        """Perform division operation."""
        pass
