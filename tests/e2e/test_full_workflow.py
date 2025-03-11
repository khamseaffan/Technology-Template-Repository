"""Module for end-to-end tests."""

from typing import Tuple
import pytest

import logger
import notifier
import calculator


@pytest.fixture
def components() -> Tuple[calculator.Calculator, logger.Logger, notifier.Notifier]:
    """Return components for full workflow testing."""
    logger = logger.get_logger()
    notifier = notifier.get_notifier()
    calculator = calculator.get_calculator()
    return (calculator, logger, notifier)


def test_full_workflow(
    components: Tuple[calculator.Calculator, logger.Logger, notifier.Notifier], capsys: pytest.CaptureFixture[str]
) -> None:
    """Test the full workflow of the calculator."""
    calc, logger, notifier = components
    result = calc.add(7, 5)
    logger.log(result)
    notifier.notify(result)
    output = capsys.readouterr().out
    assert "NOTIFICATION:" in output, "Notification message missing in output"
