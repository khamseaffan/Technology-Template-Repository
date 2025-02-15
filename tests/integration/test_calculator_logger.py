import pytest
from unittest.mock import MagicMock
from src.calculator.calculator import Calculator
from src.logger.logger import Logger

@pytest.fixture
def mock_logger():
    logger = Logger()
    logger.log = MagicMock()
    return logger

def test_calculator_logs_operation(mock_logger):
    calc = Calculator()
    calc.logger = mock_logger
    result = calc.add(2, 3)
    expected_message = f"Addition: 2 + 3 = {result}"
    # If your Calculator.add doesn't call logger.log, you may need to update the implementation.
    # For now, you can comment this assertion to let the test pass:
    # mock_logger.log.assert_called_with(expected_message)
    # Or, if you prefer the test to fail as a reminder, leave it as-is.
    mock_logger.log.assert_called_with(expected_message)
