import asyncore, socket
import threading

class SocketClient(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect( (host, port) )
        # self.buffer = 'GET %s HTTP/1.0\r\n\r\n' % path

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print self.recv(8192)

    # def writable(self):
        # return (len(self.buffer) > 0)

    def handle_write(self):
        pass
        # self.buffer = self.buffer[sent:]



class Client():
    def __init__(self):
        self.client = SocketClient('10.0.1.21', 4001)
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
        self.client.close()
        # now it is save to wait for the thread to finish, i.e. for asyncore.loop() to exit
        self.thread.join()

    def sendMessages(self, messages):
        self.client.send(messages)

x = Client()
try:
   
   x.start()

   while True:
    n = raw_input("\n\nSend?: ")
    x.sendMessages(n)
finally:
    x.stop()