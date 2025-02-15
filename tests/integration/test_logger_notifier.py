"""Module for integration tests: logger notifier."""

from unittest.mock import MagicMock

import pytest

from src.logger.logger import Logger
from src.notifier.notifier import Notifier


@pytest.fixture
def mock_notifier():
    """Return a mock notifier."""
    notifier = Notifier()
    notifier.notify = MagicMock()
    return notifier

def test_logger_triggers_notification(mock_notifier):
    """Test that the logger triggers the notifier."""
    logger = Logger()
    logger.notifier = mock_notifier
    logger.log("Threshold exceeded")
    mock_notifier.notify.assert_called_with("Threshold exceeded")
