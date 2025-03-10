"""Module for integration tests: calculator logging."""

from unittest.mock import MagicMock

import pytest

from src.calculator.calculator import Calculator
import logger


@pytest.fixture
def mock_logger() -> logger.Logger:
    """Return a mock logger."""
    return MagicMock(spec=logger.get_logger())


def test_calculator_logs_operation(mock_logger: logger.Logger) -> None:
    """Test that the calculator logs operations."""
    calc = Calculator()
    calc.logger = mock_logger
    result = calc.add(2, 3)
    expected = f"Addition: 2 + 3 = {result}"

    assert isinstance(mock_logger.log, MagicMock)
    mock_logger.log.assert_called_with(expected)
