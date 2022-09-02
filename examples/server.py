# https://gist.github.com/ingoogni/a7f7c0fed9e96b3545e9a8c6139d80b0
# pip install cherrypy

# ------------------------------------------
import os
import sys
import kth
import cherrypy
import cherrypy_SSE
# import time
# import threading
# import random

# A typical reorganization consists of one incoming and zero outgoing blocks.
def subscribe_blockchain_handler(ec, fork_height, incoming, outgoing):

    if execut.stopped or ec == 1:
        return False

    if ec != 0:
        execut.stop()
        return False

    #  Nothing to do here.
    if not incoming or incoming.count == 0:
        return True

    channel = 'cpu'
    msg = "event: time\ndata: {}\n\n".format(str(fork_height))
    cherrypy.engine.publish(channel, msg)
    return True


class Root():
    @cherrypy.expose
    def pubcpu(self):
        """
        publishes data from the subscribed channel...
        """
        channel = 'cpu'

        doorman = cherrypy_SSE.Portier(channel)

        cherrypy.response.headers["Content-Type"] = "text/event-stream"
        def pub():
            for message in doorman.messages():
                # print('-*-*-*-*-*-*-* message: ')
                # print(message)

                try:
                    yield message
                except GeneratorExit:
                    # cherrypy shuts down the generator when the client
                    # disconnects. Catch disconnect and unsubscribe to clean up
                    doorman.unsubscribe()
                    return
        return pub()
    pubcpu._cp_config = {'response.stream': True}

    @cherrypy.expose
    def index(self):
        return open('index.html')


if __name__ == '__main__':

    # with kth.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as execut:
    # with kth.Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as execut:
    execut = kth.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr)

    if not os.path.isdir("./blockchain"):
        res = execut.init_chain()
        print(res)

    res = execut.run_wait()
    print(res)

    execut.chain.subscribe_blockchain(subscribe_blockchain_handler)

    conf = {
        'global': {
            # 'server.socket_host': "10.0.0.4",
            'server.socket_host': "127.0.0.1",
            'server.socket_port': 8080,
            'server.thread_pool': 25,
            'server.socket_queue_size': 10,
            'engine.autoreload.on': False,
            }
        }

    cherrypy.quickstart(Root(), config=conf)

    execut._destroy()