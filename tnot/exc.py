'''

TERMINALNOTIFIER.

:author: Jake
:license: MIT

'''

class NotFound(Exception):
    """Called when terminal-notifier isnt present on current system."""
    pass

class InvalidSound(Exception):
    """Called when an invalid or multiple sound(s) are passed to method"""
    pass