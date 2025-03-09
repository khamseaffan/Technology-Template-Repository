from abc import ABC, abstractmethod

"""Interface for notifier implementation"""

class Notifier(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def notify(self, message):
        pass
    