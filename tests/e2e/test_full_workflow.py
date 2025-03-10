"""Module for end-to-end tests."""

from typing import Tuple
import pytest

from src.calculator.calculator import Calculator
import logger
import notifier


@pytest.fixture
def components() -> Tuple[Calculator, logger.Logger, notifier.Notifier]:
    """Return components for full workflow testing."""
    logger = logger.get_logger()
    notifier = notifier.get_notifier()
    calc = Calculator()
    calc.logger = logger
    calc.notifier = notifier
    return (calc, logger, notifier)


def test_full_workflow(
    components: Tuple[Calculator, logger.Logger, notifier.Notifier],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Test the full workflow of the calculator."""
    calc, logger, notifier = components
    result = calc.add(7, 5)
    notifier.notify(str(result))
    output = capsys.readouterr().out
    assert "NOTIFICATION:" in output, "Notification message missing in output"
