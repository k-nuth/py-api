# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth

def test_construct_using_fromData_prefix_False():
    scriptStr = '0130323066643366303435313438356531306633383837363437356630643265396130393739343332353534313766653139316438623963623230653430643863333030326431373463336539306366323433393231383761313037623634373337633937333135633932393264653431373731636565613062323563633534353732653302ae'
    scriptBytes = kth.tools.hex_str_to_bytes(scriptStr)
    result = kth.chain.Script.fromData(scriptBytes, False)
    assert result.ok == True
    s = result.obj
    roundtrip = s.rawData()
    assert roundtrip == scriptBytes

def test_construct_using_fromData_prefix_True():
    scriptStr = '3045022100ff1fc58dbd608e5e05846a8e6b45a46ad49878aef6879ad1a7cf4c5a7f853683022074a6a10f6053ab3cddc5620d169c7374cd42c1416c51b9744db2c8d9febfb84d01'
    scriptBytes = kth.tools.hex_str_to_bytes(scriptStr)
    result = kth.chain.Script.fromData(scriptBytes, True)
    assert result.ok == True

def test_construct_using_fromData_roundtrips():
    scriptStr = '76a91406ccef231c2db72526df9338894ccf9355e8f12188ac'
    scriptBytes = kth.tools.hex_str_to_bytes(scriptStr)
    result = kth.chain.Script.fromData(scriptBytes, False)
    assert result.ok == True
    s = result.obj
    roundtrip = s.rawData()
    assert roundtrip == scriptBytes
