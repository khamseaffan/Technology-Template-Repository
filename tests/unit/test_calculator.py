from src.calculator.calculator import Calculator

"""Unit tests for the calculator module."""

def test_add():
    """Test the add function."""
    calc = Calculator()
    expected = 5
    assert calc.add(2, 3) == expected

def test_subtract():
    """Test the subtract function."""
    calc = Calculator()
    expected = 2
    assert calc.subtract(5, 3) == expected

def test_multiply():
    """Test the multiply function."""
    calc = Calculator()
    expected = 6
    assert calc.multiply(2, 3) == expected
