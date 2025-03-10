"""Implementation for Logger Module."""

import logger
import notifier


class Logger(logger.Logger):
    """Logger class for outputting log messages."""

    def __init__(self, notifier_instance: notifier.Notifier) -> None:
        """Initialize instance with a notifier.

        Args:
            notifier_instance: An instance of a Notifier implementation

        """
        self.notifier = notifier_instance

    def log(self, message: str) -> None:
        """Log a message."""
        print(f"LOG: {message}")
        if self.notifier and "Threshold exceeded" in message:
            self.notifier.notify(message)

def get_logger() -> logger.Logger:
    # Note: The caller should provide the notifier instance
    notifier_instance = notifier.get_notifier()  # This should be injected by the caller
    return Logger(notifier_instance)
