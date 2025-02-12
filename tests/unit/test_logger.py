from src.logger.logger import Logger

"""Test the logger class."""

def test_log(capsys) -> None:
    """Test the log method."""
    logger = Logger()
    logger.log("Test message")
    captured = capsys.readouterr()
    assert "LOG: Test message" in captured.out
