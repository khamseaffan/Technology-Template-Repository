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

    assert calc_api is not None
    assert log_api is not None
    assert notifier_api is not None
