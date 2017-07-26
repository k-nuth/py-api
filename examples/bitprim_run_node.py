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

# ------------------------------------------------------
# 
# ------------------------------------------------------
def signal_handler(signal, frame):
    # signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGTERM, signal_handler)
    print('You pressed Ctrl-C')
    sys.exit(0)

def history_fetch_handler(e, l): 
    count = l.count()
    print('history_fetch_handler count: {0:d}'.format(count))

    for n in range(count):
        h = l.nth(n)
        # print(h)
        print(h.point_kind())
        print(h.height())
        print(h.value_or_spend())
        print(h.point().hash())
        print(h.point().is_valid())
        print(h.point().index())
        print(h.point().get_checksum())

def block_handler(e, block, height): 
    _header = block.header()
    _hash = _header.previous_block_hash()
    _hash_hex = ''.join('{:02x}'.format(x) for x in _hash[::-1])
    print("Previous Block Hash: "+ _hash_hex)

    print("Prev block original timestamp: %i" %(_header.timestamp()))
    print("Modifying timestamp to 1000000")
    _header.set_timestamp(1000000)
    print("Timestamp value is now: %i" %(_header.timestamp()))


def last_height_fetch_handler(e, h): 
    if (e == 0):
        print('Last Height is: {0:d}'.format(h))
    
    hash_str = "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048"
    hash = bytearray.fromhex(hash_str)
    hash = hash[::-1]
    t = buffer(hash)

    if h >= 1:
        execut.get_chain().fetch_block_by_hash(t, block_handler)

# ------------------------------------------------------
# Main Real
# ------------------------------------------------------
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as execut:

    res = execut.init_chain()
    print(res)

    res = execut.run_wait()
    print(res)

    while True:
        execut.get_chain().fetch_last_height(last_height_fetch_handler)
        time.sleep(30)


