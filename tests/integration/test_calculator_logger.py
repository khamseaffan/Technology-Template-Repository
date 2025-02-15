"""Module for integration tests: calculator logging."""

from unittest.mock import MagicMock

import pytest

from src.calculator.calculator import Calculator
from src.logger.logger import Logger


@pytest.fixture
def mock_logger():
    """Return a mock logger."""
    logger = Logger()
    logger.log = MagicMock()
    return logger

def test_calculator_logs_operation(mock_logger):
    """Test that the calculator logs operations."""
    calc = Calculator()
    calc.logger = mock_logger
    result = calc.add(2, 3)
    expected = f"Addition: 2 + 3 = {result}"
    mock_logger.log.assert_called_with(expected)
