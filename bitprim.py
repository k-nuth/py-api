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
import sys
import time

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

##
# Converts a bytearray into a readable format (hex string)
# @param hash (bytearray): Hash bytes
# @return (str) Hex string
# Example: "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
def encode_hash(hash):
    if (sys.version_info > (3, 0)):
        return ''.join('{:02x}'.format(x) for x in hash[::-1])
    else:
        return hash[::-1].encode('hex')

##
# Converts a string into a workable format (byte array)
# @param hash_str (str): hash hex string
# @return (bytearray): Byte array representing hash. Example "00 00 00 00 00 19 D6 68 ... E2 6F"
def decode_hash(hash_str):    
    h = bytearray.fromhex(hash_str) 
    h = h[::-1] 
    return bytes(h)

# ------------------------------------------------------

##
# Wallet handling utilities
class Wallet:
    # def __init__(self, ptr):
    #     self._ptr = ptr

    ##
    # Convert mnemonics to a seed
    # @param mnemonics: A list of strings representing the mnemonics
    # @return A new seed
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
##
# Represents a Bitcoin block's header
class Header:
    
    def __init__(self, pointer, height, auto_destroy = False):
        ##
        # @private
        self._ptr = pointer
        self._height = height
        self._auto_destroy = auto_destroy

    def _destroy(self):
        bn.header_destruct(self._ptr)

    def __del__(self):
        if self._auto_destroy:
            self._destroy()

    ##
    # Block height in the chain.
    # @return (unsigned int)
    @property
    def height(self):
        return self._height

    ##
    # Header protocol version
    # @return (unsigned int)
    @property
    def version(self):
        return bn.header_get_version(self._ptr)

    ##
    # Set version
    # @param version New version value
    @version.setter
    def set_version(self, version):
        bn.header_set_version(self._ptr, version)

    ##
    # 32 bytes hash of the previous block in the chain.
    # @return (bytearray)
    @property
    def previous_block_hash(self):
        return bn.header_get_previous_block_hash(self._ptr)
    
    #def set_previous_block_hash(self,hash):        
        #return bn.header_set_previous_block_hash(self._ptr, hash)

    ##
    # Merkle root in 32 byte array format
    # @return (bytearray)
    @property
    def merkle(self):
        return bn.header_get_merkle(self._ptr)

    #def set_merkle(self, merkle):
        #bn.header_set_merkle(self._ptr, merkle)

    ##
    # Block hash in 32 byte array format
    # @return (bytearray
    @property
    def hash(self):
        return bn.header_get_hash(self._ptr)

    ##
    # Block timestamp in UNIX Epoch (seconds since January 1st 1970)
    # Assume UTC 0
    # @return (unsigned int)
    @property
    def timestamp(self):
        return bn.header_get_timestamp(self._ptr)

    ##
    # Set header timestamp
    # @param timestamp New header timestamp value
    @timestamp.setter
    def set_timestamp(self, timestamp):
        bn.header_set_timestamp(self._ptr, timestamp)

    ##
    # Difficulty threshold
    # @return (unsigned int)
    @property
    def bits(self):
        return bn.header_get_bits(self._ptr)
    
    ##
    # Set header bits
    # @param bits New header bits value
    @bits.setter
    def set_bits(self, bits):
        bn.header_set_bits(self._ptr, bits)

    ##
    # The nonce that allowed this block to be added to the blockchain
    # @return (unsigned int)
    @property
    def nonce(self):
        return bn.header_get_nonce(self._ptr)
    
    ##
    # Set header nonce
    # @param nonce New header nonce value
    @nonce.setter
    def set_nonce(self, nonce):
        bn.header_set_nonce(self._ptr, nonce)


# --------------------------------------------------------------------

