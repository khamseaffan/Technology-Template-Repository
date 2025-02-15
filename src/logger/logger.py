"""Module for logger functionality."""

class Logger:
    """Logger class for outputting log messages."""

    def __init__(self) -> None:
        """Initialize instance."""
        self.notifier = None

    def log(self, message: str) -> None:
        """Log a message."""
        print(f"LOG: {message}")
        if self.notifier and "Threshold exceeded" in message:
            self.notifier.notify(message)
