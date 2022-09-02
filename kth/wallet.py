# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth_native as nat
import sys
import time

##
# Wallet handling utilities
class Wallet:
    # def __init__(self, ptr):
    #     self._ptr = ptr

    ##
    # Convert mnemonics to a seed
    # @param mnemonics: A list of strings representing the mnemonics
    # @return A new seed
    @classmethod
    def mnemonics_to_seed(cls, mnemonics):
        wl = nat.word_list_construct()

        for m in mnemonics:
            nat.word_list_add_word(wl, m)

        # # seed = nat.wallet_mnemonics_to_seed(wl)[::-1].hex();
        # seed = nat.wallet_mnemonics_to_seed(wl).hex();

        seed_ptr = nat.wallet_mnemonics_to_seed(wl)
        print(seed_ptr)
        seed = nat.long_hash_t_to_str(seed_ptr).hex()
        print(seed)
        nat.long_hash_t_free(seed_ptr)

        nat.word_list_destruct(wl)
        # print('Wallet.mnemonics_to_seed')

        return seed
