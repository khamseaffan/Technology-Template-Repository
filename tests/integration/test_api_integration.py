from src.api.calculator_api import CalculatorAPI
from src.api.logger_api import LoggerAPI
from src.api.notifier_api import NotifierAPI

RESULT_INTEGRATION = 10


def test_calculator_logger_notifier_integration() -> None:
    """
    Test the integration of CalculatorAPI, LoggerAPI, and NotifierAPI.
    """
    calc_api = CalculatorAPI()
    log_api = LoggerAPI()
    notifier_api = NotifierAPI()
    response = calc_api.calculate("add", 5, 5)
    assert response["result"] == RESULT_INTEGRATION
    log_response = log_api.log_message("Test log entry")
    assert log_response == {"status": "logged", "message": "Test log entry"}
    notify_response = notifier_api.send_notification("Test notification")
    assert notify_response == {"status": "notified", "message": "Test notification"}
