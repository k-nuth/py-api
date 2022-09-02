# # Copyright (c) 2016-2022 Knuth Project developers.
# # Distributed under the MIT software license, see the accompanying
# # file COPYING or http://www.opensource.org/licenses/mit-license.php.

# import kth_native as nat
# import sys
# import time
# import kth


# # ------------------------------------------------------
# ##
# # Represents a Bitcoin block's header
# class Header:
#     def __init__(self, version, previousBlockHash, merkle, timestamp, bits, nonce):
#         self.version = version
#         self.previousBlockHash = previousBlockHash
#         self.merkle = merkle
#         self.timestamp = timestamp
#         self.bits = bits
#         self.nonce = nonce

#     def toNative(self):
#         native = kth.chain_header_construct(
#             this.version,
#             this.previousBlockHash,
#             this.merkle,
#             this.timestamp,
#             this.bits,
#             this.nonce
#         );
#         return native;


#     @staticmethod
#     def _destruct(native):
#         kth.chain_header_destruct(native);

#     def _destroy(self):
#         nat.header_destruct(self._ptr)

#     def __del__(self):
#         if self._auto_destroy:
#             self._destroy()

#     @staticmethod
#     def fromNative(native, destroy = False):
#         obj = Header(
#             nat.chain_header_version(native),
#             nat.chain_header_previous_block_hash(native),
#             nat.chain_header_merkle(native),
#             nat.chain_header_timestamp(native),
#             nat.chain_header_bits(native),
#             nat.chain_header_nonce(native)
#         )
#         if destroy:
#             Header._destruct(native)
#         return obj


#     ##
#     # Block height in the chain.
#     # @return (unsigned int)
#     @property
#     def height(self):
#         return self._height

#     ##
#     # Header protocol version
#     # @return (unsigned int)
#     @property
#     def version(self):
#         return nat.header_get_version(self._ptr)

#     ##
#     # Set version
#     # @param version New version value
#     @version.setter
#     def set_version(self, version):
#         nat.header_set_version(self._ptr, version)

#     ##
#     # 32 bytes hash of the previous block in the chain.
#     # @return (bytearray)
#     @property
#     def previous_block_hash(self):
#         return nat.header_get_previous_block_hash(self._ptr)

#     #def set_previous_block_hash(self,hash):
#         #return nat.header_set_previous_block_hash(self._ptr, hash)

#     ##
#     # Merkle root in 32 byte array format
#     # @return (bytearray)
#     @property
#     def merkle(self):
#         return nat.header_get_merkle(self._ptr)

#     #def set_merkle(self, merkle):
#         #nat.header_set_merkle(self._ptr, merkle)

#     ##
#     # Block hash in 32 byte array format
#     # @return (bytearray
#     @property
#     def hash(self):
#         return nat.header_get_hash(self._ptr)

#     ##
#     # Block timestamp in UNIX Epoch (seconds since January 1st 1970)
#     # Assume UTC 0
#     # @return (unsigned int)
#     @property
#     def timestamp(self):
#         return nat.header_get_timestamp(self._ptr)

#     ##
#     # Set header timestamp
#     # @param timestamp New header timestamp value
#     @timestamp.setter
#     def set_timestamp(self, timestamp):
#         nat.header_set_timestamp(self._ptr, timestamp)

#     ##
#     # Difficulty threshold
#     # @return (unsigned int)
#     @property
#     def bits(self):
#         return nat.header_get_bits(self._ptr)

#     ##
#     # Set header bits
#     # @param bits New header bits value
#     @bits.setter
#     def set_bits(self, bits):
#         nat.header_set_bits(self._ptr, bits)

#     ##
#     # The nonce that allowed this block to be added to the blockchain
#     # @return (unsigned int)
#     @property
#     def nonce(self):
#         return nat.header_get_nonce(self._ptr)

#     ##
#     # Set header nonce
#     # @param nonce New header nonce value
#     @nonce.setter
#     def set_nonce(self, nonce):
#         nat.header_set_nonce(self._ptr, nonce)


# # --------------------------------------------------------------------

# ##
# # Represent a full Bitcoin blockchain block
# class Block:
#     def __init__(self, pointer, height, auto_destroy = False):
#         ##
#         # @private
#         self._ptr = pointer
#         self._height = height
#         self._auto_destroy = auto_destroy

