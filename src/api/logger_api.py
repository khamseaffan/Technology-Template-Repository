from src.logger.logger import SimpleLogger

class LoggerAPI:
    def __init__(self) -> None:
        self.logger = SimpleLogger()
    def log_message(self, message: str) -> dict[str, str]:
        self.logger.log(message)
        return {"status": "logged", "message": message}
