class Calculator:
    def __init__(self):
        # These can be injected later (for example, in your tests)
        self.logger = None
        self.notifier = None

    def add(self, a, b):
        result = a + b
        if self.logger:
            self.logger.log(f"Addition: {a} + {b} = {result}")
        if self.notifier:
            self.notifier.notify(result)  # Pass result, not message
        return result

    def subtract(self, a, b):
        result = a - b
        # Optionally, log subtraction if needed
        if self.logger is not None:
            self.logger.log(f"Subtraction: {a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        # Optionally, log multiplication if needed
        if self.logger is not None:
            self.logger.log(f"Multiplication: {a} * {b} = {result}")
        return result