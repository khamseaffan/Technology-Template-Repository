import pytest
from src.calculator.calculator_api import CalculatorAPI

@pytest.fixture
def calculator():
    """Fixture to create a CalculatorAPI instance."""
    return CalculatorAPI()

def test_addition(calculator) -> None:
    """Test addition functionality."""
    assert calculator.add(2, 3) == 5

def test_subtraction(calculator) -> None:
    """Test subtraction functionality."""
    assert calculator.subtract(5, 3) == 2

def test_multiplication(calculator) -> None:
    """Test multiplication functionality."""
    assert calculator.multiply(2, 3) == 6

def test_division(calculator) -> None:
    """Test division functionality."""
    assert calculator.divide(6, 2) == 3
