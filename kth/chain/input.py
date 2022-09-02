# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import functools
import kth_native as nat
import kth
# from typing import Self

class Input:
    def __init__(self, previousOutpoint, script, sequence):
        self.previousOutpoint = previousOutpoint
        self.script = script
        self.sequence = sequence

    @staticmethod
    def _destruct(native):
        return nat.chain_input_destruct(native)

    @staticmethod
    def fromData(data):
        native = nat.chain_input_factory_from_data(data)
        valid = nat.chain_input_is_valid(native)
        if not valid:
            __class__._destruct(native)
            return kth.result.Result(None, False)

        obj = __class__.fromNative(native)
        __class__._destruct(native)
        return kth.result.Result(obj, True)

    @staticmethod
    def fromNative(native, destroy = False):
        obj = Input(
            kth.chain.OutputPoint.fromNative(nat.chain_input_previous_output(native)),
            kth.chain.Script.fromNative(nat.chain_input_script(native), False),
            nat.chain_input_sequence(native)
        )
        if destroy:
            self.__class__._destruct(native)

        return obj

    def toData(self, wire):
        native = self.toNative()
        res = nat.chain_input_to_data(native, wire)
        self.__class__._destruct(native)
        return res

    def toNative(self):
        native = nat.chain_input_construct(
            self.previousOutpoint.toNative(),
            self.script.toNative(False),
            self.sequence
        )
        return native

    @functools.cache
    def rawData(self, wire = True):
        res = self.toData(wire)
        return res



