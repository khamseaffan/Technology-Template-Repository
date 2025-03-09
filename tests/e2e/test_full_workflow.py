"""Module for end-to-end tests."""

import pytest
from src.calculator.calculator import SimpleCalculator
from src.logger.logger import SimpleLogger
from src.notifier.notifier import SimpleNotifier


@pytest.fixture
def components():
    """Return components for full workflow testing."""
    logger = SimpleLogger()
    notifier = SimpleNotifier()
    calc = SimpleCalculator()
    calc.logger = logger
    calc.notifier = notifier
    return calc, logger, notifier

def test_full_workflow(components, capsys):
    """Test the full workflow of the calculator."""
    calc, logger, notifier = components
    result = calc.add(7, 5)
    notifier.notify(result)
    output = capsys.readouterr().out
    assert "NOTIFICATION:" in output, "Notification message missing in output"
