# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import functools
import kth_native as nat
import kth
# from typing import Self

class OutputPoint:
    def __init__(self, hash, index):
        self.hash = hash
        self.index = index

    @staticmethod
    def _destruct(native):
        return nat.chain_output_point_destruct(native)

    @staticmethod
    def fromNative(native, destroy = False):
        obj = OutputPoint(nat.chain_output_point_hash(native), nat.chain_output_point_index(native))
        if destroy:
            self.__class__._destruct(native)

        return obj

    def toNative(self):
        native = nat.chain_output_point_construct_from_hash_index(self.hash, self.index)
        return native
