"""Module for integration tests: logger notifier."""

from unittest.mock import MagicMock

import pytest

from src.notifier.notifier_interface import Notifier
from src.logger.logger import SimpleLogger
from src.notifier.notifier import SimpleNotifier


@pytest.fixture
def mock_notifier() -> Notifier:
    """Return a mock notifier."""
    return MagicMock(spec=SimpleNotifier)


def test_logger_triggers_notification(mock_notifier: Notifier) -> None:
    """Test that the logger triggers the notifier."""
    logger = SimpleLogger()
    logger.notifier = mock_notifier
    logger.log("Threshold exceeded")
    assert isinstance(mock_notifier.notify, MagicMock)
    mock_notifier.notify.assert_called_with("Threshold exceeded")
