# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-34m-x86_64-linux-gnu.so
# by generator 1.138
"""
The ``lxml.etree`` module implements the extended ElementTree API
for XML.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .object import object

class ErrorLevels(object):
    """ Libxml2 error levels """
    def _getName(self, *args, **kwargs): # real signature unknown
        """ D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    ERROR = 2
    FATAL = 3
    NONE = 0
    WARNING = 1
    _names = {
        0: 'NONE',
        1: 'WARNING',
        2: 'ERROR',
        3: 'FATAL',
    }
    __dict__ = None # (!) real value is ''


