from notifier import get_notifier


class NotifierAPI:
    """API class to manage notification functionalities."""

    def __init__(self) -> None:
        """Initialize the NotifierAPI with necessary attributes."""
        self.notifier = Notifier()

    def send_notification(self, recipient: str, message: str) -> bool:
        """Send a notification to a recipient."""
        return self.notifier.notify(recipient, message)
