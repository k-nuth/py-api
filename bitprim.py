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

import bitprim_native as bn

# ------------------------------------------------------

# __title__ = "bitprim"
# __summary__ = "Bitcoin development platform"
# __uri__ = "https://github.com/bitprim/bitprim-py"
# __version__ = "1.0.7"
# __author__ = "Bitprim Inc"
# __email__ = "dev@bitprim.org"
# __license__ = "MIT"
# __copyright__ = "Copyright 2017 Bitprim developers"


# ------------------------------------------------------
# Tools
# ------------------------------------------------------
def encode_hash(hash):
    """str: Converts a bytearray into a readable format.
    example return: "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
    
    Args:
        hash (bytearray): bytes of the hash.

    """
    if (sys.version_info > (3, 0)):
        return ''.join('{:02x}'.format(x) for x in h[::-1])
    else:
        return h[::-1].encode('hex')

def decode_hash(hash_str):
    """bytearray: Converts a string into a workable format. 

    Args:
        hash_str (str): string with hash. example "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"

    """
    h = bytearray.fromhex(hash_str) 
    h = h[::-1] 
    return bytes(h)

# ------------------------------------------------------
class Wallet:
    # def __init__(self, ptr):
    #     self._ptr = ptr

    @classmethod
    def mnemonics_to_seed(cls, mnemonics):
        wl = bn.word_list_construct()

        for m in mnemonics:
            bn.word_list_add_word(wl, m)

        # # seed = bn.wallet_mnemonics_to_seed(wl)[::-1].hex();
        # seed = bn.wallet_mnemonics_to_seed(wl).hex();

        seed_ptr = bn.wallet_mnemonics_to_seed(wl)
        print(seed_ptr)
        seed = bn.long_hash_t_to_str(seed_ptr).hex()
        print(seed)
        bn.long_hash_t_free(seed_ptr)

        bn.word_list_destruct(wl)
        # print('Wallet.mnemonics_to_seed')

        return seed

# ------------------------------------------------------
class Header:
    """Represent the Header of a Bitcoin Block.

    """

    def __init__(self, pointer, height, auto_destroy = False):
        """Construction of the Header class object.

        Args:
            pointer (Object): pointer to c implementation.
            height (unsigned int): Height of the block in the chain.
            auto_destroy (bool): the object will be deleted when out of scope..

        """        
        self._ptr = pointer
        self._height = height
        self._auto_destroy = auto_destroy

    def _destroy(self):
        bn.header_destruct(self._ptr)

    def __del__(self):
        if self._auto_destroy:
            self._destroy()

    @property
    def height(self):
        """unsigned int: Height of the block in the chain."""
        return self._height

    @property
    def version(self):
        """unsigned int: protocol version of the header."""
        return bn.header_get_version(self._ptr)

    @version.setter
    def set_version(self, version):
        bn.header_set_version(self._ptr, version)

    @property
    def previous_block_hash(self):
        """bytearray: 32 bytes hash of the previous block in the chain."""        
        return bn.header_get_previous_block_hash(self._ptr)
    
    #def set_previous_block_hash(self,hash):        
        #return bn.header_set_previous_block_hash(self._ptr, hash)

    @property
    def merkle(self):
        """bytearray: 32 bytes merkle root."""
        return bn.header_get_merkle(self._ptr)

    #def set_merkle(self, merkle):
        #bn.header_set_merkle(self._ptr, merkle)

    @property
    def hash(self):
        """bytearray: 32 bytes block hash."""
        return bn.header_get_hash(self._ptr)

    @property
    def timestamp(self):
        """unsigned int: block timestamp."""
        return bn.header_get_timestamp(self._ptr)

    @timestamp.setter
    def set_timestamp(self, timestamp):
        bn.header_set_timestamp(self._ptr, timestamp)

    @property
    def bits(self):
        """unsigned int: value of bits. Difficulty threshold."""
        return bn.header_get_bits(self._ptr)
    
    @bits.setter
    def set_bits(self, bits):
        bn.header_set_bits(self._ptr, bits)
   
    @property
    def nonce(self):
        """unsigned int: the nonce that allowed this block to added to the blockchain."""
        return bn.header_get_nonce(self._ptr)
    
    @nonce.setter
    def set_nonce(self, nonce):
        bn.header_set_nonce(self._ptr, nonce)


