"""Module for integration tests: calculator notifier."""

from unittest.mock import MagicMock

import pytest

from src.calculator.calculator import Calculator
from src.notifier.notifier import Notifier


@pytest.fixture
def mock_notifier():
    """Return a mock notifier."""
    notifier = Notifier()
    notifier.notify = MagicMock()
    return notifier

def test_calculator_notifier(mock_notifier):
    """Test that the calculator calls the notifier."""
    calc = Calculator()
    calc.notifier = mock_notifier
    result = calc.add(2, 3)
    mock_notifier.notify.assert_called_with(result)
