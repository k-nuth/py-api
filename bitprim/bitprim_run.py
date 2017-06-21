import bitprim_native
import os
import signal
import sys
import time

# ------------------------------------------------------

class Executor:
    def __init__(self, path, sout = None, serr = None):
        if sout != None:
            self.executor = bitprim_native.construct(path, sout, serr)
        else:
            self.executor = bitprim_native.construct_devnull(path)

        self.constructed = True
        self.running = False

    def destroy(self):
        # print('destroy')

        if self.constructed:
            if self.running:
                self.stop()

            bitprim_native.destruct(self.executor)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def run(self):
        ret = bitprim_native.run(self.executor)

        if ret:
            self.running = True

        return ret

    def stop(self):
        # precondition: self.running
        ret = bitprim_native.stop(self.executor)

        if ret:
            self.running = False

        return ret

    def init_chain(self):
        return bitprim_native.initchain(self.executor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # print('__exit__')
        self.destroy()

# ------------------------------------------------------

# class ExecutorResource:
#     def __enter__(self):
#         class Executor:
#             ...
#         self.package_obj = Package()
#         return self.package_obj
#     def __exit__(self, exc_type, exc_value, traceback):
#         self.package_obj.cleanup()

# ------------------------------------------------------
# Main Test
# ------------------------------------------------------
# with Executor(1, 2, 3, 4) as exec:
#     exec.run()
#     exec.initchain()
# ------------------------------------------------------


# ------------------------------------------------------
# 
# ------------------------------------------------------
def signal_handler(signal, frame):
    # signal.signal(signal.SIGINT, signal_handler)
    # signal.signal(signal.SIGTERM, signal_handler)
    print('You pressed Ctrl-C')
    sys.exit(0)

def last_height_fetch_handler(e, h): 
    if (e == 0):
        print('Last Height is: {0:d}'.format(h))

# ------------------------------------------------------
# Main Real
# ------------------------------------------------------
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# with Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as executor:
with Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as executor:
    # res = executor.initchain()
    res = executor.run()

    while True:
        bitprim_native.fetch_last_height(executor.executor, last_height_fetch_handler)
        time.sleep(3) 

    # print('Press Ctrl-C')
    signal.pause()

# bx fetch-history [-h] [--config VALUE] [--format VALUE] [PAYMENT_ADDRESS]