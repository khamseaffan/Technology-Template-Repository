import pytest

from src.calculator.calculator import Calculator
from src.logger.logger import Logger
from src.notifier.notifier import Notifier

@pytest.fixture
def components():
    logger = Logger()
    notifier = Notifier()
    calc = Calculator()
    calc.logger = logger
    logger.notifier = notifier
    return calc, logger, notifier

def test_full_workflow(components, capsys):
    calc, logger, notifier = components
    result = calc.add(7, 5)  
    notifier.notify(result)
    output = capsys.readouterr().out
    assert "NOTIFICATION:" in output, "Notification message missing in output"