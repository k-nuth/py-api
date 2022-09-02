# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import functools
import kth_native as nat
import kth
# from typing import Self

# kth_transaction_t kth_chain_transaction_construct(uint32_t version, uint32_t locktime, kth_input_list_t inputs, kth_output_list_t outputs);

class Transaction:
    def __init__(self, version, locktime, inputs, outputs):
        self.version = version
        self.locktime = locktime
        self.inputs = inputs
        self.outputs = outputs

    @staticmethod
    def _destruct(native):
        return nat.chain_transaction_destruct(native)


    @staticmethod
    def fromData(version, data):
        native = nat.chain_transaction_factory_from_data(version, data)
        valid = nat.chain_transaction_is_valid(native)
        if not valid:
            __class__._destruct(native)
            return kth.result.Result(None, False)

        obj = __class__.fromNative(native)
        __class__._destruct(native)
        return kth.result.Result(obj, True)

    @staticmethod
    def fromNative(native, destroy = False):
        obj = Transaction(
            nat.chain_transaction_version(native),
            nat.chain_transaction_locktime(native),
            kth.chain.InputList.fromNative(nat.chain_transaction_inputs(native)),
            kth.chain.OutputList.fromNative(nat.chain_transaction_outputs(native))
        )

        if destroy:
            self.__class__._destruct(native)

        return obj


    def toData(self, wire = True):
        native = self.toNative()
        res = nat.chain_transaction_to_data(native, wire)
        self.__class__._destruct(native)
        return res

    def toNative(self):
        native = nat.chain_transaction_construct(
            self.version,
            self.locktime,
            kth.chain.InputList.toNative(self.inputs),
            kth.chain.OutputList.toNative(self.outputs)
        )
        return native

    @property
    def hash(self):
        native = self.toNative()
        res = nat.chain_transaction_hash(native)
        self.__class__._destruct(native)
        return res

    @functools.cache
    def rawData(self, wire = True):
        res = self.toData(wire)
        return res
