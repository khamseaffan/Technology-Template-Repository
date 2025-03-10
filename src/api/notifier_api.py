from src.notifier.notifier import Notifier

class NotifierAPI:
    def __init__(self) -> None:
        self.notifier = Notifier()
    def send_notification(self, message: str) -> dict:
        self.notifier.notify(message)
        return {"status": "notified", "message": message}
