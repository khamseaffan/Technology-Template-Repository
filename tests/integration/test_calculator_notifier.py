"""Module for integration tests: calculator notifier."""

from unittest.mock import MagicMock

import pytest

from src.calculator.calculator_interface import Calculator
from src.calculator.calculator import SimpleCalculator
from src.notifier.notifier import SimpleNotifier
from src.notifier.notifier_interface import Notifier


@pytest.fixture
def mock_notifier() -> Notifier:
    """Return a mock notifier."""
    return MagicMock(spec=SimpleNotifier)


def test_calculator_notifier(mock_notifier: Notifier) -> None:
    """Test that the calculator calls the notifier."""
    calc: Calculator = SimpleCalculator()
    calc.notifier = mock_notifier
    result = calc.add(2, 3)

    assert isinstance(mock_notifier.notify, MagicMock)
    mock_notifier.notify.assert_called_with(result)
