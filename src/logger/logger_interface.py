from abc import ABC, abstractmethod

"""Module for logger interface."""

class Logger(ABC):
    """Interface for logger implementation."""

    @abstractmethod
    def log(self, message: str) -> None:
        """Abstract method for logging."""
        pass
