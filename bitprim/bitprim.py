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
    #     self._ptr = ptr

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

class Header:    

    def __init__(self, pointr):
        self._ptr = pointr;
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.header_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def version(self):
        return bitprim_native.header_get_version(self._ptr)
    def set_version(self, version):
        bitprim_native.header_set_version(self._ptr, version)

    def previous_block_hash(self):        
        return bitprim_native.header_get_previous_block_hash(self._ptr)
    
    #def set_previous_block_hash(self,hashn):        
        #return bitprim_native.header_set_previous_block_hash(self._ptr, hashn)

    def merkle(self):
        return bitprim_native.header_get_merkle(self._ptr)

    #def set_merkle(self, merkle):
        #bitprim_native.header_set_merkle(self._ptr, merkle)
    
    def timestamp(self): 
        return bitprim_native.header_get_timestamp(self._ptr)
   
    def set_timestamp(self, timestamp):
        bitprim_native.header_set_timestamp(self._ptr, timestamp)

    def bits(self):
        return bitprim_native.header_get_bits(self._ptr)

    def set_bits(self, bits):
        bitprim_native.header_set_bits(self._ptr, bits)
   
    def nonce(self):
        return bitprim_native.header_get_nonce(self._ptr)

    def set_nonce(self, nonce):
        bitprim_native.header_set_nonce(self._ptr, nonce)


class Block:
    def __init__(self, pointer):
        self._ptr = pointer
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.block_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self.destroy()
    
    def header(self):
        return Header(bitprim_native.block_get_header(self._ptr))

    def transaction_count(self):
        return bitprim_native.block_transaction_count(self._ptr)

    def hash(self):
        return Hash(bitprim_native.block_hash(self._ptr))

    def serialized_size(self, version):
        return bitprim_native.block_serialized_size(self._ptr, version)

    def fees(self):
        return bitprim_native.block_fees(self._ptr)

    def claim(self):
        return bitprim_native.block_claim(self._ptr)

    def reward(self, height):
        return bitprim_native.block_reward(self._ptr, height)

    def generate_merkle_root(self):
        return bitprim_native.block_generate_merkle_root(self._ptr)

    def is_valid(self):
        return bitprim_native.block_is_valid(self._ptr)

    def transaction_nth(self, n):
        return Transaction(bitprim_native.block_transaction_nth(self._ptr, n))

    def signature_operations(self):
        return bitprim_native.block_signature_operations(self._ptr)

    def signature_operations_bip16_active(self, bip16_active):
        return bitprim_native.block_signature_operations_bip16_active(self._ptr, bip16_active)

    def total_inputs(self, with_coinbase):
        return bitprim_native.block_total_inputs(self._ptr, with_coinbase)

    def is_extra_conbases(self):
        return bitprim_native.block_is_extra_coinbases(self._ptr)

    def is_final(self, height):
        return bitprim_native.block_is_final(self._ptr, height)

    def is_distinct_transaction_set(self):
        return bitprim_native.block_is_distinct_transaction_set(self._ptr)

    def is_valid_coinbase_claim(self, height):
        return bitprim_native.block_is_valid_coinbase_claim(self._ptr, height)

    def is_valid_coinbase_script(self, height):
        return bitprim_native.block_is_valid_coinbase_script(self._ptr, height)

    def is_internal_double_spend(self):
        return bitprim_native.block_is_internal_double_spend(self._ptr)

    def is_valid_merkle_root(self):
        return bitprim_native.block_is_valid_merkle_root(self._ptr)





# ------------------------------------------------------
class MerkleBlock:
    def __init__(self, pointer):
        self._ptr = pointer
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.merkle_block_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self.destroy()

    def header(self):
        return Header(bitprim_native.merkle_block_get_header(self._ptr))

    def is_valid(self):
        return bitprim_native.merkle_block_is_valid(self._ptr)

    def hash_count(self):
        return bitprim_native.merkle_block_hash_count(self._ptr)

    def serialized_size(self, version): 
        return bitprim_native.merkle_block_serialized_size(self._ptr, version)

    def total_transaction_count(self):
        return bitprim_native.merkle_block_total_transaction_count(self._ptr)

    def reset(self):
        return bitprim_native.merkle_block_reset(self._ptr)


