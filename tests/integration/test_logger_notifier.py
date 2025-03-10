"""Module for integration tests: logger notifier."""

from unittest.mock import MagicMock

import pytest

import notifier
from logger import get_logger


@pytest.fixture
def mock_notifier() -> notifier.Notifier:
    """Return a mock notifier."""
    return MagicMock(spec=notifier.get_notifier())


def test_logger_triggers_notification(mock_notifier: notifier.Notifier) -> None:
    """Test that the logger triggers the notifier."""
    logger = get_logger()
    logger.notifier = mock_notifier
    logger.log("Threshold exceeded")
    assert isinstance(mock_notifier.notify, MagicMock)
    mock_notifier.notify.assert_called_with("Threshold exceeded")
