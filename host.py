import asyncore
import socket
import threading

class SocketHandler(asyncore.dispatcher_with_send):
    def __init__(self):
        self.listeners = []
    def handle_read(self):
        data = self.recv(8192)
        for listener in self.listeners:
            listener.receice(data)
        #     # self.send(data)
    def sendMessages(self, messages):
        self.send(messages)

    def register(self, listener):
        self.listeners.append(listener)
        

class MyServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
        self.handlers = []

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = SocketHandler(sock)
            self.handlers.append(handler)

    def sendMessages(self, messages):
        for handler in self.handlers:
            handler.sendMessages(messages)

    def register(self, listener):
        for handler in self.handlers:
            handler.register(handler) 


class Host():
    def __init__(self):
        self.server = MyServer('10.0.1.21', 4001)
        self.thread =  threading.Thread(target=asyncore.loop,kwargs = {'timeout':1} )
    def start(self):
        """Start the listening service"""
        # here I create an instance of the SMTP server, derived from  asyncore.dispatcher
        
        # and here I also start the asyncore loop, listening for SMTP connection, within a thread
        # timeout parameter is important, otherwise code will block 30 seconds after the smtp channel has been closed
        
        self.thread.start()  

    def stop(self):
        """Stop listening now to port 25"""
        # close the SMTPserver to ensure no channels connect to asyncore
        self.server.close()
        # now it is save to wait for the thread to finish, i.e. for asyncore.loop() to exit
        self.thread.join()

    def sendMessages(self, messages):
        self.server.sendMessages(messages)

    def register(self, listener):
        self.server.register(listener)

# x = Host()
# try:
   
#    x.start()
#    while True:
#     n = raw_input("\n\nSend?: ")
#     x.sendMessages(n)
#     pass
# finally:
#     x.stop()
 # h.sendMessages('123456')
# 

