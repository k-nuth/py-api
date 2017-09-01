# class bitprim.Binary(ptr)
Represents a binary filter.

##### blocks()
Array [unsigned int]: returns the filter as an array of uint.

##### classmethod construct()
Binary: create an empty binary object.

##### classmethod construct_blocks(size, blocks)
Binary: construct binary filter from an array of int.

###### Parameters:  
- size (unsigned int) – lenght of the filter.
- blocks (array[unsigned int]) – Every int represents a byte of the filter. Example: ‘[186,173,240,13]’

##### classmethod construct_string(string_filter)
Binary: construct a binary filter form string.

###### Parameters:  
- string_filter (str) – binary string. Example: ‘10111010101011011111000000001101’

##### encoded()
str: returns the filter in a binary string.

# class bitprim.Block(pointer, height)
Represent a full Bitcoin block.

##### claim
unsigned int – value of the outputs in the coinbase.

##### fees
unsigned int – amount of fees included in coinbase.

##### generate_merkle_root()
bytearray: 32 bytes of the merkle root, for the generated merkle tree.

##### hash
bytearray – 32 bytes of the block hash.

##### header
Header – block header object.

##### height
unsigned int – Height of the block in the chain.

##### is_distinct_transaction_set()
int: returns ‘1’ if there are not two transactions with the same hash.

##### is_extra_coinbases()
int: returns ‘1’ if there is another coinbase other than the first transaction.

##### is_final(height)
int: returns ‘1’ if every transaction in the block is final.

###### Parameters:  
- height (unsigned int) – height of the block in the chain.

##### is_valid()
int: block has transactions and a valid Header. 1 if its valid.

##### is_valid_coinbase_claim(height)
int: returns ‘1’ if coinbase claim is not higher than the deserved reward.

###### Parameters:  
- height (unsigned int) – height of the block in the chain.

##### is_valid_coinbase_script(height)
int: returns ‘1’ if coinbase script is valid.

##### is_valid_merkle_root()
int: returns ‘1’ if the generated merkle root is equal to the Header merkle root.

##### reward(height)
unsigned int: value of the fees plus the reward for a block at the given height.

###### Parameters:  
- height (unsigned int) – height of the block in the chain.

##### serialized_size
unsigned int – size of the block in bytes.

##### signature_operations()
unsigned int: amount of signature operations in the block. Returns max_int in case of overflow.

##### signature_operations_bip16_active(bip16_active)
unsigned int: amount of signature operations in the block. Returns max_int in case of overflow.

###### Parameters:  
- bip16_active (int) – if bip16 is activated at this point. Should be ‘1’ if its active.

##### total_inputs(with_coinbase=1)
unsigned int: amount of inputs in every transaction in the block.

###### Parameters:  
- with_coinbase (int) – should be ‘1’ if block contains a coinbase transaction. ‘0’ otherwise.

##### transaction_count
unsigned int – amount of transaction in the block.

##### transaction_nth(n)
Transaction: given a position in the block, returns the corresponding transaction.

###### Parameters:  
- n (unsigned int) – index of the transaction in the block.

# class bitprim.Chain(chain)
Represents the Bitcoin blockchain.

##### fetch_block_by_hash(hash, handler)
Gets a block from the specified hash.

###### Parameters:  
- hash (bytearray) – 32 bytes of the block hash.
- handler (Callable (error, block)) –  Will be executed after the chain is queued.
    - error (int): error code. 0 if successfull.
    - block (Block): block found with the specified hash.

##### fetch_block_by_height(height, handler)
Gets a block from the specified height in the chain.

###### Parameters:  
- height (unsigned int) – block height in the chain.
- handler (Callable (error, block)) – Will be executed after the chain is cued.
    - error (int): error code. 0 if successfull.
    - block (Block): block at the defined height in the chain.

##### fetch_block_header_by_hash(hash, handler)
Get the block header from the specified block hash.

###### Parameters:  
- hash (bytearray) – 32 bytes of the block hash.
- handler (Callable (error, block_header)) – Will be executed after the chain is cued.
    - error (int): error code. 0 if successfull.
    - block_header (Header): header of the block found.

##### fetch_block_header_by_height(height, handler)
Get the block header from the specified height in the chain.

###### Parameters:  
- height (unsigned int) – block height in the chain.
- handler (Callable (error, block_header)) – Will be executed after the chain is cued.
    - error (int): error code. 0 if successfull.
    - block_header (Header): header of the block found.

##### fetch_block_height(hash, handler)
Given a block hash, it cues the chain for the block height.

###### Parameters:  
- hash (bytearray) – 32 bytes of the block hash.
- handler (Callable (error, block_height)) – Will be executed after the chain is cued.
    - error (int): error code. 0 if successfull.
    - block_height (unsigned int): height of the block in the chain.

##### fetch_history(address, limit, from_height, handler)
Get list of output points, values, and spends for a payment address.

###### Parameters:  
- address (PaymentAddress) – wallet to search.
- limit (unsigned int) – max amount of results to fetch.
- from_height (unsigned int) – minimum height to search for transactions.
- handler (Callable (error, list)) – Will be executed when the chain is cued.
    - error (int): error code. 0 if successfull.
    - list (HistoryList): list with every element found.

##### fetch_last_height(handler)
Gets the height of the highest block in the chain.

###### Parameters:  
- handler (Callable (error, block_height)) – Will be executed when the chain is cued.
    - error (int): error code. 0 if successfull.
    - block_height (unsigned int): height of the highest block in the chain.

##### fetch_merkle_block_by_hash(hash, handler)
Given a block hash, it retrieves a merkle block.

###### Parameters:  
- hash (bytearray) – 32 bytes of the block hash.
- handler (Callable (error, merkle_block, block_height)) – Will be executed when the chain is cued.
    - error (int): error code. 0 if successfull.
    - merkle_block (MerkleBlock): merkle block of the block found with the given hash.
    - block_height (unsigned int): height of the block in the chain.

##### fetch_merkle_block_by_height(height, handler)
Given a block height in the chain, it retrieves a merkle block.

###### Parameters:  
- height (unsigned int) – block height in the chain.
- handler (Callable (error, merkle_block, block_height)) – Will be executed when the chain is cued.
    - error (int): error code. 0 if successfull.
    - merkle_block (MerkleBlock): merkle block of the block found at the specified height.
    - block_height (unsigned int): height of the block in the chain.

##### fetch_output(hashn, index, require_confirmed, handler)
Get a transaction output by its transaction hash and index inside the transaction.

###### Parameters:  
- hashn (bytearray) – 32 bytes of the transaction hash.
- index (unsigned int) – index of the output in the transaction.
- require_confirmed (int) – if transaction should be in a block. 0 if not.
- handler (Callable (error, output)) – Will be executed when the chain is cued.
    - error (int): error code. 0 if successfull.
    - output (Output): output found.

##### fetch_spend(output_point, handler)
Fetch the transaction input which spends the indicated output. The fetch_spend_handler will be executed after cueing the chain.

###### Parameters:  
- output_point (OutputPoint) – tx hash and index pair.
- handler (Callable (error, input_point)) – Will be executed when the chain is cued.
    - error (int): error code. 0 if successfull.
    - input_point (Point): Tx hash nad index pair where the output was spent.

##### fetch_stealth(binary_filter_str, from_height, handler)
Get metadata on potential payment transactions by stealth filter. Given a filter and a height in the chain it cues the chain for transactions matching the provided filter.

###### Parameters:  
- binary_filter_str (string) – Must be at least 8 bits in lenght. example “10101010”
- from_height (unsigned int) – minimum height in the chain where to look for transactions.
- handler (Callable (error, list)) – Will be executed after the chain is cued.
    - error (int): error code. 0 if successfull.
    - list (StealthList): list with every transaction matching the given filter.

##### fetch_transaction(hashn, require_confirmed, handler)
Get a transaction by its hash.

###### Parameters:  
- hashn (bytearray) – 32 bytes of the transaction hash.
- require_confirmed (int) – if transaction should be in a block. 0 if not.
- handler (Callable (error, transaction, block_height, tx_index)) – Will be executed when the chain is cued.
    - error (int): error code. 0 if successfull.
    - transaction (Transaction): Transaction found.
    - block_height (unsigned int): height in the chain of the block containing the transaction.
    - tx_index (unsigned int): index of the transaction inside the block.

##### fetch_transaction_position(hashn, require_confirmed, handler)
Given a transaction hash it fetches the height and position inside the block.

###### Parameters:  
- hash (bytearray) – 32 bytes of the transaction hash.
- require_confirmed (int) – if transaction should be in a block. 0 if not.
- handler (Callable (error, block_height, tx_index)) – Will be executed after the chain is cued.
    - error (int): error code. 0 if successfull.
    - block_height (unsigned int): height of the block containing the transaction.
    - tx_index (unsigned int): index in the block of the transaction.

##### validate_tx(transaction, handler)
Determine if a transaction is valid for submission to the blockchain.

###### Parameters:  
- transaction (Transaction) – transaction to be checked.
- handler (Callable (error, message)) – Will be executed after the chain is cued.  
    - error (int): error code. 0 if successfull.  
    - message (str): string describing the result of the cue. example: “The transaction is valid”

# class bitprim.Executor(path, sout=None, serr=None)
Controls the execution of the Bitprim bitcoin node.

##### chain
Chain – Object containing the blockchain.

##### init_chain()
bool: Initialization of the blockchain. Returns ‘TRUE’ if successfull.

##### run()
bool: Starts running the node, initializing blockchain download. Returns ‘TRUE’ if successful.

##### run_wait()
bool: Starts running the node, initializing blockchain download. It listen to wait signals. Returns ‘TRUE’ if successful.

##### stop()
bool: it stops the node. precondition: self._running. Returns ‘TRUE’ if successfull

# class bitprim.Header(pointer, height, auto_destroy=False)
Represents the Header of a Bitcoin Block.

##### bits
unsigned int – value of bits. Difficulty threshold.

##### hash
bytearray – 32 bytes block hash.

##### height
unsigned int – Height of the block in the chain.

##### merkle
bytearray – 32 bytes merkle root.

##### nonce
unsigned int – the nonce that allowed this block to added to the blockchain.

##### previous_block_hash
bytearray – 32 bytes hash of the previous block in the chain.

##### set_bits
unsigned int – value of bits. Difficulty threshold.

##### set_nonce
unsigned int – the nonce that allowed this block to added to the blockchain.

##### set_timestamp
unsigned int – block timestamp.

##### set_version
unsigned int – protocol version of the header.

##### timestamp
unsigned int – block timestamp.

##### version
unsigned int – protocol version of the header.

# class bitprim.History(ptr)
Output points, values, and spends for a payment address

##### height
unsigned int – Height of the block containing the Point.

##### point
Point – point that identifies History.

##### point_kind
unsigned int – Used for differentiation. ‘0’ output ‘1’ spend

##### value_or_previous_checksum
unsigned int – varies depending of point_kind.

value: if output, then satoshi value of output. 
previous_checksum: if spend, then checksum hash of previous output_point.

# class bitprim.Input
Represents one of the inputs of a Transaction.

##### is_final
int: returns ‘1’ if sequence is equal to max_sequence.

##### is_valid
int: returns ‘0’ if previous outputs or script are invalid.

##### previous_output
OutputPoint: returns previous output, with transaction hash and index.

##### script
Script: script object.

##### sequence
unsigned int: sequence number of inputs. if it equals max_sequence, txs is final.

##### serialized_size()
unsigned int: size in bytes.

##### signature_operations(bip16_active)
unsigned int: amount of sigops in the script.

###### Parameters
- bip16_active(int): ‘1’ if bip 16 is active. ‘0’ if not.

# class bitprim.MerkleBlock(ptr, height)

##### hash_count
unsigned int: size of the transaction hashes list.

##### header
Header: header of the block.

##### height
unsigned int: Height of the block in the chain.

##### is_valid
int: returns true if it cointains txs hashes, and header is valid.

##### reset()
void: delete all the data inside the block.

##### serialized_size(version)
unsigned int: size of the block in bytes.

###### Parameters:
 - version (unsigned int): block protocol version.

##### total_transaction_count
unsigned int: transactions included in the block.

# class bitprim.Output(ptr)
Represents one of the outputs of a Transaction.

##### is_valid
int: returns ‘0’ if output is not found.

##### script
Script: returns the output script.

##### serialized_size(wire)
unsigned int: size in bytes.

###### Parameters
- wire (bool): if ‘TRUE’ size will include size of ‘uint32’ for storing spender height.

##### signature_operations
unsigned int: amount of signature operations in script.

##### value
unsigned int: returns output value.

# class bitprim.OutputPoint(ptr)
Transaction hash and index representing one of the transaction outputs.

##### construct()
OutputPoint: creates an empty output point.

##### construct_from_hash_index(hashn, index)
Outputpoint: creates an OutputPoint from a transaction hash and index pair.

###### Parameters:
- hashn (bytearray): 32 bytes of the transaction hash.
- index (unsigned int): position of the output in the transaction.

##### hash
bytearray: 32 bytes of the transaction hash.

##### index
unsigned int: position of the output in the transaction.

# class bitprim.PaymentAddress(ptr=None)
Represents a Bitcoin wallet address.

##### construct_from_string(address)
PaymentAddress: Creates the Payment Address based on the received string.

###### Parameters
- address: a base58 address. example ‘1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR’

##### encoded
str: readable format of the address.

##### version
unsigned int: address version.

# class Point(ptr)
Represents one of the txs input.
It’s a pair of transaction hash and index.

##### checksum
unsigned int: This is used with output_point identification within a set of history rows
of the same address. Collision will result in miscorrelation of points by
client callers. This is NOT a bitcoin checksum.

##### hash
bytearray(32): Hash of the transaction.

##### index
unsigned int: Position of the Input in the transaction.

##### is_valid
bool: returns true if its not null.

# class Script(ptr, auto_destroy=False)
Represents transaction scripts.

##### embedded_sigops(prevout_script)
unsigned int: Count the sigops in the embedded script using BIP16 rules.

###### Parameters
- prevout_script(Script): Script from the previous transaction.

##### is_valid
int: All script bytes are valid under some circumstance (e.g. coinbase).
Returns ‘0’ if a prefix and byte count does not match.

##### is_valid_operations
int: Script validity is independent of individual operation validity.
There is a trailing invalid/default op if a push op had a size mismatch.

##### satoshi_content_size
unsigned int: size in bytes.

##### serialized_size(prefix)
unsigned int: size in bytes. If prefix ‘1’ size includes a var int size.

###### Parameters
- prefix (bool): include prefix size in the final result.

##### sigops(embedded)
unsigned int: amount of signature operations in the script.

###### Parameters
- embedded (bool): is embedded script.

##### to_string(active_forks)
str: translate operations in the script to string.

###### Parameters
- active_forks (unsigned int): which rule is active.

# class bitprim.Stealth(ptr)

##### ephemeral_public_key_hash
bytearray: 33 bytes. Includes  the sign byte (0x02)

##### public_key_hash
bytearray: 20 bytes.

##### transaction_hash
bytearray: 32 bytes.

# class StealthCompact

##### ephemeral_public_key_hash
bytearray: 32 bytes. Excludes the sign byte (0x02)

##### public_key_hash
bytearray: 20 bytes.

##### transaction_hash
bytearray: 32 bytes.

# class bitprim.Transaction(ptr)
Represents a Bitcoin Transaction.

##### fees
unsigned int: fees to pay. Difference between input and output value.

##### hash
bytearray: 32 bytes transaction hash.

##### hash_sighash_type(sighash_type)
bytearray: 32 bytes transaction hash.

###### Parameters
- sighash_type (unsigned int): signature hash type.

##### inputs()
InputList: returns a list with every transaction input.

##### is_coinbase
int: return ‘1’ if transaction is coinbase.

##### is_double_spend(include_unconfirmed)
int: returns ‘1’ if at least one of the previous outputs was already spent.

##### is_final(block_height, block_time)
int: returns ‘1’ if transaction is final.

##### is_immature()
int: returns ‘1’ if at least one of the inputs is not mature.

##### is_locktime_conflict()
int: returns ‘1’ if its locked, but every input is final.

##### is_missing_previous_outputs()
int: returns ‘1’ if at least one of the previous outputs is invalid.

##### is_null_non_coinbase()
int: return ‘1’ if is not coinbase, but has null previous output.

##### is_oversized_coinbase()
int: returns ‘1’ if coinbase has invalid script size on first input.

##### is_overspent()
int: returns ‘1’ if it is not a coinbase, and outputs value is higher than its inputs.

##### locktime()
unsigned int: transaction locktime.

##### outputs()
OutputList: returns a list with every transaction output.

##### serialized_size(wire)
unsigned int: size of the transaction in bytes.

###### Parameters
- wire (bool): if ‘TRUE’ size will include size of ‘uint32’ for storing spender height of output.

##### set_version
unsigned int – Transaction protocol version.

##### signature_operations()
unsigned int: amount of signature operations in the transaction.
Returns max int in case of overflow.

##### signature_operations_bip16_active(bip16_active)
unsigned int: amount of signature operations in the transaction.
Returns max int in case of overflow.

###### Parameters
- bip16_active (int): ‘1’ if bip 16 is active. ‘0’ if not.

##### total_input_value()
unsigned int: sum of every input value in the transaction.
Returns max int in case of overflow.

##### total_output_value()
unsigned int: sum of every output value in the transaction.
return max int in case of overflow.

##### version
unsigned int: Transaction protocol version.

# class bitprim.Wallet
Wallet handling utilities

##### mnemonics_to_seed(string[])
byte array: Converts a list of mnemonic words to an HD wallet seed.

###### Parameters
- mnemonic list: List of mnemonic words.

# Global functions
Inside bitprim namespace.

##### bitprim.decode_hash(hash_str)
bytearray: Converts a hex string into a workable format.

###### Parameters
- hash_str (str): hex string representing hash. example “000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f”

##### bitprim.encode_hash(hash)
str: Converts a bytearray into a readable format.
example return: “000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f”

###### Parameters
- hash (bytearray): bytes of the hash.
