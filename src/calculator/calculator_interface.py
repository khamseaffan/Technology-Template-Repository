from abc import ABC, abstractmethod
from typing import Any

"""Module for calculator interface"""

class Calculator(ABC):
    """Interface for calculator implementation"""
    @abstractmethod
    def add(self, a: Any, b: Any) -> Any:
        """Abstract method for addition"""
        pass
    @abstractmethod
    def subtract(self, a: Any, b: Any) -> Any:
        """Abstract method for subtraction"""
        pass
    @abstractmethod
    def multiply(self, a: Any, b: Any) -> Any:
        """Abstract method for multiplication"""
        pass
    @abstractmethod
    def divide(self, a: Any, b: Any) -> Any:
        """Abstract method for division"""
        pass
    