"""Protocol for a Logger."""

from typing import Protocol

import notifier


class Logger(Protocol):
    """Protocol for logger."""

    @property
    def notifier(self) -> notifier.Notifier | None:
        """Get the notifier instance."""
        raise NotImplementedError

    @notifier.setter
    def notifier(self, value: notifier.Notifier | None) -> None:
        """Set the notifier instance."""
        raise NotImplementedError

    def log(self, message: str) -> None:
        """Log a Message."""
        raise NotImplementedError


def get_logger(notifier: notifier.Notifier | None = None) -> Logger:
    """Return an instance of a Logger."""
    raise NotImplementedError
