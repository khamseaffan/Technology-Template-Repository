"""Implementation for Logger Module."""

import logger
import notifier


class LoggerImpl(logger.Logger):
    """Logger class for outputting log messages."""

    def __init__(self, notifier_instance: notifier.Notifier | None = None) -> None:
        """Initialize instance with a notifier.

        Args:
            notifier_instance: An instance of a Notifier implementation

        """
        self.notifier_instance = notifier_instance

    @property
    def notifier_instance(self) -> notifier.Notifier | None:
        return self._notifier

    @notifier_instance.setter
    def notifier_instance(self, value: notifier.Notifier | None) -> None:
        self._notifier = value

    def log(self, message: str) -> None:
        """Log a message."""
        print(f"LOG: {message}")
        if self.notifier_instance and "Threshold exceeded" in message:  # ✅ Correct attribute name
            self.notifier_instance.notify(message)


def get_logger(notifier_instance: notifier.Notifier | None = None) -> logger.Logger:
    """Return an instance of LoggerImpl with optional notifier."""
    if notifier_instance is None:
        notifier_instance = notifier.get_notifier()  # ✅ Only create if not provided
    return LoggerImpl(notifier_instance)
