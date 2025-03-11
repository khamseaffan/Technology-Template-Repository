"""Module for end-to-end tests."""

import pytest

import logger
import notifier
import calculator 


@pytest.fixture
def components() -> tuple[calculator.Calculator, logger.Logger, notifier.Notifier]:
    """Return components for full workflow testing."""
    logger = logger.get_logger()
    notifier = notifier.get_notifier()
    calc = calculator.Calculator()
    calc.logger = logger
    calc.notifier = notifier
    return (calc, logger, notifier)


def test_full_workflow(
    components: tuple[calculator.Calculator, logger.Logger, notifier.Notifier],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Test the full workflow of the calculator."""
    calc, logger, notifier = components
    result = calc.add(7, 5)
    notifier.notify(str(result))
    output = capsys.readouterr().out
    assert "NOTIFICATION:" in output, "Notification message missing in output"
