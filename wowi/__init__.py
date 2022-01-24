import sys
import logging
from logging import NullHandler

from wowi.utils import (
    run_shell_cmd,
    countdown,
    resolve_path,
    live_as_shell_cmd
)

__all__ = [
    'countdown',
    'run_shell_cmd',
    'live_as_shell_cmd',
    'resolve_path',
]

if sys.version_info < (3, 5):
    raise BaseException('Only support Python 3.5 or newer.')


# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())
