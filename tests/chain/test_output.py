# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth

def test_construct_using_fromData():
    # // // Output end
    # // "00f2052a01000000"                                                          // 8            Amount
    # // "43"                                                                        // 1            Script size 0x43 = 67
    # // "4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac"
    # // // Output end

    scriptStr = '4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
    outputStr = '00f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'

    outputBytes = kth.tools.hex_str_to_bytes(outputStr)
    result = kth.chain.Output.fromData(outputBytes)
    assert result.ok == True
    o = result.obj

    assert o.value == kth.tools.toSatoshis(50)
    assert kth.tools.bytes_to_hex_str(o.script.rawData()) == scriptStr
    assert kth.tools.bytes_to_hex_str(o.rawData()) == outputStr

def test_construct_using_main_constructor():
    scriptStr = '4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
    scriptBytes = kth.tools.hex_str_to_bytes(scriptStr)
    result = kth.chain.Script.fromData(scriptBytes, False)
    assert result.ok == True
    s = result.obj

    o = kth.chain.Output(kth.tools.toSatoshis(50), s)
    assert o.value == kth.tools.toSatoshis(50)
    assert kth.tools.bytes_to_hex_str(o.script.rawData()) == scriptStr
    assert kth.tools.bytes_to_hex_str(o.rawData()) == '00f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
