from src.logger.logger import Logger

def test_log(capsys):
    logger = Logger()
    logger.log("Test message")
    captured = capsys.readouterr()
    assert "LOG: Test message" in captured.out