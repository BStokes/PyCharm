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

from ._Validator import _Validator

class RelaxNG(_Validator):
    """
    RelaxNG(self, etree=None, file=None)
        Turn a document into a Relax NG validator.
    
        Either pass a schema as Element or ElementTree, or pass a file or
        filename through the ``file`` keyword argument.
    """
    def __call__(self, etree): # real signature unknown; restored from __doc__
        """
        __call__(self, etree)
        
                Validate doc using Relax NG.
        
                Returns true if document is valid, false if not.
        """
        pass

    def __init__(self, etree=None, file=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is ''


