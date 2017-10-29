# https://gist.github.com/ingoogni/a7f7c0fed9e96b3545e9a8c6139d80b0

import os
import time
import threading
import cherrypy

import cherrypy_SSE
# import datapusher


import bitprim
# import bitprim_native
# import os
# import signal
import sys
# import time

import random
# import requests

# A typical reorganization consists of one incoming and zero outgoing blocks.
def subscribe_blockchain_handler(ec, fork_height, incoming, outgoing):

    service_stopped = 1

    if execut.stopped or ec == service_stopped:
        print(execut.stopped)
        print(ec)
        return False

    # print('PYTHON subscribe_blockchain_handler - 2')

    if ec != 0:
        # LOG_ERROR(LOG_NODE) << "Failure handling reorganization: " << ec.message();
        print("Failure handling reorganization: ")
        print(ec)
        execut.stop()
        return False

    # print(incoming)
    #  Nothing to do here.
    if not incoming or incoming.count == 0:
        return True

    # for block in outgoing:
    #     LOG_DEBUG(LOG_NODE << "Reorganization moved block to orphan pool [" << encode_hash(block->header().hash()) << "]"

    # height = safe_add(fork_height, incoming->size())
    # set_top_block({ incoming->back()->hash(), height });



    # if incoming.count > 0:
    #     print('subscribe_blockchain_handler - incoming.count: {0:d}'.format(incoming.count))

    print('-*-*-*-*-*-*-* subscribe_blockchain_handler - fork_height: {0:d}'.format(fork_height))


    channel = 'cpu'

    # time.sleep(random.random()*2)

    # msg = "event: time\ndata: {}\n\n".format(str(random.randint(0,100)))
    msg = "event: time\ndata: {}\n\n".format(str(fork_height))

    print('-*-*-*-*-*-*-* subscribe_blockchain_handler - msg: ' + msg)

    cherrypy.engine.publish(channel, msg)


    return True


class Root():

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def sensor(self, **kwargs):
        """
        receives POSTed data, converts to SSE ready message and
        pushes it onto the cherrypy bus
        """
        input_json = cherrypy.request.json
        msg = "event: time\ndata: {}\n\n".format(str(input_json['cpu']))
        cherrypy.engine.publish("cpu", msg)

    @cherrypy.expose
    def pubcpu(self):
        """
        publishes data from the subscribed channel...
        """
        channel = 'cpu'

        # doorman = cherrypy_SSE.Portier(channel,
        #                                heartbeat=True,
        #                                interval=5, hbmsg="event: time\ndata: 999\n\n")


        doorman = cherrypy_SSE.Portier(channel, heartbeat=False)

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

    # with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as execut:
    # with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg") as execut:
    execut = bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr)

    if not os.path.isdir("./blockchain"):
        res = execut.init_chain()
        print(res)

    res = execut.run_wait()
    print(res)

    # print('before subscribe_blockchain')
    execut.chain.subscribe_blockchain(subscribe_blockchain_handler)
    # print('after subscribe_blockchain')

    # rnd_bus = threading.Thread(target=datapusher.rndtobus, args=('cpu',))
    # rnd_bus.daemon = True
    # rnd_bus.start()    

    # rnd_port = threading.Thread(target=datapusher.rndtoport)
    # rnd_port.daemon = True
    # #rnd_port.start()    

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
