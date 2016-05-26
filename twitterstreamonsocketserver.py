
# coding: utf-8

# In[ ]:

from pubnub import Pubnub
from json import dumps
import socketserver


# In[ ]:

twitterstream = Pubnub(publish_key='demo', subscribe_key='sub-c-78806dd4-42a6-11e4-aed8-02ee2ddab7fe')
def _callback(message, channel):
    try:
        msg_array.push(message['place']['country'])
    except TypeError:
        pass
    
def _error(message):
    print("ERROR : " + str(message))
    
def _connect(message):
    print("CONNECTED")
    
def _reconnect(message):
    print("RECONNECTED")
    
def _disconnect(message):
    print("DISCONNECTED")


# In[ ]:

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isNotEmpty(self):
        "Returns true if the queue is not empty"
        return len(self.list) != 0


# In[ ]:

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        while msg_array.isNotEmpty:
            try:
                self.data = bytes(msg_array.pop()+'\n', 'utf-8')
            except IndexError:
                continue
            # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())


# In[ ]:

if __name__ == "__main__":
    msg_array = Queue()    
    HOST, PORT = "localhost", 6666
    twitterstream.subscribe(channels='pubnub-twitter', callback=_callback, error=_error,
                 connect=_connect, reconnect=_reconnect, disconnect=_disconnect)

    # Create the server, binding to localhost on port 6666
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

