"""Protocol for a Calculator."""

from typing import Any, Optional, Protocol

import logger
import notifier


class Calculator(Protocol):
    """Protocol for calculator."""

    @property
    def notifier_instance(self) -> notifier.Notifier | None:
        """Get the notifier instance."""
        raise NotImplementedError

    @notifier_instance.setter
    def notifier_instance(self, value: notifier.Notifier | None) -> None:
        """Set the notifier instance."""
        raise NotImplementedError

    @property
    def logger_instance(self) -> logger.Logger | None:
        """Get the logger instance."""
        raise NotImplementedError

    @logger_instance.setter
    def logger_instance(self, value: logger.Logger | None) -> None:
        """Set the logger instance."""
        raise NotImplementedError

    def add(self, a: Any, b: Any) -> Any:
        """Add two objects together."""
        raise NotImplementedError

    def subtract(self, a: Any, b: Any) -> Any:
        """Subtract two objects."""
        raise NotImplementedError

    def multiply(self, a: Any, b: Any) -> Any:
        """Multiply two objects together."""
        raise NotImplementedError

    def divide(self, a: Any, b: Any) -> Any:
        """Divide two objects."""
        raise NotImplementedError


def get_calculator() -> Calculator:
    """Return an instance of a Calculator."""
    raise NotImplementedError
