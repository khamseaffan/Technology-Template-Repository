import pytest

import notifier

# Unused but needed for dependency injection of notifier
from logger_impl._impl import Logger

"""Test the Logger class."""


def test_log(capsys: pytest.CaptureFixture[str]) -> None:
    """Test the log method."""
    # Dependency injection of notifier
    logger = Logger(notifier_instance=notifier.get_notifier())
    logger.log("Test message")
    captured = capsys.readouterr()
    assert "LOG: Test message" in captured.out


def test_log_threshold_exceeded(capsys: pytest.CaptureFixture[str]) -> None:
    """Test the log method when threshold is exceeded."""
    # Dependency injection of notifier
    logger = Logger(notifier_instance=notifier.get_notifier())
    logger.log("Threshold exceeded in system")
    captured = capsys.readouterr()

    # Check both logger and notifier output
    assert "LOG: Threshold exceeded in system" in captured.out
    assert "NOTIFICATION: Threshold exceeded in system" in captured.out
