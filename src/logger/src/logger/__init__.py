"""Protocol for a Logger."""

from typing import Optional, Protocol
import notifier


class Logger(Protocol):
    """Protocol for logger."""

    @property
    def notifier_instance(self) -> notifier.Notifier | None:
        """Get the notifier instance."""
        raise NotImplementedError

    @notifier_instance.setter
    def notifier_instance(self, value: notifier.Notifier | None) -> None:
        """Set the notifier instance."""
        raise NotImplementedError

    def log(self, message: str) -> None:
        """Log a Message."""
        raise NotImplementedError


# ✅ Allow the function to be dynamically overridden
def get_logger(notifier_instance: notifier.Notifier | None = None) -> Logger:
    """Return an instance of a Logger."""
    raise NotImplementedError  # 🚨 Placeholder (should be overridden by `logger_impl`)
