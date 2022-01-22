import sys
import logging
from logging import NullHandler


if sys.version_info < (3, 5):
    raise BaseException('Only support Python 3.5 or newer.')


# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())
