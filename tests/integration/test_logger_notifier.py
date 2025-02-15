import pytest
from unittest.mock import MagicMock
from src.logger.logger import Logger
from src.notifier.notifier import Notifier

@pytest.fixture
def mock_notifier():
    notifier = Notifier()
    notifier.notify = MagicMock()
    return notifier

def test_logger_triggers_notification(mock_notifier):
    logger = Logger()
    logger.notifier = mock_notifier
    logger.log("Threshold exceeded")
    mock_notifier.notify.assert_called_once()
