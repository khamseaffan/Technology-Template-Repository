import pytest
from src.notifier.notifier_api import NotifierAPI

@pytest.fixture
def notifier():
    """Fixture to create a NotifierAPI instance."""
    return NotifierAPI()

def test_send_notification(notifier) -> None:
    """Test notification sending functionality."""
    assert notifier.send_notification("user@example.com", "Test Notification") is True
