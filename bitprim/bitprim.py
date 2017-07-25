 # 
 # Copyright (c) 2017 Bitprim developers (see AUTHORS)
 # 
 # This file is part of Bitprim.
 # 
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU Affero General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # (at your option) any later version.
 # 
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU Affero General Public License for more details.
 # 
 # You should have received a copy of the GNU Affero General Public License
 # along with this program.  If not, see <http://www.gnu.org/licenses/>.
 # 

import bitprim_native

# ------------------------------------------------------

__title__ = "bitprim"
__summary__ = "Bitcoin development platform"
__uri__ = "https://github.com/bitprim/bitprim-py"
__version__ = "1.0.4"
__author__ = "Bitprim Inc"
__email__ = "dev@bitprim.org"
__license__ = "MIT"
__copyright__ = "Copyright 2017 Bitprim developers"


# ------------------------------------------------------
class Wallet:
    # def __init__(self, ptr):
    #     self.ptr = ptr

    def mnemonics_to_seed(self, mnemonics):
        wl = bitprim_native.word_list_construct()
        for m in mnemonics:
            bitprim_native.word_list_add_word(wl, m)

        # # seed = bitprim_native.wallet_mnemonics_to_seed(wl)[::-1].hex();
        # seed = bitprim_native.wallet_mnemonics_to_seed(wl).hex();

        seed_ptr = bitprim_native.wallet_mnemonics_to_seed(wl);
        print(seed_ptr)
        seed = bitprim_native.long_hash_t_to_str(seed_ptr).hex();
        print(seed)
        bitprim_native.long_hash_t_free(seed_ptr);

        bitprim_native.word_list_destruct(wl)
        # print('Wallet.mnemonics_to_seed')

        return seed;

# ------------------------------------------------------
class Header:

    def __init__(self, pointer, height):
        self.ptr = pointer
        self.height_ = height
        
    def height(self):
        return self.height_

    def version(self):
        return bitprim_native.header_get_version(self.ptr)

    def set_version(self, version):
        bitprim_native.header_set_version(self.ptr, version)

    def previous_block_hash(self):
        print('previous_block_hash BEFORE')
        return bitprim_native.header_get_previous_block_hash(self.ptr)
    
    #def set_previous_block_hash(self,hashn):        
        #return bitprim_native.header_set_previous_block_hash(self.ptr, hashn)

    def merkle(self):
        return bitprim_native.header_get_merkle(self.ptr)

    #def set_merkle(self, merkle):
        #bitprim_native.header_set_merkle(self.ptr, merkle)
    
    def timestamp(self): 
        return bitprim_native.header_get_timestamp(self.ptr)

    def set_timestamp(self, timestamp):
        bitprim_native.header_set_timestamp(self.ptr, timestamp)

    def bits(self):
        return bitprim_native.header_get_bits(self.ptr)
    
    def set_bits(self, bits):
        bitprim_native.header_set_bits(self.ptr, bits)
   
    def nonce(self):
        return bitprim_native.header_get_nonce(self.ptr)
    
    def set_nonce(self, nonce):
        bitprim_native.header_set_nonce(self.ptr, nonce)


# --------------------------------------------------------------------
class Block:
    def __init__(self, pointer, height):
        self.ptr = pointer
        self.height_ = height
    
    def height(self):
        return self.height_

    def header(self):
        return Header(bitprim_native.block_get_header(self.ptr), self.height_)

    def block_transaction_count(self):
        return bitprim_native.block_transaction_count(self.ptr)

    def block_hash(self):
        return bitprim_native.block_hash(self.ptr)

    def block_serialized_size(self, version):
        return bitprim_native.block_serialized_size(self.ptr, version)

    def block_fees(self):
        return bitprim_native.block_fees(self.ptr)

    def block_claim(self):
        return bitprim_native.block_claim(self.ptr)

    def block_reward(self, height):
        return bitprim_native.block_reward(self.ptr, height)

    def block_generate_merkle_root(self):
        return bitprim_native.block_generate_merkle_root(self.ptr)

# --------------------------------------------------------------------
class Merkle_Block:
    def __init__(self, pointer, height):
        self.ptr = pointer
        self.height_ = height

    def height(self):
        return self.height_

    def header(self):
        return Header(bitprim_native.merkle_block_get_header(self.ptr), self.height_)

    def is_valid(self):
        return bitprim_native.merkle_block_is_valid(self.ptr)

    def hash_count(self):
        return bitprim_native.merkle_block_hash_count(self.ptr)

    def serialized_size(self, version): 
        return bitprim_native.merkle_block_serialized_size(self.ptr, version)

    def total_transaction_count(self):
        return bitprim_native.merkle_block_total_transaction_count(self.ptr)

    def reset(self):
        return bitprim_native.merkle_block_reset(self.ptr)



