from logger import get_logger


class LoggerAPI:
    def __init__(self) -> None:
        self.logger = get_logger()

    def log_message(self, message: str) -> dict[str, str]:
        self.logger.log(message)
        return {"status": "logged", "message": message}
