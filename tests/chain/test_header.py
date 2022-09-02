# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth

def test_construct_using_fromData():
    genesisStr = '0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c00'
    genesisBytes = kth.tools.hex_str_to_bytes(genesisStr)
    result = kth.chain.Header.fromData(1, genesisBytes)
    assert result.ok == True
    h = result.obj
    hashStr = kth.tools.encode_hash(h.hash)

    assert hashStr == '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    assert h.hash == kth.tools.decode_hash('000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')

    assert h.version == 1
    assert h.previousBlockHash == kth.tools.nullHash()
    assert h.merkle == kth.tools.decode_hash('4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
    assert h.timestamp == 1231006505
    assert h.bits == 0x1d00ffff
    assert h.nonce == 2083236893
    assert kth.tools.bytes_to_hex_str(h.rawData(1)) == genesisStr


def test_construct_using_main_constructor():
    previousBlockHash = kth.tools.nullHash()
    merkle = kth.tools.decode_hash('4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
    h = kth.chain.Header(1, previousBlockHash, merkle, 1231006505, 0x1d00ffff, 2083236893)

    assert kth.tools.encode_hash(h.hash) == '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    assert kth.tools.encode_hash(h.hash) == '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f'
    assert h.version == 1
    assert kth.tools.encode_hash(h.previousBlockHash) == '0000000000000000000000000000000000000000000000000000000000000000'

    assert kth.tools.encode_hash(h.merkle) == '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
    assert h.timestamp == 1231006505
    assert h.bits == 0x1d00ffff
    assert h.nonce == 2083236893
    assert kth.tools.bytes_to_hex_str(h.rawData(1)) == '0100000000000000000000000000000000000000000000000000000000000000000000003ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c00'
