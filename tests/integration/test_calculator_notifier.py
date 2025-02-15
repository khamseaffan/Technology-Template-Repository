import pytest
from unittest.mock import MagicMock
from src.calculator.calculator import Calculator
from src.notifier.notifier import Notifier

@pytest.fixture
def mock_notifier():
    notifier = Notifier()
    notifier.notify = MagicMock()
    return notifier

def test_calculator_notifier(mock_notifier):
    calc = Calculator()
    calc.notifier = mock_notifier
    result = calc.add(2, 3)
    # Expect that notifier.notify is called with the result (5)
    mock_notifier.notify.assert_called_with(result)
