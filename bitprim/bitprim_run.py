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
import os
import signal
import sys
import time

import numpy as np

# # ------------------------------------------------------
# # mnemonics_to_seed example
# # ------------------------------------------------------
# # https://github.com/libbitcoin/libbitcoin-explorer/wiki/bx-mnemonic-to-seed

# mnemonics = ['rival', 'hurdle', 'address', 'inspire', 'tenant', 'almost', 'turkey', 'safe', 'asset', 'step', 'lab', 'boy']
# w = bitprim.Wallet()
# seed = w.mnemonics_to_seed(mnemonics)
# print(seed)


# ------------------------------------------------------
# 
# ------------------------------------------------------
def signal_handler(signal, frame):
    # signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGTERM, signal_handler)
    print('You pressed Ctrl-C')
    sys.exit(0)

def history_fetch_handler(e, l): 
    # print('history_fetch_handler: {0:d}'.format(e))
    # print(l)
    # if (e == 0):
    #     print('history_fetch_handler: {0:d}'.format(e))

    count = l.count()
    print('history_fetch_handler count: {0:d}'.format(count))

    for n in range(count):
        h = l.nth(n)
        # print(h)
        print(h.point_kind())
        print(h.height())
        print(h.value_or_spend())

        # print(h.point())
        print(h.point().hash())
        print(h.point().is_valid())
        print(h.point().index())
        print(h.point().get_checksum())



def last_height_fetch_handler(e, h): 
    if (e == 0):
        print('Last Height is: {0:d}'.format(h))

    if h >= 262421:
    	e.fetch_history('1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR', 0, 0, history_fetch_handler) # Juan

# ------------------------------------------------------
# Main Real
# ------------------------------------------------------
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as e:
# with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as e:

    #res = e.init_chain()
    #print(res)

    e.binary_construct()
    binary = e.binary_construct_string("10111010101011011111000000001101")
    e.binary_blocks(binary)
    x = [186,173,240,13]
    binary_block = e.binary_construct_blocks(32,x)
    e.binary_blocks(binary_block) 
    print(e.binary_encoded(binary_block))

    # ------------

    # e.run()
    # time.sleep(3)

    # ------------

    # res = e.run_wait()
    # # print(res)

    # while True:
    #     e.fetch_last_height(last_height_fetch_handler)
    #     # e.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
    #     # e.fetch_history('1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR', 0, 0, history_fetch_handler) # Juan
    #     time.sleep(120)

    # # print('Press Ctrl-C')
    # # signal.pause()

# bx fetch-history [-h] [--config VALUE] [--format VALUE] [PAYMENT_ADDRESS]


