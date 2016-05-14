
# coding: utf-8

# In[1]:

from pubnub import Pubnub
import json

TS = Pubnub(publish_key="demo", subscribe_key = 'sub-c-78806dd4-42a6-11e4-aed8-02ee2ddab7fe')
channel = 'pubnub-twitter'

def _callback(message, channel):
    with open('HDFS/tweet.txt', 'a+', encoding='UTF-8') as doc:
        print(json.dumps(message), file = doc)
#     print(message['user']['screen_name'])
#     print(message['text'])
#     print(message['place']['country'],'\t',message['place']['country_code'])
#     input()

def _error(message):
    print("ERROR : " + str(message))

def _connect(message):
    print("CONNECTED")

def _reconnect(message):
    print("RECONNECTED")

def _disconnect(message):
    print("DISCONNECTED")
    
TS.subscribe(channels='pubnub-twitter', callback=_callback, error=_error, connect=_connect, reconnect=_reconnect, disconnect=_disconnect)


# In[ ]:



