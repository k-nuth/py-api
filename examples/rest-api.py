import os
import sys
import threading
import cherrypy
import bitprim

event = threading.Event()
last_height = 0

class BlockHandler(object):
    def __init__(self, executor):
        self.executor = executor

    # A typical reorganization consists of one incoming and zero outgoing blocks.
    def __call__(self, ec, fork_height, incoming, outgoing):
        if self.executor.stopped or ec == 1:
            event.clear()
            return False

        if ec != 0:
            event.clear()
            self.executor.stop()
            return False

        #  Nothing to do here.
        if not incoming or incoming.count == 0:
            event.clear()
            return True

        global last_height
        last_height = fork_height
        event.set()
        # print(last_height)
        return True

class Root():

    @cherrypy.expose
    def index(self):
        return r'''<!DOCTYPE html>
<html>
 <head>
  <title>Server-sent events test</title>
  <style>html,body,#test{height:98%;}</style>
 </head>
 <body>
  <script type="text/javascript">
    document.addEventListener('DOMContentLoaded', function () {
      var source = new EventSource('last_height');
      source.addEventListener('time', function (event) {
        document.getElementById('lblHeight').innerHTML = event.data;
      });
      source.addEventListener('error', function (event){
        console.log('SSE error:', event);
        console.log('SSE state:', source.readyState);
      });
    }, false);
  </script>
  Last Block Height: <label id="lblHeight">0</label>
 </body>
</html>'''

    @cherrypy.expose
    def last_height(self):
        cherrypy.response.headers["Content-Type"] = "text/event-stream"
        def generator():
            while True:
                event.wait()
                yield "event: time\n" + "data: " + str(last_height) + "\n\n"
                event.clear()
        return generator()

    last_height._cp_config = {'response.stream': True}


def main():
    # execut = bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr)
    with bitprim.Executor("/home/fernando/execution_tests/btc_mainnet.cfg", sys.stdout, sys.stderr) as execut:

        if not os.path.isdir("./blockchain"):
            res = execut.init_chain()
            print(res)

        res = execut.run_wait()
        if not res:
            return

        # execut.chain.subscribe_blockchain(subscribe_blockchain_handler)
        execut.chain.subscribe_blockchain(BlockHandler(execut))

        # ----------------------------------------------------------------------------------------------------
        cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080,})
        cherrypy.quickstart(Root())
        # ----------------------------------------------------------------------------------------------------

    # execut._destroy()

if __name__ == '__main__':
    main()











# import cherrypy

# # messages = ['hola', 'como', 'va']

# class ABRoot:  

#     def index(self):
#         print("Index")
#         return """THIS is a very
#                     long string if I had the
#                     energy to type more and more ...

#                     Last Block Height: <label id="lblHeight">0</label>

#                     <script>
#                     console.log('fer 1')
#                     var source = new EventSource("/user-log-stream");
#                     console.log('fer 2')
#                     source.onmessage = function(event) {
#                         console.log('fer 3')
#                         var message = event.data;
#                         console.log('fer 4')
#                         alert(message);
#                         document.getElementById('lblHeight').innerHTML = message;
#                     };
#                     </script>"""

#     @cherrypy.expose
#     def stream(self):
#         print("stream")
#         cherrypy.response.headers["Content-Type"] = "text/event-stream"
#         messages = ['hola', 'como', 'va']
#         while True:
#             if len(messages) > 0:
#                 for msg in messages:
#                     print()
#                     data = 'data:' + msg + '\n\n'
#                     print(data)
#                     yield data
#                 messages = []


# if __name__ == '__main__':


#     dispatcher = cherrypy.dispatch.RoutesDispatcher()
#     dispatcher.explicit = False
#     dispatcher.connect('test', '/', ABRoot().index)
#     # dispatcher.connect('user-log-stream', '/', controller = ABRoot(), action='stream')
#     dispatcher.connect('user-log-stream', '/user-log-stream', ABRoot().stream)

#     conf = {
#     '/' : {
#         'request.dispatch' : dispatcher,
#         'log.screen' : True
#     }}

#     cherrypy.tree.mount(None, "/", config=conf) 
#     cherrypy.quickstart(None, config=conf)



























# # pip install cherrypy
# # pip install routes


# import cherrypy

# messages = ['hola', 'como', 'va']
	  
# class HelloWorld(object):

#     @cherrypy.expose
#     def index(self):
#         # return "Hello World!"
#         # return "Hello World!"

#         return """THIS is a very
#                   long string if I had the
#                   energy to type more and more ...
# """

# #  <script>
# # var source = new EventSource("/user-log-stream");
# # source.onmessage = function(event) {
# #     var message = event.data;
# #     alert(message);
# # };
# # </script>"""
#     @cherrypy.expose
#     def stream(self):
#         cherrypy.response.headers["Content-Type"] = "text/event-stream"
#         while True:
#             if len(messages) > 0:
#                 for msg in messages:
#                     data = 'data:' + msg + '\n\n'
#                     yield data
#                 messages = []


#     # index.exposed = True

# # cherrypy.quickstart(HelloWorld())

# dispatcher = cherrypy.dispatch.RoutesDispatcher()
# # dispatcher.explicit = False
# dispatcher.connect('user-log-stream', '/', controller = HelloWorld(), action='stream')

# # conf = {
# #     '/' : {
# #         'request.dispatch' : dispatcher,
# #         'log.screen' : True
# #     }
# #      }

# # cherrypy.tree.mount(None, "/", config=conf) 
# # cherrypy.quickstart(None, config=conf)

# # # cherrypy.tree.mount(root=None, config=conf)
# # # cherrypy.tree.mount(root=None, "/")
# # cherrypy.tree.mount(root=None)
# # cherrypy.quickstart(HelloWorld())
# cherrypy.quickstart(dispatcher, "/")


# # -----------------------------------------

# # import cherrypy
 
# # class UserLogStream:
# #     messages = []
 
# #     @cherrypy.expose
# #     def stream(self):
# #         cherrypy.response.headers["Content-Type"] = "text/event-stream"
# #         while True:
# #             if len(messages) > 0:
# #                 for msg in messages:
# #                     data = 'data:' + msg + '\n\n'
# #                     yield data
# #                 messages = []
 
# # dispatcher = cherrypy.dispatch.RoutesDispatcher()
# # dispatcher.connect('user-log-stream', '/', controller = UserLogStream(), action='stream')



# # -----------------------------------------

# # import cherrypy
	  
# # class HelloWorld(object):
# #     def index(self):
# #         return "Hello World!"
# #     index.exposed = True

# # cherrypy.quickstart(HelloWorld())


# # -----------------------------------------

# # #!flask/bin/python
# # from flask import Flask

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return "Hello, World!"

# # if __name__ == '__main__':
# #     print('before http server')
# #     app.run(debug=False)
# #     print('exiting...')
