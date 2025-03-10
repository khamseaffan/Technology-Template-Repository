from src.logger.logger import Logger

class LoggerAPI:
    """API class to manage logging functionalities."""

    def __init__(self) -> None:
        """Initialize the LoggerAPI with necessary attributes."""
        self.logger = Logger()

    def log_message(self, message: str, level: str) -> None:
        """Log a message with the specified level."""
        self.logger.log(level, message)
