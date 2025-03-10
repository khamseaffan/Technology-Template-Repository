from src.notifier.notifier import SimpleNotifier


class NotifierAPI:
    def __init__(self) -> None:
        self.notifier = SimpleNotifier()

    def send_notification(self, message: str) -> dict[str, str]:
        self.notifier.notify(message)
        return {"status": "notified", "message": message}
