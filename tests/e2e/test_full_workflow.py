"""Module for end-to-end tests."""

import pytest

import calculator  # type: ignore
import logger
import notifier


@pytest.fixture
def components() -> tuple[calculator.Calculator, logger.Logger, notifier.Notifier]:
    """Return components for full workflow testing."""
    logger_instance = logger.get_logger()
    notifier_instance = notifier.get_notifier()
    calc = calculator.get_calculator()
    calc.logger = logger_instance
    calc.notifier = notifier_instance
    return (calc, logger_instance, notifier_instance)


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


