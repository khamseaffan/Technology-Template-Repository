import pytest

from src.logger.logger import SimpleLogger

"""Test the logger class."""


def test_log(capsys: pytest.CaptureFixture[str]) -> None:
    """Test the log method."""
    logger = SimpleLogger()
    logger.log("Test message")
    captured = capsys.readouterr()
    assert "LOG: Test message" in captured.out
