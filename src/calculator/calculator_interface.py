from abc import ABC, abstractmethod

class CalculatorInterface(ABC):
    """
    Abstract base class for a calculator.
    """

    @abstractmethod
    def add(self, a: float | int, b: float | int) -> float | int:
        """
        Abstract method for addition.

        Args:
            a (float | int): The first number.
            b (float | int): The second number.

        Returns:
            float | int: The result of the addition.
        """
        pass

    @abstractmethod
    def subtract(self, a: float | int, b: float | int) -> float | int:
        """
        Abstract method for subtraction.

        Args:
            a (float | int): The first number.
            b (float | int): The second number.

        Returns:
            float | int: The result of the subtraction.
        """
        pass

    @abstractmethod
    def multiply(self, a: float | int, b: float | int) -> float | int:
        """
        Abstract method for multiplication.

        Args:
            a (float | int): The first number.
            b (float | int): The second number.

        Returns:
            float | int: The result of the multiplication.
        """
        pass

    @abstractmethod
    def divide(self, a: float | int, b: float | int) -> float | int:
        """
        Abstract method for division.

        Args:
            a (float | int): The first number.
            b (float | int): The second number.

        Returns:
            float | int: The result of the division.
        """
        pass
