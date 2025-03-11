import pytest

import notifier

# import notifier_impl._impl as notifier

"""Test the Notifier class."""


def test_notify(capsys: pytest.CaptureFixture[str]) -> None:
    """Test the notify method."""
    notifier_insatnce = notifier.get_notifier()
    notifier_insatnce.notify("Test message")
    captured = capsys.readouterr()
    assert "NOTIFICATION: Test message" in captured.out
