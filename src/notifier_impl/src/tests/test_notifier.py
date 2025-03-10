import pytest

from notifier_impl._impl import Notifier


"""Test the Notifier class."""


def test_notify(capsys: pytest.CaptureFixture[str]) -> None:
    """Test the notify method."""
    notifier = Notifier()
    notifier.notify("Test message")
    captured = capsys.readouterr()
    assert "NOTIFICATION: Test message" in captured.out
