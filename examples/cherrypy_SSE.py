import threading
import cherrypy
from cherrypy.process import plugins

class Portier(threading.Thread):
    """
    The Doorman (Portier) detects changes of message by listening to the
    subscribed channel, opens 'the door' as a message appears, yield it
    and closes the door once trough.

    channel: the cherrypy bus channel to listen to.
    """

    # Python 3
    # def __init__(self, channel, group=None, target=None, name=None,
    #              args=(), kwargs=None, *, daemon=None):
    #     super().__init__(group=group, target=target, name=name,
    #                      daemon=daemon)

    # Python 2
    def __init__(self, channel, group=None, target=None, name=None, args=(), kwargs=None):
        # super().__init__(group=group, target=target, name=name)
        # threading.Thread.__init__(group=group, target=target, name=name)
        super(Portier, self).__init__(group=group, target=target, name=name)        

        #self.daemon = True
        self.channel = channel
        self.e = threading.Event()
        # self.name = 'Portier-'+self.name
        cherrypy.engine.subscribe(channel, self._msgs)
                
    @property
    def message(self):
        """contains the last message published to the bus channel"""
        return self._message

    @message.setter
    def message(self, msg):
        """Sets the latest message and triggers the 'door' to open"""        
        self.e.set()
        self._message = msg

    def messages(self):
        """
        The Doorman's door, yields the messages as they appear on
        the bus channel.
        """        
        while True:
            self.e.wait()
            yield self._message
            self.e.clear()

    def _msgs(self, message):
        """Receives the messages from the bus"""
        self.message = message

    def unsubscribe(self):
        """
        Unsubscribe from the message stream, signals to remove the thread
        from the heartbet stream
        """     
        cherrypy.engine.unsubscribe(self.channel, self._msgs)
        # cherrypy.engine.publish('stopbeat',
        #                         {'channel': self.channel,
        #                          'listner': threading.current_thread()
        #                          })