#     @staticmethod
#     def _destruct(native):
#         kth.chain_block_destruct(native);

#     def _destroy(self):
#         nat.block_destruct(self._ptr)

#     def __del__(self):
#         if self._auto_destroy:
#             self._destroy()

#     @staticmethod
#     def fromNative(native, destroy = False):
#         obj = Block(
#             kth.chain.Header.fromNative(nat.chain_block_header(native)),
#             kth.chain.TransactionList.fromNative(nat.chain_block_transactions(native))
#         )
#         if destroy:
#             Block._destruct(native)
#         return obj

#     @staticmethod
#     def fromData(version, data):
#         native = nat.chain_block_factory_from_data(version, data);
#         valid = nat.chain_block_is_valid(native);
#         if not valid:
#             Block._destruct(native);
#             return kth.result.Result(None, False);

#         obj = Block.fromNative(native);
#         Block._destruct(native);
#         return kth.result.Result(obj, True);

#     ##
#     # The block's height in the chain. It identifies it univocally
#     # @return (int)
#     @property
#     def height(self):
#         return self._height

#     ##
#     # The block's header
#     # @return (Header)
#     @property
#     def header(self):
#         return Header(nat.block_get_header(self._ptr), self._height, False)

#     ##
#     # The total amount of transactions that the block contains
#     # @return (unsigned int)
#     @property
#     def transaction_count(self):
#         return nat.block_transaction_count(self._ptr)

#     ##
#     # The block's hash as a 32 byte array
#     # @return (bytearray)
#     @property
#     def hash(self):
#         return nat.block_hash(self._ptr)

#     ##
#     # Block size in bytes.
#     # @return (int)
#     @property
#     def serialized_size(self):
#         return nat.block_serialized_size(self._ptr, 0)

#     ##
#     # Miner fees included in the block's coinbase transaction
#     # @return (unsigned int)
#     @property
#     def fees(self):
#         return nat.block_fees(self._ptr)

#     ##
#     # Sum of coinbase outputs
#     # @return (unsigned int)
#     @property
#     def claim(self):
#         return nat.block_claim(self._ptr)

#     ##
#     # Reward = Subsidy + Fees, for the block at the given height
#     # @param height (unsigned int) Block height in the chain. Identifies it univocally
#     # @return (unsigned int)
#     def reward(self, height):
#         return nat.block_reward(self._ptr, height)

#     ##
#     # The block's Merkle root, as a 32 byte array
#     # @return (byte array)
#     def generate_merkle_root(self):
#         return nat.block_generate_merkle_root(self._ptr)

#     ##
#     # Return 1 if and only if the block has transactions and a valid header, 0 otherwise
#     # @return (int) TODO Why not a bool?
#     def is_valid(self):
#         return nat.block_is_valid(self._ptr)


#     ##
#     # Given a position in the block, returns the corresponding transaction.
#     # @param n (unsigned int): Transaction index inside the block (starting at zero)
#     # @return (Transaction)
#     def transaction_nth(self, n):
#         return Transaction(nat.block_transaction_nth(self._ptr, n), False)

#     ##
#     # Amount of signature operations in the block. Returns max_int in case of overflow.
#     # @return (unsigned int)
#     def signature_operations(self):
#         return nat.block_signature_operations(self._ptr)

#     ##
#     # Amount of signature operations in the block. Returns max_int in case of overflow.
#     # @param bip16_active (int): should be '1' if and only if bip16 is activated at this point.
#     def signature_operations_bip16_active(self, bip16_active):
#         return nat.block_signature_operations_bip16_active(self._ptr, bip16_active)

#     ##
#     # Total amount of inputs in the block (consider all transactions).
#     # @param with_coinbase (int): should be '1' if and only if the block contains a coinbase transaction, '0' otherwise.
#     # @return (unsigned int)
#     def total_inputs(self, with_coinbase = 1):
#         return nat.block_total_inputs(self._ptr, with_coinbase)

#     ##
#     # Tell whether there is more than one coinbase transaction in the block
#     # @return (int) 1 if and only if there is another coinbase other than the first transaction, 0 otherwise.
#     def is_extra_coinbases(self):
#         return nat.block_is_extra_coinbases(self._ptr)

