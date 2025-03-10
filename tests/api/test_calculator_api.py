import pytest
from src.calculator.calculator_api import CalculatorAPI

ADDITION_RESULT = 5
SUBTRACTION_RESULT = 2
MULTIPLICATION_RESULT = 6
DIVISION_RESULT = 3

@pytest.fixture
def calculator():
    """Fixture to create a CalculatorAPI instance."""
    return CalculatorAPI()

def test_addition(calculator) -> None:
    """Test addition functionality."""
    assert calculator.add(2, 3) == ADDITION_RESULT

def test_subtraction(calculator) -> None:
    """Test subtraction functionality."""
    assert calculator.subtract(5, 3) == SUBTRACTION_RESULT

def test_multiplication(calculator) -> None:
    """Test multiplication functionality."""
    assert calculator.multiply(2, 3) == MULTIPLICATION_RESULT

def test_division(calculator) -> None:
    """Test division functionality."""
    assert calculator.divide(6, 2) == DIVISION_RESULT
