# Notifier Protocol

## Overview
The Notifier Protocol defines a standardized interface for notification functionality within the system. It provides a simple, consistent way to handle notifications across different components.

## Protocol Definition
The protocol is defined in `__init__.py` and includes:

```python
class Notifier(Protocol):
    @property
    def notify(self, message: str) -> None:
        """Outputs a Notification Message"""
```

## Usage
To implement this protocol:

1. Import the protocol:
```python
from src.notifier import Notifier
```

2. Create a class that implements the protocol:
```python
class MyNotifier(Notifier):
    def notify(self, message: str) -> None:
        # Implementation here
```

## Integration
The Notifier protocol is used by multiple components:
- Calculator: For operation notifications
- Logger: For threshold notifications

## Testing
Test implementations should use the provided mock fixtures in the test suite.

## Requirements
- Python 3.13 or higher
- No additional dependencies required