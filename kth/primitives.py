# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from enum import IntEnum

class StartModules(IntEnum):
    all = 0,
    justChain = 1,
    justP2P = 2
