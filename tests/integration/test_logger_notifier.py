"""Module for integration tests: logger notifier."""

from unittest.mock import MagicMock

import pytest

import calculator
import calculator_impl
import logger
import logger_impl
# from src.notifier_impl.src.notifier_impl._impl import get_notifier
# import src.notifier_impl.src.notifier_impl._impl as notifier_impl_test
import notifier

@pytest.fixture
def mock_calculator():
    """Return a mock calculator."""
    return MagicMock(spec=calculator.Calculator, autospec=True)


def test_logger_triggers_notification(capsys: pytest.CaptureFixture[str]) -> None:
    """Test that the logger triggers the notifier."""
    # logger_with_mock_notifier.log("Threshold exceeded")
    notifier_instance = notifier.get_notifier()
    logger_instance = logger.get_logger(notifier_instance)

    # mock_calculator.add.return_value = 5
    # result = mock_calculator.add(2, 3)
    logger_instance.log("Threshold exceeded")
    expected = "LOG: Threshold exceeded\nNOTIFICATION: Threshold exceeded"
    captured = capsys.readouterr()


    assert expected in captured.out
