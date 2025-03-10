import pytest
from src.api.calculator_api import CalculatorAPI

@pytest.fixture
def api():
    return CalculatorAPI()

def test_calculate_addition(api):
    response = api.calculate("add", 2, 3)
    assert response["result"] == 5

def test_calculate_divide_by_zero(api):
    response = api.calculate("divide", 5, 0)
    assert "error" in response

def test_calculate_subtraction(api):
    response = api.calculate("subtract", 10, 5)
    assert response["result"] == 5

def test_calculate_invalid_operation(api):
    response = api.calculate("invalid", 2, 3)
    assert "error" in response
