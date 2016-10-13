import asyncore
import socket
import threading
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import Qt, QThread

class SocketHandler(asyncore.dispatcher_with_send,QtCore.QObject):
    # def __init__ 
    # listeners = []
    post = QtCore.pyqtSignal(object)

    def __init__(self,socket,message):
   	    asyncore.dispatcher.__init__(self,socket)
	    QtCore.QObject.__init__(self, None)
	    self.out_buffer = str(message)
        
    def handle_read(self):
        data = self.recv(8192)
        # print data
    	self.post.emit(data)
        #     # self.send(data)
    def sendMessages(self, messages):
        self.send(messages)

    def register(self, listener):
        self.post.connect(listener)
        

class MyServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.handlers = []
        self.registers = []

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)

            handler = SocketHandler(sock, '')
            for register in self.registers:
            	handler.register(register)
            self.handlers.append(handler)

    def sendMessages(self, messages):
        for handler in self.handlers:
            handler.sendMessages(messages)

    def register(self, listener):
    	self.registers.append(listener)
        for handler in self.handlers:
            handler.register(listener) 


class Host(QThread):

	

    def __init__(self, parent = None):
    	QThread.__init__(self, parent)
        self.server = MyServer('10.0.1.33', 4001)
        #self.thread = QtCore.QThread()  # no parent!
        #self.thread =  threading.Thread(target=.asyncoreloop,kwargs = {'timeout':1} )
    def run(self):
        """Start the listening service"""
        # here I create an instance of the SMTP server, derived from  asyncore.dispatcher
        
        # and here I also start the asyncore loop, listening for SMTP connection, within a thread
        # timeout parameter is important, otherwise code will block 30 seconds after the smtp channel has been closed
        asyncore.loop()
        #self.thread.start() 
        print 'start server' 

    def terminate(self):
        """Stop listening now to port 25"""
        # close the SMTPserver to ensure no channels connect to asyncore
        super(Host, self).terminate()
        self.server.close()
        # now it is save to wait for the thread to finish, i.e. for asyncore.loop() to exit

    def sendMessages(self, messages):
        self.server.sendMessages(messages)

    def register(self, listener):
        self.server.register(listener)

#x = Host()
#try:
   
#    x.start()
#    while True:
 #       n = raw_input("\n\nSend?: ")
#        x.sendMessages(n)
    
#finally:
 #   x.stop()
 # h.sendMessages('123456')
# 