##
# Represent a full Bitcoin blockchain block
class Block:
    def __init__(self, pointer, height, auto_destroy = False):
        ##
        # @private
        self._ptr = pointer
        self._height = height
        self._auto_destroy = auto_destroy

    def _destroy(self):
        bn.block_destruct(self._ptr)

    def __del__(self):
        if self._auto_destroy:
            self._destroy()
    
    ##
    # The block's height in the chain. It identifies it univocally
    # @return (int)
    @property
    def height(self):
        return self._height

    ##
    # The block's header
    # @return (Header)
    @property
    def header(self):
        return Header(bn.block_get_header(self._ptr), self._height, False)

    ##
    # The total amount of transactions that the block contains
    # @return (unsigned int)
    @property
    def transaction_count(self):
        return bn.block_transaction_count(self._ptr)

    ##
    # The block's hash as a 32 byte array
    # @return (bytearray)
    @property
    def hash(self):
        return bn.block_hash(self._ptr)

    ##
    # Block size in bytes.
    # @return (int)
    @property
    def serialized_size(self):
        return bn.block_serialized_size(self._ptr, 0)

    ##
    # Miner fees included in the block's coinbase transaction
    # @return (unsigned int)
    @property
    def fees(self):
        return bn.block_fees(self._ptr)

    ##
    # Sum of coinbase outputs
    # @return (unsigned int)
    @property
    def claim(self):
        return bn.block_claim(self._ptr)

    ##
    # Reward = Subsidy + Fees, for the block at the given height
    # @param height (unsigned int) Block height in the chain. Identifies it univocally
    # @return (unsigned int)
    def reward(self, height):
        return bn.block_reward(self._ptr, height)

    ##
    # The block's Merkle root, as a 32 byte array
    # @return (byte array)
    def generate_merkle_root(self):
        return bn.block_generate_merkle_root(self._ptr)

    ##
    # Return 1 if and only if the block has transactions and a valid header, 0 otherwise
    # @return (int) TODO Why not a bool?
    def is_valid(self):
        return bn.block_is_valid(self._ptr)


    ##
    # Given a position in the block, returns the corresponding transaction.
    # @param n (unsigned int): Transaction index inside the block (starting at zero)
    # @return (Transaction)
    def transaction_nth(self, n):
        return Transaction(bn.block_transaction_nth(self._ptr, n), False)

    ##
    # Amount of signature operations in the block. Returns max_int in case of overflow.
    # @return (unsigned int)
    def signature_operations(self):
        return bn.block_signature_operations(self._ptr)

    ##
    # Amount of signature operations in the block. Returns max_int in case of overflow.
    # @param bip16_active (int): should be '1' if and only if bip16 is activated at this point.
    def signature_operations_bip16_active(self, bip16_active):
        return bn.block_signature_operations_bip16_active(self._ptr, bip16_active)

    ##
    # Total amount of inputs in the block (consider all transactions).
    # @param with_coinbase (int): should be '1' if and only if the block contains a coinbase transaction, '0' otherwise.
    # @return (unsigned int)
    def total_inputs(self, with_coinbase = 1):
        return bn.block_total_inputs(self._ptr, with_coinbase)

    ##
    # Tell whether there is more than one coinbase transaction in the block
    # @return (int) 1 if and only if there is another coinbase other than the first transaction, 0 otherwise.
    def is_extra_coinbases(self):
        return bn.block_is_extra_coinbases(self._ptr)

    ##
    # Tell whether every transaction in the block is final or not   
    # @param height (unsigned int): Block height in the chain. Identifies it univocally.
    # @return (int) 1 if every transaction in the block is final, 0 otherwise.
    def is_final(self, height, block_time):
        return bn.block_is_final(self._ptr, height, block_time)

    ##
    # Tell whether all transactions in the block have a unique hash (i.e. no duplicates)
    # @return (int): 1 if there are no two transactions with the same hash in the block, 0 otherwise
    def is_distinct_transaction_set(self):
        return bn.block_is_distinct_transaction_set(self._ptr)

    ##
    # Given a block height, tell if its coinbase claim is not higher than the deserved reward
    # @param height (unsigned int): Block height in the chain. Identifies it univocally.
    # @return (int) 1 if coinbase claim is not higher than the deserved reward.
    def is_valid_coinbase_claim(self, height):
        return bn.block_is_valid_coinbase_claim(self._ptr, height)

    ##
    # Returns 1 if and only if the coinbase script is valid
    # @return (int)
    def is_valid_coinbase_script(self, height):
        return bn.block_is_valid_coinbase_script(self._ptr, height)

    def _is_internal_double_spend(self):
        return bn.block_is_internal_double_spend(self._ptr)

    ##
    # Tell if the generated Merkle root equals the header's Merkle root
    # @return (int) 1 if and only if the generated Merkle root is equal to the Header's Merkle root
    def is_valid_merkle_root(self):
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

    @property
    def count(self):
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

    @property
    def count(self):
        return bn.transaction_list_count(self._ptr)

    def _nth(self, n):
        return Transaction(bn.transaction_list_nth(self._ptr, n), False)

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

##
# Merkle tree representation of a transaction block
class MerkleBlock:

    
    def __init__(self, pointer, height):
        ##
        # @private
        self._ptr = pointer
        self._height = height

    ##
    # Height of the block in the chain
    # @return (unsigned int)
    @property
    def height(self):
        return self._height

    def _destroy(self):
        bn.merkle_block_destruct(self._ptr)

    def __del__(self):
        self._destroy()

    ##
    # The block's header
    # @return (Header)
    @property
    def header(self):
        return Header(bn.merkle_block_get_header(self._ptr), self._height, False)

    ##
    # Returns true if and only if it the block contains txs hashes, and header is valid
    # @return (int)
    @property
    def is_valid(self):
        return bn.merkle_block_is_valid(self._ptr)

    ##
    # Transaction hashes list element count
    # @return (unsigned int)
    @property
    def hash_count(self):
        return bn.merkle_block_hash_count(self._ptr)

    ##
    # Block size in bytes.
    # @param version (unsigned int): block protocol version.
    # @return (unsigned int)
    def serialized_size(self, version):
        return bn.merkle_block_serialized_size(self._ptr, version)

    ##
    # Amount of transactions inside the block
    # @return (unsigned int)
    @property
    def total_transaction_count(self):
        return bn.merkle_block_total_transaction_count(self._ptr)

    ##
    # Delete all the data inside the block
    def reset(self):
        return bn.merkle_block_reset(self._ptr)

