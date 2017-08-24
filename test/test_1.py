import unittest
import os
import signal
import sys
import time
import threading
import bitprim
from datetime import datetime

def encode_hash(hash):
    return hash[::-1].encode('hex')

def encode_hash_from_byte_array(hash):
    return ''.join('{:02x}'.format(x) for x in hash[::-1])

def decode_hash(hash_str):
    hash = bytearray.fromhex(hash_str) 
    hash = hash[::-1] 
    return bytes(hash)


class TestBitprim(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Preparing Tests ...')
        # cls._exec = bitprim.Executor("", sys.stdout, sys.stderr)
        cls._exec = bitprim.Executor("", None, None)
        res = cls._exec.init_chain()

        # if not res:
        #     raise RuntimeError('init_chain() failed')

        res = cls._exec.run_wait()
        if not res:
            raise RuntimeError('run_wait() failed')

        cls.chain = cls._exec.chain

    @classmethod
    def tearDownClass(cls):
        print('Finishing')
        # bn.destruct(cls._exec)
        cls._exec.stop()
        cls._exec._destroy()
        

    def test_fetch_last_height(self):
        evt = threading.Event()

        _error = [None]
        _height = [None]

        def handler(error, height):
            _error[0] = error
            _height[0] = height
            evt.set()

        self.__class__.chain.fetch_last_height(handler)
        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_error[0], 0)



    def test_fetch_block_header_by_height(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _header = [None]

        def handler(error, header):
            _error[0] = error
            _header[0] = header
            evt.set()

        self.__class__.chain.fetch_block_header_by_height(0, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_header[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_header[0].height, 0)
        self.assertEqual(encode_hash(_header[0].hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_header[0].merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_header[0].previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_header[0].version, 1)
        self.assertEqual(_header[0].bits, 486604799)
        self.assertEqual(_header[0].nonce, 2083236893) #TODO(fernando) ???
        
        unix_timestamp = float(_header[0].timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def test_fetch_block_header_by_hash(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _header = [None]

        def handler(error, header):
            _error[0] = error
            _header[0] = header
            evt.set()

        hash = decode_hash('000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.__class__.chain.fetch_block_header_by_hash(hash, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_header[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_header[0].height, 0)
        self.assertEqual(encode_hash(_header[0].hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_header[0].merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_header[0].previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_header[0].version, 1)
        self.assertEqual(_header[0].bits, 486604799)
        self.assertEqual(_header[0].nonce, 2083236893) #TODO(fernando) ???
        
        unix_timestamp = float(_header[0].timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def test_fetch_block_by_height(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _block = [None]

        def handler(error, block):
            _error[0] = error
            _block[0] = block
            evt.set()

        self.__class__.chain.fetch_block_by_height(0, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_block[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_block[0].header.height, 0)
        self.assertEqual(encode_hash(_block[0].header.hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_block[0].header.merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_block[0].header.previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_block[0].header.version, 1)
        self.assertEqual(_block[0].header.bits, 486604799)
        self.assertEqual(_block[0].header.nonce, 2083236893) #TODO(fernando) ???
        
        unix_timestamp = float(_block[0].header.timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def test_fetch_block_by_hash(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _block = [None]

        def handler(error, block):
            _error[0] = error
            _block[0] = block
            evt.set()

        hash = decode_hash('000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.__class__.chain.fetch_block_by_hash(hash, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_block[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_block[0].header.height, 0)
        self.assertEqual(encode_hash(_block[0].header.hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_block[0].header.merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_block[0].header.previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_block[0].header.version, 1)
        self.assertEqual(_block[0].header.bits, 486604799)
        self.assertEqual(_block[0].header.nonce, 2083236893) #TODO(fernando) ???
        
        unix_timestamp = float(_block[0].header.timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def test_fetch_transaction(self):
        evt = threading.Event()

        _error = [None]
        _transaction = [None]
        _height = [None]
        _index = [None]

        def handler(error, transaction, height, index):
            _error[0] = error
            _transaction[0] = transaction
            _height[0] = height
            _index[0] = index
            evt.set()

        hash_hex_str = '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b'
        hash = decode_hash(hash_hex_str)
        self.__class__.chain.fetch_transaction(hash, True, handler)

        evt.wait()
        #No error
        self.assertNotEqual(_error[0], None)
        self.assertEqual(_error[0], 0)
        #Tx from block zero, must have height zero
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_height[0], 0)
        #It's the first Tx from the block, so index should be zero too
        self.assertNotEqual(_index[0], None)
        self.assertEqual(_index[0], 0)
        #Validate Tx contents
        self.assertNotEqual(_transaction[0], None)
        self.assertEqual(_transaction[0].version, 1)
        self.assertEqual(encode_hash_from_byte_array(_transaction[0].hash), hash_hex_str)
        self.assertEqual(_transaction[0].locktime, 0)
        self.assertEqual(_transaction[0].serialized_size(wire=True), 204)
        self.assertEqual(_transaction[0].serialized_size(wire=False), 204 ) #TODO(dario) Does it make sense that it's the same value?
        self.assertEqual(_transaction[0].fees, 0)


# -----------------------------------------------------------------------------------------------
        
if __name__ == '__main__':
    unittest.main()
