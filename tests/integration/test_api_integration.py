import pytest
from src.api.calculator_api import CalculatorAPI
from src.api.logger_api import LoggerAPI
from src.api.notifier_api import NotifierAPI

def test_calculator_logger_notifier_integration():
    calc_api = CalculatorAPI()
    log_api = LoggerAPI()
    notif_api = NotifierAPI()

    response = calc_api.calculate("add", 5, 5)
    assert response["result"] == 10

    log_response = log_api.log_message("Test log entry")
    assert log_response["status"] == "logged"

    notif_response = notif_api.send_notification("Test notification")
    assert notif_response["status"] == "notified"
