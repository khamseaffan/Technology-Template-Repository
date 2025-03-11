"""Protocol for a Calculator."""

import notifier
from typing import Any, Optional, Protocol


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
