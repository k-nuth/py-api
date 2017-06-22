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

import bitprim_native

# ------------------------------------------------------
class Point:
    def __init__(self, ptr):
        self.ptr = ptr

    def hash(self):
        # print('Point.hash')
        return bitprim_native.point_get_hash(self.ptr)[::-1].hex()

    def is_valid(self):
        return bitprim_native.point_is_valid(self.ptr)

    def index(self):
        return bitprim_native.point_get_index(self.ptr)

    def get_checksum(self):
        return bitprim_native.point_get_checksum(self.ptr)

# ------------------------------------------------------
class History:
    def __init__(self, ptr):
        self.ptr = ptr

    def point_kind(self):
        return bitprim_native.history_compact_get_point_kind(self.ptr)

    def point(self):
        return Point(bitprim_native.history_compact_get_point(self.ptr))

    def height(self):
        return bitprim_native.history_compact_get_height(self.ptr)

    def value_or_spend(self):
        return bitprim_native.history_compact_get_value_or_spend(self.ptr)


# ------------------------------------------------------
class HistoryList:
    def __init__(self, ptr):
        self.ptr = ptr
        self.constructed = True

    def destroy(self):
        if self.constructed:
            bitprim_native.history_compact_list_destruct(self.ptr)
            self.constructed = False

    def __del__(self):
        # print('__del__')
        self.destroy()

    def count(self):
        return bitprim_native.history_compact_list_count(self.ptr)

    def nth(self, n):
        return History(bitprim_native.history_compact_list_nth(self.ptr, n))

    # def __enter__(self):
    #     return self

    # def __exit__(self, exc_type, exc_value, traceback):
    #     # print('__exit__')
    #     self.destroy()


# ------------------------------------------------------
class Executor:
    def __init__(self, path, sout = None, serr = None):
        self.executor = bitprim_native.construct(path, sout, serr)
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

    def run_wait(self):
        ret = bitprim_native.run_wait(self.executor)

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

    def fetch_last_height(self, handler):
        bitprim_native.fetch_last_height(self.executor, handler)


    def history_fetch_handler_converter(self, e, l):
        # print('history_fetch_handler_converter')
        if e == 0: 
            list = HistoryList(l)
        else:
            list = None

        self.history_fetch_handler_(e, list)

    def fetch_history(self, address, limit, from_height, handler):
        self.history_fetch_handler_ = handler
        bitprim_native.fetch_history(self.executor, address, limit, from_height, self.history_fetch_handler_converter)

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




# # ------------------------------------------------------
# # 
# # ------------------------------------------------------
# def signal_handler(signal, frame):
#     # signal.signal(signal.SIGINT, signal_handler)
#     # signal.signal(signal.SIGTERM, signal_handler)
#     print('You pressed Ctrl-C')
#     sys.exit(0)

# def history_fetch_handler(e, l): 
#     # print('history_fetch_handler: {0:d}'.format(e))
#     # print(l)
#     # if (e == 0):
#     #     print('history_fetch_handler: {0:d}'.format(e))

#     count = l.count()
#     print('history_fetch_handler count: {0:d}'.format(count))

#     for n in range(count):
#         h = l.nth(n)
#         # print(h)
#         print(h.point_kind())
#         print(h.height())
#         print(h.value_or_spend())

#         # print(h.point())
#         print(h.point().hash())
#         print(h.point().is_valid())
#         print(h.point().index())
#         print(h.point().get_checksum())



# def last_height_fetch_handler(e, h): 
#     if (e == 0):
#         print('Last Height is: {0:d}'.format(h))
#         # if h > 1000:
#         #     # executor.fetch_history('134HfD2fdeBTohfx8YANxEpsYXsv5UoWyz', 0, 0, history_fetch_handler)
#         #     executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
#         #     # executor.fetch_history('1MLVpZC2CTFHheox8SCEnAbW5NBdewRTdR', 0, 0, history_fetch_handler) # Es la de Juan




# # ------------------------------------------------------
# # Main Real
# # ------------------------------------------------------
# signal.signal(signal.SIGINT, signal_handler)
# signal.signal(signal.SIGTERM, signal_handler)

# with Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as executor:
# # with Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as executor:
#     # res = executor.initchain()
#     res = executor.run()
#     # print(res)
    
#     time.sleep(3)

#     # executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler)

#     # time.sleep(5)

#     while True:
#         executor.fetch_last_height(last_height_fetch_handler)
#         # executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler) # Satoshi
#         executor.fetch_history('1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa', 0, 0, history_fetch_handler)
#         time.sleep(10)

#     # print('Press Ctrl-C')
#     # signal.pause()

# # bx fetch-history [-h] [--config VALUE] [--format VALUE] [PAYMENT_ADDRESS]