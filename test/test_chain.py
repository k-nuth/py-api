import unittest
import os
import signal
import sys
import time
import threading
import bitprim
from datetime import datetime

def encode_hash(h):
    if (sys.version_info > (3, 0)):
        return ''.join('{:02x}'.format(x) for x in h[::-1])
    else:
        return h[::-1].encode('hex')

def encode_hash_from_byte_array(hash):
    return ''.join('{:02x}'.format(x) for x in hash[::-1])

def decode_hash(hash_str):
    h = bytearray.fromhex(hash_str) 
    h = h[::-1] 
    return bytes(h)


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
        self.assertEqual(_block[0].total_inputs(True), 1)
        
        unix_timestamp = float(_block[0].header.timestamp)
        utc_time = datetime.utcfromtimestamp(unix_timestamp)
        self.assertEqual(utc_time.strftime("%Y-%m-%d %H:%M:%S"), "2009-01-03 18:15:05")

    def wait_until_block(self, desired_height):

        _error = [0]
        _block_fetched = [False]        

        def handler(error, height):
            print("fetch_last_height handler invoked; height: %d" % height)
            _error[0] = error
            _block_fetched[0] = (height >= desired_height)

        while not _block_fetched[0] and _error[0] == 0:
            self.__class__.chain.fetch_last_height(handler)
            if not _block_fetched[0]:
                time.sleep(30)

    def test_fetch_block_height(self):
        evt = threading.Event()

        _error = [None]
        _height = [None]

        def handler(error, height):
            _error[0] = error
            _height[0] = height
            evt.set()

        self.__class__.chain.fetch_block_height(decode_hash("000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"), handler)
        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_height[0], 0)

    def test_fetch_spend(self):       
        evt = threading.Event()
        self.wait_until_block(170)
        _error = [None]
        _point = [None]

        def handler(error, point):
            _error[0] = error
            _point[0] = point
            evt.set()

        output_point = bitprim.OutputPoint.construct_from_hash_index(decode_hash("0437cd7f8525ceed2324359c2d0ba26006d92d856a9c20fa0241106ee5a597c9"),0)
        self.__class__.chain.fetch_spend(output_point, handler)
        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_point[0], None)
        self.assertEqual(_error[0], 0)

        hashresult = _point[0].hash
        self.assertEqual(encode_hash(hashresult), "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16")
        self.assertEqual(_point[0].index, 0)


    def test_fetch_merkle_block_by_hash(self):
        evt = threading.Event()

        _error = [None]
        _merkle = [None]
        _height = [None]

        def handler(error, merkle, height):
            _error[0] = error
            _merkle[0] = merkle
            _height[0] = height
            evt.set()

        self.__class__.chain.fetch_merkle_block_by_hash(decode_hash("000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"), handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_merkle[0], None)
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_error[0], 0)

        self.assertEqual(_merkle[0].height, 0)
        self.assertEqual(_merkle[0].total_transaction_count, 1)
        _header = _merkle[0].header
        self.assertEqual(encode_hash(_header.hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_header.merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_header.previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_header.version, 1)
        self.assertEqual(_header.bits, 486604799)
        self.assertEqual(_header.nonce, 2083236893)

    def test_fetch_merkle_block_by_height(self):
        evt = threading.Event()

        _error = [None]
        _merkle = [None]
        _height = [None]

        def handler(error, merkle, height):
            _error[0] = error
            _merkle[0] = merkle
            _height[0] = height
            evt.set()

        self.__class__.chain.fetch_merkle_block_by_height(0, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_merkle[0], None)
        self.assertNotEqual(_height[0], None)
        self.assertEqual(_error[0], 0)

        self.assertEqual(_merkle[0].height, 0)
        self.assertEqual(_merkle[0].total_transaction_count, 1)
        _header = _merkle[0].header
        self.assertEqual(encode_hash(_header.hash), '000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f')
        self.assertEqual(encode_hash(_header.merkle), '4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b')
        self.assertEqual(encode_hash(_header.previous_block_hash), '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(_header.version, 1)
        self.assertEqual(_header.bits, 486604799)
        self.assertEqual(_header.nonce, 2083236893)

    #  def test_fetch_compact_block_by_height(self):
    #     evt = threading.Event()

    #     _error = [None]
    #     _compact = [None]
    #     _height = [None]

    #     def handler(error, compact):
    #         _error[0] = error
    #         _compact[0] = compact
    #         #_height[0] = height
    #         evt.set()

    #     self.__class__.chain.fetch_compact_block_by_height(0, handler)

    #     evt.wait()

    #     self.assertNotEqual(_error[0], None)
    #     self.assertNotEqual(_compact[0], None)
    #     #self.assertNotEqual(_height[0], None)
    #     self.assertEqual(_error[0], 0)

    #     #self.assertEqual(_compact[0].height, 0)
    #     #self.assertEqual(_compact[0].total_transaction_count, 1)

    # def test_fetch_compact_block_by_hash(self):
    #     evt = threading.Event()

    #     _error = [None]
    #     _compact = [None]
    #     _height = [None]

    #     def handler(error, compact, height):
    #         _error[0] = error
    #         _compact[0] = compact
    #         _height[0] = height
    #         evt.set()

    #     self.__class__.chain.fetch_compact_block_by_hash(decode_hash("000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"), handler)

    #     evt.wait()

    #     self.assertNotEqual(_error[0], None)
    #     self.assertNotEqual(_compact[0], None)
    #     self.assertEqual(_error[0], 0)

    #     #self.assertEqual(_compact[0].height, 0)
    #     #self.assertEqual(_compact[0].total_transaction_count, 1)

    def test_fetch_stealth(self):
        evt = threading.Event()

        _error = [None]
        _list = [None]

        def handler(error, list):
            _error[0] = error
            _list[0] = list
            evt.set()

        self.__class__.chain.fetch_stealth("1111", 0, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        #self.assertNotEqual(_list[0], None)
        self.assertEqual(_error[0], 0)

        self.assertEqual(_list[0].count, 0)

    # def test_fetch_stealth_complete_chain(self):
    #     evt = threading.Event()

    #     _error = [None]
    #     _list = [None]

    #     def handler(error, list):
    #         _error[0] = error
    #         _list[0] = list
    #         evt.set()

    #     self.__class__.chain.fetch_stealth("01", 325500, handler)

    #     evt.wait()

    #     self.assertNotEqual(_error[0], None)
    #     self.assertNotEqual(_list[0], None)
    #     self.assertEqual(_error[0], 0)

        #     _stealthlist = _list[0]
    #     stealth = _stealthlist.nth(0)

    #     self.assertEqual(_list[0].count, 4)
    #     self.assertEqual(decode_hash(stealth.ephemeral_public_key_hash), "022ec7cd1d0697e746c4044a4582db99ac85e9158ebd2c0fb2a797759ca418dd8d")


    def test_fetch_transaction(self):
        evt = threading.Event()

        _error = [None]
        _transaction = [None]
        _height = [None]
        _index = [None]

        tx_block_height = 170 #First non-coinbase tx belongs to this block
        self.wait_until_block(tx_block_height)

        def handler(error, transaction, height, index):
            _error[0] = error
            _transaction[0] = transaction
            _height[0] = height
            _index[0] = index
            evt.set()

        hash_hex_str = 'f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16'
        hash = decode_hash(hash_hex_str)
        self.__class__.chain.fetch_transaction(hash, True, handler)

        evt.wait()
        #No error
        self.assertEqual(_error[0], 0)
        #Tx from block zero, must have height zero
        self.assertEqual(_height[0], tx_block_height)
        #It's the only non-coinbase tx from the block, so index should be 1
        self.assertEqual(_index[0], 1)
        #Validate Tx contents
        self.check_non_coinbase_tx(_transaction[0], hash_hex_str, tx_block_height)

    def check_non_coinbase_tx(self, tx, tx_hash_hex_str, tx_block_height):
        self.assertEqual(tx.version, 1)
        self.assertEqual(encode_hash_from_byte_array(tx.hash), tx_hash_hex_str)
        self.assertEqual(tx.locktime, 0)
        self.assertEqual(tx.serialized_size(wire=True), 275)
        self.assertEqual(tx.serialized_size(wire=False), 275) #TODO(dario) Does it make sense that it's the same value?
        self.assertEqual(tx.fees, 0)
        self.assertTrue(0 <= tx.signature_operations() <= 2 ** 64)
        self.assertEqual(tx.signature_operations_bip16_active(True), 2)
        self.assertEqual(tx.signature_operations_bip16_active(False), 2) #TODO(dario) Does it make sense that it's the same value?
        self.assertEqual(tx.total_input_value(), 0)
        self.assertEqual(tx.total_output_value(), 5000000000) #50 BTC = 5 M Satoshi
        self.assertEqual(tx.is_coinbase(), False)
        self.assertEqual(tx.is_null_non_coinbase(), False)
        self.assertEqual(tx.is_oversized_coinbase(), False)
        self.assertEqual(tx.is_overspent(), True) #TODO(dario) Is it really overspent?
        self.assertEqual(tx.is_double_spend(True), False)
        self.assertEqual(tx.is_double_spend(False), False)
        self.assertEqual(tx.is_missing_previous_outputs(), True)
        self.assertEqual(tx.is_final(tx_block_height, 0), True)
        self.assertEqual(tx.is_locktime_conflict(), False)

    def test_fetch_output(self):
        evt = threading.Event()

        _error = [None]
        _output = [None]

        tx_block_height = 170 #First non-coinbase tx belongs to this block
        self.wait_until_block(tx_block_height)

        def handler(error, output):
            _error[0] = error
            _output[0] = output
            evt.set()

        hash_hex_str = 'f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16'
        hash = decode_hash(hash_hex_str)
        self.__class__.chain.fetch_output(hash, 1, True, handler)

        evt.wait()
        self.assertEqual(_error[0], 0)
        self.check_tx_output(_output[0])

    def check_tx_output(self, o):
        self.assertEqual(o.is_valid, True)
        self.assertEqual(o.serialized_size(True), 76)
        self.assertEqual(o.serialized_size(False), 80)
        self.assertEqual(o.value, 4000000000)
        self.assertEqual(o.signature_operations, True)
        s = o.script
        self.assertTrue(s.is_valid)
        self.assertTrue(s.is_valid_operations)
        self.assertEqual(s.satoshi_content_size, 67)
        self.assertEqual(s.serialized_size(0), 67)
        self.assertEqual(s.serialized_size(1), 68)
        self.assertEqual(s.serialized_size(2), 68)
        #TODO(dario) Isn't this missing push data(65) at the beginning?
        self.assertEqual(s.to_string(True), "[0411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3] checksig")
        #TODO(dario) Does it make sense that it's the same value?
        self.assertEqual(s.to_string(False), "[0411db93e1dcdb8a016b49840f8c53bc1eb68a382e97b1482ecad7b148a6909a5cb2e0eaddfb84ccf9744464f82e160bfa9b8b64f9d4c03f999b8643f656b412a3] checksig")
        self.assertEqual(s.sigops(True), 1)
        self.assertEqual(s.sigops(False), 1) #TODO(dario) Does it make sense that it's the same value?
        #self.assertEqual(s.embedded_sigops(s), 0) #TODO(dario) Accessing this property segfaults
        #self.assertEqual(s.embedded_sigops(False), 0)

    def test_fetch_transaction_position(self):
        evt = threading.Event()

        tx_block_height = 170 #First non-coinbase tx belongs to this block
        self.wait_until_block(tx_block_height)

        _error = [None]
        _position = [None]
        _height = [None]

        def handler(error, position, height):
            _error[0] = error
            _position[0] = position
            _height[0] = height
            evt.set()

        hash_hex_str = 'f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16'
        hash = decode_hash(hash_hex_str)
        self.__class__.chain.fetch_transaction_position(hash, True, handler)
        evt.wait()

        self.assertEqual(_error[0], 0)
        self.assertEqual(_position[0], 1)
        self.assertEqual(_height[0], 170)

    def test_fetch_block_by_hash_170(self):
        # https://blockchain.info/es/block-height/0
        evt = threading.Event()

        _error = [None]
        _block = [None]

        self.wait_until_block(170)

        def handler(error, block):
            _error[0] = error
            _block[0] = block
            evt.set()

        hash = decode_hash('00000000d1145790a8694403d4063f323d499e655c83426834d4ce2f8dd4a2ee')
        self.__class__.chain.fetch_block_by_hash(hash, handler)

        evt.wait()

        self.assertNotEqual(_error[0], None)
        self.assertNotEqual(_block[0], None)
        self.assertEqual(_error[0], 0)
        self.assertEqual(_block[0].header.height, 170)
        self.assertEqual(encode_hash(_block[0].hash), '00000000d1145790a8694403d4063f323d499e655c83426834d4ce2f8dd4a2ee')
        self.assertEqual(encode_hash(_block[0].header.merkle), '7dac2c5666815c17a3b36427de37bb9d2e2c5ccec3f8633eb91a4205cb4c10ff')
        self.assertEqual(encode_hash(_block[0].header.previous_block_hash), '000000002a22cfee1f2c846adbd12b3e183d4f97683f85dad08a79780a84bd55')
        self.assertEqual(_block[0].header.version, 1)
        self.assertEqual(_block[0].header.bits, 486604799)
        self.assertEqual(_block[0].header.nonce, 1889418792)
        self.assertEqual(_block[0].total_inputs(True), 2)

# -----------------------------------------------------------------------------------------------
        
if __name__ == '__main__':
    unittest.main()
