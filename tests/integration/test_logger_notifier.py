"""Module for integration tests: logger notifier."""

from unittest.mock import MagicMock

import pytest

from src.logger.logger import SimpleLogger
from src.notifier.notifier import SimpleNotifier


@pytest.fixture
def mock_notifier():
    """Return a mock notifier."""
    notifier = SimpleNotifier()
    notifier.notify = MagicMock()
    return notifier


def test_logger_triggers_notification(mock_notifier):
    """Test that the logger triggers the notifier."""
    logger = SimpleLogger()
    logger.notifier = mock_notifier
    logger.log("Threshold exceeded")
    mock_notifier.notify.assert_called_with("Threshold exceeded")
