# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import functools
import kth_native as nat
import kth
# from typing import Self

class Header:
    def __init__(self, version: int, previousBlockHash, merkle, timestamp: int, bits: int, nonce: int):
        self.version = version
        self.previousBlockHash = previousBlockHash
        self.merkle = merkle
        self.timestamp = timestamp
        self.bits = bits
        self.nonce = nonce

    @staticmethod
    def _destruct(native):
        return nat.chain_header_destruct(native)

    @staticmethod
    def fromData(version: int, data):
        native = nat.chain_header_factory_from_data(version, data)
        valid = nat.chain_header_is_valid(native)
        if not valid:
            __class__._destruct(native)
            return kth.result.Result(None, False)

        obj = __class__.fromNative(native)
        __class__._destruct(native)
        return kth.result.Result(obj, True)

    @staticmethod
    def fromNative(native, destroy = False):
        obj = __class__(
            nat.chain_header_version(native),
            nat.chain_header_previous_block_hash(native),
            nat.chain_header_merkle(native),
            nat.chain_header_timestamp(native),
            nat.chain_header_bits(native),
            nat.chain_header_nonce(native)
        )
        if destroy:
            __class__._destruct(native)
        return obj

    def toNative(self):
        native = nat.chain_header_construct(
            self.version,
            self.previousBlockHash,
            self.merkle,
            self.timestamp,
            self.bits,
            self.nonce
        )
        return native

    @property
    @functools.cache
    def hash(self):
        native = self.toNative()
        res = nat.chain_header_hash(native)
        self.__class__._destruct(native)
        return res

    @functools.cache
    def rawData(self, version: int):
        native = self.toNative()
        res = nat.chain_header_to_data(native, version)
        self.__class__._destruct(native)
        return res
