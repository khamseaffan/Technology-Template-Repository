from abc import ABC, abstractmethod
from typing import Optional
from src.notifier.notifier_interface import Notifier

"""Module for logger interface."""


class Logger(ABC):
    """Interface for logger implementation."""

    notifier: Optional[Notifier]

    @abstractmethod
    def log(self, message: str) -> None:
        """Abstract method for logging."""
        pass
