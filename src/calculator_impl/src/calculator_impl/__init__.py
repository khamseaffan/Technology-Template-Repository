"""Module for a Calculator implementation."""

import calculator
from typing import Optional
from . import _impl


calculator.get_calculator = lambda: _impl.Calculator()
