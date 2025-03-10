import pytest

from src.notifier.notifier import SimpleNotifier

"""Test the Notifier class."""


def test_notify(capsys: pytest.CaptureFixture[str]) -> None:
    """Test the notify method."""
    notifier = SimpleNotifier()
    notifier.notify("Test message")
    captured = capsys.readouterr()
    assert "NOTIFICATION: Test message" in captured.out