# --------------------------------------------------------------------
class Block:
    """Represent a full Bitcoin block."""
    def __init__(self, pointer, height):
        self._ptr = pointer
        self._height = height

    def _destroy(self):
        bn.block_destruct(self._ptr)

    def __del__(self):
        self._destroy()
    
    @property
    def height(self):
        """unsigned int: Height of the block in the chain."""
        return self._height

    @property
    def header(self):
        """Header: block header object."""
        return Header(bn.block_get_header(self._ptr), self._height, False)

    @property
    def transaction_count(self):
        """unsigned int: amount of transaction in the block."""
        return bn.block_transaction_count(self._ptr)

    @property
    def hash(self):
        """bytearray: 32 bytes of the block hash."""
        return bn.block_hash(self._ptr)

    @property
    def serialized_size(self):
        """unsigned int: size of the block in bytes."""
        return bn.block_serialized_size(self._ptr, 0)

    @property
    def fees(self):
        """unsigned int: amount of fees included in coinbase."""
        return bn.block_fees(self._ptr)

    @property
    def claim(self):
        """unsigned int: value of the outputs in the coinbase. """
        return bn.block_claim(self._ptr)

    def reward(self, height):
        """unsigned int: value of the fees plus the reward for a block at the given height.
        
        Args:
            height (unsigned int): height of the block in the chain.
        
        """
        return bn.block_reward(self._ptr, height)
    
    def generate_merkle_root(self):
        """bytearray: 32 bytes of the merkle root, for the generated merkle tree."""
        return bn.block_generate_merkle_root(self._ptr)

    def is_valid(self):
        """int: block has transactions and a valid Header. 1 if its valid."""
        return bn.block_is_valid(self._ptr)

    def transaction_nth(self, n):
        """Transaction: given a position in the block, returns the corresponding transaction.
        
        Args: 
            n (unsigned int): index of the transaction in the block.
            
        """
        return Transaction(bn.block_transaction_nth(self._ptr, n))

    def signature_operations(self):
        """unsigned int: amount of signature operations in the block.
        Returns max_int in case of overflow.
        """
        return bn.block_signature_operations(self._ptr)

    def signature_operations_bip16_active(self, bip16_active):
        """unsigned int: amount of signature operations in the block.
        Returns max_int in case of overflow.
        
        Args:
            bip16_active(int): if bip16 is activated at this point. Should be '1' if its active.

        """
        return bn.block_signature_operations_bip16_active(self._ptr, bip16_active)

    def total_inputs(self, with_coinbase = 1):
        """unsigned int: amount of inputs in every transaction in the block.
        
        Args:
            with_coinbase (int): should be '1' if block contains a coinbase transaction. '0' otherwise.
        """
        return bn.block_total_inputs(self._ptr, with_coinbase)

    def is_extra_coinbases(self):
        """int: returns '1' if there is another coinbase other than the first transaction."""
        return bn.block_is_extra_coinbases(self._ptr)

    def is_final(self, height):
        """int: returns '1' if every transaction in the block is final.
        
        Args:
            height (unsigned int): height of the block in the chain.
        """
        return bn.block_is_final(self._ptr, height)

    def is_distinct_transaction_set(self):
        """int: returns '1' if there are not two transactions with the same hash."""
        return bn.block_is_distinct_transaction_set(self._ptr)

    def is_valid_coinbase_claim(self, height):
        """int: returns '1' if coinbase claim is not higher than the deserved reward.
        
        Args:
            height (unsigned int): height of the block in the chain.

        """
        return bn.block_is_valid_coinbase_claim(self._ptr, height)

    def is_valid_coinbase_script(self, height):
        """int: returns '1' if coinbase script is valid."""
        return bn.block_is_valid_coinbase_script(self._ptr, height)

    def _is_internal_double_spend(self):
        return bn.block_is_internal_double_spend(self._ptr)

    def is_valid_merkle_root(self):
        """int: returns '1' if the generated merkle root is equal to the Header merkle root."""
        return bn.block_is_valid_merkle_root(self._ptr)

