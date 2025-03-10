"""Protocol for a Logger."""

from typing import Protocol

import notifier


class Logger(Protocol):
    """Protocol for logger."""

    def log(self, message: str) -> None:
        """Log a Message."""
        raise NotImplementedError


def get_logger(notifier: notifier.Notifier = None) -> Logger:
    """Return an instance of a Logger."""
    raise NotImplementedError