# ------------------------------------------------------
class Point:
    def __init__(self, ptr):
        self._ptr = ptr

    def hash(self):
        # print('Point.hash')
        return bitprim_native.point_get_hash(self._ptr)[::-1].hex()

    def is_valid(self):
        return bitprim_native.point_is_valid(self._ptr)

    def index(self):
        return bitprim_native.point_get_index(self._ptr)

    def get_checksum(self):
        return bitprim_native.point_get_checksum(self._ptr)

# ------------------------------------------------------
class History:
    def __init__(self, ptr):
        self._ptr = ptr

    def point_kind(self):
        return bitprim_native.history_compact_get_point_kind(self._ptr)

    def point(self):
        return Point(bitprim_native.history_compact_get_point(self._ptr))

    def height(self):
        return bitprim_native.history_compact_get_height(self._ptr)

    def value_or_previous_checksum(self):
        return bitprim_native.history_compact_get_value_or_previous_checksum(self._ptr)

# ------------------------------------------------------
class HistoryList:
    def __init__(self, ptr):
        self._ptr = ptr
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.history_compact_list_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def count(self):
        return bitprim_native.history_compact_list_count(self._ptr)

    def nth(self, n):
        return History(bitprim_native.history_compact_list_nth(self._ptr, n))

    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     # print('__exit__')
    #     self.destroy()

# ------------------------------------------------------
class Stealth:
    def __init__(self, ptr):
        self._ptr = ptr

    def ephemeral_public_key_hash(self):
        return bitprim_native.stealth_compact_get_ephemeral_public_key_hash(self._ptr)

    def get_transaction_hash(self):
        return bitprim_native.stealth_compact_get_transaction_hash(self._ptr)

    def public_key_hash(self):
        return bitprim_native.stealth_compact_get_public_key_hash(self._ptr)

# ------------------------------------------------------
class StealthList:
    def __init__(self, ptr):
        self._ptr = ptr
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.stealth_compact_list_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def count(self):
        return bitprim_native.stealth_compact_list_count(self._ptr)

    def nth(self, n):
        return Stealth(bitprim_native.stealth_compact_list_nth(self._ptr, n))

# ------------------------------------------------------
class Transaction:
    def __init__(self, ptr):
        self._ptr = ptr
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.transaction_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def version(self):
        return bitprim_native.transaction_version(self._ptr)

    def set_version(self, version):
        return bitprim_native.transaction_set_version(self._ptr, version)

    def hash(self):
        return bitprim_native.transaction_hash(self._ptr)

    def hash_sighash_type(self, sighash_type):
        return bitprim_native.transaction_hash_sighash_type(self._ptr, sighash_type)

    def locktime(self):
        return bitprim_native.transaction_locktime(self._ptr)

    def serialized_size(self, wire):
        return bitprim_native.transaction_serialized_size(self._ptr, wire)

    def fees(self):
        return bitprim_native.transaction_fees(self._ptr)

    def signature_operations(self):
        return bitprim_native.transaction_signature_operations(self._ptr)

    def signature_operations_bip16_active(self, bip16_active):
        return bitprim_native.transaction_signature_operations_bip16_active(self._ptr, bip16_active)

    def total_input_value(self):
        return bitprim_native.transaction_total_input_value(self._ptr)

    def total_output_value(self):
        return bitprim_native.transaction_total_output_value(self._ptr)

    def is_coinbase(self):
        return bitprim_native.transaction_is_coinbase(self._ptr)

    def is_null_non_coinbase(self):
        return bitprim_native.transaction_is_null_non_coinbase(self._ptr)

    def is_oversized_coinbase(self):
        return bitprim_native.transaction_is_oversized_coinbase(self._ptr)

    def is_immature(self, target_height):
        return bitprim_native.transaction_is_immature(self._ptr, target_height)

    def is_overspent(self):
        return bitprim_native.transaction_is_overspent(self._ptr)

    def is_double_spend(self, include_unconfirmed):
        return bitprim_native.transaction_is_double_spend(self._ptr, include_unconfirmed)
    
    def is_missing_previous_outputs(self):
        return bitprim_native.transaction_is_missing_previous_outputs(self._ptr)

    def is_final(self, block_height, block_time):
        return bitprim_native.transaction_is_final(self._ptr, block_height, block_time)

    def is_locktime_conflict(self):
        return bitprim_native.transaction_is_locktime_conflict(self._ptr)

    #def outputs(self):
    #    return OutputList(bitprim_native.transaction_outputs(self._ptr))

    #def inputs(self):
    #    return InputList(bitprim_native.transaction_inputs(self._ptr))

