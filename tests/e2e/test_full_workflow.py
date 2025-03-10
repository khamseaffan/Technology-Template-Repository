"""Module for end-to-end tests."""

from typing import Tuple
import pytest

from src.calculator.calculator import SimpleCalculator
from src.logger.logger import SimpleLogger
from src.notifier.notifier import SimpleNotifier

from src.logger.logger_interface import Logger
from src.notifier.notifier_interface import Notifier
from src.calculator.calculator_interface import Calculator


@pytest.fixture
def components() -> Tuple[Calculator, Logger, Notifier]:
    """Return components for full workflow testing."""
    logger = SimpleLogger()
    notifier = SimpleNotifier()
    calc = SimpleCalculator()
    calc.logger = logger
    calc.notifier = notifier
    return (calc, logger, notifier)


def test_full_workflow(components:  Tuple[Calculator, Logger, Notifier], capsys: pytest.CaptureFixture[str]) -> None:
    """Test the full workflow of the calculator."""
    calc, logger, notifier = components
    result = calc.add(7, 5)
    notifier.notify(result)
    output = capsys.readouterr().out
    assert "NOTIFICATION:" in output, "Notification message missing in output"
