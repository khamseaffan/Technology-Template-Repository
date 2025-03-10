from notifier import get_notifier


class NotifierAPI:
    def __init__(self) -> None:
        self.notifier = get_notifier()

    def send_notification(self, message: str) -> dict[str, str]:
        self.notifier.notify(message)
        return {"status": "notified", "message": message}
