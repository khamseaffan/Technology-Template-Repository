from src.notifier.notifier import Notifier

def test_notify(capsys):
    notifier = Notifier()
    notifier.notify("Test message")
    captured = capsys.readouterr()
    assert "NOTIFICATION: Test message" in captured.out