#!/usr/bin/env python3

from collections import namedtuple

# a namedtuple like that given by sys.version_info
__version_info__ = namedtuple(
    'version_info', ['major', 'minor', 'micro', 'releaselevel', 'serial']
)
__version__ = '{v.major}.{v.minor}.{v.micro}'.format(
    v=__version_info__(
        major=0,
        minor=6,
        micro=9,
        releaselevel=None,
        serial=None,
    )
)
