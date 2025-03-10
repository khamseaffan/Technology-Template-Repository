"""Protocol for a Notifier."""

from typing import Protocol


class Notifier(Protocol):
    """Protocol for notifier."""

    def notify(self, message: str) -> None:
        """Output a Notification Message."""
        raise NotImplementedError

def get_notifier() -> Notifier:
    """Return an instance of a Notifier."""
    raise NotImplementedError
