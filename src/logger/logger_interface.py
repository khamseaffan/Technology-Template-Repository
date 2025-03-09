from abc import ABC, abstractmethod

"""Interface for logger implementation"""

class Logger(ABC):
    @abstractmethod
    def __init__(self):
        pass
    @abstractmethod
    def log(self, message):
        pass
    
    