#     ##
#     # Tell whether every transaction in the block is final or not
#     # @param height (unsigned int): Block height in the chain. Identifies it univocally.
#     # @return (int) 1 if every transaction in the block is final, 0 otherwise.
#     def is_final(self, height, block_time):
#         return nat.block_is_final(self._ptr, height, block_time)

#     ##
#     # Tell whether all transactions in the block have a unique hash (i.e. no duplicates)
#     # @return (int): 1 if there are no two transactions with the same hash in the block, 0 otherwise
#     def is_distinct_transaction_set(self):
#         return nat.block_is_distinct_transaction_set(self._ptr)

#     ##
#     # Given a block height, tell if its coinbase claim is not higher than the deserved reward
#     # @param height (unsigned int): Block height in the chain. Identifies it univocally.
#     # @return (int) 1 if coinbase claim is not higher than the deserved reward.
#     def is_valid_coinbase_claim(self, height):
#         return nat.block_is_valid_coinbase_claim(self._ptr, height)

#     ##
#     # Returns 1 if and only if the coinbase script is valid
#     # @return (int)
#     def is_valid_coinbase_script(self, height):
#         return nat.block_is_valid_coinbase_script(self._ptr, height)

#     def _is_internal_double_spend(self):
#         return nat.block_is_internal_double_spend(self._ptr)

#     ##
#     # Tell if the generated Merkle root equals the header's Merkle root
#     # @return (int) 1 if and only if the generated Merkle root is equal to the Header's Merkle root
#     def is_valid_merkle_root(self):
#         return nat.block_is_valid_merkle_root(self._ptr)

# class BlockList:
#     def __init__(self, ptr):
#         self._ptr = ptr

#     def _destroy(self):
#         nat.block_list_destruct(self._ptr)

#     def __del__(self):
#         self._destroy()

#     @classmethod
#     def construct_default(self):
#         return BlockList(nat.block_list_construct_default())

#     def push_back(self, block):
#         nat.block_list_push_back(self._ptr, block._ptr)

#     @property
#     def count(self):
#         return nat.block_list_count(self._ptr)

#     def _nth(self, n):
#         return Block(nat.block_list_nth(self._ptr, n))

#     def __getitem__(self, key):
#         return self._nth(key)


# class TransactionList:
#     def __init__(self, ptr):
#         self._ptr = ptr

#     def _destroy(self):
#         nat.transaction_list_destruct(self._ptr)

#     def __del__(self):
#         self._destroy()

#     @classmethod
#     def construct_default(self):
#         return TransactionList(nat.transaction_list_construct_default())

#     def push_back(self, transaction):
#         nat.transaction_list_push_back(self._ptr, transaction._ptr)

#     @property
#     def count(self):
#         return nat.transaction_list_count(self._ptr)

#     def _nth(self, n):
#         return Transaction(nat.transaction_list_nth(self._ptr, n), False)

#     def __getitem__(self, key):
#         return self._nth(key)

# # ------------------------------------------------------

# class _CompactBlock:
#     def __init__(self, pointer):
#         self._ptr = pointer
#         self._constructed = True

#     def _destroy(self):
#         if self._constructed:
#             nat.compact_block_destruct(self._ptr)
#             self._constructed = False

#     def __del__(self):
#         self._destroy()

#     @property
#     def header(self):
#         return Header(nat.compact_block_get_header(self._ptr), False)

#     @property
#     def is_valid(self):
#         return nat.compact_block_is_valid(self._ptr)

#     @property
#     def serialized_size(self, version):
#         return nat.compact_block_serialized_size(self._ptr, version)

#     @property
#     def transaction_count(self):
#         return nat.compact_block_transaction_count(self._ptr)

#     def transaction_nth(self, n):
#         return nat.compact_block_transaction_nth(self._ptr, n)

#     @property
#     def nonce(self):
#         return nat.compact_block_nonce(self._ptr)

#     def reset(self):
#         return nat.merkle_block_reset(self._ptr)


# # ------------------------------------------------------

# ##
# # Merkle tree representation of a transaction block
# class MerkleBlock:
#     def __init__(self, pointer, height):
#         ##
#         # @private
#         self._ptr = pointer
#         self._height = height

#     ##
#     # Height of the block in the chain
#     # @return (unsigned int)
#     @property
#     def height(self):
#         return self._height

#     def _destroy(self):
#         nat.merkle_block_destruct(self._ptr)

