from src.logger.logger import Logger

class LoggerAPI:
    """
    API class to manage logging functionalities.
    """

    def __init__(self) -> None:
        """
        Initializes the LoggerAPI with necessary attributes.
        """
        self.logger = Logger()

    def log_message(self, message: str, level: str) -> None:
        """
        Logs a message with the specified level.

        Args:
            message (str): The message to log.
            level (str): The logging level (e.g., 'info', 'error', 'debug').

        Returns:
            None
        """
        self.logger.log(level, message)
