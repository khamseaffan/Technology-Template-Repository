"""Module for integration tests: calculator notifier."""

import pytest
import notifier
from unittest.mock import MagicMock
from src.calculator_impl.src.calculator_impl._impl import CalculatorImpl, get_calculator  # Import from calculator_impl


@pytest.fixture
def mock_notifier() -> notifier.Notifier:
    """Return a mock notifier."""
    return MagicMock(spec=notifier.Notifier, autospec=True)


@pytest.fixture
def calculator_with_mock_notifier(mock_notifier: notifier.Notifier) -> CalculatorImpl:
    """Return an instance of CalculatorImpl with a mock notifier."""
    calc = get_calculator()  # Use the correct function from calculator_impl
    calc.notifier_instance = mock_notifier  # Assign mock notifier
    return calc


def test_calculator_notifier(calculator_with_mock_notifier: CalculatorImpl, mock_notifier: notifier.Notifier) -> None:
    """Test that the calculator calls the notifier."""
    result = calculator_with_mock_notifier.add(2, 3)

    assert result == 5
    assert isinstance(mock_notifier.notify, MagicMock)
    mock_notifier.notify.assert_called_with(5)  # Ensure notify(5) was called
