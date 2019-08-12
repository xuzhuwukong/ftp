import optparse
import socket

class FtpClient():
    address_familly = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = False
    max_packet_size = 8192
    coding = 'utf-8'
    def __init__(self,s_addr,s_port,connect=True):
        self.server_address = (s_addr,s_port)
        self.socket = socket.socket(self.address_familly,self.socket_type)
        parser = optparse.OptionParser()
        parser.add_option("-s","--server",dest="server",help="ftp server ip addr")
        if connect:
            try:
                self.client_connect()
            except:
                self.client_close()
                raise

    def client_connect(self):
        print(self.server_address)
        self.socket.connect(self.server_address)

    def client_close(self):
        self.socket.close()

    def connect(self):
        pass
    
if __name__ == "__main__":
    client = FtpClient("127.0.0.1",10000)
