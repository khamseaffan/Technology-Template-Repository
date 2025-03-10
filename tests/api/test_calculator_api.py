import pytest
from src.api.calculator_api import CalculatorAPI

RESULT_ADD = 5
RESULT_SUBTRACT = 5


@pytest.fixture
def api() -> CalculatorAPI:
    return CalculatorAPI()


def test_calculate_addition(api: CalculatorAPI) -> None:
    response = api.calculate("add", 2, 3)
    assert response["result"] == RESULT_ADD


def test_calculate_divide_by_zero(api: CalculatorAPI) -> None:
    response = api.calculate("divide", 5, 0)
    assert "error" in response


def test_calculate_subtraction(api: CalculatorAPI) -> None:
    response = api.calculate("subtract", 10, 5)
    assert response["result"] == RESULT_SUBTRACT


def test_calculate_invalid_operation(api: CalculatorAPI) -> None:
    response = api.calculate("invalid", 2, 3)
    assert "error" in response
