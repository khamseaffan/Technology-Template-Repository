from src.logger.logger import Logger

class LoggerAPI:
    def __init__(self):
        self.logger = Logger()

    def log_message(self, message: str) -> dict:
        """Log a message via the API."""
        self.logger.log(message)
        return {"status": "logged", "message": message}