# ------------------------------------------------------
class Point:
    def __init__(self, ptr):
        self.ptr = ptr

    def hash(self):
        # print('Point.hash')
        return bitprim_native.point_get_hash(self.ptr)[::-1].hex()

    def is_valid(self):
        return bitprim_native.point_is_valid(self.ptr)

    def index(self):
        return bitprim_native.point_get_index(self.ptr)

    def get_checksum(self):
        return bitprim_native.point_get_checksum(self.ptr)

# ------------------------------------------------------
class History:
    def __init__(self, ptr):
        self.ptr = ptr

    def point_kind(self):
        return bitprim_native.history_compact_get_point_kind(self.ptr)

    def point(self):
        return Point(bitprim_native.history_compact_get_point(self.ptr))

    def height(self):
        return bitprim_native.history_compact_get_height(self.ptr)

    def value_or_previous_checksum(self):
        return bitprim_native.history_compact_get_value_or_previous_checksum(self.ptr)

# ------------------------------------------------------
class HistoryList:
    def __init__(self, ptr):
        self.ptr = ptr
        self.constructed = True

    def destroy(self):
        if self.constructed:
            bitprim_native.history_compact_list_destruct(self.ptr)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def count(self):
        return bitprim_native.history_compact_list_count(self.ptr)

    def nth(self, n):
        return History(bitprim_native.history_compact_list_nth(self.ptr, n))

    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     # print('__exit__')
    #     self.destroy()

# ------------------------------------------------------
class Stealth:
    def __init__(self, ptr):
        self.ptr = ptr

    def ephemeral_public_key_hash(self):
        return bitprim_native.stealth_compact_get_ephemeral_public_key_hash(self.ptr)

    def get_transaction_hash(self):
        return bitprim_native.stealth_compact_get_transaction_hash(self.ptr)

    def public_key_hash(self):
        return bitprim_native.stealth_compact_get_public_key_hash(self.ptr)

# ------------------------------------------------------
class StealthList:
    def __init__(self, ptr):
        self.ptr = ptr
        self.constructed = True

    def destroy(self):
        if self.constructed:
            bitprim_native.stealth_compact_list_destruct(self.ptr)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def count(self):
        return bitprim_native.stealth_compact_list_count(self.ptr)

    def nth(self, n):
        return Stealth(bitprim_native.stealth_compact_list_nth(self.ptr, n))



# ------------------------------------------------------
class Chain:
    def __init__(self, chain):
        self.chain = chain

    def fetch_last_height(self, handler):
        bitprim_native.chain_fetch_last_height(self.chain, handler)

    def fetch_history(self, address, limit, from_height, handler):
        self.history_fetch_handler_ = handler
        bitprim_native.chain_fetch_history(self.chain, address, limit, from_height, self._history_fetch_handler_converter)

    # private members ... TODO: how to make private member functions in Python
    def _history_fetch_handler_converter(self, e, l):
        # print('history_fetch_handler_converter')
        if e == 0: 
            list = HistoryList(l)
        else:
            list = None

        self.history_fetch_handler_(e, list)

##### Stealth

    def stealth_fetch_handler_converter(self, e, l):
        if e == 0: 
            list = StealthList(l)
        else:
            list = None

        self.stealth_fetch_handler_(e, list)

    def fetch_stealth(self, binary_filter_str, from_height, handler):
        self.stealth_fetch_handler_ = handler
        binary_filter = bitprim_native.binary_construct_string(binary_filter_str)
        bitprim_native.fetch_stealth(self.executor, binary_filter, from_height, self.stealth_fetch_handler_converter)
        #bitprim_native.binary_destruct(binary_filter)

    def fetch_block_height(self, hashn, handler):
        bitprim_native.fetch_block_height(self.chain, hashn, handler)


    def _fetch_block_header_converter(self, e, header, height):
        print('_fetch_block_header_converter')

        if e == 0: 
            header = Header(header, height)
        else:
            header = None

        self.fetch_block_header_handler_(e, header)

    def fetch_block_header_by_height(self, height, handler):
        self.fetch_block_header_handler_ = handler
        bitprim_native.chain_fetch_block_header_by_height(self.chain, height, self._fetch_block_header_converter)

    def fetch_block_header_by_hash(self, hashn, handler):
        self.fetch_block_header_handler_ = handler
        bitprim_native.chain_fetch_block_header_by_hash(self.chain, hashn, self._fetch_block_header_converter)



    def fetch_block_by_height(self, height, handler):
        bitprim_native.chain_fetch_block_by_height(self.chain, height, handler)

    def fetch_block_by_hash(self, hashn, handler):
        bitprim_native.chain_fetch_block_by_hash(self.chain, hashn, handler)

    def fetch_merkle_block_by_height(self, height, handler):
        bitprim_native.chain_fetch_merkle_block_by_height(self.chain, height, handler)

    def fetch_merkle_block_by_hash(self, hashn, handler):
        bitprim_native.chain_fetch_merkle_block_by_hash(self.chain, hashn, handler)


