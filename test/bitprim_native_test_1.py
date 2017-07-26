import unittest
import os
import signal
import sys
import time
import threading
import bitprim_native as bn

def encode_hash(hash):
    return ''.join('{:02x}'.format(x) for x in hash[::-1])

def decode_hash(hash_str):
    hash = bytearray.fromhex(hash_str) 
    hash = hash[::-1] 
    return buffer(hash)


class TestBinary(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('Preparing Tests ...')
        # cls._exec = bn.construct("", sys.stdout, sys.stderr)
        cls._exec = bn.construct("", None, None)
        res = bn.initchain(cls._exec)
        print(res)
        res = bn.run_wait(cls._exec)
        print(res)

        cls._chain = bn.get_chain(cls._exec)


    def test_fetch_last_height(self):
        evt = threading.Event()

        ge = 7
        gh = 7

        def handler(e, h):
            ge = e
            gh = h
            evt.set()

        bn.chain_fetch_last_height(self.__class__._chain, handler)
        evt.wait()

        print(ge)
        print(gh)


    def test_fetch_block_header_by_height(self):
        evt = threading.Event()

        ge = None
        gheader = None
        gheight = None

        def handler(e, header, height):
            ge = e
            gheader = header
            gheight = height
            evt.set()

        bn.chain_fetch_block_header_by_height(self.__class__._chain, 0, handler)

        evt.wait()

        print(ge)
        print(gheader)
        print(gheight)

        merkle = bn.header_get_merkle(gheader)
        merkle_str = encode_hash(merkle)




    # def fetch_block_header_by_hash(self, hash, handler):
    #     self.fetch_block_header_handler_ = handler
    #     bn.chain_fetch_block_header_by_hash(self.chain, hash, self._fetch_block_header_converter)



    @classmethod
    def tearDownClass(cls):
        print('Finishing')
        bn.destruct(cls._exec)
        
if __name__ == '__main__':
    unittest.main()
