# encoding: utf-8
# module samba.dcerpc.epmapper
# from /usr/lib/python2.7/dist-packages/samba/dcerpc/epmapper.so
# by generator 1.138
""" epmapper DCE/RPC """

# imports
import dcerpc as __dcerpc
import talloc as __talloc


class rpc_if_id_t(__talloc.Object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(S, *more): # real signature unknown; restored from __doc__
        """ T.__new__(S, ...) -> a new object with type S, a subtype of T """
        pass

    uuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vers_major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vers_minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



