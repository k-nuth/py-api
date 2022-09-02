# Copyright (c) 2016-2022 Knuth Project developers.
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

import kth_native as nat
import sys
import time
import asyncio
import kth

# https://stackoverflow.com/questions/51328952/python3-asyncio-await-on-callback
# https://stackoverflow.com/questions/53993334/converting-a-python-function-with-a-callback-to-an-asyncio-awaitable
async def launch_helper(node, justChain):
    future = asyncio.Future()
    loop = asyncio.get_event_loop()

    def callback(args):
        loop.call_soon_threadsafe(future.set_result, args)

    nat.node_init_run_and_wait_for_signal(node, justChain, callback)

    callback_args = await future
    return callback_args

# async def launch_helper(node, justChain):
#     loop = asyncio.get_event_loop()
#     future = loop.run_in_executor(None, nat.node_init_run_and_wait_for_signal, node, justChain)
#     result = await future
#     return result

##
#  Controls the execution of the Knuth node.
class Node:

    ##
    # Node constructor.
    def __init__(self, settings, stdoutEnabled = False):
        self._native = nat.node_construct(settings, stdoutEnabled)
        self._constructed = True
        self._running = False

    async def launch(self, mods):
        res = await launch_helper(self._native, mods)
        return res

    def _destroy(self):
        if self._constructed:
            if self._running:
                self.stop()

            nat.node_destruct(self._native)
            self._constructed = False

    def __del__(self):
        self._destroy()

    ##
    # Return the chain object representation
    # @return (Chain)
    @property
    def chain(self):
        return kth.chain.Chain(self, nat.node_chain(self._native))

    # ##
    # # Return the p2p object representation
    # # @return (P2p)
    # @property
    # def p2p(self):
    #     return P2p(self, nat.get_p2p(self._native))

    ##
    # Implements acquisition part of the RAII idiom (acquires the executor object)
    # @return (Node) a newly acquired instance ready to use
    def __enter__(self):
        return self

    ##
    # Implements the release part of the RAII idiom (releases the executor object)
    # @param exc_type Ignored
    # @param exc_value Ignored
    # @param traceback Ignored
    def __exit__(self, exc_type, exc_value, traceback):
        self._destroy()