#     def __del__(self):
#         self._destroy()

#     ##
#     # The block's header
#     # @return (Header)
#     @property
#     def header(self):
#         return Header(nat.merkle_block_get_header(self._ptr), self._height, False)

#     ##
#     # Returns true if and only if it the block contains txs hashes, and header is valid
#     # @return (int)
#     @property
#     def is_valid(self):
#         return nat.merkle_block_is_valid(self._ptr)

#     ##
#     # Transaction hashes list element count
#     # @return (unsigned int)
#     @property
#     def hash_count(self):
#         return nat.merkle_block_hash_count(self._ptr)

#     ##
#     # Block size in bytes.
#     # @param version (unsigned int): block protocol version.
#     # @return (unsigned int)
#     def serialized_size(self, version):
#         return nat.merkle_block_serialized_size(self._ptr, version)

#     ##
#     # Amount of transactions inside the block
#     # @return (unsigned int)
#     @property
#     def total_transaction_count(self):
#         return nat.merkle_block_total_transaction_count(self._ptr)

#     ##
#     # Delete all the data inside the block
#     def reset(self):
#         return nat.merkle_block_reset(self._ptr)

# ##
# # Compressed representation of Stealth payment related data
# class StealthCompact:
#     def __init__(self, ptr):
#         ##
#         # @private
#         self._ptr = ptr

#     ##
#     # Ephemeral public key hash in 32 byte array format. Does not
#     # include the sign byte (0x02)
#     # @return (byte array)
#     def ephemeral_public_key_hash(self):
#         return nat.stealth_compact_ephemeral_public_key_hash(self._ptr)

#     ##
#     # Transaction hash in 32 byte array format
#     # @return (byte array)
#     @property
#     def transaction_hash(self):
#         return nat.stealth_compact_get_transaction_hash(self._ptr)

#     ##
#     # Public key hash in 20 byte array format
#     # @return (byte array)
#     @property
#     def public_key_hash(self):
#         nat.stealth_compact_get_public_key_hash(self._ptr)

# class StealthCompactList:
#     def __init__(self, ptr):
#         self._ptr = ptr

#     def _destroy(self):
#         nat.stealth_compact_list_destruct(self._ptr)

#     def __del__(self):
#         self._destroy()

#     #@classmethod
#     #def construct_default(self):
#     #    return TransactionList(nat.transaction_list_construct_default())

#     #def push_back(self, transaction):
#     #    nat.transaction_list_push_back(self._ptr, transaction._ptr)

#     @property
#     def count(self):
#         return nat.stealth_compact_list_count(self._ptr)

#     def _nth(self, n):
#         return Stealth(nat.stealth_compact_list_nth(self._ptr, n))

#     def __getitem__(self, key):
#         return self._nth(key)


# # ------------------------------------------------------
# ##
# # Represents one of the tx inputs.
# # It's a transaction hash and index pair.
# class Point:
#     def __init__(self, ptr):
#         ##
#         # @private
#         self._ptr = ptr

#     ##
#     # Transaction hash in 32 byte array format
#     # @return (byte array)
#     @property
#     def hash(self):
#         return nat.point_get_hash(self._ptr) #[::-1].hex()

#     ##
#     # returns true if its not null.
#     #
#     #Returns:
#     #    bool
#     @property
#     def is_valid(self):
#         return nat.point_is_valid(self._ptr)

#     ##
#     # Input position in the transaction (starting at zero)
#     # @return (unsigned int)
#     @property
#     def index(self):
#         return nat.point_get_index(self._ptr)

#     ##
#     # This is used with output_point identification within a set of history rows
#     # of the same address. Collision will result in miscorrelation of points by
#     # client callers. This is NOT a bitcoin checksum.
#     # @return (unsigned int)
#     @property
#     def checksum(self):
#         return nat.point_get_checksum(self._ptr)


# ##
# # Transaction hash and index pair representing one of the transaction outputs
# class OutputPoint:
#     def __init__(self, ptr ):
#         ##
#         # @private
#         self._ptr = ptr

#     ##
#     # Transaction hash in 32 byte array format
#     # @return (bytearray)
#     @property
#     def hash(self):
#         return nat.output_point_get_hash(self._ptr)

#     def _destroy(self):
#         nat.output_point_destruct(self._ptr)

#     def __del__(self):
#         self._destroy()

