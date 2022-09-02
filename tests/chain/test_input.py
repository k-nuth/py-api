# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth

def test_construct_using_fromData():
    # // // Input start
    # // "0000000000000000000000000000000000000000000000000000000000000000ffffffff"  // 36 (32+4)    Previous Outpoint
    # // "4d"                                                                        // 1            Script size 0x4d = 77
    # // "04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73"
    # // "ffffffff"                                                                  // 4            sequence
    # // // Input end

    scriptStr = '04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73'
    inputStr = '0000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff'

    inputBytes = kth.tools.hex_str_to_bytes(inputStr)
    result = kth.chain.Input.fromData(inputBytes)
    assert result.ok == True
    i = result.obj

    assert i.previousOutpoint.index == 0xffffffff
    assert kth.tools.encode_hash(i.previousOutpoint.hash) == '0000000000000000000000000000000000000000000000000000000000000000'
    assert kth.tools.bytes_to_hex_str(i.script.rawData()) == scriptStr
    assert i.sequence == 0xffffffff
    assert kth.tools.bytes_to_hex_str(i.rawData()) == inputStr

def test_construct_using_main_constructor():
    scriptStr = '04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73'
    scriptBytes = kth.tools.hex_str_to_bytes(scriptStr)
    result = kth.chain.Script.fromData(scriptBytes, False)
    assert result.ok == True
    s = result.obj

    previousOutpoint = kth.chain.OutputPoint(kth.tools.nullHash(), 0xffffffff)

    i = kth.chain.Input(previousOutpoint, s, 0xffffffff)
    assert i.previousOutpoint.index == 0xffffffff
    assert kth.tools.encode_hash(i.previousOutpoint.hash) == '0000000000000000000000000000000000000000000000000000000000000000'
    assert kth.tools.bytes_to_hex_str(i.script.rawData()) == scriptStr
    assert i.sequence == 0xffffffff
    assert kth.tools.bytes_to_hex_str(i.rawData()) == '0000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff'