class BlockList:
    def __init__(self, ptr):
        self._ptr = ptr

    def _destroy(self):
        bn.block_list_destruct(self._ptr)

    def __del__(self):
        self._destroy()
    
    @classmethod
    def construct_default(self):
        return BlockList(bn.block_list_construct_default())


    def push_back(self, block):
        bn.block_list_push_back(self._ptr, block._ptr)

    def list_count(self):
        return bn.block_list_count(self._ptr)

    def _nth(self, n):
        return Block(bn.block_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self._nth(key)


class TransactionList:
    def __init__(self, ptr):
        self._ptr = ptr

    def _destroy(self):
        bn.transaction_list_destruct(self._ptr)

    def __del__(self):
        self._destroy()
    
    @classmethod
    def construct_default(self):
        return TransactionList(bn.transaction_list_construct_default())

    def push_back(self, transaction):
        bn.transaction_list_push_back(self._ptr, transaction._ptr)

    def list_count(self):
        return bn.transaction_list_count(self._ptr)

    def _nth(self, n):
        return Transaction(bn.transaction_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self._nth(key)

# ------------------------------------------------------

class _CompactBlock:
    def __init__(self, pointer):
        self._ptr = pointer
        self._constructed = True

    def _destroy(self):
        if self._constructed:
            bn.compact_block_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self._destroy()

    @property
    def header(self):
        return Header(bn.compact_block_get_header(self._ptr), False)

    @property
    def is_valid(self):
        return bn.compact_block_is_valid(self._ptr)

    @property
    def serialized_size(self, version): 
        return bn.compact_block_serialized_size(self._ptr, version)

    @property
    def transaction_count(self):
        return bn.compact_block_transaction_count(self._ptr)

    def transaction_nth(self, n):
        return bn.compact_block_transaction_nth(self._ptr, n)

    @property
    def nonce(self):
        return bn.compact_block_nonce(self._ptr)

    def reset(self):
        return bn.merkle_block_reset(self._ptr)


# ------------------------------------------------------
class MerkleBlock:
    def __init__(self, pointer, height):
        self._ptr = pointer
        self._height = height

    @property
    def height(self):
        """unsigned int: Height of the block in the chain."""
        return self._height

    def _destroy(self):
        bn.merkle_block_destruct(self._ptr)


    def __del__(self):
        self._destroy()

    @property
    def header(self):
        """Header: header of the block."""
        return Header(bn.merkle_block_get_header(self._ptr), self._height, False)

    @property
    def is_valid(self):
        """int: returns true if it cointains txs hashes, and header is valid."""
        return bn.merkle_block_is_valid(self._ptr)

    @property
    def hash_count(self):
        """unsigned int: size of the transaction hashes list."""
        return bn.merkle_block_hash_count(self._ptr)

    def serialized_size(self, version):
        """unsigned int: size of the block in bytes.
        
        Args:
            version (unsigned int): block protocol version.

        """
        return bn.merkle_block_serialized_size(self._ptr, version)

    @property
    def total_transaction_count(self):
        """unsigned int: transactions included in the block."""
        return bn.merkle_block_total_transaction_count(self._ptr)

    def reset(self):
        """void: delete all the data inside the block."""
        return bn.merkle_block_reset(self._ptr)

class StealthCompact:
    def __init__(self, ptr):
        self._ptr = ptr

    def ephemeral_public_key_hash(self):
        """bytearray: 32 bytes. Excludes the sign byte (0x02)"""
        return bn.stealth_compact_ephemeral_public_key_hash(self._ptr)

    @property
    def transaction_hash(self):
        """bytearray: 32 bytes."""
        return bn.stealth_compact_get_transaction_hash(self._ptr)

    @property
    def public_key_hash(self):
        """bytearray: 20 bytes."""
        bn.stealth_compact_get_public_key_hash(self._ptr)

class StealthCompactList:
    def __init__(self, ptr):
        self._ptr = ptr

    def _destroy(self):
        bn.stealth_compact_list_destruct(self._ptr)

    def __del__(self):
        self._destroy()
    
    #@classmethod
    #def construct_default(self):
    #    return TransactionList(bn.transaction_list_construct_default())

    #def push_back(self, transaction):
    #    bn.transaction_list_push_back(self._ptr, transaction._ptr)

    def list_count(self):
        return bn.stealth_compact_list_count(self._ptr)

    def _nth(self, n):
        return Stealth(bn.stealth_compact_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self._nth(key)


# ------------------------------------------------------
class Point:
    """Represents one of the txs input.
    It's a pair of transaction hash and index.
    
    """
    def __init__(self, ptr):
        self._ptr = ptr

    @property
    def hash(self):
        """
        Hash of the transaction.
        
        Returns:
            bytearray: 32 bytes.
        
        """
        return bn.point_get_hash(self._ptr) #[::-1].hex()

    @property
    def is_valid(self):
        """
        returns true if its not null.

        Returns:
            bool
            
            """
        return bn.point_is_valid(self._ptr)

    @property
    def index(self):
        """
        Position of the Input in the transaction.

        Returns:
            unsigned int.
        
        """
        return bn.point_get_index(self._ptr)

    @property
    def checksum(self):
        """
        
        This is used with output_point identification within a set of history rows
        of the same address. Collision will result in miscorrelation of points by
        client callers. This is NOT a bitcoin checksum.

        Returns:
            unsigned int.
        """
        return bn.point_get_checksum(self._ptr)


class OutputPoint:
    """Transaction hash and index representing one of the transaction outputs."""
    def __init__(self, ptr ):
        self._ptr = ptr

    @property
    def hash(self):
        """bytearray: 32 bytes of the transaction hash."""
        return bn.output_point_get_hash(self._ptr)

    def _destroy(self):
        bn.output_point_destruct(self._ptr)

    def __del__(self):
        self._destroy()

    @property
    def index(self):
        """unsigned int: position of the output in the transaction."""
        return bn.output_point_get_index(self._ptr)

    @classmethod
    def construct(self):
        """OutputPoint: creates an empty output point."""
        return OutputPoint(bn.output_point_construct())

    @classmethod
    def construct_from_hash_index(self, hashn, index):
        """Outputpoint: creates an OutputPoint from a transaction hash and index pair.
        
        Args:

            hashn (bytearray): 32 bytes of the transaction hash.
            index (unsigned int): position of the output in the transaction.
        """        
        return OutputPoint(bn.output_point_construct_from_hash_index(hashn, index))

    #def is_valid(self):
    #    return bn.point_is_valid(self._ptr)

    #def get_checksum(self):
    #    return bn.point_get_checksum(self._ptr)

# ------------------------------------------------------
class History:
    """Output points, values, and spends for a payment address"""
    def __init__(self, ptr):
        self._ptr = ptr

    @property
    def point_kind(self):
        """unsigned int: Used for differentiation.
            '0' output
            '1' spend
        """
        return bn.history_compact_get_point_kind(self._ptr)

    @property
    def point(self):
        """Point: point that identifies History."""
        return Point(bn.history_compact_get_point(self._ptr))

    @property
    def height(self):
        """unsigned int: Height of the block containing the Point."""
        return bn.history_compact_get_height(self._ptr)

    @property
    def value_or_previous_checksum(self):
        """ unsigned int: varies depending of point_kind.

        value: if output, then satoshi value of output.
        
        previous_checksum: if spend, then checksum hash of previous output_point.
        """
        return bn.history_compact_get_value_or_previous_checksum(self._ptr)

# ------------------------------------------------------
class HistoryList:
    def __init__(self, ptr):
        self._ptr = ptr
        self.constructed = True

    def _destroy(self):
        if self.constructed:
            bn.history_compact_list_destruct(self._ptr)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self._destroy()

    @property
    def count(self):
        return bn.history_compact_list_count(self._ptr)

    def nth(self, n):
        return History(bn.history_compact_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self.nth(key)

    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     # print('__exit__')
    #     self._destroy()

# ------------------------------------------------------
class Stealth:
    def __init__(self, ptr):
        self._ptr = ptr

    @property
    def ephemeral_public_key_hash(self):
        """bytearray: 33 bytes. Includes  the sign byte (0x02)"""
        return bn.stealth_compact_get_ephemeral_public_key_hash(self._ptr)

    @property
    def transaction_hash(self):
        """bytearray: 32 bytes."""
        return bn.stealth_compact_get_transaction_hash(self._ptr)
    
    @property
    def public_key_hash(self):
        """bytearray: 20 bytes."""
        return bn.stealth_compact_get_public_key_hash(self._ptr)

# ------------------------------------------------------
class StealthList:
    def __init__(self, ptr):
        self._ptr = ptr
        self.constructed = True

    def _destroy(self):
        if self.constructed:
            bn.stealth_compact_list_destruct(self._ptr)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self._destroy()

    @property
    def count(self):
        return bn.stealth_compact_list_count(self._ptr)

    def nth(self, n):
        return Stealth(bn.stealth_compact_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self.nth(key)

# ------------------------------------------------------
class Transaction:
    """Represents a Bitcoin Transaction."""
    def __init__(self, ptr):
        self._ptr = ptr
        self._constructed = True

    def _destroy(self):
        if self._constructed:
            bn.transaction_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        # print('__del__')
        self._destroy()

    @property
    def version(self):
        """unsigned int: Transaction protocol version."""
        return bn.transaction_version(self._ptr)
    
    @version.setter
    def set_version(self, version):
        return bn.transaction_set_version(self._ptr, version)

    @property
    def hash(self):
        """bytearray: 32 bytes transaction hash."""
        return bn.transaction_hash(self._ptr)

    def hash_sighash_type(self, sighash_type):
        """bytearray: 32 bytes transaction hash.
        
        Args: 
            sighash_type (unsigned int): signature hash type.
        """
        return bn.transaction_hash_sighash_type(self._ptr, sighash_type)

    @property
    def locktime(self):
        """unsigned int: transaction locktime."""
        return bn.transaction_locktime(self._ptr)

    def serialized_size(self, wire):
        """unsigned int: size of the transaction in bytes.
        
        Args:
            wire (bool): if 'TRUE' size will include size of 'uint32' for storing spender height of output.
        """
        return bn.transaction_serialized_size(self._ptr, wire)

    @property
    def fees(self):
        """unsigned int: fees to pay. Difference between input and output value."""
        return bn.transaction_fees(self._ptr)

    def signature_operations(self):
        """unsigned int: amount of signature operations in the transaction. 
        Returns max int in case of overflow."""
        return bn.transaction_signature_operations(self._ptr)

    def signature_operations_bip16_active(self, bip16_active):
        """unsigned int: amount of signature operations in the transaction.
        Returns max int in case of overflow.

        Args:

            bip16_active (int): '1' if bip 16 is active. '0' if not. 
        """
        return bn.transaction_signature_operations_bip16_active(self._ptr, bip16_active)

    def total_input_value(self):
        """unsigned int: sum of every input value in the transaction.
        Returns max int in case of overflow.
        """
        return bn.transaction_total_input_value(self._ptr)

    def total_output_value(self):
        """unsigned int: sum of every output value in the transaction.
        return max int in case of overflow."""
        return bn.transaction_total_output_value(self._ptr)

    def is_coinbase(self):
        """int: return '1' if transaction is coinbase."""
        return bn.transaction_is_coinbase(self._ptr)

    def is_null_non_coinbase(self):
        """int: return '1' if is not coinbase, but has null previous output."""
        return bn.transaction_is_null_non_coinbase(self._ptr)

    def is_oversized_coinbase(self):
        """int: returns '1' if coinbase has invalid script size on first input."""
        return bn.transaction_is_oversized_coinbase(self._ptr)

    def is_immature(self, target_height):
        """int: returns '1' if at least one of the inputs is not mature."""
        return bn.transaction_is_immature(self._ptr, target_height)

    def is_overspent(self):
        """int: returns '1' if it is not a coinbase, and outputs value is higher than its inputs."""
        return bn.transaction_is_overspent(self._ptr)

    def is_double_spend(self, include_unconfirmed):
        """int: returns '1' if at least one of the previous outputs was already spent."""
        return bn.transaction_is_double_spend(self._ptr, include_unconfirmed)
    
    def is_missing_previous_outputs(self):
        """int: returns '1' if at least one of the previous outputs is invalid."""
        return bn.transaction_is_missing_previous_outputs(self._ptr)

    def is_final(self, block_height, block_time):
        """int: returns '1' if transaction is final. """
        return bn.transaction_is_final(self._ptr, block_height, block_time)

    def is_locktime_conflict(self):
        """int: returns '1' if its locked, but every input is final. """
        return bn.transaction_is_locktime_conflict(self._ptr)

    def outputs(self):
        """OutputList: returns a list with every transaction output. """
        return OutputList(bn.transaction_outputs(self._ptr))

    def inputs(self):
        """InputList: returns a list with every transaction input. """
        return InputList(bn.transaction_inputs(self._ptr))

# ------------------------------------------------------
class Script:
    """Represents transaction scripts."""
    def __init__(self, ptr, auto_destroy = False):
        self._ptr = ptr
        self._constructed = True
        self._auto_destroy = auto_destroy

    def _destroy(self):
        if self._constructed:
            bn.script_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        if self._auto_destroy:
            self._destroy()

    @property
    def is_valid(self):
        """int: All script bytes are valid under some circumstance (e.g. coinbase).
        Returns '0' if a prefix and byte count does not match.
        """
        return bn.script_is_valid(self._ptr)
    
    @property
    def is_valid_operations(self):
        """int: Script validity is independent of individual operation validity.
        There is a trailing invalid/default op if a push op had a size mismatch."""
        return bn.script_is_valid_operations(self._ptr)

    @property
    def satoshi_content_size(self):
        """unsigned int: size in bytes."""
        return bn.script_satoshi_content_size(self._ptr)

    def serialized_size(self, prefix):
        """unsigned int: size in bytes. If prefix '1' size includes a var int size. 
        
        Args:
            prefix (bool): include prefix size in the final result.
        """
        return bn.script_serialized_size(self._ptr, prefix)
    
    def to_string(self, active_forks):
        """str: translate operations in the script to string. 
        
        Args:
            active_forks (unsigned int): which rule is active.

        """
        return bn.script_to_string(self._ptr, active_forks)

    def sigops(self, embedded):
        """unsigned int: amount of signature operations in the script.
        
        Args:
            embedded (bool): is embedded script."""
        return bn.script_sigops(self._ptr, embedded)  

    def embedded_sigops(self, prevout_script):
        """unsigned int: Count the sigops in the embedded script using BIP16 rules.
        """
        return bn.script_embedded_sigops(self._ptr, prevout_script)  


# ------------------------------------------------------
class PaymentAddress:
    """Represents a Bitcoin wallet address."""
    def __init__(self, ptr = None):
        self._ptr = ptr
        self._constructed = False
        if ptr != None:
            self._constructed = True

    def _destroy(self):
        if self._constructed:
            bn.payment_address_destruct(self._ptr)
            self._constructed = False

    #def __del__(self):
        #self._destroy()

    @property
    def encoded(self):
        """str: readable format of the address."""
        if self._constructed:
            return bn.payment_address_encoded(self._ptr)

    @property
    def version(self):
        """unsigned int: address version."""
        if self._constructed:
            return bn.payment_address_version(self._ptr)

    @classmethod
    def construct_from_string(self, address):
        """Creates the Payment Address based on the received string.
        
        Args:
            address(str): a base58 address. example '1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR'
        
        """
        self._ptr = bn.payment_address_construct_from_string(address)
        self._constructed = True

    

# ------------------------------------------------------

class Output:
    """Represents one of the outputs of a Transaction."""
    def __init__(self, ptr):
        self._ptr = ptr
        self._constructed = True

    def _destroy(self):
        if self._constructed:
            #bn.output_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self._destroy()

    @property
    def is_valid(self):
        """int: returns '0' if output is not found."""
        return bn.output_is_valid(self._ptr)

    def serialized_size(self, wire):
        """unsigned int: size in bytes.
        
        Args:
            wire (bool): if 'TRUE' size will include size of 'uint32' for storing spender height.
        """
        return bn.output_serialized_size(self._ptr, wire)

    @property
    def value(self):
        """unsigned int: returns output value."""
        return bn.output_value(self._ptr)

    @property
    def signature_operations(self):
        """unsigned int: amount of signature operations in script."""
        return bn.output_signature_operations(self._ptr)

    @property
    def script(self):
        """Script: returns the output script."""
        return Script(bn.output_script(self._ptr))

    #def get_hash(self):
    #    return bn.output_get_hash(self._ptr)

    #def get_index(self):
    #    return bn.output_get_index(self._ptr)

class Input:
    """Represents one of the inputs of a Transaction."""
    def __init__(self, ptr):
        self._ptr = ptr
        self._constructed = True

    def _destroy(self):
        if self._constructed:
            #bn.input_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self._destroy()

    @property
    def is_valid(self):
        """int: returns '0' if previous outputs or script are invalid."""
        return bn.input_is_valid(self._ptr)

    @property
    def is_final(self):
        """int: returns '1' if sequence is equal to max_sequence."""
        return bn.input_is_final(self._ptr)

    def serialized_size(self):
        """unsigned int: size in bytes."""
        return bn.input_serialized_size(self._ptr, 0)

    @property
    def sequence(self):
        """unsigned int: sequence number of inputs. if it equals max_sequence, txs is final."""
        return bn.input_sequence(self._ptr)

    @property
    def signature_operations(self, bip16_active):
        """unsigned int: amount of sigops in the script.

        Args:
            bip16_active (int): '1' if bip 16 is active. '0' if not. 
        
        """
        return bn.input_signature_operations(self._ptr, bip16_active)

    @property
    def script(self):
        """Script: script object."""
        return Script(bn.input_script(self._ptr))

    @property
    def previous_output(self):
        """OutputPoint: returns previous output, with transaction hash and index."""
        return OutputPoint(bn.input_previus_output(self._ptr))
    
    #def get_hash(self):
    #    return bn.input_get_hash(self._ptr)

    #def get_index(self):
    #    return bn.input_get_index(self._ptr)

class OutputList:
    def __init__(self, ptr):
        self._ptr = ptr

    @property
    def push_back(self, output):
        bn.output_list_push_back(self._ptr, output._ptr)

    @property
    def list_count(self):
        return bn.output_list_count(self._ptr)

    def _nth(self, n):
        return Output(bn.output_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self._nth(key)
    

class InputList:
    def __init__(self, ptr):
        self._ptr = ptr

    @property
    def push_back(self, inputn):
        bn.input_list_push_back(self._ptr, inputn._ptr)

    @property
    def list_count(self):
        return bn.input_list_count(self._ptr)

    def _nth(self, n):
        return Input(bn.input_list_nth(self._ptr, n))
        
    def __getitem__(self, key):
        return self._nth(key)
    
# ------------------------------------------------------
class Chain:
    """Represents the Bitcoin blockchain."""
    def __init__(self, chain):
        self._chain = chain

    def fetch_last_height(self, handler):
        """Gets the height of the highest block in the chain. 
        
        Args:
            handler (Callable (error, block_height)): Will be executed when the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * block_height (unsigned int): height of the highest block in the chain.
            
        """
        bn.chain_fetch_last_height(self._chain, handler)

    def fetch_history(self, address, limit, from_height, handler):
        """
        Get list of output points, values, and spends for a payment address.
        
        Args:
            address (PaymentAddress): wallet to search.
            limit (unsigned int): max amount of results to fetch.
            from_height (unsigned int): minimum height to search for transactions.
            handler (Callable (error, list)): Will be executed when the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * list (HistoryList): list with every element found.
        """
        self.history_fetch_handler_ = handler
        bn.chain_fetch_history(self._chain, address, limit, from_height, self._history_fetch_handler_converter)

    # private members ... TODO: how to make private member functions in Python
    def _history_fetch_handler_converter(self, e, l):
        # print('history_fetch_handler_converter')
        if e == 0: 
            list = HistoryList(l)
        else:
            list = None

        self.history_fetch_handler_(e, list)

##### Stealth

    def _stealth_fetch_handler_converter(self, e, l):
        if e == 0: 
            _list = StealthList(l)
        else:
            _list = None

        self._stealth_fetch_handler(e, _list)

    def fetch_stealth(self, binary_filter_str, from_height, handler):
        """Get metadata on potential payment transactions by stealth filter. 
        Given a filter and a height in the chain it cues the chain for transactions matching the provided filter.

        Args:
            binary_filter_str (string): Must be at least 8 bits in lenght. example "10101010"
            from_height (unsigned int): minimum height in the chain where to look for transactions.
            handler (Callable (error, list)): Will be executed after the chain is cued.

                * error (int): error code. 0 if successfull.
                * list (StealthList): list with every transaction matching the given filter.
        
        """
        self._stealth_fetch_handler = handler
        binary_filter = Binary.construct_string(binary_filter_str)
        bn.chain_fetch_stealth(self._chain, binary_filter._ptr, from_height, self._stealth_fetch_handler_converter)

    def fetch_block_height(self, hash, handler):
        """Given a block hash, it cues the chain for the block height. 
        
        Args:
            hash (bytearray): 32 bytes of the block hash.
            handler (Callable (error, block_height)): Will be executed after the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * block_height (unsigned int): height of the block in the chain.
            
        """
        bn.chain_fetch_block_height(self._chain, hash, handler)

    def _fetch_block_header_converter(self, e, header, height):
        if e == 0: 
            header = Header(header, height, True)
        else:
            header = None

        self.fetch_block_header_handler_(e, header)

    def fetch_block_header_by_height(self, height, handler):
        """Get the block header from the specified height in the chain.

        Args:
            height (unsigned int): block height in the chain.
            handler (Callable (error, block_header)): Will be executed after the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * block_header (Header): header of the block found.
            
        """
        self.fetch_block_header_handler_ = handler
        bn.chain_fetch_block_header_by_height(self._chain, height, self._fetch_block_header_converter)

    def fetch_block_header_by_hash(self, hash, handler):
        """Get the block header from the specified block hash.

        Args:
            hash (bytearray): 32 bytes of the block hash.
            handler (Callable (error, block_header)): Will be executed after the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * block_header (Header): header of the block found.
            
        """
        self.fetch_block_header_handler_ = handler
        bn.chain_fetch_block_header_by_hash(self._chain, hash, self._fetch_block_header_converter)
    
    def _fetch_block_converter(self, e, block, height):
        if e == 0: 
            _block = Block(block, height)
        else:
            _block = None

        self._fetch_block_handler(e, _block)

    def fetch_block_by_height(self, height, handler):
        """Gets a block from the specified height in the chain.

        Args:
            height (unsigned int): block height in the chain.
            handler (Callable (error, block)): Will be executed after the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * block (Block): block at the defined height in the chain.
            
        """
        self._fetch_block_handler = handler
        bn.chain_fetch_block_by_height(self._chain, height, self._fetch_block_converter)

    def fetch_block_by_hash(self, hash, handler):
        """Gets a block from the specified hash.

        Args:
            hash (bytearray): 32 bytes of the block hash.
            handler (Callable (error, block)): Will be executed after the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * block (Block): block found with the specified hash.
            
        """
        self._fetch_block_handler = handler
        bn.chain_fetch_block_by_hash(self._chain, hash, self._fetch_block_converter)

    def _fetch_merkle_block_converter(self, e, merkle_block, height):
        if e == 0: 
            _merkle_block = MerkleBlock(merkle_block, height)
        else:
            _merkle_block = None

        self._fetch_merkle_block_handler(e, _merkle_block, height)

    def fetch_merkle_block_by_height(self, height, handler):
        """Given a block height in the chain, it retrieves a merkle block. 
        
        Args:
            height (unsigned int): block height in the chain.
            handler (Callable (error, merkle_block, block_height)): Will be executed when the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * merkle_block (MerkleBlock): merkle block of the block found at the specified height.
                * block_height (unsigned int): height of the block in the chain.
            
        """
        self._fetch_merkle_block_handler = handler
        bn.chain_fetch_merkle_block_by_height(self._chain, height, self._fetch_merkle_block_converter)

    def fetch_merkle_block_by_hash(self, hash, handler):
        """Given a block hash, it retrieves a merkle block. 
        
        Args:
            hash (bytearray): 32 bytes of the block hash.
            handler (Callable (error, merkle_block, block_height)): Will be executed when the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * merkle_block (MerkleBlock): merkle block of the block found with the given hash.
                * block_height (unsigned int): height of the block in the chain.
            
        """
        self._fetch_merkle_block_handler = handler
        bn.chain_fetch_merkle_block_by_hash(self._chain, hash, self._fetch_merkle_block_converter)

    def _fetch_transaction_converter(self, e, transaction, height, index):
        if e == 0: 
            _transaction = Transaction(transaction)
        else:
            _transaction = None

        self._fetch_transaction_handler(e, _transaction, height, index)

    def fetch_transaction(self, hashn, require_confirmed,handler):
        """Get a transaction by its hash. 
        
        Args:
            hashn (bytearray): 32 bytes of the transaction hash.
            require_confirmed (int): if transaction should be in a block. 0 if not.
            handler (Callable (error, transaction, block_height, tx_index)): Will be executed when the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * transaction (Transaction): Transaction found.
                * block_height (unsigned int): height in the chain of the block containing the transaction.
                * tx_index (unsigned int): index of the transaction inside the block.
            
        """
        self._fetch_transaction_handler = handler
        bn.chain_fetch_transaction(self._chain, hashn, require_confirmed, self._fetch_transaction_converter)


    def _fetch_output_converter(self, e, output):
        if e == 0: 
            _output = Output(output)
        else:
            _output = None

        self._fetch_output_handler(e, _output)

    def fetch_output(self, hashn, index, require_confirmed, handler):
        """Get a transaction output by its transaction hash and index inside the transaction. 
        
        Args:
            hashn (bytearray): 32 bytes of the transaction hash.
            index (unsigned int): index of the output in the transaction.
            require_confirmed (int): if transaction should be in a block. 0 if not.
            handler (Callable (error, output)): Will be executed when the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * output (Output): output found.            
        """
        self._fetch_output_handler = handler
        bn.chain_fetch_output(self._chain, hashn, index, require_confirmed, self._fetch_output_converter)


    def fetch_transaction_position(self, hashn, require_confirmed, handler):
        """Given a transaction hash it fetches the height and position inside the block.

        Args:
            hash (bytearray): 32 bytes of the transaction hash.
            require_confirmed (int): if transaction should be in a block. 0 if not.
            handler (Callable (error, block_height, tx_index)): Will be executed after the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * block_height (unsigned int): height of the block containing the transaction.
                * tx_index (unsigned int): index in the block of the transaction.            
        
        """
        bn.chain_fetch_transaction_position(self._chain, hashn, require_confirmed, handler)

    def _organize_block(self, block, handler):
        bn.chain_organize_block(self._chain, block, handler)

    def _organize_transaction(self, transaction, handler):
        bn.chain_organize_transaction(self._chain, transaction, handler)

    def validate_tx(self, transaction, handler):
        """Determine if a transaction is valid for submission to the blockchain.

        Args:
            transaction (Transaction): transaction to be checked.
            handler (Callable (error, message)): Will be executed after the chain is cued. 
                
                * error (int): error code. 0 if successfull.
                * message (str): string describing the result of the cue. example: 'The transaction is valid'
        
        """
        bn.chain_validate_tx(self._chain, transaction, handler)

  
    def _fetch_compact_block_converter(self, e, compact_block, height):
        if e == 0: 
            _compact_block = _CompactBlock(compact_block)
        else:
            _compact_block = None

        self._fetch_compact_block_handler(e, _compact_block, height)

    def _fetch_compact_block_by_height(self, height, handler):
        self._fetch_compact_block_handler = handler
        bn.chain_fetch_compact_block_by_height(self._chain, height,  self._fetch_compact_block_converter)

    def _fetch_compact_block_by_hash(self, hashn, handler):
        self._fetch_compact_block_handler = handler
        bn.chain_fetch_compact_block_by_hash(self._chain, hashn, self._fetch_compact_block_converter)

    def _fetch_spend_converter(self, e, point):
        if e == 0: 
            _spend = Point(point)
        else:
            _spend = None

        self._fetch_spend_handler(e, _spend)

    def fetch_spend(self, output_point, handler):
        """Fetch the transaction input which spends the indicated output. The `fetch_spend_handler` will be executed after cueing the chain. 
        
        Args:
            output_point (OutputPoint): tx hash and index pair.
            handler (Callable (error, input_point)): Will be executed when the chain is cued.
                
                * error (int): error code. 0 if successfull.
                * input_point (Point): Tx hash nad index pair where the output was spent.
            
        """
        self._fetch_spend_handler = handler
        bn.chain_fetch_spend(self._chain, output_point._ptr, self._fetch_spend_converter)


    def _subscribe_reorganize_converter(self, e, fork_height, blocks_incoming, blocks_replaced):
        if e == 0:
            _incoming = BlockList(blocks_incoming)
            _replaced = BlockList(blocks_replaced)
        else:
            _incoming = None
            _replaced = None
    
        return self._subscribe_reorganize_handler(e, fork_height,_incoming, _replaced)
    
    def _subscribe_reorganize(self, handler):
        self._subscribe_reorganize_handler = handler
        bn.chain_subscribe_reorganize(self._chain, self._subscribe_reorganize_converter)

    def _subscribe_transaction_converter(self, e, tx):
        if e == 0:
            _tx = Transacion(tx)
        else:
            _tx = None
    
        self._subscribe_transaction_handler(e, _tx)
    
    def _subscribe_transaction(self, handler):
        self._subscribe_transaction_handler = handler
        bn.chain_subscribe_transaction(self._chain, self._subscribe_transaction_converter)


class Binary:
    """Represents a binary filter."""
    def __init__(self, ptr):
        self._ptr = ptr

    @classmethod
    def construct(self):
        """Binary: create an empty binary object."""
        return Binary(bn.binary_construct())

    @classmethod
    def construct_string(self, string_filter):
        """Binary: construct a binary filter form string.
        
        Args:
            string_filter (str): binary string. Example: '10111010101011011111000000001101'
        """
        return Binary(bn.binary_construct_string(string_filter))

    @classmethod
    def construct_blocks(self, size, blocks):
        """Binary: construct binary filter from an array of int.

        Args:
            size (unsigned int): lenght of the filter.
            blocks (array[unsigned int]): Every int represents a byte of the filter. Example: '[186,173,240,13]'        
        
        """
        return Binary(bn.binary_construct_blocks(size, len(blocks), blocks))

    def blocks(self):
        """Array [unsigned int]: returns the filter as an array of uint.  
        
        """
        return bn.binary_blocks(self._ptr)

    def encoded(self):
        """str: returns the filter in a binary string."""
        return bn.binary_encoded(self._ptr)


# ------------------------------------------------------
class Executor:
    """Controls the execution of the Bitprim bitcoin node."""
    def __init__(self, path, sout = None, serr = None):
        self._executor = bn.construct(path, sout, serr)
        self._constructed = True
        self._running = False

    def _destroy(self):
        # print('_destroy')

        if self._constructed:
            if self._running:
                self.stop()

            bn.destruct(self._executor)
            self._constructed = False

    def __del__(self):
        # print('__del__')
        self._destroy()

    def init_chain(self):
        """bool: Initialization of the blockchain. 
        Returns 'TRUE' if successfull."""
        return bn.initchain(self._executor) != 0

    def run(self):
        """bool: Starts running the node, initializing blockchain download.
        Returns 'TRUE' if successful. """
        ret = bn.run(self._executor)

        if ret:
            self._running = True

        return ret == 0

    def run_wait(self):
        """bool: Starts running the node, initializing blockchain download. 
        It listen to wait signals.
        Returns 'TRUE' if successful. """
        ret = bn.run_wait(self._executor)

        if ret:
            self._running = True

        return ret == 0

    def stop(self):
        """bool: it stops the node.
        precondition: self._running.
        Returns 'TRUE' if successfull"""
        # precondition: self._running
        # print('def stop(self):')
        ret = bn.stop(self._executor)

        if ret:
            self._running = False

        return ret


    @property
    def chain(self):
        """Chain: Object containing the blockchain."""
        return Chain(bn.get_chain(self._executor))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print('__exit__')
        self._destroy()

# def main()
#     print('main')

# if __name__ == '__main__':
#     main()


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
#     # signal.signal(signal.SNoneIGINT, signal_handler)
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
