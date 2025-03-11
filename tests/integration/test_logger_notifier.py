"""Module for integration tests: logger notifier."""

from unittest.mock import MagicMock
import pytest


import logger
import logger_impl
import calculator
import calculator_impl
import notifier


# @pytest.fixture
# def mock_notifier() -> notifier.Notifier:
#     """Return a mock notifier."""
#     return MagicMock(spec=notifier.Notifier, autospec=True)

@pytest.fixture
def mock_calculator() -> calculator.Calculator:
    """Return a mock calculator."""
    return MagicMock(spec=calculator.Calculator, autospec=True)





def test_logger_triggers_notification( mock_calculator: calculator.Calculator) -> None:
    """Test that the logger triggers the notifier."""
    # logger_with_mock_notifier.log("Threshold exceeded")
    notifier_instance = notifier.get_notifier()
    logger_instance = logger.get_logger(notifier_instance)
    
    mock_calculator.add(2, 3)

    assert isinstance(mock_notifier.notify, MagicMock)
    mock_notifier.notify.assert_called_with("Threshold exceeded")  # ✅ Ensures notify() was called
