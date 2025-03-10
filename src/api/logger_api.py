from logger import get_logger


class LoggerAPI:
    """A simple API wrapper for logging functionality.
    Provides a clean interface for logging messages through the system logger."""

    def __init__(self) -> None:
        """Initialize LoggerAPI with a system logger."""
        self.logger = get_logger()

    def log_message(self, message: str) -> dict[str, str]:
        """Log a message and return status dictionary."""
        self.logger.log(message)
        return {"status": "logged", "message": message}