##
# Compressed representation of Stealth payment related data
class StealthCompact:

    def __init__(self, ptr):
        ##
        # @private
        self._ptr = ptr

    ##
    # Ephemeral public key hash in 32 byte array format. Does not
    # include the sign byte (0x02)
    # @return (byte array)
    def ephemeral_public_key_hash(self):
        return bn.stealth_compact_ephemeral_public_key_hash(self._ptr)

    ##
    # Transaction hash in 32 byte array format
    # @return (byte array)
    @property
    def transaction_hash(self):
        return bn.stealth_compact_get_transaction_hash(self._ptr)

    ##
    # Public key hash in 20 byte array format
    # @return (byte array)
    @property
    def public_key_hash(self):
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

    @property
    def count(self):
        return bn.stealth_compact_list_count(self._ptr)

    def _nth(self, n):
        return Stealth(bn.stealth_compact_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self._nth(key)


# ------------------------------------------------------
##
# Represents one of the tx inputs.
# It's a transaction hash and index pair.
class Point:
    
    def __init__(self, ptr):
        ##
        # @private
        self._ptr = ptr

    ##
    # Transaction hash in 32 byte array format
    # @return (byte array)
    @property
    def hash(self):
        return bn.point_get_hash(self._ptr) #[::-1].hex()

    ##
    # returns true if its not null.
    #
    #Returns:
    #    bool
    @property
    def is_valid(self):
        return bn.point_is_valid(self._ptr)

    ##
    # Input position in the transaction (starting at zero)
    # @return (unsigned int)
    @property
    def index(self):
        return bn.point_get_index(self._ptr)

    ##
    # This is used with output_point identification within a set of history rows
    # of the same address. Collision will result in miscorrelation of points by
    # client callers. This is NOT a bitcoin checksum.
    # @return (unsigned int)
    @property
    def checksum(self):
        return bn.point_get_checksum(self._ptr)


##
# Transaction hash and index pair representing one of the transaction outputs
class OutputPoint:
    
    def __init__(self, ptr ):
        ##
        # @private
        self._ptr = ptr

    ##
    # Transaction hash in 32 byte array format
    # @return (bytearray)
    @property
    def hash(self):
        return bn.output_point_get_hash(self._ptr)

    def _destroy(self):
        bn.output_point_destruct(self._ptr)

    def __del__(self):
        self._destroy()

    ##
    # Position of the output in the transaction (starting at zero)
    # @return (unsigned int)
    @property
    def index(self):
        return bn.output_point_get_index(self._ptr)

    ##
    # Creates an empty output point
    # @return (OutputPoint)
    @classmethod
    def construct(self):
        return OutputPoint(bn.output_point_construct())

    ##
    # Creates an OutputPoint from a transaction hash and index pair
    # @param hashn (bytearray): Transaction hash in 32 byte array format
    # @param index (unsigned int): position of the output in the transaction.
    # @return (Outputpoint)
    @classmethod
    def construct_from_hash_index(self, hashn, index):
        return OutputPoint(bn.output_point_construct_from_hash_index(hashn, index))

    #def is_valid(self):
    #    return bn.point_is_valid(self._ptr)

    #def get_checksum(self):
    #    return bn.point_get_checksum(self._ptr)

# ------------------------------------------------------
##
# Output points, values, and spends for a payment address
class History:

    def __init__(self, ptr):
        ##
        # @private
        self._ptr = ptr

    ##
    # Used for differentiation.
    #    '0' output
    #    '1' spend
    # @return (unsigned int)
    @property
    def point_kind(self):
        return bn.history_compact_get_point_kind(self._ptr)

    ##
    # The point that identifies the History instance
    # @return (Point)
    @property
    def point(self):
        return Point(bn.history_compact_get_point(self._ptr))

    ##
    # Height of the block containing the Point
    # @return (unsigned int)
    @property
    def height(self):
        return bn.history_compact_get_height(self._ptr)

    ##
    #  Varies depending of point_kind.
    #    value: if output, then satoshi value of output.
    #    previous_checksum: if spend, then checksum hash of previous output_point.
    # @return (unsigned int)
    @property
    def value_or_previous_checksum(self):
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
        self._destroy()

    @property
    def count(self):
        return bn.history_compact_list_count(self._ptr)

    def _nth(self, n):
        return History(bn.history_compact_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self._nth(key)

    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     # print('__exit__')
    #     self._destroy()

# ------------------------------------------------------

##
# Stealth payment related data
class Stealth:
    
    def __init__(self, ptr):
        ##
        # @private
        self._ptr = ptr

    ##
    # 33 bytes. Includes the sign byte (0x02)
    # @return (bytearray) 
    @property
    def ephemeral_public_key_hash(self):
        return bn.stealth_compact_get_ephemeral_public_key_hash(self._ptr)

    ##
    # Transaction hash in 32 bytes format
    # @return (bytearray)
    @property
    def transaction_hash(self):
        return bn.stealth_compact_get_transaction_hash(self._ptr)

    ##
    # Public key hash in 20 byte array format
    # @return (bytearray)
    @property
    def public_key_hash(self):
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
        self._destroy()

    @property
    def count(self):
        return bn.stealth_compact_list_count(self._ptr)

    def _nth(self, n):
        return Stealth(bn.stealth_compact_list_nth(self._ptr, n))

    def __getitem__(self, key):
        return self._nth(key)

# ------------------------------------------------------

##
# Represents a Bitcoin Transaction
class Transaction:
    def __init__(self, ptr, auto_destroy = False):
        ##
        # @private
        self._ptr = ptr
        self._constructed = True
        self._auto_destroy = auto_destroy

    def _destroy(self):
        if self._constructed:
            bn.transaction_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        if self._auto_destroy:
            self._destroy()

    ##
    # Transaction protocol version
    # @return (unsigned int)
    @property
    def version(self):
        return bn.transaction_version(self._ptr)

    ##
    # Set new transaction version value
    # @param version New transaction version value
    @version.setter
    def set_version(self, version):
        return bn.transaction_set_version(self._ptr, version)

    @property
    def hash(self):
        """bytearray: 32 bytes transaction hash."""
        return bn.transaction_hash(self._ptr)

    ##
    # 32 bytes transaction hash + 4 bytes signature hash type
    # @param sighash_type (unsigned int): signature hash type
    # @return (byte array)
    def hash_sighash_type(self, sighash_type):
        return bn.transaction_hash_sighash_type(self._ptr, sighash_type)

    ##
    # Transaction locktime
    # @return (unsigned int)
    @property
    def locktime(self):
        return bn.transaction_locktime(self._ptr)

    ##
    # Transaction size in bytes.
    # @param wire (bool): if true, size will include size of 'uint32' for storing spender
    # output height
    # @return (unsigned int)
    def serialized_size(self, wire):
        return bn.transaction_serialized_size(self._ptr, wire)

    ##
    # Fees to pay to the winning miner. Difference between sum of inputs and outputs
    # @return (unsigned int)
    @property
    def fees(self):
        return bn.transaction_fees(self._ptr)

    ##
    # Amount of signature operations in the transaction
    # @return (unsigned int) max_int in case of overflow
    def signature_operations(self):
        return bn.transaction_signature_operations(self._ptr)

    ##
    # Amount of signature operations in the transaction.
    # @param bip16_active (int): 1 if and only if bip 16 is active, 0 otherwise
    # @return (unsigned int) max_int in case of overflow.
    def signature_operations_bip16_active(self, bip16_active):
        return bn.transaction_signature_operations_bip16_active(self._ptr, bip16_active)

    ##
    # Sum of every input value in the transaction
    # @return (unsigned int) max_int in case of overflow
    def total_input_value(self):
        return bn.transaction_total_input_value(self._ptr)


    ##
    # Sum of every output value in the transaction.
    # @return (unsigned int) max_int in case of overflow
    def total_output_value(self):
        return bn.transaction_total_output_value(self._ptr)

    ##
    # Return 1 if and only if transaction is coinbase, 0 otherwise
    # @return (int)
    def is_coinbase(self):
        return bn.transaction_is_coinbase(self._ptr)

    ##
    # Return 1 if and only if the transaction is not coinbase
    # and has a null previous output, 0 otherwise
    # @return (int)
    def is_null_non_coinbase(self):
        return bn.transaction_is_null_non_coinbase(self._ptr)

    ##
    # Returns 1 if the transaction is coinbase and
    # has an invalid script size on its first input
    # @return (int)
    def is_oversized_coinbase(self):
        return bn.transaction_is_oversized_coinbase(self._ptr)

    ##
    # Returns 1 if and only if at least one of the inputs is
    # not mature, 0 otherwise
    # @return (int)
    def is_mature(self, target_height):
        return bn.transaction_is_mature(self._ptr, target_height)

    ##
    # Returns 1 if transaction is not a coinbase,
    # and the sum of its outputs is higher than the sum of
    # its inputs, 0 otherwise
    # @return (int)
    def is_overspent(self):
        return bn.transaction_is_overspent(self._ptr)

    ##
    # Returns 1 if at least one of the previous outputs was
    # already spent, 0 otherwise
    # @return (int)
    def is_double_spend(self, include_unconfirmed):
        return bn.transaction_is_double_spend(self._ptr, include_unconfirmed)

    ##
    # Returns 1 if and only if at least one of the previous outputs
    # is invalid, 0 otherwise
    # @return (int)
    def is_missing_previous_outputs(self):
        return bn.transaction_is_missing_previous_outputs(self._ptr)

    ##
    # Returns 1 if and only if the transaction is final, 0 otherwise
    # @return (int)
    def is_final(self, block_height, block_time):
        return bn.transaction_is_final(self._ptr, block_height, block_time)

    ##
    # Returns 1 if and only if the transaction is locked
    # and every input is final, 0 otherwise
    # @return (int)
    def is_locktime_conflict(self):
        return bn.transaction_is_locktime_conflict(self._ptr)

    ##
    # Returns a list with all of this transaction's outputs
    # @return (OutputList)
    def outputs(self):
        return OutputList(bn.transaction_outputs(self._ptr))

    ##
    # Returns a list with all of this transaction's inputs
    # @return (InputList)
    def inputs(self):
        return InputList(bn.transaction_inputs(self._ptr))

    def to_data(self, wired):
        return bn.transaction_to_data(self._ptr, wired)
# ------------------------------------------------------
##
# Represents a transaction script
class Script:
    
    
    def __init__(self, ptr, auto_destroy = False):
        ##
        # @private
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

    ##
    # All script bytes are valid under some circumstance (e.g. coinbase).
    # @return (int) 0 if and only if prefix and byte count do not match.
    @property
    def is_valid(self):
        return bn.script_is_valid(self._ptr)
    
    ##
    # Script validity is independent of individual operation validity.
    # Ops are considered invalid if there is a trailing invalid/default
    # op or if a push op has a size mismatch
    # @return (int)
    @property
    def is_valid_operations(self):
        return bn.script_is_valid_operations(self._ptr)

    ##
    # Size in bytes
    # @return (unsigned int)
    @property
    def satoshi_content_size(self):
        return bn.script_satoshi_content_size(self._ptr)

    ##
    # Size in bytes. If prefix is 1 size, includes a var int size
    # @param prefix (int): include prefix size in the final result
    # @return (unsigned int)
    def serialized_size(self, prefix):
        
        return bn.script_serialized_size(self._ptr, prefix)
    
    ##
    # Translate operations in the script to string
    # @param active_forks (unsigned int): Tells which rule is active
    # @return (str)
    def to_string(self, active_forks):
        return bn.script_to_string(self._ptr, active_forks)

    ##
    # Amount of signature operations in the script
    # @param embedded (bool): Tells whether this is an embedded script
    # @return (unsigned int)
    def sigops(self, embedded):
        return bn.script_sigops(self._ptr, embedded)  

    ##
    # Count the sigops in the embedded script using BIP16 rules
    # @return (unsigned int)
    def embedded_sigops(self, prevout_script):
        return bn.script_embedded_sigops(self._ptr, prevout_script)  


# ------------------------------------------------------
## 
# Represents a Bitcoin wallet address
class PaymentAddress:
    
    
    def __init__(self, ptr = None):
        ##
        # @private
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

    ##
    # Address in readable format (hex string)
    # @return (str) 
    @property
    def encoded(self):
        if self._constructed:
            return bn.payment_address_encoded(self._ptr)

    ##
    # Address version
    # @return (unsigned int)
    @property
    def version(self):
        if self._constructed:
            return bn.payment_address_version(self._ptr)

    ##
    # Creates the Payment Address based on the received string.
    # @param address (str) A base58 address. Example: '1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR'
    @classmethod
    def construct_from_string(self, address):
        self._ptr = bn.payment_address_construct_from_string(address)
        self._constructed = True

    
# ------------------------------------------------------
##
# Represents one of the outputs of a Transaction
class Output:
    
    def __init__(self, ptr):
        ##
        # @private
        self._ptr = ptr
        self._constructed = True

    def _destroy(self):
        if self._constructed:
            #bn.output_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self._destroy()

    ##
    # Returns 0 if and only if output is not found
    # @return (int) 
    @property
    def is_valid(self):
        return bn.output_is_valid(self._ptr)

    ##
    # Block size in bytes
    # @param wire (bool): if true, size will include size of 'uint32' for storing spender height
    # @return (unsigned int)
    def serialized_size(self, wire):
        return bn.output_serialized_size(self._ptr, wire)

    ##
    # Output value in Satoshis
    # @return (unsigned int)
    @property
    def value(self):
        return bn.output_value(self._ptr)

    ##
    # Amount of signature operations in script
    # @return (unsigned int)
    @property
    def signature_operations(self):
        return bn.output_signature_operations(self._ptr)

    ##
    # Script: returns the output script."""
    @property
    def script(self):
        return Script(bn.output_script(self._ptr))

    #def get_hash(self):
    #    return bn.output_get_hash(self._ptr)

    #def get_index(self):
    #    return bn.output_get_index(self._ptr)

##
# Represents one of the inputs of a Transaction
class Input:

    def __init__(self, ptr):
        ##
        # @private
        self._ptr = ptr
        self._constructed = True

    def _destroy(self):
        if self._constructed:
            #bn.input_destruct(self._ptr)
            self._constructed = False

    def __del__(self):
        self._destroy()

    ##
    # Returns 0 if and only if previous outputs or script are invalid
    # @return (int)
    @property
    def is_valid(self):
        return bn.input_is_valid(self._ptr)

    ##
    # Returns 1 if and only if sequence is equal to max_sequence.
    # @return int
    @property
    def is_final(self):
        return bn.input_is_final(self._ptr)

    ##
    # Size in bytes
    # @return (unsigned int)
    def serialized_size(self):
        return bn.input_serialized_size(self._ptr, 0)

    ##
    # Sequence number of inputs. If it equals max_sequence, txs is final
    # @return (unsigned int)
    @property
    def sequence(self):
        return bn.input_sequence(self._ptr)

    ##
    # Total amount of sigops in the script.
    # @param bip16_active (int): 1 if and only if bip 16 is active. 0 if not. 
    # @return (unsigned int)
    @property
    def signature_operations(self, bip16_active):
        return bn.input_signature_operations(self._ptr, bip16_active)

    ##
    # The input's script
    # @return (Script)
    @property
    def script(self):
        return Script(bn.input_script(self._ptr))

    ##
    # Returns the previous output, with its transaction hash and index
    # @return (OutputPoint)
    @property
    def previous_output(self):
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
    def count(self):
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
    def count(self):
        return bn.input_list_count(self._ptr)

    def _nth(self, n):
        return Input(bn.input_list_nth(self._ptr, n))
        
    def __getitem__(self, key):
        return self._nth(key)
    
# ------------------------------------------------------

##
# Represents the Bitcoin `P2P` Networking API.
class P2p:

    def __init__(self, executor, p2p):
        ##
        # @private
        self._executor = executor
        self._p2p = p2p

    @property
    def address_count(self):
        return bn.p2p_address_count(self._p2p)

    def stop(self):
        bn.p2p_stop(self._p2p)

    def close(self):
        bn.p2p_close(self._p2p)

    @property
    def stopped(self):
        return bn.p2p_stopped(self._p2p) != 0

# PyObject* bitprim_native_p2p_address_count(PyObject* self, PyObject* args);
# PyObject* bitprim_native_p2p_stop(PyObject* self, PyObject* args);
# PyObject* bitprim_native_p2p_close(PyObject* self, PyObject* args);
# PyObject* bitprim_native_p2p_stopped(PyObject* self, PyObject* args);


# ------------------------------------------------------


##
# Represents the Bitcoin blockchain.
class Chain:

    def __init__(self, executor, chain):
        ##
        # @private
        self._executor = executor
        self._chain = chain

    ##
    # Gets the height of the highest block in the local copy of the blockchain.
    # This number will grow as the node synchronizes with the blockchain.
    # This is an asynchronous method; a callback must be provided to receive the result
    #
    # Args:
    #   handler (Callable (error, block_height)): Will be executed when the chain is queried.
    #       * error (int): Error code. 0 if and only if successful.
    #       * block_height (unsigned int): Height of the highest block in the chain.
    def fetch_last_height(self, handler):
        bn.chain_fetch_last_height(self._chain, handler)

    ##
    # Get a list of output points, values, and spends for a given payment address.
    # This is an asynchronous method; a callback must be provided to receive the result
    #
    # Args:
    #    address (PaymentAddress): Wallet to search.
    #    limit (unsigned int): Max amount of results to fetch.
    #    from_height (unsigned int): Starting height to search for transactions.
    #    handler (Callable (error, list)): Will be executed when the chain is queried.
    #        * error (int): Error code. 0 if and only if successful.
    #        * list (HistoryList): A list with every element found.
    def fetch_history(self, address, limit, from_height, handler):
        self.history_fetch_handler_ = handler
        bn.chain_fetch_history(self._chain, address, limit, from_height, self._history_fetch_handler_converter)

    def _history_fetch_handler_converter(self, e, l):
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

    ##
    # Get metadata on potential payment transactions by stealth filter. 
    # Given a filter and a height in the chain, it queries the chain for transactions matching the given filter.
    # Args:
    #    binary_filter_str (string): Must be at least 8 bits in length. example "10101010"
    #    from_height (unsigned int): Starting height in the chain to search for transactions.
    #    handler (Callable (error, list)): Will be executed when the chain is queried.
    #        * error (int): Error code. 0 if and only if successful.
    #        * list (StealthList): list with every transaction matching the given filter.
    def fetch_stealth(self, binary_filter_str, from_height, handler):
        self._stealth_fetch_handler = handler
        binary_filter = Binary.construct_string(binary_filter_str)
        bn.chain_fetch_stealth(self._chain, binary_filter._ptr, from_height, self._stealth_fetch_handler_converter)

    ##
    # Given a block hash, it queries the chain for the block height. 
    #    
    # Args:
    #   hash (bytearray): 32 bytes of the block hash.
    #   handler (Callable (error, block_height)): Will be executed after the chain is cued. 
    #       * error (int): Error code. 0 if and only if successful.
    #       * block_height (unsigned int): height of the block in the chain.
    def fetch_block_height(self, hash, handler):
        bn.chain_fetch_block_height(self._chain, hash, handler)

    def _fetch_block_header_converter(self, e, header, height):
        if e == 0: 
            header = Header(header, height, True)
        else:
            header = None

        self.fetch_block_header_handler_(e, header)

    ##
    # Get the block header from the specified height in the chain.
    #
    # Args:
    #    height (unsigned int): Block height in the chain.
    #    handler (Callable (error, block_header)): Will be executed after the chain is queried.
    #        * error (int): Error code. 0 if successful.
    #        * block_header (Header): The found block's header.
    def fetch_block_header_by_height(self, height, handler):
        self.fetch_block_header_handler_ = handler
        bn.chain_fetch_block_header_by_height(self._chain, height, self._fetch_block_header_converter)

    ##
    # Get the block header from the specified block hash.
    # Args:
    #    hash (bytearray): 32 bytes of the block hash.
    #    handler (Callable (error, block_header)): Will be executed after the chain is queried.
    #        * error (int): Error code. 0 if successful.
    #        * block_header (Header): The found block's header.
    def fetch_block_header_by_hash(self, hash, handler):
        self.fetch_block_header_handler_ = handler
        bn.chain_fetch_block_header_by_hash(self._chain, hash, self._fetch_block_header_converter)
    
    def _fetch_block_converter(self, e, block, height):
        if e == 0: 
            _block = Block(block, height, True)
        else:
            _block = None

        self._fetch_block_handler(e, _block)

    ##
    # Gets a block from the specified height in the chain.
    # Args:
    #    height (unsigned int): Block height in the chain.
    #    handler (Callable (error, block)): Will be executed after the chain is queried.
    #        * error (int): Error code. 0 if successful.
    #        * block (Block): Block at the given height in the chain.
    def fetch_block_by_height(self, height, handler):
        self._fetch_block_handler = handler
        bn.chain_fetch_block_by_height(self._chain, height, self._fetch_block_converter)

    ##
    # Gets a block from the specified hash.
    # Args:
    #    hash (bytearray): 32 bytes of the block hash.
    #    handler (Callable (error, block)): Will be executed after the chain is queried.
    #       * error (int): Error code. 0 if successful.
    #       * block (Block): Block found with the specified hash.
    def fetch_block_by_hash(self, hash, handler):
        self._fetch_block_handler = handler
        bn.chain_fetch_block_by_hash(self._chain, hash, self._fetch_block_converter)

    def _fetch_merkle_block_converter(self, e, merkle_block, height):
        if e == 0: 
            _merkle_block = MerkleBlock(merkle_block, height)
        else:
            _merkle_block = None

        self._fetch_merkle_block_handler(e, _merkle_block, height)

    ##
    # Given a block height in the chain, it retrieves the block's associated Merkle block.
    # Args:
    #    height (unsigned int): Block height in the chain.
    #    handler (Callable (error, merkle_block, block_height)): Will be executed when the chain is queried.
    #        * error (int): Error code. 0 if successful.
    #        * merkle_block (MerkleBlock): The requested block's Merkle block.
    #        * block_height (unsigned int): The block's height in the chain.
    def fetch_merkle_block_by_height(self, height, handler):
        self._fetch_merkle_block_handler = handler
        bn.chain_fetch_merkle_block_by_height(self._chain, height, self._fetch_merkle_block_converter)

    ##
    # Given a block hash, it retrieves the block's associated Merkle block. 
    # Args:
    #    hash (bytearray): 32 bytes of the block hash.
    #    handler (Callable (error, merkle_block, block_height)): Will be executed when the chain is queried.
    #        * error (int): Error code. 0 if successful.
    #        * merkle_block (MerkleBlock): The requested block's Merkle block.
    #        * block_height (unsigned int): The block's height in the chain.
    def fetch_merkle_block_by_hash(self, hash, handler):
        self._fetch_merkle_block_handler = handler
        bn.chain_fetch_merkle_block_by_hash(self._chain, hash, self._fetch_merkle_block_converter)

    def _fetch_transaction_converter(self, e, transaction, index, height):
        if e == 0: 
            _transaction = Transaction(transaction, True)
        else:
            _transaction = None

        self._fetch_transaction_handler(e, _transaction, index, height)

    ##
    # Get a transaction by its hash.
    # Args:
    #    hashn (bytearray): 32 bytes of the transaction hash.
    #    require_confirmed (int): If transaction should be in a block. 0 if not.
    #    handler (Callable (error, transaction, block_height, tx_index)): Will be executed when the chain is queried.
    #        * error (int): Error code. 0 if successful.
    #        * transaction (Transaction): Transaction found.
    #        * block_height (unsigned int): height in the chain of the block containing the transaction.
    #        * tx_index (unsigned int): index of the transaction inside the block (starting at zero).
    def fetch_transaction(self, hashn, require_confirmed,handler):
        self._fetch_transaction_handler = handler
        bn.chain_fetch_transaction(self._chain, hashn, require_confirmed, self._fetch_transaction_converter)


    # ----------------------------------------------------------------------------
    # Note: removed on 3.3.0

    # def _fetch_output_converter(self, e, output):
    #     if e == 0: 
    #         _output = Output(output)
    #     else:
    #         _output = None

    #     self._fetch_output_handler(e, _output)

    # ##
    # # Get a transaction output by its transaction hash and index inside the transaction.
    # # Args:
    # #    hashn (bytearray): 32 bytes of the transaction hash.
    # #    index (unsigned int): Output index inside the transaction (starting at zero).
    # #    require_confirmed (int): 1 if and only if transaction should be in a block, 0 otherwise.
    # #    handler (Callable (error, output)): Will be executed when the chain is queried.
    # #        * error (int): Error code. 0 if successful.
    # #        * output (Output): Output found.
    # def fetch_output(self, hashn, index, require_confirmed, handler):
    #     self._fetch_output_handler = handler
    #     bn.chain_fetch_output(self._chain, hashn, index, require_confirmed, self._fetch_output_converter)

    # ----------------------------------------------------------------------------

    ##
    # Given a transaction hash, it fetches the height and position inside the block.
    # Args:
    #    hash (bytearray): 32 bytes of the transaction hash.
    #    require_confirmed (int): 1 if and only if transaction should be in a block, 0 otherwise.
    #    handler (Callable (error, block_height, tx_index)): Will be executed after the chain is queried.
    #        * error (int): Error code. 0 if successful.
    #        * block_height (unsigned int): Height of the block containing the transaction.
    #        * tx_index (unsigned int): Transaction index inside the block (starting at zero).
    def fetch_transaction_position(self, hashn, require_confirmed, handler):
        bn.chain_fetch_transaction_position(self._chain, hashn, require_confirmed, handler)

    def _organize_block(self, block, handler):
        bn.chain_organize_block(self._chain, block, handler)

    def _organize_transaction(self, transaction, handler):
        bn.chain_organize_transaction(self._chain, transaction, handler)

    ##
    # Determine if a transaction is valid for submission to the blockchain.
    # Args:
    #    transaction (Transaction): transaction to be checked.
    #    handler (Callable (error, message)): Will be executed after the chain is queried.
    #        * error (int): error code. 0 if successful.
    #        * message (str): string describing the result of the query. Example: 'The transaction is valid'
    def validate_tx(self, transaction, handler):
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

    ##
    # Fetch the transaction input which spends the indicated output. The `fetch_spend_handler`
    # callback will be executed after querying the chain. 
    # Args:
    #    output_point (OutputPoint): tx hash and index pair.
    #    handler (Callable (error, input_point)): Will be executed when the chain is queried.
    #        * error (int): Error code. 0 if successful.
    #        * input_point (Point): Tx hash and index pair where the output was spent.
    def fetch_spend(self, output_point, handler):
        self._fetch_spend_handler = handler
        bn.chain_fetch_spend(self._chain, output_point._ptr, self._fetch_spend_converter)


    def _subscribe_blockchain_converter(self, e, fork_height, blocks_incoming, blocks_replaced):
        if self._executor.stopped or e == 1:
            return False

        if e == 0:
            _incoming = BlockList(blocks_incoming) if blocks_incoming else None
            _replaced = BlockList(blocks_replaced) if blocks_replaced else None
        else:
            _incoming = None
            _replaced = None
    
        return self._subscribe_blockchain_handler(e, fork_height, _incoming, _replaced)
    
    def subscribe_blockchain(self, handler):
        self._subscribe_blockchain_handler = handler
        bn.chain_subscribe_blockchain(self._executor._executor, self._chain, self._subscribe_blockchain_converter)

    def _subscribe_transaction_converter(self, e, tx):
        if self._executor.stopped or e == 1:
            return False

        if e == 0:
            _tx = Transacion(tx) if tx else None
        else:
            _tx = None
    
        self._subscribe_transaction_handler(e, _tx)
    
    def _subscribe_transaction(self, handler):
        self._subscribe_transaction_handler = handler
        bn.chain_subscribe_transaction(self._executor._executor, self._chain, self._subscribe_transaction_converter)


    def unsubscribe(self):
        bn.chain_unsubscribe(self._chain)

    ##
    # @var history_fetch_handler_
    # Internal callback which is called by the native fetch_history function and marshalls parameters to the managed callback

    ##
    # @var fetch_block_header_handler_
    # Internal callback which is called by the native fetch_block_header function and marshalls parameters to the managed callback

##
# Represents a binary filter
class Binary:

    def __init__(self, ptr):
        ##
        # @private
        self._ptr = ptr

    ##
    # Create an empty binary object
    # @return (Binary) New instance
    @classmethod
    def construct(self):
        return Binary(bn.binary_construct())


    ##
    # Creates a binary filter from a binary string
    # @param string_filter Binary string. Example: '10111010101011011111000000001101'
    # @return (Binary) Instance representing the given filter string
    @classmethod
    def construct_string(self, string_filter):
        return Binary(bn.binary_construct_string(string_filter))

    ##
    # Creates a binary filter from an int array
    # @param size (int) Filter length
    # @param blocks (int array) Filter representation. Example: '[186,173,240,13]'
    # @return (Binary) Instance representing the given filter
    @classmethod
    def construct_blocks(self, size, blocks):
        return Binary(bn.binary_construct_blocks(size, len(blocks), blocks))

    ##
    # Filter representation as uint array
    # @return (uint array)
    def blocks(self):
        return bn.binary_blocks(self._ptr)

    ##
    # Filter representation as binary string
    # @return (str)
    def encoded(self):
        return bn.binary_encoded(self._ptr)


# ------------------------------------------------------
##
#  Controls the execution of the Bitprim bitcoin node.
class Executor:

    ##
    # Node executor constructor.
    # @param path (string): Absolute path to node configuration file.
    # @param sout (file handle): File handle for redirecting standard output. If None, output goes to the a log file in the current directory.
    # @param serr (file handle): File handle for redirecting standard error output. If None, output goes to log file in the current directory. 
    def __init__(self, path, sout = None, serr = None):
        self._executor = bn.construct(path, sout, serr)
        self._constructed = True
        self._running = False

    def _destroy(self):
        if self._constructed:
            if self._running:
                self.stop()

            bn.destruct(self._executor)
            self._constructed = False

    def __del__(self):
        self._destroy()

    ##
    # Initializes blockchain local copy. 
    # @return (bool) true if and only if successful.
    def init_chain(self):
        return bn.initchain(self._executor) != 0

    ##
    # Starts running the node; blockchain starts synchronizing (downloading).
    # Returns right away (doesn't wait for init process to end)
    # @return (bool) true if and only if successful.
    def run(self):
        ret = bn.run(self._executor)

        if ret == 0:
            self._running = True

        return ret == 0
    
    ##
    # Starts running the node; blockchain start synchronizing (downloading).
    # Call blocks until init process is completed or fails.
    # @return (bool) true if and only if successful.
    def run_wait(self):
        ret = bn.run_wait(self._executor)

        if ret == 0:
            self._running = True

        return ret == 0

    ##
    # Stops the node; that includes all activies, such as synchronization
    # and networking
    # precondition: self._running.
    # @return (bool) true if and only if successful
    def stop(self):
        self._running = False
        self.chain.unsubscribe()
        time.sleep(0.5)
        ret = bn.stop(self._executor)
        return ret

    ##
    # To know if the node is stopped.
    # @return (bool) true if the node is stopped
    @property
    def stopped(self):
        return not self._running or bn.stopped(self._executor) != 0
    ##
    # Return the chain object representation
    # @return (Chain)
    @property
    def chain(self):
        return Chain(self, bn.get_chain(self._executor))

    ##
    # Return the p2p object representation
    # @return (P2p)
    @property
    def p2p(self):
        return P2p(self, bn.get_p2p(self._executor))


    ## 
    # Implements acquisition part of the RAII idiom (acquires the executor object)
    # @return (Executor) a newly acquired instance ready to use
    def __enter__(self):
        return self

    ## 
    # Implements the release part of the RAII idiom (releases the executor object)
    # @param exc_type Ignored
    # @param exc_value Ignored
    # @param traceback Ignored
    def __exit__(self, exc_type, exc_value, traceback):
        self._destroy()

# def main()

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
