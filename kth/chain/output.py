# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import functools
import kth_native as nat
import kth
# from typing import Self

class Output:
    def __init__(self, value, script):
        self.value = value
        self.script = script

    @staticmethod
    def _destruct(native):
        return nat.chain_output_destruct(native)

    @staticmethod
    def fromData(data):
        native = nat.chain_output_factory_from_data(data)
        valid = nat.chain_output_is_valid(native)
        if not valid:
            __class__._destruct(native)
            return kth.result.Result(None, False)

        obj = __class__.fromNative(native)
        __class__._destruct(native)
        return kth.result.Result(obj, True)

    @staticmethod
    def fromNative(native, destroy = False):
        obj = Output(nat.chain_output_value(native), kth.chain.Script.fromNative(nat.chain_output_script(native), False))
        if destroy:
            self.__class__._destruct(native)
        return obj

    def toData(self, wire):
        native = self.toNative()
        res = nat.chain_output_to_data(native, wire)
        self.__class__._destruct(native)
        return res

    def toNative(self):
        native = nat.chain_output_construct(self.value, self.script.toNative(False))
        return native

    @functools.cache
    def rawData(self, wire = True):
        res = self.toData(wire)
        return res
