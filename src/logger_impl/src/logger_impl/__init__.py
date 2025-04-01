"""Module for a Logger implementation."""

import logger  # ✅ Import logger module
import notifier

from ._impl import LoggerImpl  # ✅ Ensure correct import


def get_logger_impl(
    notifier_instance: notifier.Notifier | None = None,
) -> logger.Logger:
    """Return a Logger with an optional notifier parameter."""
    if notifier_instance is None:
        notifier_instance = notifier.get_notifier()
    return LoggerImpl(notifier_instance)  # ✅ Ensure LoggerImpl is returned

# ✅ Ensure `get_logger()` is overridden properly
logger.get_logger = get_logger_impl