#     ##
#     # Position of the output in the transaction (starting at zero)
#     # @return (unsigned int)
#     @property
#     def index(self):
#         return nat.output_point_get_index(self._ptr)

#     ##
#     # Creates an empty output point
#     # @return (OutputPoint)
#     @classmethod
#     def construct(self):
#         return OutputPoint(nat.output_point_construct())

#     ##
#     # Creates an OutputPoint from a transaction hash and index pair
#     # @param hashn (bytearray): Transaction hash in 32 byte array format
#     # @param index (unsigned int): position of the output in the transaction.
#     # @return (Outputpoint)
#     @classmethod
#     def construct_from_hash_index(self, hashn, index):
#         return OutputPoint(nat.output_point_construct_from_hash_index(hashn, index))

#     #def is_valid(self):
#     #    return nat.point_is_valid(self._ptr)

#     #def get_checksum(self):
#     #    return nat.point_get_checksum(self._ptr)

# # ------------------------------------------------------
# ##
# # Output points, values, and spends for a payment address
# class History:
#     def __init__(self, ptr):
#         ##
#         # @private
#         self._ptr = ptr

#     ##
#     # Used for differentiation.
#     #    '0' output
#     #    '1' spend
#     # @return (unsigned int)
#     @property
#     def point_kind(self):
#         return nat.history_compact_get_point_kind(self._ptr)

#     ##
#     # The point that identifies the History instance
#     # @return (Point)
#     @property
#     def point(self):
#         return Point(nat.history_compact_get_point(self._ptr))

#     ##
#     # Height of the block containing the Point
#     # @return (unsigned int)
#     @property
#     def height(self):
#         return nat.history_compact_get_height(self._ptr)

#     ##
#     #  Varies depending of point_kind.
#     #    value: if output, then satoshi value of output.
#     #    previous_checksum: if spend, then checksum hash of previous output_point.
#     # @return (unsigned int)
#     @property
#     def value_or_previous_checksum(self):
#         return nat.history_compact_get_value_or_previous_checksum(self._ptr)

# # ------------------------------------------------------
# class HistoryList:
#     def __init__(self, ptr):
#         self._ptr = ptr
#         self.constructed = True

#     def _destroy(self):
#         if self.constructed:
#             nat.history_compact_list_destruct(self._ptr)
#             self.constructed = False

#     def __del__(self):
#         self._destroy()

#     @property
#     def count(self):
#         return nat.history_compact_list_count(self._ptr)

#     def _nth(self, n):
#         return History(nat.history_compact_list_nth(self._ptr, n))

#     def __getitem__(self, key):
#         return self._nth(key)

#     # def __enter__(self):
#     #     return self

#     # def __exit__(self, exc_type, exc_value, traceback):
#     #     # print('__exit__')
#     #     self._destroy()

# # ------------------------------------------------------

# ##
# # Stealth payment related data
# class Stealth:
#     def __init__(self, ptr):
#         ##
#         # @private
#         self._ptr = ptr

#     ##
#     # 33 bytes. Includes the sign byte (0x02)
#     # @return (bytearray)
#     @property
#     def ephemeral_public_key_hash(self):
#         return nat.stealth_compact_get_ephemeral_public_key_hash(self._ptr)

#     ##
#     # Transaction hash in 32 bytes format
#     # @return (bytearray)
#     @property
#     def transaction_hash(self):
#         return nat.stealth_compact_get_transaction_hash(self._ptr)

#     ##
#     # Public key hash in 20 byte array format
#     # @return (bytearray)
#     @property
#     def public_key_hash(self):
#         return nat.stealth_compact_get_public_key_hash(self._ptr)

# # ------------------------------------------------------
# class StealthList:
#     def __init__(self, ptr):
#         self._ptr = ptr
#         self.constructed = True

#     def _destroy(self):
#         if self.constructed:
#             nat.stealth_compact_list_destruct(self._ptr)
#             self.constructed = False

#     def __del__(self):
#         self._destroy()

#     @property
#     def count(self):
#         return nat.stealth_compact_list_count(self._ptr)

#     def _nth(self, n):
#         return Stealth(nat.stealth_compact_list_nth(self._ptr, n))

#     def __getitem__(self, key):
#         return self._nth(key)

# # ------------------------------------------------------