# ------------------------------------------------------
class Script:
    def __init__(self, ptr):
        self._ptr
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.script_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self.destroy()

    def is_valid(self):
        return bitprim_native.script_is_valid(self._ptr)
    
    def is_valid_operations(self):
        return bitprim_native.script_is_valid_operations(self._ptr)

    def satoshi_content_size(self):
        return bitprim_native.script_satoshi_content_size(self._ptr)

    def serialized_size(self, prefix):
        return bitprim_native.script_serialized_size(self._ptr, prefix)    

    def to_string(self, active_forks):
        return bitprim_native.script_to_string(self._ptr, active_forks)    

    def sigops(self, embedded):
        return bitprim_native.script_sigops(self._ptr, embedded)  

    def embedded_sigops(self, prevout_script):
        return bitprim_native.script_embedded_sigops(self._ptr, prevout_script)  


# ------------------------------------------------------

class Output:
    def __init__(self, ptr):
        self._ptr
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.output_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self.destroy()

    def is_valid(self):
        return bitprim_native.output_is_valid(self._ptr)

    def serialized_size(self, wire):
        return bitprim_native.output_serialized_size(self._ptr, wire)

    def value(self):
        return bitprim_native.output_value(self._ptr)

    def signature_operations(self):
        return bitprim_native.output_signature_operations(self._ptr)

    #def script(self):
        #return Script(bitprim_native.output_script(self._ptr))

    #def get_hash(self):
    #    return bitprim_native.output_get_hash(self._ptr)

    #def get_index(self):
    #    return bitprim_native.output_get_index(self._ptr)

class Input:
    def __init__(self, ptr):
        self._ptr
        self._constructed = True

    def destroy(self):
        if self._constructed:
            bitprim_native.output_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self.destroy()

    def is_valid(self):
        return bitprim_native.input_is_valid(self._ptr)

    def is_final(self):
        return bitprim_native.input_is_final(self._ptr)

    def serialized_size(self, wire):
        return bitprim_native.input_serialized_size(self._ptr, wire)

    def sequence(self):
        return bitprim_native.input_sequence(self._ptr)

    def signature_operations(self, bip16_active):
        return bitprim_native.input_signature_operations(self._ptr, bip16_active)

    #def script(self):
        #return Script(bitprim_native.output_script(self._ptr))

    #def get_hash(self):
    #    return bitprim_native.input_get_hash(self._ptr)

    #def get_index(self):
    #    return bitprim_native.input_get_index(self._ptr)

class OutputList:
    def __init__(self, ptr):
        self._ptr = ptr

    def push_back(self, output):
        bitprim_native.output_list_push_back(self._ptr, output)

    def list_count(self):
        return bitprim_native.output_list_count(self._ptr)

    def list_nth(self, n):
        return Output(bitprim_native.output_list_nth(self._ptr, n))
    

class InputList:
    def __init__(ptr):
        self._ptr = ptr

    def push_back(self, inputn):
        bitprim_native.input_list_push_back(self._ptr, inputn)

    def list_count(self):
        return bitprim_native.input_list_count(self._ptr)

    def list_nth(self, n):
        return Input(bitprim_native.input_list_nth(self._ptr, n))

        

# ------------------------------------------------------
class Chain:
    def __init__(self, chain):
        self._chain = chain

    def fetch_last_height(self, handler):
        bitprim_native.chain_fetch_last_height(self._chain, handler)

    def fetch_history(self, address, limit, from_height, handler):
        self._history_fetch_handler = handler
        bitprim_native.chain_fetch_history(self._chain, address, limit, from_height, self._history_fetch_handler_converter)

    # private members ... TODO: how to make private member functions in Python
    def _history_fetch_handler_converter(self, e, l):
        # print('history_fetch_handler_converter')
        if e == 0: 
            _list = HistoryList(l)
        else:
            _list = None

        self._history_fetch_handler(e, _list)

