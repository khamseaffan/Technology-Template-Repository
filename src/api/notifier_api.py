from src.notifier.notifier import Notifier

class NotifierAPI:
    """
    API class to manage notification functionalities.
    """

    def __init__(self) -> None:
        """
        Initializes the NotifierAPI with necessary attributes.
        """
        self.notifier = Notifier()

    def send_notification(self, recipient: str, message: str) -> bool:
        """
        Sends a notification to a recipient.

        Args:
            recipient (str): The recipient of the notification.
            message (str): The message to be sent.

        Returns:
            bool: True if the notification was sent successfully, False otherwise.
        """
        return self.notifier.notify(recipient, message)
