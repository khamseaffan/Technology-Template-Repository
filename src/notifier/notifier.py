from __future__ import annotations

from .notifier_interface import Notifier

"""Module for notifier functionality."""


class SimpleNotifier(Notifier):
    """Notifier class for sending notifications."""

    def __init__(self) -> None:
        """Initialize instance."""

    def notify(self, message: str) -> None:
        """Output a notification message."""
        print(f"NOTIFICATION: {message}")
