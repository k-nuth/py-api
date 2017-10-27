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

import bitprim
import bitprim_native
import os
import signal
import sys
import time

# ------------------------------------------------------
# 
# ------------------------------------------------------
def signal_handler(signal, frame):
    # signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGTERM, signal_handler)
    print('You pressed Ctrl-C')

    # time.sleep(2)

    # print('before unsubscribe()')
    # execut.chain.unsubscribe()
    # print('after unsubscribe()')

    # time.sleep(0.5)

    print('before execut.stop() - 1')
    execut.stop()
    print('after execut.stop() - 1')
    # sys.exit(0)

def history_fetch_handler(e, l): 
    count = l.count()
    print('history_fetch_handler count: {0:d}'.format(count))

    for n in range(count):
        h = l.nth(n)
        # print(h)
        print(h.point_kind)
        print(h.height)
        print(h.value_or_spend)

        # print(h.point)
        print(h.point.hash)
        print(h.point.is_valid)
        print(h.point.index)
        print(h.point.get_checksum)

def block_header_handler(e, header): 
    print('block_header_handler -- start')

    if (e != 0):
        print('block_header_handler - error: {0:d}'.format(e))
        return

    hash = header.previous_block_hash
    # print(hash)
    hash_hex = bitprim.encode_hash(hash)
    print(hash_hex)



def last_height_fetch_handler(e, h): 
    if (e != 0):
        print('last_height_fetch_handler - error: {0:d}'.format(e))
        return

    print('Last Height is: {0:d}'.format(h))
    
    if h >= 1:
        execut.chain.fetch_block_header_by_height(1, block_header_handler)


    # if h >= 262421:
    # 	e.fetch_history('1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR', 0, 0, history_fetch_handler) # Juan


# -------------------------------------------------------------------------------------------

# service_stopped = 1,

# // A typical reorganization consists of one incoming and zero outgoing blocks.
# bool full_node::handle_reorganized(code ec, size_t fork_height,
#     block_const_ptr_list_const_ptr incoming,
#     block_const_ptr_list_const_ptr outgoing)
# {
#     if (stopped() || ec == error::service_stopped)
#         return false;

#     if (ec)
#     {
#         LOG_ERROR(LOG_NODE)
#             << "Failure handling reorganization: " << ec.message();
#         stop();
#         return false;
#     }

#     // Nothing to do here.
#     if (!incoming || incoming->empty())
#         return true;

#     for (const auto block: *outgoing)
#         LOG_DEBUG(LOG_NODE)
#             << "Reorganization moved block to orphan pool ["
#             << encode_hash(block->header().hash()) << "]";

#     const auto height = safe_add(fork_height, incoming->size());

#     set_top_block({ incoming->back()->hash(), height });
#     return true;
# }

# -------------------------------------------------------------------------------------------


# def subscribe_blockchain_handler(e, fork_height, incoming, replaced): 
#     if (e != 0):
#         print('subscribe_blockchain_handler - error: {0:d}'.format(e))
#         return True

#     # print('subscribe_blockchain_handler - incoming.count: {0:d}'.format(incoming.count))
#     # for b in incoming:
#     #     b.

#     if incoming.count > 0:
#         if incoming[0].height % 1000 == 0:
#             print('subscribe_blockchain_handler - incoming[0].height: {0:d}'.format(incoming[0].height))

#     return True


# A typical reorganization consists of one incoming and zero outgoing blocks.
def subscribe_blockchain_handler(ec, fork_height, incoming, outgoing):

    # if incoming:
    #     print('subscribe_blockchain_handler - incoming.count: {0:d}'.format(incoming.count))
    # else:
    #     print('subscribe_blockchain_handler - incoming.count: NONE')

    # if outgoing:
    #     print('subscribe_blockchain_handler - outgoing.count: {0:d}'.format(outgoing.count))
    # else:
    #     print('subscribe_blockchain_handler - outgoing.count: NONE')

    # if ec == 0 and fork_height == 0:
    #     print('ec == 0 and fork_height == 0')
    #     print(incoming)
    #     print(outgoing)
    #     time.sleep(5)


    service_stopped = 1
    # print('PYTHON subscribe_blockchain_handler - 1')
    # print('PYTHON execut.stopped: ')
    # print(execut.stopped)
    # print(ec)

    if execut.stopped or ec == service_stopped:
        print(execut.stopped)
        print(ec)
        return False

    # if ec == 0 and fork_height == 0 and not incoming and not outgoing:
    #     print('-- UNSUBSCRIBE SIGNAL --')
    #     print(ec)
    #     print(fork_height)
    #     print(incoming)
    #     print(outgoing)
    #     return False


    # print('PYTHON subscribe_blockchain_handler - 2')

    if ec != 0:
        # LOG_ERROR(LOG_NODE) << "Failure handling reorganization: " << ec.message();
        print("Failure handling reorganization: ")
        print(ec)
        execut.stop()
        return False

    # print(incoming)
    #  Nothing to do here.
    if not incoming or incoming.count == 0:
        return True

    # for block in outgoing:
    #     LOG_DEBUG(LOG_NODE << "Reorganization moved block to orphan pool [" << encode_hash(block->header().hash()) << "]"

    # height = safe_add(fork_height, incoming->size())
    # set_top_block({ incoming->back()->hash(), height });



    # if incoming.count > 0:
    #     print('subscribe_blockchain_handler - incoming.count: {0:d}'.format(incoming.count))



    return True



# # ------------------------------------------------------
# # Main Real
# # ------------------------------------------------------

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as execut:
# with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as execut:


    if not os.path.isdir("./blockchain"):
        res = execut.init_chain()
        print(res)

    res = execut.run_wait()
    print(res)

    # print('before subscribe_blockchain')
    execut.chain.subscribe_blockchain(subscribe_blockchain_handler)
    # print('after subscribe_blockchain')

    loops = 0
    while not execut.stopped:
        # execut.chain.fetch_last_height(last_height_fetch_handler)

        # loops = loops + 1
        # if loops == 3:
        #     print('before unsubscribe()')
        #     execut.chain.unsubscribe()
        #     print('after unsubscribe()')

        # if loops >= 6:
        #     # print('before execut.stop() - 2 - *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        #     # execut.stop()
        #     # print('after execut.stop() - 2 - *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        #     break



        time.sleep(5)


    # print('exiting... wait 10s')
    # time.sleep(10)
    # print('before unsubscribe()')
    # execut.chain.unsubscribe()
    # print('after unsubscribe()')
    # print('exiting... wait 10s')
    # time.sleep(10)
    # print('exiting...')












#     # e.chain.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
#     # e.chain.fetch_history('1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR', 0, 0, history_fetch_handler) # Juan


# import numpy as np

# # ------------------------------------------------------
# # mnemonics_to_seed example
# # ------------------------------------------------------
# # https://github.com/libbitcoin/libbitcoin-explorer/wiki/bx-mnemonic-to-seed

# mnemonics = ['rival', 'hurdle', 'address', 'inspire', 'tenant', 'almost', 'turkey', 'safe', 'asset', 'step', 'lab', 'boy']
# w = bitprim.Wallet()
# seed = w.mnemonics_to_seed(mnemonics)
# print(seed)
