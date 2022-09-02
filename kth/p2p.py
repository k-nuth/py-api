# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth_native as nat
import sys
import time

##
# Represents the Bitcoin `P2P` Networking API.
class P2p:
    def __init__(self, executor, p2p):
        ##
        # @private
        self._executor = executor
        self._p2p = p2p

    @property
    def address_count(self):
        return nat.p2p_address_count(self._p2p)

    def stop(self):
        nat.p2p_stop(self._p2p)

    def close(self):
        nat.p2p_close(self._p2p)

    @property
    def stopped(self):
        return nat.p2p_stopped(self._p2p) != 0

# PyObject* kth_native_p2p_address_count(PyObject* self, PyObject* args);
# PyObject* kth_native_p2p_stop(PyObject* self, PyObject* args);
# PyObject* kth_native_p2p_close(PyObject* self, PyObject* args);
# PyObject* kth_native_p2p_stopped(PyObject* self, PyObject* args);
