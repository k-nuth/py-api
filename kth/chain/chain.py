# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth_native as nat
import sys
import time
import asyncio
import kth

# def fetch_last_height_async(chain):
#     loop = asyncio.get_event_loop()
#     fut = loop.create_future()
#     nat.chain_fetch_last_height(chain, lambda err, h: fut.set_result((err, h)))
#     return fut

def generic_async_1(func, *args):
    loop = asyncio.get_event_loop()
    fut = loop.create_future()
    func(*args, lambda a: fut.set_result((a)))
    return fut

def generic_async_2(func, *args):
    loop = asyncio.get_event_loop()
    fut = loop.create_future()
    func(*args, lambda a, b: fut.set_result((a, b)))
    return fut

def generic_async_3(func, *args):
    loop = asyncio.get_event_loop()
    fut = loop.create_future()
    func(*args, lambda a, b, c: fut.set_result((a, b, c)))
    return fut

def generic_async_4(func, *args):
    loop = asyncio.get_event_loop()
    fut = loop.create_future()
    func(*args, lambda a, b, c, d: fut.set_result((a, b, c, d)))
    return fut


# async def generic_async_3(func, *args):
#     future = asyncio.Future()
#     loop = asyncio.get_event_loop()

#     def callback(args):
#         loop.call_soon_threadsafe(future.set_result, args)

#     func(*args, callback)

#     callback_args = await future
#     return callback_args


##
# Represents the Bitcoin blockchain.
class Chain:
    def __init__(self, executor, chain):
        ##
        # @private
        self._executor = executor
        self._chain = chain

    # Gets the height of the highest block in the local copy of the blockchain.
    # This number will grow as the node synchronizes with the blockchain.
    # This is an asynchronous method; a callback must be provided to receive the result
    async def getLastHeight(self):
        # ret = await fetch_last_height_async(self._chain)
        ret = await generic_async_2(nat.chain_fetch_last_height, self._chain)
        return ret

    # Given a block hash, it queries the chain for the block height.
    async def getBlockHeight(self, hash):
        # nat.chain_fetch_block_height(self._chain, hash, handler)
        ret = await generic_async_2(nat.chain_fetch_block_height, self._chain, hash)
        return ret

    # Get the block header from the specified height in the chain.
    async def getBlockHeaderByHeight(self, height):
        # nat.chain_fetch_block_header_by_height(self._chain, height, self._fetch_block_header_converter)
        (err, obj, height) = await generic_async_3(nat.chain_fetch_block_header_by_height, self._chain, height)
        if err != 0:
            return (err, None, height)
        return (err, kth.chain.Header.fromNative(obj), height)

    # Get the block header from the specified block hash.
    async def getBlockHeaderByHash(self, hash):
        # nat.chain_fetch_block_header_by_hash(self._chain, hash, self._fetch_block_header_converter)
        (err, obj, height) = await generic_async_3(nat.chain_fetch_block_header_by_hash, self._chain, hash)
        if err != 0:
            return (err, None, height)
        return (err, kth.chain.Header.fromNative(obj), height)

    # Gets a block from the specified height in the chain.
    async def getBlockByHeight(self, height):
        # nat.chain_fetch_block_by_height(self._chain, height, self._fetch_block_converter)
        (err, obj, height) = await generic_async_3(nat.chain_fetch_block_by_height, self._chain, height)
        if err != 0:
            return (err, None, height)
        return (err, kth.chain.Block.fromNative(obj), height)

    # Gets a block from the specified hash.
    async def getBlockByHash(self, hash):
        # nat.chain_fetch_block_by_hash(self._chain, hash, self._fetch_block_converter)
        (err, obj, height) = await generic_async_3(nat.chain_fetch_block_by_hash, self._chain, hash)
        if err != 0:
            return (err, None, height)
        return (err, kth.chain.Block.fromNative(obj), height)

    # Get a transaction by its hash.
    async def getTransaction(self, hash, require_confirmed):
        # nat.chain_fetch_transaction(self._chain, hash, require_confirmed, self._fetch_transaction_converter)
        (err, obj, index, height) = await generic_async_4(nat.chain_fetch_transaction, self._chain, hash, require_confirmed)
        if err != 0:
            return (err, None, index, height)
        return (err, kth.chain.Transaction.fromNative(obj), index, height)

    # Given a transaction hash, it fetches the height and position inside the block.
    async def getTransactionPosition(self, hash, require_confirmed):
        # nat.chain_fetch_transaction_position(self._chain, hash, require_confirmed, handler)
        ret = await generic_async_3(nat.chain_fetch_transaction_position, self._chain, hash, require_confirmed)
        return ret

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
        nat.chain_fetch_merkle_block_by_height(self._chain, height, self._fetch_merkle_block_converter)

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
        nat.chain_fetch_merkle_block_by_hash(self._chain, hash, self._fetch_merkle_block_converter)



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
    # #    hash (bytearray): 32 bytes of the transaction hash.
    # #    index (unsigned int): Output index inside the transaction (starting at zero).
    # #    require_confirmed (int): 1 if and only if transaction should be in a block, 0 otherwise.
    # #    handler (Callable (error, output)): Will be executed when the chain is queried.
    # #        * error (int): Error code. 0 if successful.
    # #        * output (Output): Output found.
    # def fetch_output(self, hash, index, require_confirmed, handler):
    #     self._fetch_output_handler = handler
    #     nat.chain_fetch_output(self._chain, hash, index, require_confirmed, self._fetch_output_converter)

    # ----------------------------------------------------------------------------

    async def organizeBlock(self, block):
        # void chain_organize_handler(kth_chain_t chain, void* ctx, kth_error_code_t error) {
        ret = await generic_async_1(nat.chain_organize_block, self._chain, block.toNative())
        return ret
        # nat.chain_organize_block(self._chain, block, handler)


    async def organizeTransaction(self, transaction):
        # nat.chain_organize_transaction(self._chain, transaction, handler)
        ret = await generic_async_1(nat.chain_organize_transaction, self._chain, transaction.toNative())
        return ret

    ##
    # Determine if a transaction is valid for submission to the blockchain.
    # Args:
    #    transaction (Transaction): transaction to be checked.
    #    handler (Callable (error, message)): Will be executed after the chain is queried.
    #        * error (int): error code. 0 if successful.
    #        * message (str): string describing the result of the query. Example: 'The transaction is valid'
    def validate_tx(self, transaction, handler):
        nat.chain_validate_tx(self._chain, transaction, handler)


    def _fetch_compact_block_converter(self, e, compact_block, height):
        if e == 0:
            _compact_block = _CompactBlock(compact_block)
        else:
            _compact_block = None

        self._fetch_compact_block_handler(e, _compact_block, height)

    def _fetch_compact_block_by_height(self, height, handler):
        self._fetch_compact_block_handler = handler
        nat.chain_fetch_compact_block_by_height(self._chain, height,  self._fetch_compact_block_converter)

    def _fetch_compact_block_by_hash(self, hash, handler):
        self._fetch_compact_block_handler = handler
        nat.chain_fetch_compact_block_by_hash(self._chain, hash, self._fetch_compact_block_converter)

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
        nat.chain_fetch_spend(self._chain, output_point._ptr, self._fetch_spend_converter)


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
        nat.chain_subscribe_blockchain(self._executor._executor, self._chain, self._subscribe_blockchain_converter)

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
        nat.chain_subscribe_transaction(self._executor._executor, self._chain, self._subscribe_transaction_converter)


    def unsubscribe(self):
        nat.chain_unsubscribe(self._chain)

    ##
    # @var history_fetch_handler_
    # Internal callback which is called by the native fetch_history function and marshalls parameters to the managed callback

    ##
    # @var fetch_block_header_handler_
    # Internal callback which is called by the native fetch_block_header function and marshalls parameters to the managed callback




