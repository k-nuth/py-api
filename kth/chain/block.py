# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import functools
import kth_native as nat
import kth
# from typing import Self

class Block:
    def __init__(self, header, transactions):
        self.header = header
        self.transactions = transactions

    @staticmethod
    def _destruct(native):
        return nat.chain_block_destruct(native)

    @staticmethod
    def fromData(version, data):
        native = nat.chain_block_factory_from_data(version, data)
        valid = nat.chain_block_is_valid(native)
        if not valid:
            __class__._destruct(native)
            return kth.result.Result(None, False)

        obj = __class__.fromNative(native)
        __class__._destruct(native)
        return kth.result.Result(obj, True)

    @staticmethod
    def fromNative(native, destroy = False):
        obj = Block(
            kth.chain.Header.fromNative(nat.chain_block_header(native)),
            kth.chain.TransactionList.fromNative(nat.chain_block_transactions(native))
        )
        if destroy:
            __class__._destruct(native)

        return obj

    def toData(self, wire = True):
        native = self.toNative()
        res = nat.chain_block_to_data(native, wire)
        self.__class__._destruct(native)
        return res

    def toNative(self):
        native = nat.chain_block_construct(self.header.toNative(), kth.chain.TransactionList.toNative(self.transactions))
        return native

    @property
    def hash(self):
        native = self.toNative()
        res = nat.chain_block_hash(native)
        self.__class__._destruct(native)
        return res

    @functools.cache
    def rawData(self, wire = True):
        res = self.toData(wire)
        return res
