# Calculator Protocol

## Overview
The Calculator Protocol defines a standardized interface for calculation functionality within the system. It provides a simple, consistent way to handle calculations.

## Protocol Definition
The protocol is defined in `__init__.py` and includes:

```python
class Calculator(Protocol):
    """Protocol for calculator."""

    def add(self, a: Any, b: Any) -> Any:
        """Adds two objects together."""
        raise NotImplementedError
    def subtract(self, a: Any, b: Any) -> Any:
        """Subtracts two objects."""
        raise NotImplementedError
    def multiply(self, a: Any, b: Any) -> Any:
        """Multiply two objects together."""
        raise NotImplementedError
    def divide(self, a: Any, b: Any) -> Any:
        """Divides two objects."""
        raise NotImplementedError

def get_calculator() -> Calculator:
    """Return an instance of a Calculator."""
    raise NotImplementedError
```

## Usage
To implement this protocol:

1. Import the protocol:
```python
from src.calculator import Calculator
```

2. Create a class that implements the protocol:
```python
class MyCalculator(Calculator):
    def add(self, a: Any, b: Any) -> Any:
        #implementation here
```

## Integration
The Calculator protocol is used by multiple components:
- Logger: Logs calculations done by calculator.
- Notifier: For threshold notifications when calculator exceeds threshold.

## Testing
Test implementations should use the provided mock fixtures in the test suite.

## Requirements
- Python 3.13 or higher
- No additional dependencies required