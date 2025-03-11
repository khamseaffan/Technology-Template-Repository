"""Module for a Logger implementation."""

import logger
import notifier

from typing import Optional
from ._impl import Logger


def get_logger_impl(
    notifier_instance: notifier.Notifier | None = None,
) -> logger.Logger:
    """Return a Logger with an optional notifier parameter."""
    if notifier_instance is None:
        notifier_instance = notifier.get_notifier()
    return Logger(notifier_instance)


logger.get_logger = get_logger_impl  # type: ignore[assignment]
