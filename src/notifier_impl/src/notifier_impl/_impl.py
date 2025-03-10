"""Implementation for Notifier Module."""

import notifier


class Notifier(notifier.Notifier):
    """Notifier class for sending notifications."""

    def __init__(self) -> None:
        """Initialize instance."""

    def notify(self, message: str) -> None:
        """Output a notification message."""
        print(f"NOTIFICATION: {message}")

def get_notifier() -> notifier.Notifier:
    return Notifier()