class Binary:

    def binary_construct(self):
        return bitprim_native.binary_construct()

    def binary_construct_string(self, string_filter):
        return bitprim_native.binary_construct_string(string_filter)

    def binary_construct_blocks(self, size, blocks):
        return bitprim_native.binary_construct_blocks(size, len(blocks), blocks)

    def binary_blocks(self, binary):
        return bitprim_native.binary_blocks(binary)

    def binary_encoded(self, binary):
        return bitprim_native.binary_encoded(binary)


# ------------------------------------------------------
class Executor:
    def __init__(self, path, sout = None, serr = None):
        self.executor = bitprim_native.construct(path, sout, serr)
        self.constructed = True
        self.running = False

    def destroy(self):
        # print('destroy')

        if self.constructed:
            if self.running:
                self.stop()

            bitprim_native.destruct(self.executor)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def run(self):
        ret = bitprim_native.run(self.executor)

        if ret:
            self.running = True

        return ret

    def run_wait(self):
        ret = bitprim_native.run_wait(self.executor)

        if ret:
            self.running = True

        return ret

    def stop(self):
        # precondition: self.running
        ret = bitprim_native.stop(self.executor)

        if ret:
            self.running = False

        return ret

    def init_chain(self):
        return bitprim_native.initchain(self.executor)

    def get_chain(self):
        return Chain(bitprim_native.get_chain(self.executor))

## fetch_stealth(executor_t exec, binary_t filter, size_t from_height, stealth_fetch_handler_t handler){


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print('__exit__')
        self.destroy()





# ------------------------------------------------------

# class ExecutorResource:
#     def __enter__(self):
#         class Executor:
#             ...
#         self.package_obj = Package()
#         return self.package_obj
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.package_obj.cleanup()




# # ------------------------------------------------------
# # 
# # ------------------------------------------------------
# def signal_handler(signal, frame):
#     # signal.signal(signal.SIGINT, signal_handler)
#     # signal.signal(signal.SIGTERM, signal_handler)
#     print('You pressed Ctrl-C')
#     sys.exit(0)

# def history_fetch_handler(e, l): 
#     # print('history_fetch_handler: {0:d}'.format(e))
#     # print(l)
#     # if (e == 0):
#     #     print('history_fetch_handler: {0:d}'.format(e))

#     count = l.count()
#     print('history_fetch_handler count: {0:d}'.format(count))

#     for n in range(count):
#         h = l.nth(n)
#         # print(h)
#         print(h.point_kind())
#         print(h.height())
#         print(h.value_or_spend())

#         # print(h.point())
#         print(h.point().hash())
#         print(h.point().is_valid())
#         print(h.point().index())
#         print(h.point().get_checksum())



# def last_height_fetch_handler(e, h): 
#     if (e == 0):
#         print('Last Height is: {0:d}'.format(h))
#         # if h > 1000:
#         #     # executor.fetch_history('134HfD2fdeBTohfx8YANxEpsYXsv5UoWyz', 0, 0, history_fetch_handler)
#         #     executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
#         #     # executor.fetch_history('1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR', 0, 0, history_fetch_handler) # Es la de Juan




# # ------------------------------------------------------
# # Main Real
# # ------------------------------------------------------
# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGTERM, signal_handler)

# with Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as executor:
# # with Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as executor:
#     # res = executor.initchain()
#     res = executor.run()
#     # print(res)
    
#     time.sleep(3)

#     # executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler)

#     # time.sleep(5)

#     while True:
#         executor.fetch_last_height(last_height_fetch_handler)
#         # executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
#         executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler)
#         time.sleep(10)

#     # print('Press Ctrl-C')
#     # signal.pause()

# # bx fetch-history [-h] [--config VALUE] [--format VALUE] [PAYMENT_ADDRESS]