# ##
# # Represents a Bitcoin Transaction
# class Transaction:
#     def __init__(self, ptr, auto_destroy = False):
#         ##
#         # @private
#         self._ptr = ptr
#         self._constructed = True
#         self._auto_destroy = auto_destroy

#     def _destroy(self):
#         if self._constructed:
#             nat.transaction_destruct(self._ptr)
#             self._constructed = False

#     def __del__(self):
#         if self._auto_destroy:
#             self._destroy()

#     ##
#     # Transaction protocol version
#     # @return (unsigned int)
#     @property
#     def version(self):
#         return nat.transaction_version(self._ptr)

#     ##
#     # Set new transaction version value
#     # @param version New transaction version value
#     @version.setter
#     def set_version(self, version):
#         return nat.transaction_set_version(self._ptr, version)

#     @property
#     def hash(self):
#         """bytearray: 32 bytes transaction hash."""
#         return nat.transaction_hash(self._ptr)

#     ##
#     # 32 bytes transaction hash + 4 bytes signature hash type
#     # @param sighash_type (unsigned int): signature hash type
#     # @return (byte array)
#     def hash_sighash_type(self, sighash_type):
#         return nat.transaction_hash_sighash_type(self._ptr, sighash_type)

#     ##
#     # Transaction locktime
#     # @return (unsigned int)
#     @property
#     def locktime(self):
#         return nat.transaction_locktime(self._ptr)

#     ##
#     # Transaction size in bytes.
#     # @param wire (bool): if true, size will include size of 'uint32' for storing spender
#     # output height
#     # @return (unsigned int)
#     def serialized_size(self, wire):
#         return nat.transaction_serialized_size(self._ptr, wire)

#     ##
#     # Fees to pay to the winning miner. Difference between sum of inputs and outputs
#     # @return (unsigned int)
#     @property
#     def fees(self):
#         return nat.transaction_fees(self._ptr)

#     ##
#     # Amount of signature operations in the transaction
#     # @return (unsigned int) max_int in case of overflow
#     def signature_operations(self):
#         return nat.transaction_signature_operations(self._ptr)

#     ##
#     # Amount of signature operations in the transaction.
#     # @param bip16_active (int): 1 if and only if bip 16 is active, 0 otherwise
#     # @return (unsigned int) max_int in case of overflow.
#     def signature_operations_bip16_active(self, bip16_active):
#         return nat.transaction_signature_operations_bip16_active(self._ptr, bip16_active)

#     ##
#     # Sum of every input value in the transaction
#     # @return (unsigned int) max_int in case of overflow
#     def total_input_value(self):
#         return nat.transaction_total_input_value(self._ptr)


#     ##
#     # Sum of every output value in the transaction.
#     # @return (unsigned int) max_int in case of overflow
#     def total_output_value(self):
#         return nat.transaction_total_output_value(self._ptr)

#     ##
#     # Return 1 if and only if transaction is coinbase, 0 otherwise
#     # @return (int)
#     def is_coinbase(self):
#         return nat.transaction_is_coinbase(self._ptr)

#     ##
#     # Return 1 if and only if the transaction is not coinbase
#     # and has a null previous output, 0 otherwise
#     # @return (int)
#     def is_null_non_coinbase(self):
#         return nat.transaction_is_null_non_coinbase(self._ptr)

#     ##
#     # Returns 1 if the transaction is coinbase and
#     # has an invalid script size on its first input
#     # @return (int)
#     def is_oversized_coinbase(self):
#         return nat.transaction_is_oversized_coinbase(self._ptr)

#     ##
#     # Returns 1 if and only if at least one of the inputs is
#     # not mature, 0 otherwise
#     # @return (int)
#     def is_mature(self, target_height):
#         return nat.transaction_is_mature(self._ptr, target_height)

#     ##
#     # Returns 1 if transaction is not a coinbase,
#     # and the sum of its outputs is higher than the sum of
#     # its inputs, 0 otherwise
#     # @return (int)
#     def is_overspent(self):
#         return nat.transaction_is_overspent(self._ptr)

#     ##
#     # Returns 1 if at least one of the previous outputs was
#     # already spent, 0 otherwise
#     # @return (int)
#     def is_double_spend(self, include_unconfirmed):
#         return nat.transaction_is_double_spend(self._ptr, include_unconfirmed)

