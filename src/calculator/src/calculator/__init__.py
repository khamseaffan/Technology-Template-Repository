"""Protocol for a Calculator."""

from typing import Protocol, Any

class Calculator(Protocol):
    """Protocol for calculator."""

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