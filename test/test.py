import unittest
import os
import signal
import sys
import time


scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
os.chdir(scriptPath)
sys.path.append("../bitprim")
import bitprim

#class TestBitprim(unittest.TestCase):

    #def setUp(self):
        #print('Preparing Tests')
        #self.chain= bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr)

    #def test_binary(self):
        #res = self.chain.init_chain()
        #print('In test()')
        #self.assertEqual(1,res)

    #def tearDown(self):
        #print('Finishing\n')

class TestBinary(unittest.TestCase):
    
    def setUp(self):
        print('Preparing Binary Tests')
        self.executor= bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr)

    def test_binary_string(self):
        binary = bitprim.Binary.construct_string("10111010101011011111000000001101")
        self.assertEqual(binary.encoded(), "10111010101011011111000000001101");
        
    def test_binary_blocks(self):
        x = [186,173,240,13]
        binary_block = bitprim.Binary.construct_blocks(32,x)
        #print(','.join(x.encode('hex') for x in binary_block.blocks()))
        self.assertEqual(binary_block.encoded(), "10111010101011011111000000001101");



    def tearDown(self):
        print('Finishing\n')
        
if __name__ == '__main__':
    unittest.main()
