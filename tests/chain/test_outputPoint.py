# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth

def test_use_constructor():
    op = kth.chain.OutputPoint(kth.tools.nullHash(), 0xffffffff)
    assert op.index == 0xffffffff
    assert kth.tools.encode_hash(op.hash) == '0000000000000000000000000000000000000000000000000000000000000000'
