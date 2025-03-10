"""Module for a Logger implementation."""

import logger
import notifier

from . import _impl


def get_logger_impl(notifier_instance: notifier.Notifier = None) -> logger.Logger:
    """Return a Logger with an optional notifier parameter."""
    if notifier_instance is None:
        notifier_instance = notifier.get_notifier()
    return _impl.Logger(notifier_instance)


logger.get_logger = get_logger_impl
