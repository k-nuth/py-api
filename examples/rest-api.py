# pip install cherrypy
# pip install routes


import cherrypy

messages = ['hola', 'como', 'va']
	  
class HelloWorld(object):

    @cherrypy.expose
    def index(self):
        # return "Hello World!"
        # return "Hello World!"

        return """THIS is a very
                  long string if I had the
                  energy to type more and more ...

<script>
var source = new EventSource("/user-log-stream");
source.onmessage = function(event) {
    var message = event.data;
    alert(message);
};
</script>"""

 
    @cherrypy.expose
    def stream(self):
        cherrypy.response.headers["Content-Type"] = "text/event-stream"
        while True:
            if len(messages) > 0:
                for msg in messages:
                    data = 'data:' + msg + '\n\n'
                    yield data
                messages = []


    # index.exposed = True

# cherrypy.quickstart(HelloWorld())

dispatcher = cherrypy.dispatch.RoutesDispatcher()
dispatcher.explicit = False
dispatcher.connect('user-log-stream', '/', controller = HelloWorld(), action='stream')

conf = {
    '/' : {
        'request.dispatch' : dispatcher,
        'log.screen' : True
    }
     }

# cherrypy.tree.mount(None, "/", config=conf) 
# cherrypy.quickstart(None, config=conf)

# # cherrypy.tree.mount(root=None, config=conf)
# # cherrypy.tree.mount(root=None, "/")
# cherrypy.tree.mount(root=None)
cherrypy.quickstart(HelloWorld())


# -----------------------------------------

# import cherrypy
 
# class UserLogStream:
#     messages = []
 
#     @cherrypy.expose
#     def stream(self):
#         cherrypy.response.headers["Content-Type"] = "text/event-stream"
#         while True:
#             if len(messages) > 0:
#                 for msg in messages:
#                     data = 'data:' + msg + '\n\n'
#                     yield data
#                 messages = []
 
# dispatcher = cherrypy.dispatch.RoutesDispatcher()
# dispatcher.connect('user-log-stream', '/', controller = UserLogStream(), action='stream')



# -----------------------------------------

# import cherrypy
	  
# class HelloWorld(object):
#     def index(self):
#         return "Hello World!"
#     index.exposed = True

# cherrypy.quickstart(HelloWorld())


# -----------------------------------------

# #!flask/bin/python
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello, World!"

# if __name__ == '__main__':
#     print('before http server')
#     app.run(debug=False)
#     print('exiting...')
