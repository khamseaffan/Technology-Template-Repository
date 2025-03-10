from abc import ABC, abstractmethod
from typing import Any, Optional
import logger
import notifier

"""Module for calculator interface."""

class Calculator(ABC):
    """Interface for calculator implementation."""

    @property
    @abstractmethod
    def logger(self) -> Optional[logger.Logger]:
        pass

    @logger.setter
    @abstractmethod
    def logger(self, value: Optional[logger.Logger]) -> None:
        pass

    @property
    @abstractmethod
    def notifier(self) -> Optional[notifier.Notifier]:
        pass

    @notifier.setter
    @abstractmethod
    def notifier(self, value: Optional[notifier.Notifier]) -> None:
        pass

    @abstractmethod
    def add(self, a: Any, b: Any) -> Any:
        """Abstract method for addition."""
        pass
    @abstractmethod
    def subtract(self, a: Any, b: Any) -> Any:
        """Abstract method for subtraction."""
        pass
    @abstractmethod
    def multiply(self, a: Any, b: Any) -> Any:
        """Abstract method for multiplication."""
        pass
    @abstractmethod
    def divide(self, a: Any, b: Any) -> Any:
        """Abstract method for division."""
        pass