"""Module for a Logger implementation."""

from typing import Optional
import logger
import notifier

from ._impl import Logger


def get_logger_impl(
    notifier_instance: Optional[notifier.Notifier] = None,
) -> logger.Logger:
    """Return a Logger with an optional notifier parameter."""
    if notifier_instance is None:
        notifier_instance = notifier.get_notifier()
    return Logger(notifier_instance)


logger.get_logger = get_logger_impl  # type: ignore[assignment]
