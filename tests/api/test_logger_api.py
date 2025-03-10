import pytest
from src.logger.logger_api import LoggerAPI

@pytest.fixture
def logger():
    """Fixture to create a LoggerAPI instance."""
    return LoggerAPI()

def test_logging(logger) -> None:
    """Test if messages are logged correctly."""
    assert logger.log_message("Test message", "info") is None
