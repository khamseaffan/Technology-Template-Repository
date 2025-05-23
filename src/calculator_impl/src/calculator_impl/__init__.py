"""Module for a Calculator implementation."""

import calculator

from . import _impl

calculator.get_calculator = lambda: _impl.CalculatorImpl()

__all__ = ["get_notifier"]
