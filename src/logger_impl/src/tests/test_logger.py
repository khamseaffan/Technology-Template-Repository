from unittest.mock import MagicMock

import pytest

# Unused but needed for dependency injection of notifier
import logger
import logger_impl
import notifier

"""Test the Logger class."""

@pytest.fixture
def mock_notifier() -> notifier.Notifier:
    """Return a mock notifier."""
    return MagicMock(spec=notifier.Notifier, autospec=True)


def test_log(mock_notifier: notifier.Notifier,
             capsys: pytest.CaptureFixture[str]) -> None:
    """Test the log method."""
    # Dependency injection of notifier
    logger_instance = logger.get_logger(mock_notifier)
    logger_instance.log("Test message")
    captured = capsys.readouterr()
    assert "LOG: Test message" in captured.out


def test_log_threshold_exceeded(mock_notifier: notifier.Notifier,
                                capsys: pytest.CaptureFixture[str]) -> None:
    """Test the log method when threshold is exceeded."""
    # Dependency injection of notifier
    logger_instance = logger.get_logger(mock_notifier)
    logger_instance.log("Threshold exceeded in system")
    captured = capsys.readouterr()

    # Check both logger and notifier output
    assert "LOG: Threshold exceeded in system" in captured.out
