"""Module for integration tests: calculator notifier."""

from unittest.mock import MagicMock

import pytest

from src.calculator.calculator import SimpleCalculator
from src.notifier.notifier import SimpleNotifier


@pytest.fixture
def mock_notifier():
    """Return a mock notifier."""
    notifier = SimpleNotifier()
    notifier.notify = MagicMock()
    return notifier

def test_calculator_notifier(mock_notifier):
    """Test that the calculator calls the notifier."""
    calc = SimpleCalculator()
    calc.notifier = mock_notifier
    result = calc.add(2, 3)
    mock_notifier.notify.assert_called_with(result)
