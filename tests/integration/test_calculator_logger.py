"""Module for integration tests: calculator logging."""
from unittest.mock import MagicMock

import pytest

import calculator
import calculator_impl
import logger
import logger_impl
import notifier


@pytest.fixture
def mock_notifier() -> notifier.Notifier:
    """Return a mock notifier."""
    return MagicMock(spec=notifier.Notifier, autospec=True)


@pytest.fixture
def calculator_with_mock_logger(mock_notifier: notifier.Notifier) -> calculator.Calculator:
    """Return an instance of CalculatorImpl with a mock logger."""
    logger_instance = logger.get_logger(mock_notifier)
    # logger_instance.notifier_instance =
    calc = calculator.get_calculator()
     # Use the implemented function
    calc.logger_instance = logger_instance  # Ensure mock logger is assigned
    return calc


def test_calculator_logs_operation(calculator_with_mock_logger: calculator.Calculator,
                                   capsys: pytest.CaptureFixture[str]) -> None:
    """Test that the calculator logs operations."""
    result = calculator_with_mock_logger.add(2, 3)
    expected = f"Addition: 2 + 3 = {result}"

    captured = capsys.readouterr()
    assert f"LOG: {expected}" in captured.out
    assert result == 5
