# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth_native as nat
from kth.chain.genericList import GenericList
from kth.chain import Output

methods = dict(
    count= lambda native: nat.chain_output_list_count(native),
    nth= lambda native, i: nat.chain_output_list_nth(native, i),
    fromNative= lambda elementNative: Output.fromNative(elementNative),
    constructDefault= lambda: nat.chain_output_list_construct_default(),
    pushBack= lambda native, elementNative: nat.chain_output_list_push_back(native, elementNative),
    destruct= lambda native: nat.chain_output_list_destruct(native)
)
instance = GenericList(methods)

class OutputList:
    @staticmethod
    def fromNative(native, destroy = False):
        return instance['fromNative'](native, destroy)

    @staticmethod
    def toNative(arr):
        return instance['toNative'](arr)

    @staticmethod
    def destruct(native):
        return instance['destruct'](native)
