import threading
import cherrypy
from cherrypy.process import plugins

class Portier(threading.Thread):
    """
    The Doorman (Portier) detects changes of message by listening to the
    subscribed channel, opens 'the door' as a message appears, yield it
    and closes the door once trough.

    channel: the cherrypy bus channel to listen to.
    heartbeat: start a default heartbeat on the channel, every 30 s a blank SSE
    comment line.
    interval: set interval of heartbeat, in s.
    hbmsg: set message for the heartbeat, mostley usefull for debugging.
    """
    def __init__(self, channel, heartbeat=None, interval=None, hbmsg=None,group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         daemon=daemon)
        #self.daemon = True
        self.channel = channel
        self.e = threading.Event()
        self.name = 'Portier-'+self.name
        cherrypy.engine.subscribe(channel, self._msgs)
        if heartbeat:
            beatmsg = {'channel': self.channel,
                       'listner': threading.current_thread()}
            if interval:
                beatmsg['interval'] = interval
            if hbmsg:
                beatmsg['message'] = hbmsg
            cherrypy.engine.publish('startbeat', beatmsg)

                
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
        cherrypy.engine.publish('stopbeat',
                                {'channel': self.channel,
                                 'listner': threading.current_thread()
                                 })


class Beats(threading.Thread):
    """
    publishes a heartbeat message on the cherrypy bus in a steady rithm.

    interval: in seconds
    channel: channel to publish the heartbeat message to
    message: the heartbeat message to be published
    """
    
    def __init__(self, interval, channel, message):
        threading.Thread.__init__(self)
        self.daemon = True
        self.event = threading.Event()
        self.interval = interval
        self.channel = channel
        self.message = message # ": \n\n"
        self.start()

    def run(self):
        """publishes the messages"""
        
        while not self.event.is_set():
            cherrypy.engine.publish(self.channel, self.message)
            self.event.wait(self.interval)

    def backbeat(self):
        """'awakens the thread, paused by 'breakbeat'"""
        
        self.event.clear()

    def breakbeat(self):
        """'pauses' the beats until awakend by 'backbeat'"""
        
        self.event.is_set()


class Beatmanager():
    """
    Instantiates the Beats classes, one per channel. Registers the channel,
    the listners of a channel and pauses the heartbeat when there are no
    listeners left. Communication with the Beatmaster is through the
    Heartbeat class that listens to the channels 'startbeat' and 'stopbeat'.
    """
    def __init__(self):
        self.threads = {}
        self.listners = {}

    def start(self, msg):
        """
        Starts or resumes a Beats thread.

        msg: requires a dictionary as message
        {'channel': channel name, required
        'listner': listner name (can be treadID), required
        'interval': interval in seconds, optional, default 30
        'message': optional, default, a blank SSE comment
        }
        """
        channel = msg['channel']
        listner = msg['listner']
        interval = msg.setdefault('interval', 30)
        message = msg.setdefault('message', ": \n\n") 
        if channel not in self.threads:
            self.threads[channel] = Beats(interval, channel, message)
            self.listners[channel] = [listner]
        elif len(self.listners[channel])==0:
            self.listners[channel] = [listner]
            self.threads[channel].backbeat()            
        else:
            self.listners[channel].append(listner)
    
    def stop(self, msg):
        """
        Listens to the 'stopbeat' channel, removes listeners, pauses the
        Beats thread when there are no listeners left.

        msg: requires a dictionary as message
        {'channel': channel name, 'listener': listnername}
        """
        channel = msg['channel']
        listner = msg['listner']        
        if listner in self.listners[channel]:
            self.listners[channel].remove(listner)
        if len(self.listners[channel])==0:
            self.threads[channel].breakbeat()


class Heartbeat(plugins.SimplePlugin):
    """
    Accesspoint to the Beatmanager and thus Beats classes. Listens to
    the startbeat and stopbeat channels and passes the data on. Registers
    both to the bus.
    """
    def __init__(self, bus, Beatmanager):
        plugins.SimplePlugin.__init__(self, bus)
        self.heartbeat = Beatmanager()
        self.bus.subscribe('startbeat', self.heartbeat.start)
        self.bus.subscribe('stopbeat', self.heartbeat.stop)

    def start(self):
        self.bus.log('Starting up Heartbeat')

    def stop(self):
        self.bus.unsubscribe('startbeat', self.heartbeat.start)
        self.bus.unsubscribe('stopbeat', self.heartbeat.stop)
        self.bus.log('Shut down Heartbeat')

Heartbeat(cherrypy.engine, Beatmanager).subscribe()