#     ##
#     # Returns 1 if and only if at least one of the previous outputs
#     # is invalid, 0 otherwise
#     # @return (int)
#     def is_missing_previous_outputs(self):
#         return nat.transaction_is_missing_previous_outputs(self._ptr)

#     ##
#     # Returns 1 if and only if the transaction is final, 0 otherwise
#     # @return (int)
#     def is_final(self, block_height, block_time):
#         return nat.transaction_is_final(self._ptr, block_height, block_time)

#     ##
#     # Returns 1 if and only if the transaction is locked
#     # and every input is final, 0 otherwise
#     # @return (int)
#     def is_locktime_conflict(self):
#         return nat.transaction_is_locktime_conflict(self._ptr)

#     ##
#     # Returns a list with all of this transaction's outputs
#     # @return (OutputList)
#     def outputs(self):
#         return OutputList(nat.transaction_outputs(self._ptr))

#     ##
#     # Returns a list with all of this transaction's inputs
#     # @return (InputList)
#     def inputs(self):
#         return InputList(nat.transaction_inputs(self._ptr))

#     def to_data(self, wired):
#         return nat.transaction_to_data(self._ptr, wired)

# # ------------------------------------------------------
# ##
# # Represents a transaction script
# class Script:
#     def __init__(self, ptr, auto_destroy = False):
#         ##
#         # @private
#         self._ptr = ptr
#         self._constructed = True
#         self._auto_destroy = auto_destroy

#     def _destroy(self):
#         if self._constructed:
#             nat.script_destruct(self._ptr)
#             self._constructed = False

#     def __del__(self):
#         if self._auto_destroy:
#             self._destroy()

#     ##
#     # All script bytes are valid under some circumstance (e.g. coinbase).
#     # @return (int) 0 if and only if prefix and byte count do not match.
#     @property
#     def is_valid(self):
#         return nat.script_is_valid(self._ptr)

#     ##
#     # Script validity is independent of individual operation validity.
#     # Ops are considered invalid if there is a trailing invalid/default
#     # op or if a push op has a size mismatch
#     # @return (int)
#     @property
#     def is_valid_operations(self):
#         return nat.script_is_valid_operations(self._ptr)

#     ##
#     # Size in bytes
#     # @return (unsigned int)
#     @property
#     def satoshi_content_size(self):
#         return nat.script_satoshi_content_size(self._ptr)

#     ##
#     # Size in bytes. If prefix is 1 size, includes a var int size
#     # @param prefix (int): include prefix size in the final result
#     # @return (unsigned int)
#     def serialized_size(self, prefix):

#         return nat.script_serialized_size(self._ptr, prefix)

#     ##
#     # Translate operations in the script to string
#     # @param active_forks (unsigned int): Tells which rule is active
#     # @return (str)
#     def to_string(self, active_forks):
#         return nat.script_to_string(self._ptr, active_forks)

#     ##
#     # Amount of signature operations in the script
#     # @param embedded (bool): Tells whether this is an embedded script
#     # @return (unsigned int)
#     def sigops(self, embedded):
#         return nat.script_sigops(self._ptr, embedded)

#     ##
#     # Count the sigops in the embedded script using BIP16 rules
#     # @return (unsigned int)
#     def embedded_sigops(self, prevout_script):
#         return nat.script_embedded_sigops(self._ptr, prevout_script)

# # ------------------------------------------------------
# ##
# # Represents a Bitcoin wallet address
# class PaymentAddress:
#     def __init__(self, ptr = None):
#         ##
#         # @private
#         self._ptr = ptr
#         self._constructed = False
#         if ptr != None:
#             self._constructed = True

#     def _destroy(self):
#         if self._constructed:
#             nat.payment_address_destruct(self._ptr)
#             self._constructed = False

#     #def __del__(self):
#         #self._destroy()

#     ##
#     # Address in readable format (hex string)
#     # @return (str)
#     @property
#     def encoded(self):
#         if self._constructed:
#             return nat.payment_address_encoded(self._ptr)

#     ##
#     # Address version
#     # @return (unsigned int)
#     @property
#     def version(self):
#         if self._constructed:
#             return nat.payment_address_version(self._ptr)

#     ##
#     # Creates the Payment Address based on the received string.
#     # @param address (str) A base58 address. Example: '1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR'
#     @classmethod
#     def construct_from_string(self, address):
#         self._ptr = nat.payment_address_construct_from_string(address)
#         self._constructed = True

