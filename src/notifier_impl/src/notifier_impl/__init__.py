"""Module for a Notifier implementation."""

import notifier

from . import _impl

# Dependency Injection of this implementation into the API

notifier.get_notifier = lambda: _impl.NotifierImpl()
