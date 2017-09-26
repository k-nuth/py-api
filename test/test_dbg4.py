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

# import pdb
# import yourmodule
# pdb.run('yourmodule.foo()')

print('Preparing execution ...')
# execu = bitprim.Executor("", sys.stdout, sys.stderr)
execu = bitprim.Executor("", None, None)
res = execu.init_chain()

print(res)
# if not res:
#     raise RuntimeError('init_chain() failed')

res = execu.run_wait()
print(res)

if not res:
    raise RuntimeError('run_wait() failed')


print('Finishing')
# cls._exec.stop()
# cls._exec._destroy()
