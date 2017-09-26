import os
import signal
import sys
import time
import threading
import bitprim
from datetime import datetime

# -----------------------------------------------------------------------------------------------
def get_last_height(chain):
    evt = threading.Event()

    _error = [0]
    _height = [False]        

    def handler(error, height):
        _error[0] = error
        _height[0] = height
        evt.set()

    chain.fetch_last_height(handler)
    evt.wait()

    return (_error[0], _height[0])

def wait_until_block(chain, desired_height):
    error, height = get_last_height(chain)
    while error == 0 and height < desired_height:
        error, height = get_last_height(chain)
        if height < desired_height:
            time.sleep(10)

# --------------------------------------

print('Preparing execution ...')
# execu = bitprim.Executor("", sys.stdout, sys.stderr)
execu = bitprim.Executor("", None, None)
res = execu.init_chain()

# if not res:
#     raise RuntimeError('init_chain() failed')

res = execu.run_wait()
if not res:
    print(res)
    raise RuntimeError('run_wait() failed')

# chain = execu.chain

wait_until_block(execu.chain, 170)


print('Finishing')
# cls._exec.stop()
# cls._exec._destroy()
