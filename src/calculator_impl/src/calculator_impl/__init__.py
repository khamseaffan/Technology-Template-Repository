"""Module for a Calculator implementation."""

from typing import Optional
import calculator

from . import _impl


calculator.get_calculator = lambda: _impl.Calculator()