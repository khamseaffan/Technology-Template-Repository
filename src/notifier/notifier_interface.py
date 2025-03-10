from abc import ABC, abstractmethod

"""Module for notifier interface."""


class Notifier(ABC):
    """Interface for notifier implementation."""

    @abstractmethod
    def notify(self, message: str) -> None:
        """Abstract method for notification."""
        pass
