# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth
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
    sys.exit(0)


# ------------------------------------------------------
# Main Real
# ------------------------------------------------------
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

with kth.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as execut:

    hash_str = "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098"
    hash = bytearray.fromhex(hash_str)
    hash = hash[::-1]
    taa = buffer(hash)
    point = kth.OutputPoint.construct_from_hash_index(taa,0)
    print("hash")
    point.hash()
    print(point.hash())
    print("index")
    point.index()

    hashresult = point.hash()
    hash_hex = hashresult[::-1].encode('hex')
    print(hash_hex)
    print("finish")

