"""Module for end-to-end tests."""

from typing import Tuple
import pytest

from src.calculator.calculator import SimpleCalculator
import logger
import notifier
from src.calculator.calculator_interface import Calculator


@pytest.fixture
def components() -> Tuple[Calculator, logger.Logger, notifier.Notifier]:
    """Return components for full workflow testing."""
    logger = logger.get_logger()
    notifier = notifier.get_notifier()
    calc:Calculator = SimpleCalculator()
    calc.logger = logger
    calc.notifier = notifier
    return (calc, logger, notifier)


def test_full_workflow(
    components: Tuple[Calculator, logger.Logger, notifier.Notifier], capsys: pytest.CaptureFixture[str]
) -> None:
    """Test the full workflow of the calculator."""
    calc, logger, notifier = components
    result = calc.add(7, 5)
    notifier.notify(result)
    output = capsys.readouterr().out
    assert "NOTIFICATION:" in output, "Notification message missing in output"
