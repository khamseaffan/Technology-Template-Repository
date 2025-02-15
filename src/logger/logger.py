class Logger:
    def __init__(self) -> None:
        self.notifier = None

    def log(self, message):
        print(f"LOG: {message}")
        if self.notifier and "Threshold exceeded" in message:
            self.notifier.notify(message)