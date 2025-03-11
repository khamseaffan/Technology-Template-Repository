
import calculator # type: ignore

"""Unit tests for the calculator module."""


def test_add() -> None:
    """Test the add function."""
    calc = calculator.get_calculator()
    expected = 5
    assert calc.add(2, 3) == expected


def test_subtract() -> None:
    """Test the subtract function."""
    calc = calculator.get_calculator()
    expected = 2
    assert calc.subtract(5, 3) == expected


def test_multiply() -> None:
    """Test the multiply function."""
    calc = calculator.get_calculator()
    expected = 6
    assert calc.multiply(2, 3) == expected


def test_divison() -> None:
    """Test the multiply function."""
    calc = calculator.get_calculator()
    expected = 4
    assert calc.divide(8, 2) == expected
