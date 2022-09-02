# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import functools
import kth_native as nat
import kth
# from typing import Self

class Script:
    def __init__(self, encoded):
        self.encoded = encoded;

    @staticmethod
    def _destruct(native):
        return nat.chain_script_destruct(native)

    @staticmethod
    def fromData(encoded, prefix):
        native = nat.chain_script_construct(encoded, prefix)
        valid = nat.chain_script_is_valid(native)
        if not valid:
            __class__._destruct(native)
            return kth.result.Result(None, False)

        obj = __class__.fromNative(native, prefix)
        __class__._destruct(native)
        return kth.result.Result(obj, True)

    @staticmethod
    def fromNative(native, prefix, destroy = False):
        obj = Script(nat.chain_script_to_data(native, prefix))
        if destroy:
            __class__._destruct(native)
        return obj

    def toNative(self, prefix):
        native = nat.chain_script_construct(self.encoded, prefix)
        return native

    def toData(self):
        res = self.encoded
        return res

    @functools.cache
    def rawData(self):
        return self.toData()
