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
    expected_message = (
        f"Addition: 2 + 3 = {result}"
    )
    mock_logger.log.assert_called_with(expected_message)
