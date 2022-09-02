# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth

def test_construct_using_fromData():
    genesisStr = '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'
    genesisBytes = kth.tools.hex_str_to_bytes(genesisStr)
    result = kth.chain.Transaction.fromData(1, genesisBytes)
    assert result.ok == True

    tx = result.obj

    hashStr = kth.tools.encode_hash(tx.hash)
    assert hashStr == '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
    assert tx.hash == kth.tools.decode_hash('4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')

    assert tx.version == 1
    assert tx.locktime == 0
    assert len(tx.inputs) == 1
    assert len(tx.outputs) == 1

    inputScriptStr = '04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73'
    inputStr = '0000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff'
    i = tx.inputs[0]
    assert i.previousOutpoint.index == 0xffffffff
    assert kth.tools.encode_hash(i.previousOutpoint.hash) == '0000000000000000000000000000000000000000000000000000000000000000'
    assert kth.tools.bytes_to_hex_str(i.script.rawData()) == inputScriptStr
    assert kth.tools.bytes_to_hex_str(i.rawData()) == inputStr
    assert i.sequence == 0xffffffff

    outputScriptStr = '4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
    outputStr = '00f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
    o = tx.outputs[0]
    assert o.value == kth.tools.toSatoshis(50)
    assert kth.tools.bytes_to_hex_str(o.script.rawData()) == outputScriptStr
    assert kth.tools.bytes_to_hex_str(o.rawData()) == outputStr

    assert kth.tools.bytes_to_hex_str(tx.rawData()) == genesisStr

def test_construct_using_main_constructor():
    inputScriptStr = '04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73'
    inputScriptBytes = kth.tools.hex_str_to_bytes(inputScriptStr)
    result = kth.chain.Script.fromData(inputScriptBytes, False)
    assert result.ok == True
    inputScript = result.obj
    previousOutpoint = kth.chain.OutputPoint(kth.tools.nullHash(), 0xffffffff)
    inputs = [kth.chain.Input(previousOutpoint, inputScript, 0xffffffff)]

    outputScriptStr = '4104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
    outputScriptBytes = kth.tools.hex_str_to_bytes(outputScriptStr)
    result = kth.chain.Script.fromData(outputScriptBytes, False)
    assert result.ok == True
    outputScript = result.obj
    outputs = [kth.chain.Output(kth.tools.toSatoshis(50), outputScript)]
    tx = kth.chain.Transaction(1, 0, inputs, outputs)

    hashStr = kth.tools.encode_hash(tx.hash)
    assert hashStr == '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
    assert tx.hash == kth.tools.decode_hash('4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
    assert tx.version == 1
    assert tx.locktime == 0
    assert len(tx.inputs) == 1
    assert len(tx.outputs) == 1

    genesisStr = '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'

    inputStr = '0000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff'
    i = tx.inputs[0]
    assert i.previousOutpoint.index == 0xffffffff
    assert kth.tools.encode_hash(i.previousOutpoint.hash) == '0000000000000000000000000000000000000000000000000000000000000000'
    assert kth.tools.bytes_to_hex_str(i.script.rawData()) == inputScriptStr
    assert kth.tools.bytes_to_hex_str(i.rawData()) == inputStr
    assert i.sequence == 0xffffffff

    outputStr = '00f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac'
    o = tx.outputs[0]
    assert o.value == kth.tools.toSatoshis(50)
    assert kth.tools.bytes_to_hex_str(o.script.rawData()) == outputScriptStr
    assert kth.tools.bytes_to_hex_str(o.rawData()) == outputStr

    assert kth.tools.bytes_to_hex_str(tx.rawData()) == genesisStr