# # ------------------------------------------------------
# ##
# # Represents one of the outputs of a Transaction
# class Output:
#     def __init__(self, ptr):
#         ##
#         # @private
#         self._ptr = ptr
#         self._constructed = True

#     def _destroy(self):
#         if self._constructed:
#             #nat.output_destruct(self._ptr)
#             self._constructed = False

#     def __del__(self):
#         self._destroy()

#     ##
#     # Returns 0 if and only if output is not found
#     # @return (int)
#     @property
#     def is_valid(self):
#         return nat.output_is_valid(self._ptr)

#     ##
#     # Block size in bytes
#     # @param wire (bool): if true, size will include size of 'uint32' for storing spender height
#     # @return (unsigned int)
#     def serialized_size(self, wire):
#         return nat.output_serialized_size(self._ptr, wire)

#     ##
#     # Output value in Satoshis
#     # @return (unsigned int)
#     @property
#     def value(self):
#         return nat.output_value(self._ptr)

#     ##
#     # Amount of signature operations in script
#     # @return (unsigned int)
#     @property
#     def signature_operations(self):
#         return nat.output_signature_operations(self._ptr)

#     ##
#     # Script: returns the output script."""
#     @property
#     def script(self):
#         return Script(nat.output_script(self._ptr))

#     #def get_hash(self):
#     #    return nat.output_get_hash(self._ptr)

#     #def get_index(self):
#     #    return nat.output_get_index(self._ptr)

# ##
# # Represents one of the inputs of a Transaction
# class Input:
#     def __init__(self, ptr):
#         ##
#         # @private
#         self._ptr = ptr
#         self._constructed = True

#     def _destroy(self):
#         if self._constructed:
#             #nat.input_destruct(self._ptr)
#             self._constructed = False

#     def __del__(self):
#         self._destroy()

#     ##
#     # Returns 0 if and only if previous outputs or script are invalid
#     # @return (int)
#     @property
#     def is_valid(self):
#         return nat.input_is_valid(self._ptr)

#     ##
#     # Returns 1 if and only if sequence is equal to max_sequence.
#     # @return int
#     @property
#     def is_final(self):
#         return nat.input_is_final(self._ptr)

#     ##
#     # Size in bytes
#     # @return (unsigned int)
#     def serialized_size(self):
#         return nat.input_serialized_size(self._ptr, 0)

#     ##
#     # Sequence number of inputs. If it equals max_sequence, txs is final
#     # @return (unsigned int)
#     @property
#     def sequence(self):
#         return nat.input_sequence(self._ptr)

#     ##
#     # Total amount of sigops in the script.
#     # @param bip16_active (int): 1 if and only if bip 16 is active. 0 if not.
#     # @return (unsigned int)
#     @property
#     def signature_operations(self, bip16_active):
#         return nat.input_signature_operations(self._ptr, bip16_active)

#     ##
#     # The input's script
#     # @return (Script)
#     @property
#     def script(self):
#         return Script(nat.input_script(self._ptr))

#     ##
#     # Returns the previous output, with its transaction hash and index
#     # @return (OutputPoint)
#     @property
#     def previous_output(self):
#         return OutputPoint(nat.input_previus_output(self._ptr))

#     #def get_hash(self):
#     #    return nat.input_get_hash(self._ptr)

#     #def get_index(self):
#     #    return nat.input_get_index(self._ptr)

# class OutputList:
#     def __init__(self, ptr):
#         self._ptr = ptr

#     @property
#     def push_back(self, output):
#         nat.output_list_push_back(self._ptr, output._ptr)

#     @property
#     def count(self):
#         return nat.output_list_count(self._ptr)

#     def _nth(self, n):
#         return Output(nat.output_list_nth(self._ptr, n))

#     def __getitem__(self, key):
#         return self._nth(key)

# class InputList:
#     def __init__(self, ptr):
#         self._ptr = ptr

#     @property
#     def push_back(self, inputn):
#         nat.input_list_push_back(self._ptr, inputn._ptr)

#     @property
#     def count(self):
#         return nat.input_list_count(self._ptr)

#     def _nth(self, n):
#         return Input(nat.input_list_nth(self._ptr, n))

#     def __getitem__(self, key):
#         return self._nth(key)
