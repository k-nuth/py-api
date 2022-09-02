# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from enum import IntEnum

class Network(IntEnum):
    mainnet = 0,
    testnet = 1,
    regtest = 2,
    testnet4 = 3,
    scalenet = 4
