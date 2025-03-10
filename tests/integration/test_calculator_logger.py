"""Module for integration tests: calculator logging."""

from unittest.mock import MagicMock

import pytest

from src.calculator.calculator_interface import Calculator
from src.calculator.calculator import SimpleCalculator
from src.logger.logger import SimpleLogger
from src.logger.logger_interface import Logger


@pytest.fixture
def mock_logger() -> Logger :
    """Return a mock logger."""
    logger= MagicMock(spec=SimpleLogger)
    return logger


def test_calculator_logs_operation(mock_logger: Logger) -> None:
    """Test that the calculator logs operations."""
    calc: Calculator = SimpleCalculator()
    calc.logger = mock_logger
    result = calc.add(2, 3)
    expected = f"Addition: 2 + 3 = {result}"

    assert isinstance(mock_logger.log, MagicMock)
    mock_logger.log.assert_called_with(expected)
