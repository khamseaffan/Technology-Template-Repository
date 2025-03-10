"""Module for integration tests: calculator notifier."""

from unittest.mock import MagicMock

import pytest

from src.calculator.calculator import Calculator
import notifier


@pytest.fixture
def mock_notifier() -> notifier.Notifier:
    """Return a mock notifier."""
    return MagicMock(spec=notifier.get_notifier())


def test_calculator_notifier(mock_notifier: notifier.Notifier) -> None:
    """Test that the calculator calls the notifier."""
    calc = Calculator()
    calc.notifier = mock_notifier
    result = calc.add(2, 3)

    assert isinstance(mock_notifier.notify, MagicMock)
    mock_notifier.notify.assert_called_with(result)
