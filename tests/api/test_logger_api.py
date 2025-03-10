import pytest
from src.api.logger_api import LoggerAPI

@pytest.fixture
def logger_api():
    return LoggerAPI()

def test_log_message(logger_api):
    response = logger_api.log_message("Test log")
    assert response == {"status": "logged", "message": "Test log"}
