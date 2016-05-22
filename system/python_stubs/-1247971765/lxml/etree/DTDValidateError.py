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

from .DTDError import DTDError

class DTDValidateError(DTDError):
    """ Error while validating an XML document with a DTD. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


