# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth

def test_construct_using_fromData():
    genesisStr = '0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c0101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'
    genesisBytes = kth.tools.hex_str_to_bytes(genesisStr)
    result = kth.chain.Block.fromData(1, genesisBytes)
    assert result.ok == True

    blk = result.obj

    hashStr = kth.tools.encode_hash(blk.hash)
    assert hashStr == '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    assert blk.hash == kth.tools.decode_hash('000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
    assert blk.header.version == 1
    assert blk.header.previousBlockHash == kth.tools.nullHash()
    assert blk.header.merkle == kth.tools.decode_hash('4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
    assert blk.header.timestamp == 1231006505
    assert blk.header.bits == 0x1d00ffff
    assert blk.header.nonce == 2083236893

    assert len(blk.transactions) == 1

    tx = blk.transactions[0]
    assert tx.version == 1
    assert tx.locktime == 0
    assert len(tx.inputs) == 1
    assert len(tx.outputs) == 1
    assert len(tx.inputs) == 1
    assert len(tx.outputs) == 1
    assert kth.tools.encode_hash(tx.hash) == '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
    transactionStr = '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'
    assert kth.tools.bytes_to_hex_str(tx.rawData()) == transactionStr

    assert kth.tools.bytes_to_hex_str(blk.rawData()) == genesisStr

def test_construct_using_main_constructor():
    headerStr = '0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c00'
    headerBytes = kth.tools.hex_str_to_bytes(headerStr)
    result = kth.chain.Header.fromData(1, headerBytes)
    assert result.ok == True
    head = result.obj

    trasactionStr = '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'
    trasactionBytes = kth.tools.hex_str_to_bytes(trasactionStr)
    result = kth.chain.Transaction.fromData(1, trasactionBytes)
    assert result.ok == True

    transactions = [result.obj]

    blk = kth.chain.Block(head, transactions)

    hashStr = kth.tools.encode_hash(blk.hash)
    assert hashStr == '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    assert blk.hash == kth.tools.decode_hash('000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')

    assert blk.header.version == 1
    assert blk.header.previousBlockHash == kth.tools.nullHash()
    assert blk.header.merkle == kth.tools.decode_hash('4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')

    assert blk.header.timestamp == 1231006505
    assert blk.header.bits == 0x1d00ffff
    assert blk.header.nonce == 2083236893

    assert len(blk.transactions) == 1

    tx = blk.transactions[0]
    assert tx.version == 1
    assert tx.locktime == 0
    assert len(tx.inputs) == 1
    assert len(tx.outputs) == 1
    assert len(tx.inputs) == 1
    assert len(tx.outputs) == 1
    assert kth.tools.encode_hash(tx.hash) == '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
    transactionStr = '01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'
    assert kth.tools.bytes_to_hex_str(tx.rawData()) == transactionStr

    genesisStr = '0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c0101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000'
    assert kth.tools.bytes_to_hex_str(blk.rawData()) == genesisStr


# // public void CreateBlockFromHex', async () => {
# //     hex = "0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4adae5494dffff7f20020000000101000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4d04ffff001d0104455468652054696d65732030332f4a616e2f32303039204368616e63656c6c6f72206f6e206272696e6b206f66207365636f6e64206261696c6f757420666f722062616e6b73ffffffff0100f2052a01000000434104678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5fac00000000"
# //     Block b = new Block(1, hex)) {
# //         assert ).toBeTruthy(b.IsValid)
# //     }
# // }