# ----------------------------------------------------------------------
# TODO(fernando): implement the following
# ----------------------------------------------------------------------

#     ##
#     # Get a list of output points, values, and spends for a given payment address.
#     # This is an asynchronous method; a callback must be provided to receive the result
#     #
#     # Args:
#     #    address (PaymentAddress): Wallet to search.
#     #    limit (unsigned int): Max amount of results to fetch.
#     #    from_height (unsigned int): Starting height to search for transactions.
#     #    handler (Callable (error, list)): Will be executed when the chain is queried.
#     #        * error (int): Error code. 0 if and only if successful.
#     #        * list (HistoryList): A list with every element found.
#     def fetch_history(self, address, limit, from_height, handler):
#         self.history_fetch_handler_ = handler
#         nat.chain_fetch_history(self._chain, address, limit, from_height, self._history_fetch_handler_converter)

#     def _history_fetch_handler_converter(self, e, l):
#         if e == 0:
#             list = HistoryList(l)
#         else:
#             list = None

#         self.history_fetch_handler_(e, list)

# ##### Stealth
#     def _stealth_fetch_handler_converter(self, e, l):
#         if e == 0:
#             _list = StealthList(l)
#         else:
#             _list = None

#         self._stealth_fetch_handler(e, _list)

#     ##
#     # Get metadata on potential payment transactions by stealth filter.
#     # Given a filter and a height in the chain, it queries the chain for transactions matching the given filter.
#     # Args:
#     #    binary_filter_str (string): Must be at least 8 bits in length. example "10101010"
#     #    from_height (unsigned int): Starting height in the chain to search for transactions.
#     #    handler (Callable (error, list)): Will be executed when the chain is queried.
#     #        * error (int): Error code. 0 if and only if successful.
#     #        * list (StealthList): list with every transaction matching the given filter.
#     def fetch_stealth(self, binary_filter_str, from_height, handler):
#         self._stealth_fetch_handler = handler
#         binary_filter = Binary.construct_string(binary_filter_str)
#         nat.chain_fetch_stealth(self._chain, binary_filter._ptr, from_height, self._stealth_fetch_handler_converter)
