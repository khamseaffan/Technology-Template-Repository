# Logger Protocol

## Overview
The Logger Protocol defines a standardized interface for logging functionality within the system. It provides a simple, consistent way to handle logging across different components.

## Protocol Definition
The protocol is defined in `__init__.py` and includes:

```python
class Logger(Protocol):
    @property
    def log(self, message: str) -> None:
        """Log a Message"""
```

## Usage
To implement this protocol:

1. Import the protocol:
```python
from src.logger import Logger
```

2. Create a class that implements the protocol:
```python
class MyLogger(Logger):
    def log(self, message: str) -> None:
        # Implementation here
```

## Integration
The Logger protocol is used by multiple components:
- Calculator: For logging operations.
- Notifier: Checks logger to see if operation exceeds threshold.

## Testing
Test implementations should use the provided mock fixtures in the test suite.

## Requirements
- Python 3.13 or higher
- No additional dependencies required