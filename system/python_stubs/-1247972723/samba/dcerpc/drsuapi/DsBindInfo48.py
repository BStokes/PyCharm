# encoding: utf-8
# module samba.dcerpc.drsuapi
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/drsuapi.so
# by generator 1.138
""" drsuapi DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class DsBindInfo48(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    config_dn_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    repl_epoch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supported_extensions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    supported_extensions_ext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



