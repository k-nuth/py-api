# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth_native as nat
from kth.chain.genericList import GenericList
from kth.chain import Transaction

methods = dict(
    count= lambda native: nat.chain_transaction_list_count(native),
    nth= lambda native, i: nat.chain_transaction_list_nth(native, i),
    fromNative= lambda elementNative: Transaction.fromNative(elementNative),
    constructDefault= lambda: nat.chain_transaction_list_construct_default(),
    pushBack= lambda native, elementNative: nat.chain_transaction_list_push_back(native, elementNative),
    destruct= lambda native: nat.chain_transaction_list_destruct(native)
)
instance = GenericList(methods)

class TransactionList:
    @staticmethod
    def fromNative(native, destroy = False):
        return instance['fromNative'](native, destroy)

    @staticmethod
    def toNative(arr):
        return instance['toNative'](arr)

    @staticmethod
    def destruct(native):
        return instance['destruct'](native)
