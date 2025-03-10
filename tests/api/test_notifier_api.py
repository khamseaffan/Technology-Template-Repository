import pytest
from src.api.notifier_api import NotifierAPI


@pytest.fixture
def notifier_api() -> NotifierAPI:
    return NotifierAPI()


def test_send_notification(notifier_api: NotifierAPI) -> None:
    response = notifier_api.send_notification("Test notification")
    assert response == {"status": "notified", "message": "Test notification"}
