#!/usr/bin/env python
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

import socket
import base64

src     = '192.168.1.XXX'     # ip of remote
mac     = '00-AB-11-11-11-11' # mac of remote
remote  = 'python remote'     # remote name
dst     = '192.168.1.XXX'     # ip of tv
app     = 'python'            # iphone..iapp.samsung
tv      = 'LE32C650'          # iphone.LE32C650.iapp.samsung

def push(key):
    try:
        new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new.connect((dst, 55000))
        msg = chr(0x64) + chr(0x00) +\
            chr(len(base64.b64encode(src)))    + chr(0x00) + base64.b64encode(src) +\
            chr(len(base64.b64encode(mac)))    + chr(0x00) + base64.b64encode(mac) +\
            chr(len(base64.b64encode(remote))) + chr(0x00) + base64.b64encode(remote)
        pkt = chr(0x00) +\
            chr(len(app)) + chr(0x00) + app +\
            chr(len(msg)) + chr(0x00) + msg
        new.send(pkt)
        msg = chr(0x00) + chr(0x00) + chr(0x00) +\
            chr(len(base64.b64encode(key))) + chr(0x00) + base64.b64encode(key)
        pkt = chr(0x00) +\
            chr(len(tv))  + chr(0x00) + tv +\
            chr(len(msg)) + chr(0x00) + msg
        new.send(pkt)
        new.close()
    except:
        print "The tv cannot be found at address " + str(dst)

class SamsungServer(Protocol):
    def connectionMade(self):
        self.factory.clients.append(self)
        print "clients are ", self.factory.clients

    def connectionLost(self, reason):
        self.factory.clients.remove(self)
        
    def dataReceived(self, data):
        #print "data is ", data
        a = data.split(':')
        if len(a) > 1:
            command = a[0]
            content = a[1]
            
            if command == "cmd":
                if content == "volup":
                    push("KEY_VOLUP")
                elif content == "voldown":
                    push("KEY_VOLDOWN")
                elif content == "poweroff":
                    push("KEY_POWEROFF")
		elif content == "chup":
		    push("KEY_CHUP");
		elif content == "chdown":
		    push("KEY_CHDOWN")
		elif content == "mute":
		    push("KEY_MUTE")
		elif content == "source":
		    push("KEY_SOURCE")
		elif content == "enter":
		    push("KEY_ENTER")
		elif content == "info":
		    push("KEY_INFO")
		elif content == "guide":
		    push("KEY_INFO")
		elif content == "prech":
		    push("KEY_PRECH")
		elif content == "menu":
		    push("KEY_MENU")
		elif content == "right":
		    push("KEY_RIGHT")
		elif content == "left":
		    push("KEY_LEFT")
		elif content == "down":
		    push("KEY_DOWN")
		elif content == "up":
		    push("KEY_UP")
		elif content == "0":
		    push("KEY_0")
		elif content == "1":
		    push("KEY_1")
		elif content == "2":
		    push("KEY_2")
		elif content == "3":
		    push("KEY_3")
		elif content == "4":
		    push("KEY_4")
		elif content == "5":
		    push("KEY_5")
		elif content == "6":
		    push("KEY_6")
		elif content == "7":
		    push("KEY_7")
		elif content == "8":
		    push("KEY_8")
		elif content == "9":
		    push("KEY_9")


factory = Factory()
factory.protocol = SamsungServer
factory.clients = []

reactor.listenTCP(82, factory)
print "TV server started"
reactor.run()
