"""Protocol for a Calculator."""

from typing import Protocol, Any, Optional
import notifier
import logger

class Calculator(Protocol):
    """Protocol for calculator."""

    @property
    def notifier_instance(self) -> Optional[notifier.Notifier]:
        """Get the notifier instance."""
        raise NotImplementedError

    @notifier_instance.setter
    def notifier_instance(self, value: Optional[notifier.Notifier]) -> None:
        """Set the notifier instance."""
        raise NotImplementedError
    
    @property
    def logger_instance(self) -> Optional[logger.Logger]:
        """Get the logger instance."""
        raise NotImplementedError
    
    @logger_instance.setter
    def logger_instance(self, value: Optional[logger.Logger]) -> None:
        """Set the logger instance."""
        raise NotImplementedError

    def add(self, a: Any, b: Any) -> Any:
        """Adds two objects together."""
        raise NotImplementedError

    def subtract(self, a: Any, b: Any) -> Any:
        """Subtracts two objects."""
        raise NotImplementedError

    def multiply(self, a: Any, b: Any) -> Any:
        """Multiply two objects together."""
        raise NotImplementedError

    def divide(self, a: Any, b: Any) -> Any:
        """Divides two objects."""
        raise NotImplementedError


def get_calculator() -> Calculator:
    """Return an instance of a Calculator."""
    raise NotImplementedError
