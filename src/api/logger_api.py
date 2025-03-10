from src.logger.logger import Logger

class LoggerAPI:
    def __init__(self) -> None:
        self.logger = Logger()

    def log_message(self, message: str) -> dict:
        self.logger.log(message)
        return {"status": "logged", "message": message}