##### Stealth

    def _stealth_fetch_handler_converter(self, e, l):
        if e == 0: 
            _list = StealthList(l)
        else:
            _list = None

        self._stealth_fetch_handler(e, _list)

    def fetch_stealth(self, binary_filter_str, from_height, handler):
        self._stealth_fetch_handler = handler
        binary_filter = bitprim_native.binary_construct_string(binary_filter_str)
        bitprim_native.fetch_stealth(self._executor, binary_filter, from_height, self._stealth_fetch_handler_converter)
        #bitprim_native.binary_destruct(binary_filter)

    def fetch_block_height(self, hashn, handler):
        bitprim_native.fetch_block_height(self._chain, hashn, handler)


    def _fetch_block_header_converter(self, e, header, height):
        if e == 0: 
            _header = Header(header)
        else:
            _header = None

        self._fetch_block_header_handler(e, _header)

    def fetch_block_header_by_height(self, height, handler):
        self._fetch_block_header_handler = handler
        bitprim_native.chain_fetch_block_header_by_height(self._chain, height, self._fetch_block_header_converter)

    def fetch_block_header_by_hash(self, hashn, handler):
        self._fetch_block_header_handler = handler
        bitprim_native.chain_fetch_block_header_by_hash(self._chain, hashn, self._fetch_block_header_converter)

    
    def _fetch_block_converter(self, e, block, height):
        if e == 0: 
            _block = Block(block)
        else:
            _block = None

        self._fetch_block_handler(e, _block, height)


    def fetch_block_by_height(self, height, handler):
        self._fetch_block_handler = handler
        bitprim_native.chain_fetch_block_by_height(self._chain, height, handler)

    def fetch_block_by_hash(self, hashn, handler):
        self._fetch_block_handler = handler
        bitprim_native.chain_fetch_block_by_hash(self._chain, hashn, self._fetch_block_converter)

    def _fetch_merkle_block_converter(self, e, merkle_block, height):
        if e == 0: 
            _merkle_block = MerkleBlock(merkle_block)
        else:
            _merkle_block = None

        self._fetch_merkle_block_handler(e, _merkle_block)

    def fetch_merkle_block_by_height(self, height, handler):
        self._fetch_merkle_block_handler = handler
        bitprim_native.chain_fetch_merkle_block_by_height(self._chain, height, handler)

    def fetch_merkle_block_by_hash(self, hashn, handler):
        self._fetch_merkle_block_handler = handler
        bitprim_native.chain_fetch_merkle_block_by_hash(self._chain, hashn, self._fetch_merkle_block_converter)

    def _fetch_transaction_converter(self, e, transaction, height, index):
        if e == 0: 
            _transaction = Transaction(transaction)
        else:
            _transaction = None

        self._fetch_transaction_handler(e, _transaction, height, index)

    def fetch_transaction(self, hashn, require_confirmed,handler):
        self._fetch_transaction_handler = handler
        bitprim_native.chain_fetch_transaction(self._chain, hashn, require_confirmed, self._fetch_transaction_converter)



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
        self._executor = bitprim_native.construct(path, sout, serr)
        self._constructed = True
        self._running = False

    def destroy(self):
        # print('destroy')

        if self._constructed:
            if self._running:
                self.stop()

            bitprim_native.destruct(self._executor)
            self._constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def run(self):
        ret = bitprim_native.run(self._executor)

        if ret:
            self._running = True

        return ret

    def run_wait(self):
        ret = bitprim_native.run_wait(self._executor)

        if ret:
            self._running = True

        return ret

    def stop(self):
        # precondition: self._running
        ret = bitprim_native.stop(self._executor)

        if ret:
            self._running = False

        return ret

    def init_chain(self):
        return bitprim_native.initchain(self._executor)

    def get_chain(self):
        return Chain(bitprim_native.get_chain(self._executor))

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
