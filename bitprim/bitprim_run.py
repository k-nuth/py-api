import bitprim_native
import signal
import sys

# ------------------------------------------------------

class Executor:
    def __init__(self, path, sin, sout, serr):
        self.executor = bitprim_native.construct(path, sin, sout, serr)
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
    print('You pressed Ctrl-C')
    sys.exit(0)


# ------------------------------------------------------
# Main Real
# ------------------------------------------------------

signal.signal(signal.SIGINT, signal_handler)


with Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdin, sys.stdout, sys.stderr) as executor:
    # res = executor.initchain()
    res = executor.run()

    # print("********************************* AFTER run *********************************")
    # print(res)

    # print('Press Ctrl-C')
    signal.pause()






# # ------------------------------------------------------
# # Main Real
# # ------------------------------------------------------
#
# executor = bitprim_native.construct("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdin, sys.stdout, sys.stderr)
#
# # res = bitprim_native.initchain(executor)
#
# print("before run")
#
# res = bitprim_native.run(executor)
#
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
# # print("********************************* AFTER run *********************************")
#
# print(res)
#
#
# bitprim_native.destruct(executor)