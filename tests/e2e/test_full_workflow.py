"""Module for end-to-end tests."""

import calculator
import logger
import notifier
import pytest
import logger_impl
import notifier_impl
import calculator_impl


@pytest.fixture
def components() -> tuple[calculator.Calculator, logger.Logger, notifier.Notifier]:
    """Return components for full workflow testing."""
    notifier_instance = notifier.get_notifier()
    logger_instance = logger.get_logger(notifier_instance) 
    calc = calculator.get_calculator()

    calc.logger_instance = logger_instance
    calc.notifier_instance = notifier_instance

    return (calc, logger_instance, notifier_instance)


def test_full_workflow(
    components: tuple[calculator.Calculator, logger.Logger, notifier.Notifier],
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Test the full workflow of the calculator."""
    calc, logger, notifier = components 
    result = calc.add(7, 5)

    notifier.notify(str(result)) # This line might be redundant if calc.add does it

    output = capsys.readouterr().out
    assert "LOG: Addition: 7 + 5 = 12" in output 
    assert "NOTIFICATION: 12" in output        
